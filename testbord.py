T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    germs = [input().split() for _ in range(K)]
    for k in range(K):
        i = int(germs[k][0])
        j = int(germs[k][1])
        nums = int(germs[k][2])
        direction = int(germs[k][3])
        arr[i][j] = 1
        print(arr)