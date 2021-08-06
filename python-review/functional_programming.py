#Pure functions -> has no side effects -> always produces the same result
def multiply_by2(li):
  new_list = []
  for item in li:
    new_list.append(item*2)
  return new_list

print(multiply_by2([1,2,3])) #[2,4,6]

# BUILT IN FUNCTIONS: map, filter, zip and reduce

#map(action, [1,2,3])
def multiplyby_2(item):
  return item*2

print(list(map(multiplyby_2, [1,2,3]))) #[2, 4, 6] -> it creates a new list, it doesn't affect the original list

def check_odd(item):
  return item % 2 != 0

print(list(filter(check_odd, [1,2,3]))) # [1,3] -> filters

my_list = [1,2,3]
your_list = 10,20,20

print(list(zip(my_list, your_list))) #[(1, 10), (2, 20), (3, 20)] -> it will zip the items combines
their_list = (4,7,9)
print(list(zip(my_list, your_list, their_list))) #[(1, 10, 4), (2, 20, 7), (3, 20, 9)]

from functools import reduce

def accumulator(acc, item):
  print(acc, item)
  return acc + item

print(reduce( accumulator, my_list,0)) #6 -> it will return a value from adding the list items together


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_names(name):
  return name.upper()
 
print(list(map(capitalize_names, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def filter_nums(num):
  return num > 50

print(list(filter(filter_nums, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def combined_nums(acc, num):
  return acc + num

total = reduce(combined_nums, my_numbers, 0)+ reduce(combined_nums, scores,0)
print(total)
#or
print(reduce(accumulator, (my_numbers + scores)))

#Lambda expresions -> anonymous functions that we need to use only once so they don't need a name
## lambda param: action(param)

print(list(map(lambda item: item *8, scores)))
print(list(filter(lambda item: item % 2 != 0, scores)))
print(reduce(lambda acc, item: acc + item, scores))

another_list = [5,4,3]
print(list(map(lambda item: item **2, another_list)))

#List sorting
tuple_list = [(90,2),(4,3), (9,9), (10,-1)]

tuple_list.sort(key=lambda x: x[1])
print(tuple_list)

# List, set, dictionary Comprehension -> my_list = [param for param in iterable]

#list
comp_list = [char for char in "hello"]
print(comp_list) #['h', 'e', 'l', 'l', 'o']

range_list = [num for num in range(0,20)]
print(range_list)

range_list_mult = [num ** 2 for num in range(0,20) if num % 2 ==0] # -> loop through a list return every number to power of 2 if the number is even
print(range_list_mult)

# set
comp_set = {char for char in "hello"}
print(comp_set) #{'o', 'h', 'e', 'l'}
range_set = {num for num in range(0,20)}
print(range_set)
range_set_mult = {num ** 2 for num in range(0,20) if num % 2 ==0} 
print(range_set_mult)

#dictionary
simple_dict = {'a':1, 'b':2}
my_dict = {key: value**2 for key,value in simple_dict.items() if value %2 == 0} #{'b': 4}
print(my_dict)
another_dict = {num: num*2 for num in [1,2,3,4]}
print(another_dict)

duplicate_list = ['a','b','c','b','d','n','n']
duplicates = list(set([item for item in duplicate_list if duplicate_list.count(item) > 1])) #['n', 'b']
print(duplicates)