# 부지는 N^2 최대한으로 긴 등산로..(max_cnt)
# 가장 높은 봉우리에서부터 시작하는 등산로..foriN for j N ...
# 딱 한 곳을 정해서 최대 K깊이만큼 깎을 수 있다(???????)
# 깎을 수 있는 크기 받고
# 그보다 최소필요량 깎기가 깎을 수 있는 만큼보다 작으면 한번 pass?
# dfs하되, 변수는 현재 등산로 길이, 공사 여부, 좌표
# 현재 등산로의 높이에 대해서 마주치는 친구와의 대소 관계를 비교합시다...
# mountain[nx][ny]-K < mountain[x][y] 반드시 만족해야 한다.

def construction(x, y, length, K):  # dfs구현 해보기
    global max_length

    if length > max_length:
        max_length = length

    visited[x][y] = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if peaks[nx][ny] < peaks[x][y]:
                visited[x][y] = 1
                construction(nx, ny, length + 1, K)
            elif K and peaks[nx][ny] - K < peaks[x][y] and visited[nx][ny] == 0:
                # 공사하고 나면 K에 0을 줄 것이므로 K가 존재할 때에,
                # 그리고 공사가 가능한 상황에,
                a = peaks[nx][ny]
                peaks[nx][ny] = peaks[x][y] - 1
                # 재귀는 하는데, 이제 공사 못하므로 K부분을 0으로 바꿔줍니다.
                visited[x][y] = 1
                construction(nx, ny, length + 1, 0)
                # length 반영했으므로 리스트 순회 에러가 나지 않도록 다시 원상복귀 시킵니다
                peaks[nx][ny] = a

    visited[x][y]=0

    # construction(nx, ny, total_length, K)  # 재귀하도록
    # if K:  # 공사가능여부 매번
    # 방문 처리를 하고 탐색이동을 반환함

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    peaks = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0  # 최대 등산로 길이
    highest = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if peaks[i][j] > highest:
                highest = peaks[i][j]


    for i in range(N):
        for j in range(N):
            if peaks[i][j] == highest:
                construction(i, j, 1, K)
                # 가장 높은 언덕의 높이가 같은 것이 여럿 있을 수 있으므로
                # 가장 높은 highest가 찍혔을 때에 첫 번째 등산로가 만들어지는 것이므로
                # , 1부터 시작하는 것이 바람직하다
                # 는 좌표, 0은 현재의 등산로 길이 K는 공사가능 깊이 또는 여부
                # K는 사용하고 나서 0으로 바꿔준다.
    print(f'#{tc} {max_length}')
