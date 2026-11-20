def subset_sum(values, target):
    answers = []
    def search(index, chosen, total):
        if total == target:
            answers.append(chosen[:])
            return
        if index == len(values) or total > target:
            return
        search(index + 1, chosen + [values[index]], total + values[index])
        search(index + 1, chosen, total)
    search(0, [], 0)
    return answers

values = list(map(int, input("Enter positive numbers: ").split()))
target = int(input("Enter target sum: "))
answers = subset_sum(values, target)
print("Subsets with target sum:")
for answer in answers:
    print(answer)
if not answers:
    print("No subset found.")
