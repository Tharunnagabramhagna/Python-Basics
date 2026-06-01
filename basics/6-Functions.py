# FUNCTIONS
def addition(num1, num2):
    return num1+num2


x = addition(10, 89)
print(x)


# RECURSION
def factorial(n):
    if n == 0:  # base case
        return 1
    else:  # recursion case
        return n*factorial(n-1)


print(factorial(5))


# SUM OF NUMBERS RECURSION
def add(n):
    if n == 0:
        return 0
    else:
        return n+add(n-1)


print(add(10))
