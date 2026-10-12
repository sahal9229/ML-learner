const fs = require('fs');
const d = fs.readFileSync('js/catalog.js', 'utf8');
const mods = new Set();
const re = /"module":\s*"([^"]+)"/g;
let m;
while (m = re.exec(d)) mods.add(m[1]);
console.log([...mods].join('\n'));
