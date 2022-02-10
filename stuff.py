fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

def myfunt():
    if 2 > 1:
        print(x,y,z)

myfunt()

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

xyellow = "Hi"
print(type(xyellow))

import random
print(random.randrange(1,20))

#in python,strings are considered to be arrays
word = "Hello there random person how are you"
print(word[1])
print(len(word))

#check for a value in an array
print("Hello" in word)

if "dshjubvfsd" not in word:
    print(type(word))
    #slicing through an array
    print(word[3:22])

myList = [3, 5, 6, 7,7, 787878, 77]
if 24 in myList:
    print(myList[0])