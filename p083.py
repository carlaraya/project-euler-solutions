matrix = [list(map(int, line.split(','))) for line in open('p083_matrix.txt', 'r').read().strip().split('\n')]
num = len(matrix)
h = lambda nx, ny: num-1-nx + num-1-ny
highest_possible = sum(sum(matrix, []))
min_sum = [[highest_possible] * num for i in range(num)]
min_sum[0][0] = matrix[0][0] + h(0,0)
is_final = [[False] * num for i in range(num)]
tentative = {(0, 0)}
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
while tentative:
    nx, ny = min(tentative, key=lambda t: min_sum[t[0]][t[1]])
    if (nx, ny) == (num-1, num-1):
        break
    adjacents = [(nx+mx, ny+my) for mx, my in moves if 0 <= nx+mx < num and 0 <= ny+my < num]
    for ax, ay in adjacents:
        curr_sum = min_sum[nx][ny] - h(nx, ny) + matrix[ax][ay]
        if curr_sum < min_sum[ax][ay] - h(ax, ay):
            min_sum[ax][ay] = curr_sum + h(ax, ay)
            tentative.add((ax, ay))
    tentative.remove((nx, ny))
    is_final[nx][ny] = True
print(min_sum[nx][ny])
