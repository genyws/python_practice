__author__ = 'ws'

def solution(A):
    if len(A)<3:
        return 0
    nextPeak = createNextPeaks(A)
    from math import sqrt
    maxFlag= int(sqrt(len(A)))+1
    pos = 0
    result = 0
    for d in range(maxFlag,0,-1):
        pos = 0
        flags = 0
        while pos < len(A) and flags <= d:
            pos = nextPeak[pos]
            if pos == -1:
                break
            else:
                flags+=1
                pos = pos + d
        result = max(result,flags)
    return result

def createNextPeaks(A):
    result = [0]* len(A)
    result[len(A)-1] = -1
    for i in range(len(A)-2,0,-1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            result[i] = i
        else:
            result[i] = result[i+1]
    result[0] = result[1]
    return result

if __name__ == '__main__':
    print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))