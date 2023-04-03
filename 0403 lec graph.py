# 그래프 탐색 기법인 BFS, DFS에 대한 이해
# 그래프 유형(무향[방향성 없음],유향[방향이 존재],가중치[각 노선에 가중치가 존재함],
# 완전(모든 정점에 가능한 모든 간선이 존재) / 부분(원래 그래프에서 일부의 정점 또는 간선을 제외함)
# 경로 -

# 예시 (노드, 간선)
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

#인접 행렬 방식
#방향성을 만들 수 있다.
#무향, 유향에 따라 그래프의 이차원배열 표현이 달라진다.
#각 행번호에서 갖는 인덱스 넘버는 해당 노드에서 진출차수,
#각 열번호에서 갖는 인덱스 넘버는 해당 노드로 들어오는 진입차수

V, E = map(int,input().split())

arr = list(map(int,input().split()))

adjM = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1


#인접 리스트
V, E = map(int,input().split())
arr = list(map(int,input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)

#그래프의 두가지 표현 방식 - (인접행렬/인접리스트)
#에 대한 DFS/BFS
#서로소 집합
#최소비용 신장트리
#최단 경로