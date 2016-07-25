__author__ = 'ws'

def solution(A):
    print(A)
    if len(A)<3:
        return 0
    peaks = list(findPeaks(A))
    print(peaks)
    if len(peaks)<2:
        return len(peaks)


def findPeaks(A):
    for i in range(1,len(A)):
        if A[i]> A[i-1] and A[i] > A[i+1]:
            yield  i


if __name__ == '__main__':
    print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))