import math
def numcat(a, b):
    return a * 10 ** (int(math.log10(b)) + 1) + b
def connected(a, b):
    return a != b and sieve[numcat(a, b)] and sieve[numcat(b, a)]
sieve = [1]
cliques = []
power = 1
while True:
    new_power = power * 10
    sieve += [1] * (new_power - power)
    for i in range(2, new_power):
        if i:
            for j in range(i * 2, new_power, i):
                sieve[j] = 0
    # print(list(enumerate(sieve)))
    max_len = int(math.log10(new_power))
    print('max_len', max_len)
    for i in range(max(3, 10 ** ((max_len - 1) // 2)), 10 ** max_len):
        if sieve[i]:
            i_len = int(math.log10(i)) + 1
            j_max_len = 10 ** (max_len - i_len)
            print(i)
            #print(max(3, j_max_len // 10), min(i, j_max_len))
            for j in range(max(3, j_max_len // 10), min(i, j_max_len)):
                if sieve[j]:
                    if connected(i, j):
                        print(i, j)
                        print(cliques)
                        input()
                        def look_for_cliques(a, b):
                            was_found = True
                            subset = [clique for clique in cliques if a in clique]
                            if subset:
                                for clique in subset:
                                    is_part_of_clique = True
                                    for clique_mem in clique:
                                        if not connected(b, clique_mem):
                                            is_part_of_clique = False
                                    if is_part_of_clique:
                                        clique.append(b)
                                        was_found = True
                            return False
                        was_found = look_for_cliques(i, j)
                        was_found = was_found or look_for_cliques(j, i)
                        if not was_found:
                            cliques.append([j, i])
    power = new_power
