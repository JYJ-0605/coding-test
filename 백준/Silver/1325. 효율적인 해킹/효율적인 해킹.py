from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([start])
    count = 1

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1

    return count

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)  # B가 해킹당하면 A도 해킹 가능

result = []
max_value = 0

for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_value:
        result = [i]
        max_value = cnt
    elif cnt == max_value:
        result.append(i)

print(*result)
