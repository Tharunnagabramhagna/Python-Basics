# Bitwise operators

# 1)AND bitwise operation

a = 2
b = 3
print(a & b)  # output=2


# 2)OR bitwise operation

print(a | b)  # output=3
print(type(a | b))

# 3)XOR bitwise operation

print(a ^ b)  # output=1

# 4)NOT bitwise operation

print(~a)  # ouput=-3

# 5)Bitwise Left Shift(<<)

print(2 << 2)  # output=8

# 6)Bitwise Right Shift(>>)

print(2 >> 1)  # output=1
print(32 >> 2)  # ouput=8


'''Ex of bit:-
        1)6=0110   
         shortcut is 32 16 8 4 2 1 so..4+2=6 
         this are taken as 1 in bits
        2)10=1010
         shortcut is 32 16 8 4 2 1 so..8+2=10
         this are taken as 1 in bits
detailed:-      8 4 2 1
            10= 1 0 1 0
'''
'''Shortcut for NOT operation:-
      ex:-a=5
      print(~a) then output is -6
      shortcut is -(a+1)=-6

      same for any number

     watch this:- https://youtu.be/XbjQ-heGd58?si=b83r-zdyK3lzvz2m
'''
'''left shift shortcut
    ex:- x<<n
    ans= x*2pow(n)
'''
'''Right shift shortcut
      ex:- x>>n
      ans= x%2pow(n)
'''
# Calculate bitwise operation of any integer with this formula

print(bin(int(input("Enter a number: "))))

# Identity operator

a = 5
b = 5
print(id(a))
print(a is b)
print(id(a) == id(b))
