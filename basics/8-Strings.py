# x=input("Enter the string:") # e.g. tharun == tthhaarruunn
# for t in x:
#     print(t+t,end="")
x = input('Enter your name:')
print(len(x))
if "ar" in x:
    print("ar undhi annaaa")
if "pu" not in x:
    print("undha ra brain undha")
print(x.upper())
print(x.lower())
print(x.strip())
print(x.replace("ar", "ru"))
print(x.split(" "))
print(x)
b = "Hello,World!"
print(b[2:5])
print(b[:5])
print(b[2:])
