def word_break(text, dictionary):
    dp = [False] * (len(text) + 1)
    dp[0] = True
    for i in range(1, len(text) + 1):
        for j in range(i):
            if dp[j] and text[j:i] in dictionary:
                dp[i] = True
                break
    return dp[-1]

words = set(input("Enter dictionary words separated by spaces: ").split())
text = input("Enter the text: ")
print("Can be segmented:", "Yes" if word_break(text, words) else "No")
