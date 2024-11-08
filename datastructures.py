myList = ["ferrari" , "bmw" , "audi", "mercedes", "tesla", "lamborghini", "porsche", "bugatti"]

myDictionary = { 
    "brand": "ferrari",
    "model": "f430",
    "year": 2006
}

myTuple = ("banana", "apple", "cherry", "pineapple")

#lists

myListTwo = ["ford", "honda", "toyota"]

#myList.pop(1) #removes element at index 1

#del myList #deletes the list

#myList.clear() #clears the list



for x in myList:
    print(x)

i = 0
while i < len(myList):
    print(myList[i])
    i += 1

[print (x) for x in myList]

#list comprehensions

myList = ["apple", "banana", "cherry", "pineapple", "mango"]
#newList = [expression for item in iterable if condition == True]
newList =  [fruit for fruit in myList if x == "apple"]

newList = [fruit if fruit != "apple" else "cherry" for fruit in myList]

for fruit in myList:
    if fruit == "apple":
        newList.append("cherry")
    else:
        newList.append(fruit)

print(newList)

myList.sort(reverse=True)
print(myList)

newList = myList.copy()
print(newList)


