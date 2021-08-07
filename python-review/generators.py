# Generators
# list(range(100)) # creates a list in memory
# range(100) # it creates it one by one

from typing import Iterator


def make_list(num):
  result = []
  for i in range(num):
    result.append(i*2)
  return result

my_list = make_list(100) # this uses up memory
print(my_list)

# __iter__ iterable has this method under the hood
# Generators are iterable

def generator_function(num):
  for i in range(10):
    yield i #pauses the function 
  
g = generator_function(10)
next(g) #next will continue the function to the next iteration
next(g)
print(next(g))

for item in generator_function(10):
  print(item)

def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print("iterator", iterator)
      print(next(iterator) * 2)
    except StopIteration:
      break
special_for([1,2,3,4])
# It shows the same space in memory for every iteration:
'''
iterator <list_iterator object at 0x10fe84be0>
2
iterator <list_iterator object at 0x10fe84be0>
4
iterator <list_iterator object at 0x10fe84be0>
6
iterator <list_iterator object at 0x10fe84be0>
8
iterator <list_iterator object at 0x10fe84be0>
'''

# Create a range function
class MyGen():
    current = int
    def __init__(self, first, last):
      self.first = first
      self.last = last
      MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
          num = MyGen.current
          MyGen.current += 1
          return num
        raise StopIteration


gen = MyGen(0,10)

for i in gen:
  print(i)
print("*************************************")
# Fibonacci number with a generator
def fib(num):
  first = 0
  second = 1

  for i in range(num):
    yield first
    temp = first
    first = second
    second = temp + second

for x in fib(10):
  print(x)
    
# Fibonacci number with a list
def fib2(num):
  first = 0
  second = 1
  result = []
  for i in range(num):
    result.append(first)
    temp = first
    first = second
    second = temp + second
  return result
print(fib2(20))

