# 하나의 노드가 가능한 모든 연산은 -1 1 2 -10 으로 4가지.
# 백트래킹으로도 가능은 함. #단 재귀호출 한계에 걸릴 것
# 4가지 계산을 계속 타면서 가장 짧게, 해당 결과에 닿는 것을 채택하기
# 즉, bfs 문제임
# bfs (조건) 4종류 연산, 범위 내([1,1000000]), 중복 방지(visited등의 사용)
# bfs(s,e) #start end
# queue 생성, visited 생성
# 초기데이터 q 삽입, v[s] = 1
# while queue:
#   c = queue.pop(0)
#   if c == e: return v[c]
#   네방향(연산) 범위내, 중복불가
from collections import deque
def bfs(s, e):
    q = deque()
    v = [0] * 1000001  # 1~1백만까지

    q.append(s)
    v[s] = 1
    while q:
        c = q.popleft() #queue는 선입선출

        if c == e: #기저조건
            return v[c] - 1 #다음 도착점에서 다시 +1을 해서 방문했음을 찍어야 하기 때문에 -1해서 0으로 바꿔준다(그냥 객체로 0 지정하면 False를 답으로 반환함)

        # 4방향, 범위내 중복허용x #메인로직
        for n in ((c + 1), (c - 1), (c * 2), (c - 10)): #4방향 계산을 돌면서 행함.
            if 1 <= n <= 1000000 and v[n] == 0: #n이 정해진 범위를 벗어나지 않고 + 아직 방문하지 않았다면,
                q.append(n) #
                v[n] = v[c] + 1
    return # 만들 수 없는 숫자인 경우

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ans = bfs(N, M)
    print(f'#{tc} {ans}')
