# 1부터 시작하기 때문에 1을 queue에 넣고 while문을 돌린다. 
# while문 안에서 빠져나오면 그 값을 now라고 하고, 
# now와 연결되어있는 node들 중에서 가보지 않는 노드들을 가서
#  ans[nxt]의 값에 now를 넣으면 된다.

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res = ans[2:]
for x in res:
    print(x)