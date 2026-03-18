# 오셀로 재배치
'''
1. 배치한 말 중 임의의 2개의 말을 골라 서로의 위치를 바꾼다.
2. 말 1개를 들어 뒤집어 놓아 색상을 변경한다.

3
5
WBBWW
WBWBW
7
BBBBBBB
BWBWBWB
4
WWBB
BBWB
'''
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    orig = input()
    goal = input()
    Black = 0
    White = 0
    for i in range(N):
        if orig[i] == 'B':
            if goal[i] == 'W':
                Black += 1
            continue
        elif orig[i] == 'W':
            if goal[i] == 'B':
                White += 1
            continue

    print(max(White, Black))
