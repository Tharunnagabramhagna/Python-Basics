# While loop example 1
i = int(input("Enter your number:"))
ans = 0
while i > 1:
    ans += 1
    if i % 2 == 0:
        i /= 2  # i=i/2
    else:
        i -= 1  # i=i-1
print(f"result={ans}")

# Nested loops

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

# Looping through lists
# 1)
fruits = ["apple", "banana", "cherry"]
print("My fruits are:")
for x in fruits:
    print(x)

# 2)
fruits = ["apple", "banana", "cherry"]
print("\nMy fruits in Reverse: ")
for x in reversed(fruits):
    print(x)


# list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"squares from 1 to 5 are: {squares}")
