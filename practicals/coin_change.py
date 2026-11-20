def coin_change(coins, amount):
    dp = [0] + [float("inf")] * amount
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], 1 + dp[value - coin])
    return dp[amount] if dp[amount] != float("inf") else -1

coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))
print("Minimum number of coins:", coin_change(coins, amount))
