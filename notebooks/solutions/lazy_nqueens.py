import facile


def lazy_n_queens(n: int, *args, **kwargs) -> facile.Solution:
    queens = [facile.variable(range(n)) for i in range(n)]
    diag1 = [queens[i] + i for i in range(n)]
    diag2 = [queens[i] - i for i in range(n)]

    # facile.constraint(facile.alldifferent(queens))
    for i, q1 in enumerate(queens):
        for q2 in queens[i + 1 :]:
            facile.constraint(q1 != q2)

    # facile.constraint(facile.alldifferent(diag1))
    for i, q1 in enumerate(diag1):
        for q2 in diag1[i + 1 :]:
            facile.constraint(q1 != q2)

    # facile.constraint(facile.alldifferent(diag2))
    for i, q1 in enumerate(diag2):
        for q2 in diag2[i + 1 :]:
            facile.constraint(q1 != q2)

    return facile.solve(queens, *args, **kwargs)
