def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def place(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            safe = True
            for previous in range(row):
                if board[previous] == col or abs(board[previous] - col) == abs(previous - row):
                    safe = False
                    break
            if safe:
                board[row] = col
                place(row + 1)

    place(0)
    return solutions

n = int(input("Enter number of queens: "))
solutions = solve_n_queens(n)
print("Number of solutions:", len(solutions))
for solution in solutions:
    for col in solution:
        print("." * col + "Q" + "." * (n - col - 1))
    print()
