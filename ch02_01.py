# 동전 0
'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = []
for _ in range (N):
    arr.insert(0, int(input()))

count = 0
for coin in arr:
    if K == 0:
        break
    count += K // coin
    K %= coin

print(count)
