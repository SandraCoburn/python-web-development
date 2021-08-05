#Functions -> should do one thing really well, should return something
#parameters and default parameters
def say_hello(name, emoji=None):
  print(f'Hello {name}, {emoji}')

#positional arguments
say_hello("Jackie","smile")

# keyword arguments
say_hello(emoji="smily", name="Sean")

#Return exits the function
def sum3(num1, num2):
  return num1 + num2

total = sum3(5,2)
print(sum3(9, total))

def sum2(num1, num2):
  def another_func(n1,n2):
    return n1 + n2
  return another_func(num1,num2)
print(sum2(10,20))

# Methods vs Functions
'''
list()
print()
max()
min()
input()
'''

def some_random_stuff():
  '''
  This function prints string to uppercase
  '''
  return "helloooo".upper()

print(some_random_stuff())

#Dunder method will print the comments from the function
print(some_random_stuff.__doc__) # This function prints string to uppercase

#Clean code
def is_even(num):
  return num % 2 == 0

print(is_even(51)) #false

# *args and **kwargs
#Rule: params, *args, default parameters, **kwargs
def super_func(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

def highest_even(li):
  highest = 0
  for num in li:
    if num % 2 == 0:
      highest = max(highest, num)
  return highest


print(highest_even({10,2,3,4,8,11}))

#Walrus operator := assignment expression
a = "hellllllooooo"
if len(a) > 10:
  print(f'too long {len(a)} elements')

if ((n := len(a)) > 10):
  print(f'too long {n} elements')

#remove the last letter in every loop
while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]
print(a)

#Scope -> what variables do I have access to?
#Rules:
#1 - start with local
#2 - Parent locals?
#3 - Global
#4 - built in python functions

total = 0
def count():
  global total
  total += 1
  return total
print(count())
print(count())

#or
def count2(total):
  total += 1
  return total
print(count2(count2(count2(total))))