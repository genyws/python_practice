__author__ = 'ws'

def solution(A):
    if len(A) <=1:
        return 0
    maxSoFar = 0
    maxEndingHere = 0
    minPrice = A[0]
    for i in range(0,len(A)):
        maxEndingHere = max(maxEndingHere, A[i]- minPrice)
        minPrice = min(minPrice,A[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar

if __name__ == '__main__':
  print(solution([23171,21011,21123,21366,21013,21367]))