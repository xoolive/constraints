---
layout: default
permalink: /problems/
---

# Problems

Several projects are available in the `problems/` folder. You will be evaluated on one of the projects available there. Obviously, these projects do not contain any hint or solution.

## List of candidate problems

- [Airlines](airlines), scheduling crew members for a (small) airline;
- [Picross](picross), a popular puzzle of a similar nature to Sudoku;
- [Tatami](tatami), how to place tatamis in rooms in Japan;
- [Renovation](renovation), how to cover the external facade of houses with the right number of well-dimensioned panels.

## Useful tips for the `facile` library

- You may **index arrays of variables** with a `facile` variable or expression. But you first need to wrap the array with the facile.array function.

  Example: find the position of the first 0 in a given array.

  ```python
  a = facile.array([1, 2, 0, 4, 5, 0])
  i = facile.variable(range(len(a)))
  facile.constraint(a[i] == 0)
  sol = facile.minimize([i], i)
  ```

  **Warning.**

  - Be aware that the indexing value will be constrained between 0 and `len(array)`.

  - If you work with multi-dimensional arrays, indices should be linearized for you, but this feature is still experimental.

    **Do not use** `a[i][j]` as `a[i]` returns a new variable (considering linearized indices) and it cannot be indexed.  
    **Do use** `a[i, j]` instead. If you want a line (or column) in your array, use slices: `a[:, 0]` returns an array, as well as `a[0, :]`.

  - There are facilities to build arrays of variables:

  ```python
  # a 10×10 array of binary variables
  facile.Array.binary((10, 10))
  # a 5×5 array of variables with a domain of [0, 1, 2]
  facile.Array.variable((5, 5), range(3))
  # a 1D array of 10 variables taking values over [0, 9]
  facile.Array.variable(10, 0, 9)
  ```

- **Constraints may be summed**: the result is the number of `True` values in the set of constraints. However, this doesn't work with global constraints such as `alldifferent`.

  _Example_: Find an array of length $n$ taking values in $[0, n-1]$ so that the $i$-th value is equal to the number of $i$ inside the array.

  ```python
  import facile

  n = 10
  array = facile.Array.variable(n, range(n))

  for i in range(n):
      sum_expr = sum([x == i for x in array])
      facile.constraint(sum_expr == array[i])

  if facile.solve(array):
      print(f"indices: {list(range(n))}")
      print(f"array: {array.value()}")
  ```

- **You may use the & and \| operators** for the logical $\land$ (and) and $\lor$ (or). However, this doesn't work with global constraints such as `alldifferent`.

  ```python
  import facile

  a = facile.variable([0, 1, 2])
  b = facile.variable([0, 1, 2])
  # The following syntax would also be correct:
  # a, b = facile.Array.variable(2, [0, 1, 2])

  left = (a == b) & (a + b == 2)
  right = a > b
  facile.constraint(left | right)

  sol = facile.solve([a, b])
  ```

- You may use the `solve_all` function to get **all the solutions** to a CSP problem.

  ```python
  a = facile.variable([0, 1, 2])
  b = facile.variable([0, 1, 2])

  left = (a == b) & (a + b == 2)
  right = a > b
  facile.constraint(left | right)

  sol_list: list[facile.Solution] = facile.solve_all([a, b])
  ```

  **Warning**

  Using `solve_all` does not assign any value to a variable. You will get `None` for any `x.value()`. The explanation lies in the fact the Branch&Bound algorithm returns with no solution found, hence the last `None`. Note the similar behaviour with the `minimize` function.

- **Search goals** may be defined in order to conduct your resolution process. For tiling problems, i.e. placing elements in a two-dimensional grid, it is common to first assign the x variables, ensure they don't violate any constraint, then assign the y variables.

  This would be written in `facile` as:

  ```python
  gx = facile.Goal.forall(x, assign="assign")
  gy = facile.Goal.forall(y, assign="assign")

  solution = facile.solve(gx & gy)
  ```
