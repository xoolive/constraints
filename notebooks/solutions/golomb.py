import facile


def golomb(n: int) -> facile.Solution:
    ticks = [facile.variable(range(2 ** n)) for i in range(n)]

    # First tick at the start of the ruler
    facile.constraint(ticks[0] == 0)

    # Ticks are ordered
    for i in range(n - 1):
        facile.constraint(ticks[i] < ticks[i + 1])

    # All distances
    distances = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            distances.append(facile.variable(ticks[j] - ticks[i]))
    facile.constraint(facile.alldifferent(distances))

    for d in distances:
        facile.constraint(d > 0)

    # Breaking the symmetry
    size = len(distances)
    facile.constraint(distances[size - 1] > distances[0])

    return facile.minimize(
        ticks, ticks[n - 1], backtrack=True, on_solution=print
    )


print(golomb(9))
