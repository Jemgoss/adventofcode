const data = require('fs').readFileSync('6.input', 'utf8').trim().split("\n\n");

// Part 1
console.log((data.map(group => (new Set([...group.replaceAll("\n", "")])).size)).reduce((a, b) => a + b));

// Part 2
console.log((data.map(group => group.split("\n").map(g => new Set([...g])).reduce((a, b) => new Set([...a].filter(x => b.has(x)))).size)).reduce((a, b) => a + b));
