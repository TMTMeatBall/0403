def hdiffs(i, N, B):
    global ans
    # 기저조건
    if i == N:
        sum = 0

        for i in range(N):
            if vis[i] == 1:
                sum += heights[i]

        if sum >= B:

            ans = min(ans, sum - B)

            return

    #메인 로직
    else:
        vis[i] = 0
        hdiffs(i + 1, N, B)
        vis[i] = 1
        hdiffs(i + 1, N, B)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    vis = [0] * N
    ans = 100000
    hdiffs(0, N, B)
    print(f'#{tc} {ans}')
# 부분 수열의 합을 구하듯이 vis따지면서 구하고 B와 비교하는 것.
# 답이 최솟값을 구하는 방식이므로, 크게 잡고 시작한다.
# 변수로 뭘 넣어야 높이차를 구해낼 수 있을까
