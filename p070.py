n = 10 ** 7
sieve = list(range(n))
for i in range(2, int(n ** 0.5) + 1):
    if sieve[i] == i:
        for j in range(i * 2, n, i):
            if sieve[j] == j or i > sieve[j]:
                sieve[j] = i
best = 0
best_ratio = 0
for i in range(2, n):
    tmp = i
    tot = i
    prev = 0
    while tmp > 1:
        if prev != sieve[tmp]:
            tot -= tot // sieve[tmp]
        prev = sieve[tmp]
        tmp //= sieve[tmp]
    if sorted(str(tot)) == sorted(str(i)):
        if tot / i > best_ratio:
            best = i
            best_ratio = tot / i
print(best, best_ratio)
