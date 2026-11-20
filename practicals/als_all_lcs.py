def all_lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    memo = {}
    def build(i, j):
        if i == m or j == n:
            return {""}
        if (i, j) in memo:
            return memo[(i, j)]
        answers = set()
        if a[i] == b[j]:
            answers = {a[i] + tail for tail in build(i + 1, j + 1)}
        else:
            if dp[i + 1][j] >= dp[i][j + 1]:
                answers |= build(i + 1, j)
            if dp[i][j + 1] >= dp[i + 1][j]:
                answers |= build(i, j + 1)
        memo[(i, j)] = answers
        return answers

    return sorted(build(0, 0))

first = input("Enter first string: ")
second = input("Enter second string: ")
answers = all_lcs(first, second)
print("All longest common subsequences:")
for item in answers:
    print(item)
