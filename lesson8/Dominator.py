def solution(A):
    if len(A) <1:
        return -1
    counter = {}
    for i in range(0,len(A)):
        cnt = counter.get(A[i],0)
        counter[A[i]] = cnt+1
    keys = counter.keys()
    print(keys)
    frequency = 0
    dominator = 0
    for key in keys:
        if counter.get(key) > frequency:
            frequency = counter.get(key)
            dominator = key
    if frequency > len(A)//2:
        ret =  [ i for i in range(0,len(A)) if A[i] == dominator]
        return ret[0]
    else:
        return -1

if __name__ == '__main__':
    print(solution([3,4,3,2,3,-1,3,3]))