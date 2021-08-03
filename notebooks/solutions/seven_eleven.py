import facile

# -- Variables --
# There is a risk of integer overflow when computing a*b*c*d
# We need smaller domains...
a = facile.variable(range(0, 321))
b = facile.variable(range(0, 161))
c = facile.variable(range(0, 131))
d = facile.variable(range(0, 131))

# -- Constraints --

# The problem
facile.constraint(a + b + c + d == 711)

print("Domains after posting the sum constraint")
for x in [a, b, c, d]:
    domain = x.domain()
    print("  {!r} (size {})".format(domain, len(domain)))

facile.constraint(a * b * c * d == 711000000)

print("\nDomains after posting the mul constraint")
for x in [a, b, c, d]:
    domain = x.domain()
    print("  {!r} (size {})".format(domain, len(domain)))

print()

# -- Resolution --
sol = facile.solve([a, b, c, d], backtrack=True)

# wow ! Only two backtracks !!
print(sol)
print("Solution found: a={}, b={}, c={}, d={}".format(*sol.solution))
