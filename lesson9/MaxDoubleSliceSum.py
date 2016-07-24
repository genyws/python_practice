import random
from string import printable


def solution(A):
    if len(A) == 3:
        return 0
    A=A[1:len(A)-1]
    print(A)
    leftMax = []
    leftMax.append(0)
    for i in range(1,len(A)):
        leftMax.append(max(leftMax[i-1]+A[i-1],leftMax[i-1]))
    rightMax = [0 for i in range(0,len(leftMax))]
    for i in range(-2,len(leftMax)*(-1)-1,-1):
        rightMax[i] = max(rightMax[i+1]+A[i+1],rightMax[i+1])
    print(leftMax)
    print(rightMax)
    maxDoubleSlice = 0
    for i in range(0,len(leftMax)):
        maxDoubleSlice = max(maxDoubleSlice,leftMax[i]+rightMax[i])
    return maxDoubleSlice

    # for i in range(1,len(A)):


if __name__ == '__main__':
    A = [3,2,6,-1,4,5,-1,2]
    print(solution(A))
    print(solution([6, 1, 5, 6, 4, 2, 9, 4]))
    # 1, 5, 6, 4, 2, 9
    # print(max_subarray(A))
    # print(A[1:1])