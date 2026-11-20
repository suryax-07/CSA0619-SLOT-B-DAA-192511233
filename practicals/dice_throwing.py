def dice_ways(dice, faces, target):
    dp = [[0] * (target + 1) for _ in range(dice + 1)]
    dp[0][0] = 1

    for d in range(1, dice + 1):
        for total in range(1, target + 1):
            for face in range(1, faces + 1):
                if total >= face:
                    dp[d][total] += dp[d - 1][total - face]
    return dp[dice][target]

dice = int(input("Number of dice: "))
faces = int(input("Number of faces on each die: "))
target = int(input("Target sum: "))
print("Number of ways:", dice_ways(dice, faces, target))
