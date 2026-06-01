# addition of two inputs of my own
num1 = float(input("Enter your num1:"))
num2 = float(input("enter your num2:"))
print(num1+num2)
print(type(num1+num2))
print(
    f"you have entered{num1},you have entered{num2},final result is{num1+num2}")

# Working with multiple inputs on one line
x, y = input("Enter two values seperated by space: ").split()
print(f"first value:{x},second value:{y}")

# f string method
age = int(input("Enter your age: "))
time_turns_100 = 100-age
print(f"you will be 100 in {time_turns_100} more years")

# choice in input and outputs
user_choice = input("Enter a colour (or click enter for default): ")
if user_choice == "":
    user_choice = "white"
print(f"selected colour is {user_choice}")
