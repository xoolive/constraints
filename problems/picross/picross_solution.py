from __future__ import annotations

import signal
import sys
import time

import facile

from picross import picross


def channel(
    start: list[facile.Variable], data: list[int], grid_v: int, j: int
) -> None:

    cstr = (start[0] <= j) & (j < start[0] + data[0])
    for k in range(1, len(data)):
        cstr = cstr | ((start[k] <= j) & (j < start[k] + data[k]))
    facile.constraint(cstr == grid_v)


def picross_solve(
    lines: list[list[int]],
    columns: list[list[int]],
    indexing: bool,
    channeling: bool,
) -> tuple[facile.Solution, facile.Array]:

    n_l, n_c = len(lines), len(columns)

    # -- Definition of the variables --

    grid = facile.Array.binary((n_c, n_l))

    start_l = [[facile.variable(range(n_c)) for _ in l_] for l_ in lines]
    start_c = [[facile.variable(range(n_l)) for _ in c_] for c_ in columns]

    start = time.time()

    # -- Constraints --

    # No overlapping (similar to scheduling precedence)
    for cur_start, cur_line in zip(start_l, lines):
        for cur_, len_, next_ in zip(cur_start, cur_line, cur_start[1:]):
            facile.constraint(cur_ + len_ < next_)

        facile.constraint(cur_start[-1] + cur_line[-1] <= n_c)

    for cur_start, cur_column in zip(start_c, columns):
        for cur_, len_, next_ in zip(cur_start, cur_column, cur_start[1:]):
            facile.constraint(cur_ + len_ < next_)

        facile.constraint(cur_start[-1] + cur_column[-1] <= n_l)

    if indexing:
        # black cells in lines
        for i, (cur_start, cur_line) in enumerate(zip(start_l, lines)):
            for cur_, len_ in zip(cur_start, cur_line):
                for j in range(len_):
                    facile.constraint(grid[i, cur_ + j] == 1)

            # for maintaining white cells
            facile.constraint(grid[i, :].sum() == sum(cur_line))

        # black cells in columns
        for j, (cur_start, cur_column) in enumerate(zip(start_c, columns)):
            for cur_, len_ in zip(cur_start, cur_column):
                for i in range(len_):
                    facile.constraint(grid[cur_ + i, j] == 1)

            # for maintaining white cells
            facile.constraint(grid[:, j].sum() == sum(cur_column))

    if channeling:
        for i in range(n_l):
            for j in range(n_c):
                channel(start_l[i], lines[i], grid[i, j], j)
                channel(start_c[j], columns[j], grid[i, j], i)

    stop = time.time()

    variables = sum(start_l, []) + sum(start_c, [])  # type: ignore
    sol = facile.solve(variables, backtrack=True)
    sol["Initial propagation time"] = "{:.2g}s".format(stop - start)

    return sol, grid


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Picross solver program")

    parser.add_argument(
        "problem",
        help=(
            "name of problem among (moon, star, cat, horse,"
            " house, duck or any *.non file)"
        ),
    )

    parser.add_argument(
        "-i",
        dest="indexing",
        action="store_true",
        help="use only indexing formulation",
    )

    parser.add_argument(
        "-c",
        dest="channeling",
        action="store_true",
        help="use only channeling formulation",
    )

    args = parser.parse_args()

    lines, columns = picross[args.problem]
    if not args.indexing or not args.channeling:
        args.channeling = True
        args.indexing = True

    def signal_handler(signal, frame):
        print("You pressed Ctrl+C!")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    sol, grid = picross_solve(lines, columns, args.indexing, args.channeling)
    print(sol)

    for line in grid.value():
        for item in line:
            if item == 1:
                print("█", end="")
            else:
                print("·", end="")
        print()
