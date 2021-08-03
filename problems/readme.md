---
title: Problems
layout: default
permalink: /problems/
---

# Problems

Several projects are available in the `problems/` folder. You will be evaluated on one of the projects available there. Obviously, these notebooks do not contain any hint or solution.

List of problems:

- [Airlines](airlines), scheduling crews for a (small) airline;
- [Picross](picross), a popular puzzle of a similar nature to Sudoku;
- [Tatami](tatami), how to place tatamis in rooms in Japan;
- [Renovation](renovation), how to cover the external facade of houses with the right number of well-dimensioned panels.

## More about the `facile` library

- Constraints may be summed: the result is the number of True values in the set of constraints. However, this doesn't work with global constraints such as `alldifferent`.

  _Example_: Find an array of length $n$ taking values in $[0, n-1]$ so that the $i$-th value is equal to the number of $i$ inside the array.

  ```python
  import facile

  n = 10
  array = [facile.variable(range(n)) for i in range(n)]

  for i in range(n):
      sum_expr = sum([x == i for x in array])
      facile.constraint(sum_expr == array[i])

  if facile.solve(array):
      print(f"indices: {list(range(n))}")
      print(f"array:   {[v.value() for v in array]}")
  ```

- You may use the & and \| operators for the logical $\land$ and $\lor$. However, this doesn't work with global constraints such as alldifferent

  ```python
  import facile

  a = facile.variable([0, 1, 2])
  b = facile.variable([0, 1, 2])

  left = (a == b) & (a + b == 2)
  right = a > b
  facile.constraint(left | right)
  result = facile.solve([a, b])
  a.value(), b.value()
  ```
