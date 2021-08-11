n = int(input())
price = [int(i) for i in input().split(' ')]
days = []

buy = 0
sell = 0
for i in range(1, n):
    if price[i] >= price[i - 1] and i != buy:
        sell = i
    elif buy == sell:
        buy = sell = i
    else:
        days.append([buy + 1, sell + 1])
        buy = sell = i

    if buy != n - 1 and sell == n - 1:
        days.append([buy + 1, sell + 1])

if len(days) == 0:
    print("No profit")

print(days)
