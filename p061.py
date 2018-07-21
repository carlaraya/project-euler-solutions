figurates = [[], [], []]
for sides in range(3, 9):
    n = 0
    figurates.append([])
    while True:
        P = round(n * ((sides-2)*n + (4-sides))/2)
        if P >= 10000:
            break
        elif P >= 1000:
            figurates[sides].append(P)
        n += 1
def search(octa, curr, remaining, figurates):
    if len(remaining) == 1:
        last_num = (curr % 100 * 100 + octa // 100)
        if last_num in figurates[remaining[0]]:
            return [last_num]
        else:
            return []
    for i in remaining:
        for num in figurates[i]:
            lower_bound = curr % 100 * 100
            upper_bound = lower_bound + 100
            if num >= upper_bound:
                break
            elif num >= lower_bound:
                new_remaining = remaining[:]
                new_remaining.remove(i)
                results = search(octa, num, new_remaining, figurates)
                if len(results) == len(new_remaining):
                    return [num] + results
    return []
for octa in figurates[8]:
    results = [octa] + search(octa, octa, list(range(3, 8)), figurates)
    if len(results) > 1:
        print(sum(results))
        break
