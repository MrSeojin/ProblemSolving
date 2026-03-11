# ACM Hotel
import sys
input = sys.stdin.readline

T = int(input())

room = []
for _ in range(T):
    H, W, N = map(int, input().split())
    if (N % H == 0):
        room.append( (H * 100) + (N//H))
    else:
        room.append( (N % H)*100 + (N//H) + 1 )

for a in range (T):
    print(room[a])