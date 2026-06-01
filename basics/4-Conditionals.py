# Example 1
m = int(input("Enter the rating of MAD square movie:"))
c = int(input("Enter the rating of court movie:"))
n = int(input("enter the rating of  HIT3 movie:"))
if m > c and m > n:
    print('i will go to mad square movie')
elif n > m and n > c:
    print('i will go to HIT3 movie')
else:
    print('i will go to court movie')

# shortcut method
age = 17
message = "Eligible" if age >= 18 else "not eligible"
print(message)

# Example 2
age = 19
license = False

if age >= 18 and license:
    print("you are allowed to drive the vehicle")
elif age >= 18 and not license:
    print("sir please get a driving license")
else:
    print("you are too young to drive a vehicle")

# Nested conditionals
score = 94
if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A")
    elif score >= 80:
        print("You got an B")
    elif score >= 70:
        print("You got an C")
    else:
        print("You got an D")
else:
    print("You failed")
