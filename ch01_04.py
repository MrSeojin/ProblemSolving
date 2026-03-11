#문자열 폭발
import sys
input = sys.stdin.readline

S = input()
boom = input()

Flag = True
while (Flag):
    Flag = False
    for i in range (len(S) - len(boom) + 1):
        if (boom == S[i : i + len(boom)]):
            S = S.replace(boom, '')
            Flag = True

print(S)
