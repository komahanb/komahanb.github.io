/* Skins: Georgia Tech unless the visitor chooses otherwise; Classic follows the system's light or dark theme; Futuristic, Alien, Cosmos, India and Georgia Tech restate the colour tokens of site.css. The choice is kept in this browser. */
(function () {
  var KEY = 'komahanb:skin', SKINS = { gatech: 'Georgia Tech', alien: 'Alien', 'default': 'Classic', futuristic: 'Futuristic', cosmos: 'Cosmos', india: 'India' };
  var FONTS = { futuristic: 'Exo+2:wght@500;600;700', alien: 'Chakra+Petch:wght@500;600;700', india: 'Rajdhani:wght@500;600;700', gatech: 'Roboto+Slab:wght@500;600;700' };
  var root = document.documentElement;
  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function keep(s) { try { localStorage.setItem(KEY, s); } catch (e) {} }
  function font(s) {
    if (!FONTS[s] || document.getElementById('skin-font-' + s)) { return; }
    var l = document.createElement('link'); l.id = 'skin-font-' + s; l.rel = 'stylesheet';
    l.href = 'https://fonts.googleapis.com/css2?family=' + FONTS[s] + '&display=swap';
    document.head.appendChild(l);
  }
  function apply(s) {
    if (!SKINS[s]) { s = 'default'; }
    if (s === 'default') { root.removeAttribute('data-skin'); } else { root.setAttribute('data-skin', s); font(s); }
    return s;
  }
  var asked = /[?&]skin=([a-z]+)/.exec(location.search);
  var current = apply(asked && SKINS[asked[1]] ? asked[1] : (read() || 'gatech'));
  if (asked && SKINS[asked[1]]) { keep(current); }
  document.addEventListener('DOMContentLoaded', function () {
    var bar = document.querySelector('.top .wrap');
    if (!bar) { return; }
    var label = document.createElement('label'), select = document.createElement('select');
    label.className = 'skin-pick'; label.appendChild(document.createTextNode('Skin'));
    Object.keys(SKINS).forEach(function (k) { var o = document.createElement('option'); o.value = k; o.textContent = SKINS[k]; select.appendChild(o); });
    select.value = current;
    select.addEventListener('change', function () { current = apply(select.value); keep(current); });
    label.appendChild(select); bar.appendChild(label);
  });
})();
