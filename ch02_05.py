# 체육복
import sys
input = sys.stdin.readline


def solution(n, lost, reserve):
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    _reserve.sort()
    for i in _reserve:
        if i -1 in _lost:
            _lost.remove(i -1)
        elif i +1 in _lost:
            _lost.remove(i +1)

    return n - len(_lost)

num = int(input())

lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

print(solution(num, lost, reserve))

'''
n	lost	reserve	    return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	        4
3	[3]	    [1]     	2
'''