list = ["summer", "winter", "autumn", "rainy"]
for x in list:
    if x == "summer":
        print("summer is hot")

# loops in lists

num1 = [1, 3, 5, 6, 2, 86, 34, 8, 2, 10]
ans = 0
for x in num1:
    if x > ans:
        ans = x
print(f"result={ans}")

# added two lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1+list2
print(list3)


x = ("apple", 'banana', "cherry")
y = list(x)
y[0] = "kiwi"
x = tuple(y)
print(x)
