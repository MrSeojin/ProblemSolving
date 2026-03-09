#오셀로 재배치
'''
1. 배치한 말 중 임의의 2개의 말을 골라 서로의 위치를 바꾼다.
2. 말 1개를 들어 뒤집어 놓아 색상을 변경한다.
'''

T = int(input())

for _ in range(T):
    N = int(input())
    pre = input()
    goal = input()
    Black = 0
    White = 0
    for i in range(N):
        if (pre[i] == goal[i]):
            pass
        elif (pre[i] == 'B'):
            Black += 1
        else:
            White += 1
    if (Black < White):
        print (White)
    else:
        print (Black)
