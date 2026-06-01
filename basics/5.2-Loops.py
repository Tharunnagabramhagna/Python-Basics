# While loop example 2
i = 1
while i < 7:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
print(f"while loop has stopped at i value that is {i}")

# Looping with enumerate using lists
fruits = ["apple", "banana", "cherry"]
print("Fruits with their index:")
for index, fruits in enumerate(fruits):
    print(f"{index}:{fruits}")

# Looping with zip() function
fruits = ["apple", "banana", "cherry"]
colour = ["red", "yellow", "dark red"]
for fruits, colour in zip(fruits, colour):
    print(f"{fruits} is {colour}")
