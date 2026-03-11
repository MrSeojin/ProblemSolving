# White square
import sys
input = sys.stdin.readline

count = 0   # 하얀칸 위에 말의 개수

for j in range(8):
    L = input()
    for i in range(8):
        if (i + j) % 2 == 0 and L[i] =='F':
            count += 1

print(count)