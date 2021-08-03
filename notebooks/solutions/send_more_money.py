import facile
import functools

# The list comprehension mechanism is always helpful!
[s, e, n, d, m, o, r, y] = [facile.variable(range(10)) for i in range(8)]

# A shortcut
letters = [s, e, n, d, m, o, r, y]

# Constraints
facile.constraint(s > 0)
facile.constraint(m > 0)
facile.constraint(facile.alldifferent(letters))


send = functools.reduce(lambda x, y: 10 * x + y, [s, e, n, d])
more = functools.reduce(lambda x, y: 10 * x + y, [m, o, r, e])
money = functools.reduce(lambda x, y: 10 * x + y, [m, o, n, e, y])

facile.constraint(send + more == money)

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
