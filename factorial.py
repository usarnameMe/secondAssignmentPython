def factorial(n):
    if n == 0 or n == 1:
        return 1
    final_result = 1
    for i in range(2, n + 1):
        final_result *= i
    return final_result


def calculate_factorials(n):
    if n < 1:
        return "Input must be a positive integer."

    factorials = {}
    for i in range(n, 0, -1):
        factorials[i] = factorial(i)

    return factorials


try:
    n = int(input("Enter a positive number to calculate recursive factorial: "))
    if n <= 0:
        print("Input must be a positive integer.")
    else:
        result = calculate_factorials(n)
        print(result)
except ValueError:
    print("Invalid input! Please enter a positive integer.")
