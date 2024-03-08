# Fibonacci sequence generator
def fibonacci(n):
    fib_sequence = [0, 1]

    for _ in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

# Example: Generate and print the first 10 Fibonacci numbers
if __name__ == "__main__":
    n = 10
    result = fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {result}")
