def determine_number_of_mines_around():
    for i in range(n):
        for j in range(m):
            if mine_map[i][j] != '*':
                if j - 1 >= 0 and mine_map[i][j - 1] == '*':
                    mine_map[i][j] += 1
                if j + 1 < m and mine_map[i][j + 1] == '*':
                    mine_map[i][j] += 1
                if i - 1 >= 0 and mine_map[i - 1][j] == '*':
                    mine_map[i][j] += 1
                if i + 1 < n and mine_map[i + 1][j] == '*':
                    mine_map[i][j] += 1
                if i - 1 >= 0 and j - 1 >= 0 and mine_map[i - 1][j - 1] == '*':
                    mine_map[i][j] += 1
                if i - 1 >= 0 and j + 1 < m and mine_map[i - 1][j + 1] == '*':
                    mine_map[i][j] += 1
                if i + 1 < n and j - 1 >= 0 and mine_map[i + 1][j - 1] == '*':
                    mine_map[i][j] += 1
                if i + 1 < n and j + 1 < m and mine_map[i + 1][j + 1] == '*':
                    mine_map[i][j] += 1

n, m = map(int, input().split(' '))
k = int(input())
mine_map = [[0 for j in range(m)] for i in range(n)]

for k in range(k):
    i, j = map(int, input().split(' '))
    mine_map[i - 1][j - 1] = '*'

determine_number_of_mines_around()

print('\n'.join([' '.join(map(str, row)) for row in mine_map]))