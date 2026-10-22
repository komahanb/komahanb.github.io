"""Redraw Figures 1 and 2 of Komahan's Sensitivity Method Hierarchy.

Continuous notation matches the website note. Figure 2 retains all response
laws in R, including representation and initial conditions. One shared graph
is rendered with four highlight sets; edges mean dependence, not solve order.
Run this script to regenerate the SVG assets in its directory.
"""
from pathlib import Path
from html import escape
import cairosvg
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path as MplPath

OUT = Path(__file__).resolve().parent
NAVY = '#18384c'
TEAL = '#167987'
GOLD = '#a76b17'
DIM = '#c9d2d7'
LIGHT = '#f7f9fa'


def sub(base, index):
    base = {'λ': r'\lambda', 'Ω': r'\Omega'}.get(base, base)
    index = {'λ': r'\lambda', 'Ω': r'\Omega'}.get(index, index)
    return '$' + base + '_{' + index + '}$'


def label(x, y, text, size=20, color=NAVY, weight='normal', anchor='middle'):
    # Store math as vector paths so every renderer positions subscripts alike.
    path = TextPath((0, 0), text, size=size,
                    prop=FontProperties(family='DejaVu Sans', weight=weight))
    bounds = path.get_extents()
    offset = (bounds.x0 + bounds.x1)/2 if anchor == 'middle' else bounds.x0
    commands = []
    for vertices, code in path.iter_segments(curves=True):
        op = {MplPath.MOVETO:'M', MplPath.LINETO:'L', MplPath.CURVE3:'Q',
              MplPath.CURVE4:'C', MplPath.CLOSEPOLY:'Z'}[code]
        commands.append(op + (' '.join(f'{v:.3f}' for v in vertices) if op != 'Z' else ''))
    return f'<path d="{" ".join(commands)}" transform="translate({x-offset:.3f} {y}) scale(1 -1)" fill="{color}"/>'


def box(x,y,w,h,fill='#ffffff',stroke=NAVY,r=10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'


def line(path, color=NAVY, width=1.8, dashed=False, arrow=True):
    marker = {'#18384c':'navy','#167987':'teal','#a76b17':'gold','#c9d2d7':'dim'}[color]
    return f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{width}"' + (' stroke-dasharray="6 5"' if dashed else '') + (f' marker-end="url(#{marker})"' if arrow else '') + '/>'


def save(name,w,h,title,desc,body):
    markers=''.join(f'<marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="{color}"/></marker>' for name,color in [('navy',NAVY),('teal',TEAL),('gold',GOLD),('dim',DIM)])
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs>{markers}</defs><rect width="{w}" height="{h}" rx="14" fill="white"/><g font-family="DejaVu Sans, Arial, sans-serif">'+''.join(body)+'</g></svg>'
    (OUT/(name+'.svg')).write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(),write_to='/tmp/komahan-coordinate-pass/'+name+'.png',scale=1.4)


laws=[
    (sub('r','s')+' = s − '+sub('s','0'),'design pin · point',sub('λ','s')),
    (sub('r','Ω')+'[Q,s]','physical law · I',sub('λ','Ω')),
    (sub('r','t')+'[Q]','coordinate relations · I',sub('λ','t')),
    (sub('r','ic')+'[Q]','initial data · {0}',sub('λ','ic')),
    ('J[Q,s]','scalar metric','1'),
]

# Figure 1: source graph, laid out for a wide reading column.
b=[]
for x,title in [(110,'FIELDS'),(445,'RELATIONS'),(705,'PAIRINGS'),(915,'SCALAR')]:
    b.append(label(x,34,title,18,TEAL,'bold'))
ys=[70,168,266,364,462]
for i,y in enumerate(ys):
    if i in (0,1): b.append(line(f'M200 177 L290 {y+32}'))
    if i in (1,2,3,4): b.append(line(f'M200 381 L290 {y+32}',TEAL))
    b.append(line(f'M600 {y+32} H674'))
    b.append(line(f'M736 {y+32} L848 296'))
b.append(line('M110 219 V554 H262 L290 514',GOLD,dashed=True))
b.append(label(480,558,'direct design dependence, when present',14,GOLD))
b.extend([box(20,135,180,84,'#eef5f6',TEAL),label(110,167,'s = ν',25,weight='bold'),label(110,197,'design parameter',16),box(20,339,180,84,'#eef5f6',TEAL),label(110,371,'Q = (u, v, a)',23,weight='bold'),label(110,401,'state fields on I',16)])
for (name,meaning,mult),y in zip(laws,ys):
    b.extend([box(290,y,310,64,LIGHT),label(445,y+27,name,23,weight='bold'),label(445,y+51,meaning,16)])
    b.append(f'<circle cx="705" cy="{y+32}" r="30" fill="#eef5f6" stroke="{TEAL}" stroke-width="1.5"/>')
    b.append(label(705,y+39,mult,24))
b.extend([box(848,247,136,100,NAVY),label(916,291,'ℒ',38,'white'),label(916,321,'one scalar',16,'white'),label(500,592,'Each law is paired on its own domain; J enters with coefficient 1.',17,TEAL)])
save('figure-1-lagrangian-graph',1000,610,'Figure 1. Fields and paired laws form one Lagrangian','The design s feeds its pin and the physical law. The state Q feeds the physical law, coordinate relations, initial conditions and metric. Each residual is paired with its own multiplier on its own domain. These terms and J sum to one scalar. A dashed edge denotes optional direct dependence of J on s.',b)

# The same dependency graph, using two input buses for narrow screens.
b=[label(240,32,'Fields and paired laws',25,NAVY,'bold'),box(60,57,155,64,'#eef5f6',TEAL),box(265,57,155,64,'#eef5f6',TEAL),label(137,85,'s = ν',23,weight='bold'),label(137,109,'design',17),label(342,85,'Q = (u, v, a)',19,weight='bold'),label(342,109,'state fields on I',16)]
b.append(line('M137 121 V142 H24 V811',NAVY,arrow=False))
b.append(line('M342 121 V158 H46 V828',TEAL,arrow=False))
ys=[185,325,465,605,745]
for i,y in enumerate(ys):
    if i in (0,1): b.append(line(f'M24 {y+28} H72'))
    if i in (1,2,3,4): b.append(line(f'M46 {y+52} H72',TEAL))
    if i==4: b.append(line(f'M24 {y+28} H72',GOLD,dashed=True))
    b.append(line(f'M326 {y+38} H352'))
    b.append(line(f'M414 {y+38} H450 V905 H354'))
    name,meaning,mult=laws[i]
    b.extend([box(72,y,254,76,LIGHT),label(199,y+31,name,22,weight='bold'),label(199,y+59,meaning,17)])
    b.append(f'<circle cx="384" cy="{y+38}" r="30" fill="#eef5f6" stroke="{TEAL}" stroke-width="1.5"/>')
    b.append(label(384,y+46,mult,24))
b.extend([box(126,867,228,76,NAVY),label(240,900,'ℒ',32,'white'),label(240,928,'one scalar',19,'white'),label(240,976,'Each law is paired on its own domain.',18,TEAL),label(240,1003,'Gold dashed edge: J may read s directly.',16,GOLD)])
save('figure-1-lagrangian-graph-mobile',480,1030,'Figure 1. Fields and paired laws form one Lagrangian','The same graph as the wide figure, arranged vertically. Two input lines carry the single design and state to the laws that depend on them; these lines do not create copies of the fields.',b)

# Figure 2: one topology, four choices of variation.
nodes={
 'Q':('circle',55,185,'Q'),
 's':('circle',55,310,'s'),
 'J':('box',205,90,'J'),
 'R':('box',205,185,'R'),
 'pin':('box',205,310,sub('r','s')),
 'lam':('circle',318,185,'λ'),
 'lams':('circle',318,310,sub('λ','s')),
 'L':('circle',430,185,'ℒ'),
}
edges={
 'QJ':('Q','J','M77 167 L163 105'),
 'QR':('Q','R','M83 185 H162'),
 'sR':('s','R','M77 292 L164 205'),
 'spin':('s','pin','M83 310 H162'),
 'JL':('J','L','M248 90 L407 167'),
 'Rlam':('R','lam','M248 185 H289'),
 'lamL':('lam','L','M346 185 H401'),
 'pinlams':('pin','lams','M248 310 H289'),
 'lamsL':('lams','L','M340 292 L412 208'),
}
variants=[
 ('response','Response','Vary the law multipliers','lam',TEAL,{'Q','s','R','lam','L'},{'QR','sR','Rlam','lamL'},sub('D','λ')+'ℒ = R = 0','Determine the response Q'),
 ('adjoint','Adjoint','Vary the state fields','Q',GOLD,{'Q','J','R','lam','L'},{'QJ','QR','JL','Rlam','lamL'},sub('D','Q')+'ℒ = 0','Determine the multipliers λ'),
 ('sensitivity','Sensitivity','Vary the pinned design','s',TEAL,{'s','R','pin','lam','lams','L'},{'sR','spin','Rlam','lamL','pinlams','lamsL'},sub('D','s')+'ℒ = Dj + '+sub('λ','s')+' = 0','Read '+sub('λ','s')+' = −Dj'),
 ('design','Design','Vary the free design','s',GOLD,{'s','R','lam','L'},{'sR','Rlam','lamL'},sub('D','s')+'ℒ = Dj = 0','Determine a stationary design'),
]
for slug,title,subtitle,seed,color,active_nodes,active_edges,eq,outcome in variants:
    b=[box(1,1,478,438,'#ffffff','#c9d2d7',14),label(240,34,title,28,color,'bold'),label(240,61,subtitle,18)]
    for key,(_,_,path) in edges.items():
        b.append(line(path,color if key in active_edges else DIM,2.7 if key in active_edges else 1.4))
    for key,(kind,x,y,text) in nodes.items():
        c=color if key in active_nodes else DIM
        fill='#f0f7f8' if key in active_nodes and color==TEAL else ('#fcf6ec' if key in active_nodes else '#fafbfc')
        if kind=='circle':
            b.append(f'<circle cx="{x}" cy="{y}" r="27" fill="{fill}" stroke="{c}" stroke-width="2"/>')
        else: b.append(box(x-43,y-23,86,46,fill,c,8))
        b.append(label(x,y+8,text,25,c,'bold'))
    _,x,y,_=nodes[seed]
    if seed=='s': b.append(line(f'M{x} 368 V340',color,2.5))
    else: b.append(line(f'M{x} {y-67} V{y-31}',color,2.5))
    if slug=='design': b.append(label(307,357,sub('λ','s')+' = 0 · pin removed',15,NAVY))
    b.extend([label(240,394,eq,22,color,'bold'),label(240,424,outcome,18)])
    save('figure-2-'+slug,480,440,'Figure 2. '+title,subtitle+'. R contains all response laws. The grey edges retain the common graph; highlighted edges show the dependence read by this variation.',b)
print('Generated Figure 1 (wide and mobile) and the four Figure 2 panels.')
