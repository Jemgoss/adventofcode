# Notes on my solutions

In general, my solutions are supposed to be generalized and <i>ought</i> to work on any valid input data. The code makes all the assumptions given in the puzzle descriptions so there's virttually no error checking and it's assumed there's a solution, otherwise they'd break or infinite loop. I think all the solutions simply print the two answers, nothing else.

## Day 1

### Python
1.py was my first stab. Simple enumeration of combinations of a list. Python doesn't have a native list.find() or list.search() function, so I had to use a for loop. I abused the next() function with a generator expression (rather than a list comprehension, which would unnecessarily create a large list only for the purpose of enumerating it). But I'm using a list slice, so this kind of makes that optimization moot!

Part 2 is just an extension of the same algorithm.

1b.py is a different take on the same problem: this time use the itertools.combinations() iterator to supply combination indexes, whoch should be more efficient. Using the native sum() and math.prod() functions, we can avoid messy loops and counters.

### JavaScript

1.js is my JS take, again trying to use functional constructs and avoid messy loops and counters.

## Day 2

Using a RegEx to do the heavy lifting.
Note the use of chaining comparison operators: `a <= b <= c`.

Part 2 uses an `xor` type comparison: `((a == c) != (b == c))`.

## Day 3

After doing part 1, I turned it into a function to be used in part 2. Use of `map()` and `prod()` avoid messy loops.

## Day 4

Using sets to find missing keys. Part 2 uses a bit more regex's and validator functions with the built-in all() function.

## Day 5

In my first stab, 5.py, I read a bit too literally the decoding algorithm for a seat.

Part 2 is a bit clumsy, removing assigned seats from a set of seats from 0 to max_seat_no + 1, then having to remove the initial consecutive seats from the set to leave our single unoccupied seat.

For 5b.py, I realized the seat code is simply a binary number using BR instead of 1 and LF instead of 0. Use int(x, 2) to binary parse that. Also simplified the set arithmatic.

The problem with 5b.py is that it uses list comprehensions to create temporary lists. That's unnecessary and inefficient, as it could lead to excessive resource use for large sets of data.

5c.py improves the solution by using a generator function (lazy evaluation) that yields the seat numbers when necessary to be acted upon instead of creating a list the size of the data set. I also realized the seat assignments set only need go from lowest to highest.

## Day 6

I decided to solve each part as a one-liner, just for kicks. You'll have to unravel to see what the hell it's doing :)

I did notice python provides a nice `set.intersection()` method that takes multiple set arguments.

Strangely, the JS version was a bit more clumsy since there's no set intersection method - WTF? Also, no sum() on an iterable - again, WTF?

## Day 7

Not much to say. I was coming down from a general anesthetic so maybe not the best solution. Create a map then operate on each key using a generator function, recursively.

Part 2 again trying to use functional constructs to avoid messy nested loops.

## Day 8

I kinda cheated here: the program self-destructs as it runs, therefore crashing (raising an Exception) if it revisits an instruction. I save the acc in the Exception so the caller can extract.

Part 2 uses a generator function to fix up programs. Wait until it runs without crashing.

## Day 9

Using itertools.combinations() again to generrate the combinations to test.

Had a go at a JS version. Managed to do part 1 in as a one-liner but couldn;t figure out how to do part 2 in one line. So basically mimicked the py version.
