#convert list to string
fruits = [ 'apple', 'orange', 'mango', 'papaya', 'guava']
listAsString =  ' '.join(fruits)
print(listAsString)

#convert string to list
print(listAsString.split(' '))

#In the list data structure of python we count the number of occurrences of an element by using count() function.
fruits = [ 'apple', 'orange', 'mango', 'papaya', 'guava']
print(fruits.count('apple'))
print(fruits[::-1])  # reverse the list
                   
#reverse a string
codestring = "abcdefg"
reversed_string = codestring[::-1]
print(reversed_string)

#using reversed funtion
codestring = "abcdefg"
reversed_string = "".join(reversed(codestring))
print(reversed_string)

# Sort list
my_list = [3, 4, 1, 2]
my_list.sort()
print(my_list)
my_list = [3, 4, 1, 2]
sorted_list = sorted(my_list)
print(sorted_list)

#Using the sort function from the operator module:
from operator import itemgetter

my_list = [{"a": 3}, {"a": 1}, {"a": 2}]
sorted_list = sorted(my_list, key=itemgetter("a"))
print(sorted_list)
