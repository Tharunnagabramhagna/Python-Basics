marvel = {"iron man": 1000, "thor": 900, "hulk": 700}
print(len(marvel))
print(marvel["iron man"])
x = marvel.keys()
print(x)
marvel["superman"] = 1200
print(x)
# list in dit
x = list(marvel.values())
print(x)
marvel["spiderman"] = 800
print(marvel)

# functions in dictionary

print(marvel.get("iron man"))  # 1
print(marvel.keys())  # 2
print(marvel.values())  # 3
print(marvel.items())  # 4
print(marvel.pop("thor"))  # 5
print(marvel.popitem())  # 6
print(marvel.clear())  # 7

# loops in dict

fruits = {"apple": 30, "banana": 50, "grapes": 100}
for x in fruits:  # 1
    print(x)
    print(fruits[x])
for x in fruits.values():  # 2
    print(x)
for x in fruits.keys():  # 3
    print(x)
for x, y in fruits.items():  # 4
    print(x, y)

# SETS

set = {"apple", "banana", "cherry", "apple",
       True, 1, 2, False, 0}  # True==1 , False==0
print(set)
for x in set:  # 1
    print(x)
print("apple" in set)  # output==True #2
set.add("orange")  # 3
print(set)
set2 = ("tharun", "rohith", "varun")  # 4
set.update(set2)
print(set)
set.remove("apple")  # 5
print(set)

# Loop with dictionaries
person = {"name": "Tharun", "age": 17, "city": "Madanapalle"}
print("\nperson's dict")
for key, value in person.items():
    print(f"{key}:{value}")
