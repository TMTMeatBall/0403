def f(x, y, path, way):
    global cnt, i, j
    if way == 3 and x == i and y == j and len(path) > 2:
        cnt = max(cnt, len(path))
        return  # 종료 조건

    if 0 <= x < N and 0 <= y < N and arr[x][y] not in path:
        new = path + [arr[x][y]]

        nx, ny = x + dxy[way][0], y + dxy[way][1]
        f(nx, ny, new, way)
        # 방향을 꺾지 않고 진행할 수 있도록 재귀호출
        if way < 3:
            nx, ny = x + dxy[way + 1][0], y + dxy[way + 1][1]
            f(nx, ny, new, way + 1)
        # 방향을 꺾게 하고 재귀 호출
        # 꺾고 꺾지 않고를 정하는 건 3회 꺾는 것을 요구하는 조건에
        # 따라서 만든 변수인 way를 통해 조절


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = -1
    dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    for i in range(N):
        for j in range(N):
            f(i, j, [], 0)
    print(f'#{tc} {cnt}')