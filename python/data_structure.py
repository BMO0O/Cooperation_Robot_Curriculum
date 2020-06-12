def dfs(x, y):
    check[x][y] = 1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= h+1 and 0 <= ny <= w and land[nx][ny] == 1 and check[nx][ny] == 0:
            dfs(nx, ny)

result = []
dx = [-1, 0, 1, -1, 1, -1, 0, 1] #대각선 포함 단위좌표
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


while True:
    w, h = map(int, input().split())
    count = 0
    
    if w == 0 and h == 0:
        break

    land = [[0]*(w+1) for _ in range(h+2)]
    check = [[0]*(w+1) for _ in range(h+2)]

    for i in range(1,h+1):
        land[i] = [0]+ list(map(int, input().split())) + [0]

    land[h+1] = [0]*(w+1)

    


    for i in range(h+2):
        for j in range(w+1):
            if check[i][j] == 0 and land[i][j] == 1:
                dfs(i, j)
                count+=1

    result.append(count)

for i in result:
    print(i)
