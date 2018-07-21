sieve = list(range(10 ** 8))
for i in range(2, int(n ** 0.5) + 1):
    if sieve[i] == i:
        for j in range(i * 2, n, i):
            if sieve[j] == j or i > sieve[j]:
                sieve[j] = i
