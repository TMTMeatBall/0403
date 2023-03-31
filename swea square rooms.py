# 사방탐색하고 계속 이동하되,
# 매 시행마다 성공하면 cnt+1해주고,
# 더 이상 이동할 수 없는 경우에 탐색을 종료하고, 저장해둔 cnt값과
# 비교하고 가장 큰 cnt 를 정답으로 한다.
# cnt가 같다면, array[i][j]가 최소인 것을 출력합니다.
# nonpromising할 때가 종료조건?
# dfs하는게 맞겠지?
# 사방탐색을 하되, visited = 0이고,
# array[nx][ny] -1 = array[x][y] 를 만족할 때에,
# cnt + 1 하는 방식으로 간다.
# cnt가 같다면 방 번호가 더 작은 쪽을 선택한다.
# 기저조건


def search(k, l):
    global total_cnt #여기서 지정한 total_cnt는 max_cnt와 비교해야 하므로 글로벌 지정
    total_cnt += 1 #visited 찍힐 때마다 cnt +1 씩 반환
    visited[k][l] = 1 #방문하였음
    for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]: #사방탐색
        nk, nl = k + di, l + dj
        if 0<= nk < N and 0 <= nl < N: #사방 만족 조건,
            if array[nk][nl] == array[k][l] + 1: #사방탐색 후 이동가능조건
                search(nk,nl) #전부 만족하면, 이동했으므로 다시 재귀호출



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0 # total_cnt와 비교할 출력값
    number = 0 # max_cnt가 같은 경우에서 비교할 방 번호 기록
    visited = [[0] * N for _ in range(N)] #되돌아가는 경우 없도록 vis잡기


    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                total_cnt = 0
                search(i, j)
                if total_cnt > max_cnt:
                    max_cnt = total_cnt
                    number = array[i][j]
                elif total_cnt == max_cnt:
                    number = min(number, array[i][j])

    print(f'#{tc} {number} {max_cnt}')
# 뭐를 패러미터로 잡을까?
#
