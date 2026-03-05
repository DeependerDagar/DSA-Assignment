# AERT - Algorithmic Efficiency & Recursion Toolkit
# Name: Deepender
# Roll No: 2501730292
# Course: B.Tech CSE (AI ML), 2nd Semester
# Data Structures (ETCCDS202)
# School of Engineering & Technology
# Batch: 2025-26
# Submitted To: Mrs. Neetu Chauhan

# -------------------------------
# PART A: Stack ADT
# -------------------------------
class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# -------------------------------
# PART B: Factorial & Fibonacci
# -------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Naive Fibonacci
naive_calls = 0
def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# Memoized Fibonacci
memo_calls = 0
def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# -------------------------------
# PART C: Tower of Hanoi
# -------------------------------
def hanoi(n, source, aux, dest, stack, log):
    if n == 1:
        move = f"Move disk 1 from {source} to {dest}"
        log(move)
        stack.push(move)
        return
    hanoi(n - 1, source, dest, aux, stack, log)
    move = f"Move disk {n} from {source} to {dest}"
    log(move)
    stack.push(move)
    hanoi(n - 1, aux, source, dest, stack, log)


# -------------------------------
# PART D: Recursive Binary Search
# -------------------------------
def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main(log):
    log("=== Factorial Tests ===")
    for n in [0, 1, 5, 10]:
        log(f"{n}! = {factorial(n)}")

    log("\n=== Fibonacci Tests ===")
    for n in [5, 10, 20]:
        global naive_calls, memo_calls
        naive_calls = 0
        result_naive = fib_naive(n)
        log(f"Naive fib({n}) = {result_naive}, calls = {naive_calls}")
        memo_calls = 0
        result_memo = fib_memo(n, {})
        log(f"Memo fib({n}) = {result_memo}, calls = {memo_calls}")

    log("\n=== Tower of Hanoi (N=3) ===")
    stack = StackADT()
    hanoi(3, "A", "B", "C", stack, log)
    log("Moves stored in stack: " + str(stack.size()))

    log("\n=== Binary Search Tests ===")
    arr = [1, 3, 5, 7, 9, 11, 13]
    for key in [7, 1, 13, 2]:
        idx = binary_search(arr, key, 0, len(arr) - 1)
        log(f"Search {key}: Index = {idx}")
    log("Empty array test: " + str(binary_search([], 5, 0, -1)))


if __name__ == "__main__":
    # open file for writing
    with open("output.txt", "w") as file:
        # log function writes to both terminal and file
        def log(msg=""):
            print(msg)
            file.write(msg + "\n")

        main(log)