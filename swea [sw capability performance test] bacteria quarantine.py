def timelapse


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    germs = [input().split() for _ in range(K)]
    for k in range(K):
        i = germs[k][0]
        j = germs[k][1]
        nums = germs[k][2]
        direction = germs[k][3]
        arr[i][j] = 1

# 인풋 제대로 받기


# 세균은 1시간마다 정해놓은 방향의 다음 셀로 이동한다.
# 만약 각 끝에 부딪히면,절반이 죽는다 num //2
# 같은 셀에서 만난 경우, 전부 더하되, 방향은 가장 많은 군집이었던 것
# 의 방향을 따라간다(같은 수끼리 만나는 경우는 없다!)
# 이동 전에 만남을 따지는 게 아니라, 이동하고 나서 셀 확인했을 때에
# 둘 이상의 군집이 같은 셀에 있으면, 그 때에 한다. 즉, 교차할 수 있다.
# 변수는 어떻게 진행해야 할까?

dir = {'1':(-1,0),
       '2':(1,0),
       '3':(0,-1),
        '4':(0,1),
       }
#방향 잡고 이동은 딕셔너리 콜하면서 이동하면 되고
#끝 라인에 접하면,
# if nx == N-1 or nx == 0 or ny == N-1 or ny == 0:
#방향을 꺾어주는 걸 설정하기