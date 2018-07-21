n = 10 ** 6 + 1
sieve = list(range(n))
for i in range(2, int(n ** 0.5) + 1):
    if sieve[i] == i:
        for j in range(i * 2, n, i):
            if sieve[j] == j or i > sieve[j]:
                sieve[j] = i
ct = 0
for i in range(2, n):
    tmp = i
    tot = i
    prev = 0
    while tmp > 1:
        if prev != sieve[tmp]:
            tot -= tot // sieve[tmp]
        prev = sieve[tmp]
        tmp //= sieve[tmp]
    ct += tot
print(ct)
