x = ("apple", 'banana', "cherry")
y = list(x)
y[0] = "kiwi"
x = tuple(y)
print(x)
