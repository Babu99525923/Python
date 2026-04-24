import array

numbers = array.array('i',[10,20,30])
print(numbers)                                           

#accesing elements
print(numbers[0])
# Here i indicates the types of data it will be storing example  Integer float
# Whenever we print the numbers it will print with array only
# print(numbers)   will print array('i', [10, 20, 30])
# to print it clean either conver it to list


numbers.append(40)

print(numbers)

numbers.remove(20)
print(numbers)