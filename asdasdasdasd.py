hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def htod(num):  # 숫자를 받았을 때에 거꾸로 세면서 16*16*16....
    d = 0
    for i in range(len(num)):
        char = num[i]
        if char.isdigit():
            d += int(char) * (16 ** (len(num) - i - 1))
        else:
            d += hex[char] * (16 ** (len(num) - i - 1))
    return d


def dtob(num):  # 10진수를 2진수로 변환
    result = ''
    while num >= 2:
        result = str(num % 2) + result
        num = num // 2
    if num:
        result = str(num) + result
    return result, len(result)


def cnt_1(num):
    global ans
    num = htod(num)
    num, length = dtob(num)

    cnt = 0
    max_cnt = 0
    for i in range(length):
        if num[i] == '1':
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0

    if max_cnt < cnt:
        max_cnt = cnt

    return max_cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    hexa = input().strip()
    ans = cnt_1(hexa)
    print(f'#{tc} {ans}')