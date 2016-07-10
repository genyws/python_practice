__author__ = 'ws'

def solution(A):
    max_slice_ending_here = A[0]
    max_slice = A[0]

    for element in A[1:]:
        max_slice_ending_here = max(element, max_slice_ending_here+element)
        max_slice = max(max_slice, max_slice_ending_here)

    return max_slice


if __name__ == '__main__':
#     A[0] = 3  A[1] = 2  A[2] = -6
# A[3] = 4  A[4] = 0
    print(solution([3,2,-6,4,0,-1,3]))