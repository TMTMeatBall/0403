# dxy = [(0,1),(0,-1),(-1,0),(1,0)]
# for di,dj in range(4)
# nx = x + dxy[direction][0]
# ny = y + dxy[direction][1]
# 0<=nx<4 and 0<=ny<4 #성립 조건

def NSEW(N, point, i, j):
    # 기저 조건
    if N == 6:
        relay.add(point)  # set은 중복허용x 중복input은 걸러짐
        return
    for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            # 재귀형태는 어떻게?
            NSEW(N + 1, point + array[ni][nj], ni, nj)

    #     if N == 6: #동서남북을 전부 종료한 시점에서,

    # 가지 치기
    # 겹치면 전부 날려준다
    # ni,nj가 격자를 벗어나면 전부 날린다.
    #
    # 메인 로직(재귀호출로 계속해서 계산해나갈 수 있도록
    # 겹치지 않으면 cnt에 반영해준다?


T = int(input())
for tc in range(1, T + 1):
    array = [input().split() for _ in range(4)] #array제대로 받기
    relay = set()
    for i in range(4):
        for j in range(4):
            NSEW(0, array[i][j], i, j)
            # 0은 포인터가 이동한 숫자를 말하고, 6이 넘은 순간 종료한다.
    ans = len(relay)
    print(f'#{tc} {ans}')
# 문제를 잘못 생각하였음
# arr[i][j]에서 동-중-서-중-남-중-북 으로 7개 지점을 찍는다고 생각했지만 그게 아니고
# 그냥 arrij가 자유롭게 7번 이동하고 나서 결과물을 저장하고,
# 중복을 허용하지 않게 만들면 된다.
