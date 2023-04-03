# 입력받은 간선을 양방향으로 저장, 1~n번까지 dfs를 수행, visited를 사용하여 그룹을 만든다.
# visited 가 1이라면 스킵하고, 다음 노드에 dfs를 돌린다.
# n번까지 탐색하면서 만들어지는 그룹 개수를 센다.
# 미리미리 하기



# 주어지는 값 N - 노드, M - 간선, 이후 제공되는 n1,n2 - 연결정보
# union find set 을 적용해서 풀어보기?
# 자기 자신을 대표로 하는 union-find , 간선정보를 따라 union과정으로 합해주면 된다
# 모든 작업이 끝난 뒤에 몇 개의 무리가 있는지 세기
p = []

def make_set():
    global p
    p = [i for i in range(N+1)]

#대표자를 찾는 함수 (재귀)
#이전 대표자를 현재 대표자로 정정하는 기능
#find
def find_set(x):
    #기저조건(부모노드로 자기자신을 갖는다면 해당 노드를 반환함)
    if x == p[x]:
        return x
    #재귀적으로 대표자에 대해 경로 압축이 진행된다.
    p[x] = find_set(p[x])
    return p[x]
    #잘못 연결된 경로들을(옛날 대표자 경로)를 재귀적으로 정정함

# 하나의 집합으로 합치는 union함수
def union(x,y):
    global p
    x = find_set(x)
    y = find_set(y)
    p[y] = x
    return x
    #제약 조건이 더 낮은 숫자의 노드를 대표자로 뽑아야 할 경우
    # if x < y :
    #     p[y] = x
    #     return x
    # else: #y < x
    #     p[y] = x
    #     return x

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    #union-find 과정 초기화 필요
    make_set()
    #   N - 노드갯수, M - 간선갯수
    for _ in range(M):
        #       간선의 갯수만큼 노드 u <-> v 에 대한 연결 정보
        u, v = map(int, input().split())
        union(u,v)

    # 모든 노드를 순회하면서 어떤 집합이 있는지 확인
    # 대표자가 몇명 있는지 확인하기
    reps = set() #대표자들
    for node in range(1,N+1):
        reps.add(find_set(node)) #대표자들 set자료형에 추가

    print(f'#{tc} {len(reps)}')

