# Operations in list
list1 = ["true", "false", "pass", "fail"]
print(list1[2])
list2 = [1, 4, 7, 10, 13, 15]
print(list2[1])
print(len(list2))
print(list1[-1])
print(list2[2:4])  # 2,3 elemnts are printed
print(list2[1:])
print(list1[:3])
print(list2[::-1])  # used to reverse the list
print(list2[::2])  # Every other element is printed
# same as list1[-1]  #this code is used to acess the last element of list
print(list1[len(list1)-1])
print(list2 + [6, 7, 8])  # merging of two lists with addition
print(list2 * 2)  # repeating the list


# conditions in lists
list3 = ["apple", "banana", "cherry"]
if "apple" in list3:
    print("yes")
    list3[1] = "black current"
    print(list3)
# types of functions in lists
list4 = ["apple", "orange", "grapes"]
list4.append("banana")  # 1
print(list4)
# list4.insert("orange", "Watermelon")  # 2 (insert function can't be used for str )
# print(list4)
tropical = ["storm", "winter", "summer"]  # 3
list4.extend(tropical)
print(list4)
list4.remove("winter")  # 4
print(list4)
list4.pop(1)  # 5 #removes the last element in the list
print(list4)
list4.clear()  # 6
print(list4)
list4.reverse()  # 7
print(list4)
list4.sort()  # 8
print(list4)
list4.copy()  # 9
print(list4)


# insert function in numbers
numbers = [1, 2, 3, 4, 5]
numbers.insert(5, 6)
print(numbers)
