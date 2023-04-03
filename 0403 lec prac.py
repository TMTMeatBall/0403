# 그래프를 인접 리스트로 저장
n, edge = map(int, input().split())  # n:노드갯수, edge:간선갯수

# 인접 리스트 : 정점 i -> 다른정점에대한연결정보
graph = [[] for _ in range(n + 1)]

# 간선정보입력받고, 그것을 인접리스트에 적용
arr = list(map(int, input().split()))
for i in range(0, len(arr), 2):
    # u = 정점 i <-> v=정점 (i+1)
    u = arr[i]
    v = arr[i + 1]
    graph[u].append(v)
    graph[v].append(u)
#
# # 방문정점 체크 목적의 visited
# visited = [False for _ in range(n + 1)]
#
#
# # dfs 순회 (재귀호출)
# def dfs(v):
#     #현재 방문한 정점은 v.(방문체크)
#     visited[v] = True
#
#     #현재 v정점에 대해서 인접한(그러나 방문하지 않은) 노드를 방문
#     for u in graph[v]:
#         if visited[u] == False:
#             dfs(u) #방문의 진행

# dfs로 완전탐색을 한다
# 방문체크를 하는 것으로 사이클로 무한 탐색을 방지하자


# bfs 구현
#deque 써보기
from collections import deque #double-end queue 양 쪽으로 다 뺄 수 있기 때문에 이렇게 불린다.

def bfs(v):
# 큐 생성
    visited = [[0] for _ in range(n+1)]
    q = deque()
#시작점v를 큐에 넣기
    q.append(v)
#점 v를 방문한 것으로 표시
    visited[v] = True

#while큐가 비어있지 않은 경우,
    while len(q) > 0:
# t <- 큐의 첫 번째 원소 반환
        t = q.popleft()
# for t와 연결된 모든 선에 대해서,
    for u in graph[t]:
#  u <- t의 이웃점
        if visited[u] == False:
#  u가 방문되지 않은 곳이면,
            q.append(u)
            visited[u] = True
#  u를 큐에 넣고, 방문한 것으로 표시하기
bfs(1) #bfs 방식으로 1번 노드부터 순회하기