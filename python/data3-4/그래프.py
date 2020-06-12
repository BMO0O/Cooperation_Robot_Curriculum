#최소 비용 신장트리
#Kruskal 알고리즘
print('\nKruskal 알고리즘')
weights = [(1, 0, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5),
           (6, 1, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2),
           (3, 5, 4), (3, 6, 8), (4, 6, 1), (5, 6, 6)]
weights.sort(key=lambda t: t[2])   #lambda 입력매개변수는 t
print(weights)
mst = []
N = 7
p = []
for i in range(N):
    p.append(i)
def find(u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]
# 합집합 연산
def union(u,v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1
tree_edges = 0
mst_cost = 0
while True:
    if tree_edges == N-1:
        break
    u,v,wt = weights.pop(0)
    print(p, '상호배타적 집합 변화 ')
    print((u,v))
    if find(u) != find(v):
        mst.append((u,v))
        union(u,v)
        tree_edges += 1
        mst_cost += wt
print('\n최소신장트리: ', mst)
print('최소신장트리 가중치 :', mst_cost)
#최소 비용 신장트리
#Prime 알고리즘
import sys
N = 7
s = 0
g = [None] * N
g[0] = [(1, 9), (2, 10)]
g[1] = [(0, 9), (3, 10), (4, 5), (6, 3)]
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]
g[4] = [(1, 5), (2, 7), (6, 1)]
g[5] = [(2, 2), (3, 4), (6, 6)]
g[6] = [(1, 3), (3, 8), (4, 1), (5, 6)]
visited = [False] * N
D = [sys.maxsize] * N
D[s] = 0
previous = [None] * N
previous[s] = s

for i in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value :
            min_value = D[j]
            m = j
    visited[m] = True


    for w,wt in list(g[m]):
        if  not visited[w]:
            if wt < D[w]:
                D[w] = wt
                previous[w] = m


print('\nPrime 알고리즘\n최소신장트리: ', end='')
mst_cost = 0
for i in range(1, N):
    print(f'({i}, {previous[i]})', end='')
    mst_cost += D[i]
print(f'\n최소신장트리 가중치 : {mst_cost}')
