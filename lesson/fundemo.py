a = lambda x: x * x
print(a(2))

c = [1, 2, 3, 4]

a = lambda arr: arr * 2

print(a(c))
print(c)

m = list(map(lambda x: x * x * x, range(8)))
print(m)

m = list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

print(m)
