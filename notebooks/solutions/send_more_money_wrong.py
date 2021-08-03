import facile

# The list comprehension mechanism is always helpful!
[s, e, n, d, m, o, r, y] = [facile.variable(range(10)) for i in range(8)]

# A shortcut
letters = [s, e, n, d, m, o, r, y]

# Retenues
[c0, c1, c2] = [facile.variable([0, 1]) for i in range(3)]

# Constraints
# facile.constraint(s > 0)
# facile.constraint(m > 0)
facile.constraint(facile.alldifferent(letters))
facile.constraint(d + e == y + 10 * c0)
facile.constraint(c0 + n + r == e + 10 * c1)
facile.constraint(c1 + e + o == n + 10 * c2)
facile.constraint(c2 + s + m == o + 10 * m)

if facile.solve(letters):
    [vs, ve, vn, vd, vm, vo, vr, vy] = [x.value() for x in letters]
    print("Solution found :")
    print
    print("  %d%d%d%d" % (vs, ve, vn, vd))
    print("+ %d%d%d%d" % (vm, vo, vr, ve))
    print("------")
    print(" %d%d%d%d%d" % (vm, vo, vn, ve, vy))
else:
    print("No solution found")
