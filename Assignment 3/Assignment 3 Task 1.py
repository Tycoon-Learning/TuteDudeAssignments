def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n - 1)

n = int(input("Enter a number to calculate its factorial: "))

# Calculate and print the factorial
print(f"The factorial of {n} is: {factorial(n)}")