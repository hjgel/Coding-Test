def binarySearch(n, pay_, maxpay):
    start = 0
    end = max(pay_)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(n):
            if pay_[i] >= mid:
                cnt += mid
            else:
                cnt += pay_[i]
        

        if cnt <= maxpay:
            start = mid + 1
        else:
            end = mid -1 
    return end

    

N = int(input())
pay = list(map(int, input().split()))
max_pay = int(input())
pay.sort()

print(binarySearch(N, pay, max_pay))
