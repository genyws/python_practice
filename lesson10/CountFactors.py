from math import *

def solution(N):
    factors = set()
    for i,j in [(i,int(N/i)) for i in range(1,int(sqrt(N))+1) if N%i==0]:
        factors.add(i)
        factors.add(j)
    return len(factors)

if __name__ == '__main__':
    print(solution(25))