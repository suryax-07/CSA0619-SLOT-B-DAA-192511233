def job_sequence(jobs):
    jobs.sort(key=lambda job: job[2], reverse=True)
    slots = [None] * (max((job[1] for job in jobs), default=0))
    total = 0
    for job_id, deadline, profit in jobs:
        for slot in range(min(deadline, len(slots)) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total += profit
                break
    return [job for job in slots if job is not None], total

n = int(input("Number of jobs: "))
jobs = []
print("Enter job id, deadline and profit:")
for _ in range(n):
    job_id, deadline, profit = input().split()
    jobs.append((job_id, int(deadline), int(profit)))
sequence, profit = job_sequence(jobs)
print("Selected job sequence:", sequence)
print("Maximum profit:", profit)
