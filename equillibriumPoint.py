a = [int(x) for x in input().split(' ')]
n = len(a)
flag = 1
if n == 1:
    print(1)
elif n == 2:
    print(-1)
else:
    l_sum = 0
    r_sum = 0
    sum = [0 for _ in range(n)]
    sum[0] = a[0]
    for i in range(1,n):
        sum[i] = sum[i-1] + a[i]
    for i in range(1, n-1):
        l_sum = sum[i] - a[i]
        r_sum = sum[n-1] - sum[i]
        if r_sum == l_sum:
            print(i+1)
            flag = 0
    if(flag):
        print(-1)



