# Example 1 of "For loop"
count = 0
for num in range(1, 10):
    if num % 2 == 0:
        count += 1
        print(num)
print(f"we have {count} even numbers")


# Example 2 of "For loop"
print("counting numbers from 1 to 5")
for i in range(1, 6):
    print(i)

print("\nReversed counting of numbers from 5 to 1")
for i in range(5, 0, -1):
    print(i)

# Same Example in while loop
# 1)
count = 1
print("While loop")
while count <= 5:
    print(count)
    count += 1
# 2)
count = 5
print("\nReversed While loop")
while count >= 1:
    print(count)
    count -= 1
