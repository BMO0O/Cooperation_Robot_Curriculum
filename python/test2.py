'''
N = int(input())
for i in range(1,10):
    print(N*i)
n, m = map(int, input().split())
print(n*m)
'''
#아아아아아아아아가강가ㅏㅇ가어라ㅓ아ㅣㅓ라ㅓㅏ이ㅏ아가악졸려
print("입력")
N = int(input())
print("출력")
dx = [1,0,-1,0]
dy=[0,1,0,-1]
direc = 0 # 0=right, 1=down, 2=left, 3=up
x = 0
y = 0
#num_map = [[0]*N for i in range(N)]
num_map = [[0]*10 for i in range(10)]

for j in range(1, N*N):
    num_map[x][y] = j
    gx = x + dx
    gy = y + dy
    
    if((gx>=0 and gx<n) and (gy>=0 and gy<n)):
        if (k[gy][gx] == 0):
            x = gx
            y = gy
        else:
            do = (direc + 1)%4
            x += dx[do]
            y += dy[do]
    else:
        do(direc + 1)

print(num_map)
