#십자말 풀이

A, B = map(str, input().split())
Flag = False
array = [['.']*len(A) for _ in range(len(B))]

for i in range (len(A)):
    for j in range (len(B)):
        if (A[i] == B[j]):
            for a in range (len(A)):
                array[j][a] = A[a]
            for b in range (len(B)):
                array[b][i] = B[b]
            Flag = True
            break
    if (Flag):
        break

for i in range (len(B)):
    print(''.join(array[i]))