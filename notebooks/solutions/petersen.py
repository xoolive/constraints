import facile

colouring = [facile.variable(range(3)) for i, _ in enumerate(points)]
colours = ["ro", "bo", "go"]

# Build edges between the five nodes in the inner circle
for i in range(5):
    j, j_ = i, (i + 2) % 5  # % (modulo -> j=4, j_=0)
    facile.constraint(colouring[j] != colouring[j_])

# Build edges between the inner and the outer circle
for i in range(5):
    facile.constraint(colouring[i] != colouring[i + 5])

# Build edges between the five nodes on the outer circle
for i in range(5):
    j, j_ = 5 + i, 5 + (i + 1) % 5  # % (modulo -> j=9, j_=5)
    facile.constraint(colouring[j] != colouring[j_])

plot_edges()

if facile.solve(colouring):
    for i, (x_, y_) in enumerate(points):
        plt.plot(x_, y_, colours[colouring[i].value()])
else:
    print("No solution found")
