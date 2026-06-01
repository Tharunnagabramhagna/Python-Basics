try:
    x = int(input("Enter your number: "))
    result = 10/x
    print(f"10 is divided by {x} to give {result}")
except ValueError:
    # run this code upto here and divide with zero to continue
    print("that's not a vaild number")
except ZeroDivisionError:
    print("you can't divide with zero")
finally:
    print("this code always works")
