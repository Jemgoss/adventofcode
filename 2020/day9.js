const data = require('fs').readFileSync('day9.input', 'utf8').split("\n").map(x => parseInt(x));

// Part 1
let found_val = data.find((val, pos) => pos >= 25 && !data.slice(pos - 25, pos).find((a, i, arr) => arr.find((b, j) => j > i && a + b === val)));
console.log(found_val);

// Part 2
for (let pos = 0; ; pos++) {
  let sum = 0;
  let end = pos;
  while (sum < found_val) {
    sum += data[end]
    end++;
  }
  if (sum === found_val) {
    let range = data.slice(pos, end);
    console.log(Math.min(...range) + Math.max(...range));
    break;
  }
}
