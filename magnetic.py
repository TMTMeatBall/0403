T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    #전치행렬 만들어보기
    # arr_t = list(zip(*arr)) #set출력
    arr_t = map(list,zip(*arr)) #리스트 출력
    for i in arr_t: #행단위 처리 전치행렬 위의 i가 돌면서
        prev = 0
        for n in i: #위에서 아래로 가는 것이므로 2를 만났을 때에 앞의 것이 0이면 교착상태인 것이 된다.
            #n은 i가 지나간 이전의 것을 살펴보는 것이므로,
            if n: #n이 값을 가졌다는 것은 뭔가 만났다는 뜻이고 0이 아닌 것만을 처리한다
                if n == 2 and prev == 1: #n이 S극이고, 이전의 것이 N극일 때에 교착상태가 된다
                    cnt += 1
                prev = n #n이 진행할 때마다, prev는 0에서 n이었던 값으로 바뀐다. n 바로 이전의 값이 되는 것.
    print(f'#{tc} {cnt}')


    #arr[i][j]에서 1일 때에 아래탐색해서 2찾고, 교착상태 1개 cnt 직전값이 1일 떄에 2를 만나면 교착 힌개
    #전치행렬로