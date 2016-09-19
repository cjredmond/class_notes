# for loop iterating over loop
l = [4,1,11,13]
ages = []
for person in l:
    petyears = person*7
    ages.append(petyears)
print(ages) # [28,7,77,91]

#comprehension

ages = [person*7 for person in l]

#only younger than 10

ages = [person*7 for person in l if person < 10]
###############################
#old way
list_of_numbers = [9, 10, 5 ,100 ,23 ,2]
half_val = []
for x in list_of_numbers:
    half_of_x = x / 2
    half_val.append(half_of_x)
print(half_val)
#############################
list_of_numbers = [6, 14, 82, 52, 2, 1, 14]
half_val = [x / 2 for x in list_of_numbers]
print(half_val)
#############################
#dictionary comprehension
#old way

list_of_numbers = [100, 67, 23, 45, 11]
square_numbers = {}

for x in list_of_numbers:
    square_numbers[x] = x ** 2
print(square_numbers)

#new way
list_of_numbers = [100, 67, 23, 45, 11]
square_numbers = {number: number ** 2 for number in list_of_numbers}
print(square_numbers)

################################
#nested comprehensions

matrix =    [["_", "X", "_"],
             ["O", "X", "O"],
             ["O", "X", "O"]]
target_column = []
for row in matrix:
    target_column.append(row[1])

print(target_column)

################################
matrix =    [["_", "X", "_"],
             ["O", "X", "O"],
             ["O", "X", "O"]]

target_column = [row[2] for row in matrix]
print(target_column)
