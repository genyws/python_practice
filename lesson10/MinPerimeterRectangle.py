from math import *

def solution(N):
    perimeter = [ int(2*(i+(N/i))) for i in [i for i in range(1, int(sqrt(N))+1) if N % i == 0]]
    return min(perimeter)

if __name__ == '__main__':
    print(solution(31))