const data = require('fs').readFileSync('day5.input', 'utf8').trim().split("\n");

// Part 1
const decoder = (acc, key) => {
  if (key === acc.upperKey) {
    acc.seat += acc.upperSeatCount;
  }
  acc.upperSeatCount /= 2;
  return acc;
};

const seatNumFn = (assignment) => {
  return Array.from(assignment.slice(0, 7)).reduce(decoder, {upperKey: 'B', seat: 0, upperSeatCount: 64}).seat * 8 +
         Array.from(assignment.slice(7)).reduce(decoder, {upperKey: 'R', seat: 0, upperSeatCount: 4}).seat;
};

const maxSeatNum = Math.max(...data.map(seatNumFn, data));
console.log(maxSeatNum);

// Part 2
const seating = Array(maxSeatNum + 1);
data.forEach(assignment => seating[seatNumFn(assignment)] = true);
const firstOccupied = seating.findIndex(e => e !== undefined);
const mySeat = seating.findIndex((e, i) => i > firstOccupied && e === undefined);
console.log(mySeat);
