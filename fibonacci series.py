def fibonacci(n):
    fib_series = [0, 1] if n > 1 else [0] if n == 1 else "Please enter a positive integer."
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Test the function
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
print(f"Fibonacci series with {num_terms} terms:", fibonacci(num_terms))
