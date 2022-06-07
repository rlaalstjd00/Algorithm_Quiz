def solution(n, times):
    left = 0
    right = 20000000000000

    while left + 1 < right :
        mid = (left + right) // 2
        k = 0

        for i in range(0, len(times)) :
            k += mid // times[i]
        
        if k >= n:
            right = mid
        else:
            left = mid
    
    return right