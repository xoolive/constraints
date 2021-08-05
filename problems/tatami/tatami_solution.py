from __future__ import annotations

import click
import facile
import matplotlib.pyplot as plt


def tatami_solve(xmax: int, ymax: int) -> list[facile.Solution]:
    """Solves the tatami problem.

    The variables in the solve_all must be passed in order:
    - x coordinates;
    - y coordinates;
    - xs the size of the tatami on the x axis (1: vertical, 2: horizontal);
    - other variables
    """

    if (xmax * ymax) & 1 == 1:
        raise ValueError(f"The room area must be an even number: {xmax * ymax}")
    n = xmax * ymax // 2  # noqa: F841

    # start with a "simple" solve(), then comment the line when things work
    return [facile.solve([], backtrack=True)]
    # the evaluation process expects that you return *all* solutions
    return facile.solve_all([], backtrack=True)


@click.command()
@click.argument("xmax", type=int, default=4)
@click.argument("ymax", type=int, default=3)
def main(xmax: int, ymax: int):
    sol = tatami_solve(xmax, ymax)
    for solution in sol:
        print(solution)

        if solution.solution is None:
            continue

        n = len(solution.solution) // 3
        x = solution.solution[:n]
        y = solution.solution[n : 2 * n]
        xs = solution.solution[2 * n :]

        fig, ax = plt.subplots()

        for (xi, yi, xsi) in zip(x, y, xs):
            ysi = 3 - xsi
            ax.fill([xi, xi, xi + xsi, xi + xsi], [yi, yi + ysi, yi + ysi, yi])

        ax.set_xlim((0, xmax))
        ax.set_ylim((0, ymax))
        ax.set_aspect(1)
        ax.set_xticks(range(xmax + 1))
        ax.set_yticks(range(ymax + 1))

        plt.show()


if __name__ == "__main__":
    main()
