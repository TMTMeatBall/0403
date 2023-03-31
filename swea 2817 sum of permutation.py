# N개 자연수가 들어옴, 최소 1개의 수를 선택, 그 합이 K가 되는 경우의 수를 구하는 프로그램의 구현
def permute(i, N, K):
    global cnt
    # 기저조건
    if i == N:
        sum = 0
    # 가지치기
        if sum > K:
            return

        for i in range(N):
            if vis[i] == 1:
                sum += A[i]

        if sum == K:
            cnt += 1
        return

    # 메인 로직
    else:
        vis[i] = 0
        permute(i + 1, N, K)
        vis[i] = 1
        permute(i + 1, N, K)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    vis = [0] * N
    permute(0, N, K) #0~N까지 부분수열 구하고, 합이 K인 경우를 뽑아내는 함수 설정
    print(f'#{tc} {cnt}')

# 백트래킹 - 가능한 모든 경우를 답으로
# 복잡도 미리 검토
# 이진트리 -> 멀티트리
# 시각트리 구현해서 0(포함x) 1(포함함)의 형태 구현
# 0,1,2,3,4,...,N에 닿은 순간 종료되도록 설정
# 0에서의 포함/제외,1에서의 포함/제외,....,....,
