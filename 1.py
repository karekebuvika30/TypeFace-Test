from sys import stdin, stdout
m, n = map(int, stdin.readline().strip().split())
arr = []
for i in range(m):
    arr.append(list(map(int, stdin.readline().strip().split())))

# print(*arr)
from collections import deque
def bfs(i, j):
    global arr
    x8, y8 = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
    q = deque()
    q.append([i, j])
    li, lj = i, j
    while q:
        # print(q)
        p = q.popleft()
        for d in range(8):
            ci, cj = p[0] + x8[d], p[1] + y8[d]
            if ci >= 0 and ci < len(arr) and cj >= 0  and cj < len(arr[0]) and arr[ci][cj] != 0:
                # print(*arr)
                arr[ci][cj] = 0
                li, lj = ci, cj
                q.append([ci, cj])
    return li, lj

def countPatches(m, n, arr):
    count = 0
    idx = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                ei, ej = bfs(i, j)
                print(i, ei, j, ej)
                idx.append([(i+ei+1)//2, (j+ej+1)//2, (ei - i)+1, (ej - j)+1])
                count += 1
    stdout.write("has "+str(count)+" isolated patches\n")
    return idx

print(countPatches(m,n,arr))