
n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

target = int(input("Enter target sum: "))

total = sum(arr)

dp = [False] * (total + 1)
dp[0] = True

for num in arr:
    for j in range(total, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

for i in range(target, total + 1):
    if dp[i]:
        print("Minimum Subset Sum:", i)
        break
else:
    print("No possible subset sum")
