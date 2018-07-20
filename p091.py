from fractions import gcd
print(3 * 50 ** 2 + 2 * sum([sum([min(x // (y // gcd(x, y)), (50 - y) // (x // gcd(x, y)))for y in range(1, 51)]) for x in range(1, 51)]))

n = 50
ct = 0
for x in range(1, n + 1):
    for y in range(1, n + 1):
        g = gcd(x, y)
        incx, incy = y // g, x // g
        ct += min(x // incx, (n - y) // incy)
print(3 * n ** 2 + 2 * ct)
