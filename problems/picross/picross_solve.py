from __future__ import annotations

import click
import facile
import signal
import sys


from picross import picross


def picross_solve(
    lines: list[list[int]],
    columns: list[list[int]],
) -> tuple[facile.Solution, facile.Array]:
    n, m = len(lines), len(columns)
    grid = facile.Array.binary((n, m))

    sol = facile.solve(grid)

    return sol, grid


@click.command(help="Picross solver program")
@click.argument(
    "name",
    default="moon",
    # help="The name of the problem you want to solve.",
    # show_default=True,
)
def main(name: str) -> None:
    lines, columns = picross[name]

    def signal_handler(signal, frame):
        print("You pressed Ctrl+C!")
        sys.exit(1)

    signal.signal(signal.SIGINT, signal_handler)

    sol, grid = picross_solve(lines, columns)

    print(sol)

    for line in grid.value():
        for item in line:
            if item == 1:
                print("█", end="")
            else:
                print("·", end="")
        print()


if __name__ == "__main__":
    main()
