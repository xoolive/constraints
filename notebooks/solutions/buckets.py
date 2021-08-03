import facile

# Number of buckets
nb = 3
# Number of steps (let's say we know... :p)
steps = 8
# The capacity of each bucket
capacity = [8, 5, 3]

buckets = [
    [facile.variable(range(capacity[b] + 1)) for b in range(nb)]
    for i in range(steps)
]

facile.constraint(buckets[0][0] == 8)
facile.constraint(buckets[0][1] == 0)
facile.constraint(buckets[0][2] == 0)

facile.constraint(buckets[steps - 1][0] == 4)
facile.constraint(buckets[steps - 1][1] == 4)
facile.constraint(buckets[steps - 1][2] == 0)

for i in range(steps - 1):
    # we change the contents of two buckets at a time
    facile.constraint(
        sum([buckets[i][b] != buckets[i + 1][b] for b in range(nb)]) == 2
    )
    # we play with a constant amount of water
    facile.constraint(sum([buckets[i][b] for b in range(nb)]) == 8)
    for b1 in range(nb):
        for b2 in range(b1):
            facile.constraint(
                # either the content of the bucket does not change
                (buckets[i][b1] == buckets[i + 1][b1])
                | (buckets[i][b2] == buckets[i + 1][b2])
                |
                # or the bucket ends up empty or full
                (buckets[i + 1][b1] == 0)
                | (buckets[i + 1][b1] == capacity[b1])
                | (buckets[i + 1][b2] == 0)
                | (buckets[i + 1][b2] == capacity[b2])
            )

print(facile.solve([b for sub in buckets for b in sub], backtrack=True))
for sub in buckets:
    print([b.value() for b in sub])
