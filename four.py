# creating an array of elements

numbers = [0, 1, 2, 3, 4, 5]

# referring to the index of an array 

firstElement = numbers[0]
secondElement = numbers[1]
thirdElement = numbers[2]   

# printing the elements

print (firstElement)
print (secondElement)
print (thirdElement)

# using a loop to print the elements

for number in numbers:
    print (number)

for i in range(len(numbers)):
    print (f"Element at index {i+1} is", numbers[i])