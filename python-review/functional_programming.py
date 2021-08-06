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

