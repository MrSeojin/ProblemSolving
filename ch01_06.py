#다트게임
'''
1S2D*3T
1D2S#10S
1D2S0T
1S*2T*3S
1D#2S*3S
1T2D3D#
1D2S3T*
'''
import sys
input = sys.stdin.readline

def solution(dartResult):
    answer = 0

    Flag = False
    num = [0 for i in range (2)]
    for c in dartResult:
        if ('0'<=c<='9'):
            if (Flag):
                num[-1] = num[-1] * 10 + int(c)
            else:
                num.append(int(c))
            Flag = True
            pass
        else:
            Flag = False
            if (c == '*'):
                num[-2] *= 2
                num[-1] *= 2
            elif(c == '#'):
                num[-1] *= -1
            elif (c == 'S'):
                pass
            elif(c == 'D'):
                num[-1] = num[-1]**2
            elif (c == 'T'):
                num[-1] = num[-1]**3

    for N in num:
        answer += N

    return answer


Score = input()
print(solution(Score))