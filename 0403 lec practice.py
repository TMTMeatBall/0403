# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 간선이 다음과 같이 나열되었을 떄에, 모든 정점을
# 깊이 우선 탐색하여 화면에 탐색경로를 출력하시오

def dfs1(v, k):  # 중복없고, 전부 빠짐없이 들른다
    visited[i] = 1  # 중복 방지용
    print(v)
    # for w in adjL[v]:
    #     if visited[w] == 0:  # 방문한 적 없는 w가 존재할 떄에,
    #         dfs1(w, k)
    for w in range(1, k + 1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs1(w, k)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)

    visited = [0] * (V + 1)


# 스택에 넣었다가 뺴는 방식

def dfs2(s, V):
    stack = []
    v = [0] * (V + 1)
    v = s
    while True:  # 내가v에서 갈 수 있는 정점이 있다면,
        print(v)
        for w in range(1, k + 1):
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return

def dfs3(v,k,g):
    global cnt
    if v == g:
        cnt += 1

    else:
        visited[i] = 1  # 중복 방지용
        for w in range(1,k+1):
            if adjM[v][w] == 1 and visited[w] == 0:
                dfs3(w,k,g)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)

    visited = [0] * (V + 1)