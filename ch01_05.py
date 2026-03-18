# 십자말 풀이;l;
import sys
input = sys.stdin.readline

A, B = map(str, input().split())

array = [['.']*len(A) for _ in range(len(B))]

for c in range (len(A)):
    r =B.find(A[c])
    if r != -1:
        break

    for a in range (len(A)):
        array[r][a] = A[a]
    for b in range (len(B)):
        array[b][c] = B[b]

for i in range (len(B)):
    print(''.join(array[i]))