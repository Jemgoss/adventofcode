const fs = require('fs');
const data = fs.readFileSync('day1.input', 'utf8').split("\n").map(x => parseInt(x));

{ // Part 1
  var b = undefined;
  var a = data.find((a,i) => (b = data.slice(i+1).find(b => a + b === 2020)));
  console.log(a, b, a * b);
}

{ // Part 2
  var c = undefined;
  var b = undefined;
  var a = data.find((a,i) => (b = data.slice(i+1).find((b,j) => (c = data.slice(j+1).find(c => a + b + c === 2020)))));
  console.log(a, b, c, a * b * c);
}
