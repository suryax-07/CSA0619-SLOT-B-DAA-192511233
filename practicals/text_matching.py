def naive_search(text, pattern):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions

text = input("Enter text: ")
pattern = input("Enter pattern: ")
print("Pattern found at positions:", naive_search(text, pattern))
