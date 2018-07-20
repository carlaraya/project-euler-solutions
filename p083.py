matrix = [list(map(int, line.split(','))) for line in open('p083_matrix.txt', 'r').read().strip().split('\n')]
num = len(matrix)
highest_possible = sum(sum(matrix, []))
g_score = [[highest_possible] * num for i in range(num)]
g_score[0][0] = matrix[0][0]
tentative = {(0, 0)}
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
while tentative:
    nx, ny = min(tentative, key=lambda t: g_score[t[0]][t[1]])
    if (nx, ny) == (num-1, num-1):
        break
    adjacents = [(nx+mx, ny+my) for mx, my in moves if 0 <= nx+mx < num and 0 <= ny+my < num]
    for ax, ay in adjacents:
        curr_sum = g_score[nx][ny] + matrix[ax][ay]
        if curr_sum < g_score[ax][ay]:
            g_score[ax][ay] = curr_sum
            tentative.add((ax, ay))
    tentative.remove((nx, ny))
print(g_score[nx][ny])
