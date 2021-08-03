import facile


def n_queens(n: int, *args, **kwargs) -> facile.Solution:
    queens = [facile.variable(range(n)) for i in range(n)]
    diag1 = [queens[i] + i for i in range(n)]
    diag2 = [queens[i] - i for i in range(n)]

    facile.constraint(facile.alldifferent(queens))
    facile.constraint(facile.alldifferent(diag1))
    facile.constraint(facile.alldifferent(diag2))

    return facile.solve(queens, *args, **kwargs)


def print_line(val, n):
    cumul = ""
    for i in range(n):
        if val == i:
            cumul = cumul + "♛ "
        else:
            cumul = cumul + "- "
    print(cumul)


n = 8
solutions = n_queens(n).solution

if solutions is not None:
    print("Solution found :")
    print
    [print_line(s, n) for s in solutions]
else:
    print("No solution found")
