# clean code
def is_even(num):
  return num % 2 == 0
    
print(is_even(51))


# *args **args
def super_func(*args):
  return sum(args)

print(super_func(1,2,3,4,5)) #15

def another_super_func(**kwargs):
  print(kwargs)
  total = 0
  for items in kwargs.values():
    total += items
  return total
print(another_super_func(num1=5,num2=10)) #{'num1': 5, 'num2': 10}

#List Slicing creates a new slice
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]
amazon_cart[0] ='laptop'
print(amazon_cart[0::2]) #['laptop', 'toys']
new_cart = amazon_cart[:] #coppy amazon cart
new_cart[0] = 'gum'
print(new_cart) #['gum', 'sunglasses', 'toys', 'grapes']
print(amazon_cart)#['notebooks', 'sunglasses', 'toys', 'grapes']

#Matrix -> multi dimensional lists
matrix = [ 
  [1,2,3],
  [2,4,6],
  [7,8,9]
]
print(matrix[0][1])

# List Methods
basket = [1,2,3,4,5]
#adding
print(basket) #[1, 2, 3, 4, 5]
print(basket.append(100)) #None
print(basket) #[1, 2, 3, 4, 5, 100]
basket.insert(3,200)
print(basket) #[1, 2, 3, 200, 4, 5, 100]

new_list = basket.extend([500])
print("new LIst",new_list) #new LIst None
new_list= basket
print(new_list) #[1, 2, 3, 200, 4, 5, 100, 500]

#removing
basket.pop() #removes at the end of the list
print(basket.pop(0)) #1 -> removes the first item and returns it 
print(basket) #[2, 3, 200, 4, 5, 100]
print(basket.remove(2)) # None -> returns nothing, only modifies the list by removin mumber 2
print(basket) #[3, 200, 4, 5, 100]
basket.clear() # removes all the items from list
print(basket) # []

#Index (item, start, finish) -> letters.index('d',0,2)
letters = ['x','a','b','c','d','e','f']
print(letters.index('d')) # 4 -> returns the index where the letter d is

#Python Keywords -> sorted() produces a new array
print('d' in letters) # True
print(letters.count("c")) # 1
# letters.sort() 
# print(letters) # ['a', 'b', 'c', 'd', 'e', 'f', 'x']
print(sorted(letters)) #['a', 'b', 'c', 'd', 'e', 'f', 'x'] 
copied_list = letters.copy() # copies the original list
copied_list.reverse()
print(copied_list) #['f', 'e', 'd', 'c', 'b', 'a', 'x']

print(letters[::-1]) # -> creates a new array and reverses it

#Range
print(list(range(1,20))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(20))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] -> starts at 0

#.join() creates a new item
sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name'])
print(new_sentence) # hi!my!name
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name'])
print(new_sentence) #hi my name
new_sentence = ' '.join(['hi', 'my', 'name'])
print(new_sentence) #hi my name

# List unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9] # -> assigns a variable to each item in list
print(a) # 1
print(b) # 2
print(c) # 3
print(other) #[4, 5, 6, 7, 8]
print(d) # 9

# None -> the abscense of value
weapons = None
print(weapons)

# Dictionary or dict -> data structure -> unordered key, value pairs
dictionary = {
  'a': [1,2,3],
  'b': 6,
}
print(dictionary['b']) # 6
print(dictionary['a'][1]) # 2

my_list_dict = [ 
  {'a':[4,5,6], 'b': "hello", 'c': True},
  {'a':[7,8,9], 'b': "hello", 'c': True}
]
print(my_list_dict[1]['a'][2]) # 9

#get() -> it will look for the key and if it's not there it will return None, no errors
print(dictionary.get('age')) # None
print(dictionary.get('age', 55)) # 55 -> it will look for age if not found it gill return default value 55

dictionary2 = dict(name='JohnC')
print(dictionary2) #{'name': 'JohnC'}

# Find an item in a dictionary
print("age" in dictionary2) #False
print('name' in dictionary2) #True

print('hello' in my_list_dict[0].values()) #True
print('a' in my_list_dict[0].keys()) #True

print(dictionary2.items()) #dict_items([('name', 'JohnC')])
dictionary3 = dictionary2.copy() # will copy the dictionary
dictionary2.clear() # -> will clear the dictionary and return an empty {}
print(dictionary2) #{}
print(dictionary3) # {'name': 'JohnC'}
dictionary3['age'] = 20
print(dictionary3.update({'age': 40}))
print(dictionary3)

#Tuples -> immutable list -> you can use list methods in tuples like len, in , slice, unzipping
my_tuple = (1,2,3,4,5,1,1)
# my_tuple[0] = 9 # TypeError: 'tuple' object does not support item assignment

new_tuple = my_tuple[1:4]
print(new_tuple) #(2, 3, 4)
print(my_tuple.count(1)) # 3 -> it counts how many times 1 is in tuple
print(my_tuple.index(4)) # 3 -> it returns the index of number 4

# Sets -> unordered collection of unique items(no duplicates)
my_set = {1,2,3,4,5,5}
print(my_set) #{1, 2, 3, 4, 5}

duplicate_list = [1,2,3,4,5,5,4,4,3,3,6,6,7,8,]
# make it into a set with no duplicates
no_duplicates_set = set(duplicate_list)
print(no_duplicates_set) #{1, 2, 3, 4, 5, 6, 7, 8}

#Sets methods
print("difference",no_duplicates_set.difference(my_set)) #difference {8, 6, 7}
print(my_set.discard(3))
print(my_set) #{1, 2, 4, 5}
#no_duplicates_set.difference_update(my_set) # -> it removes the numbers that are not in my_set
print(no_duplicates_set) #{3, 6, 7, 8}
print(my_set.intersection(no_duplicates_set)) #{1, 2, 4, 5} -> it will return the same numbers that are present in both sets

print(my_set.union(no_duplicates_set)) # {1, 2, 3, 4, 5, 6, 7, 8} -> it will combine both sets and remove duplicates
print(my_set | no_duplicates_set) # {1, 2, 3, 4, 5, 6, 7, 8} -> it will also combine both sets and remove duplicates

# Ternary Operator -> conditional expressions
#condition_if_true if condition else condition_if_else

is_friend = False
can_message = "message allowed" if is_friend else "not allowed"

print(can_message)

#Short Circuiting -> only one condidtion is true -> the interpreter stops evaluating after one condition is true

is_friend_true = True
is_User = True

if is_friend_true or is_User:
    print("best friends forever")

#Logical operators:
'''
>
<
==
!=
<=
>=
and
or
not
'''

# == checks for equality
print(True == 1) #true
print('' == 1)# false
print([] == 1)# false
print(10 == 10.0)# true
print([] == [])#true

# is checks for location in memory
print(True is True) #true
print('' is 1)# false
print([] is 1)# false
print(10 is 10.0)# false
print([] is [])#false

#Loops -> for loop will work with lists, tuples, sets, strings
for item in "The dance of the wind":
  #print(item)
  pass

for item in (1,2,3,4,5):
  for x in ['a','b','c']:
    print(item, x)

# iterable - list, dictionary, tuple, set, string -> one by one check each item in the collection

user_sample = {
  "name": "Golem",
  "age": 500,
  "can_swim": False
}
for item in user_sample:
  print(item)

for item in user_sample.values():
  print("value",item)

for item in user_sample.items():
  key,value = item
  print(key, value)

for key,value  in user_sample.items(): #same as above
  print(key, value)

my_adding_list = [1,2,3,4,5,6,7,8,9,10]

total = 0
for item in my_adding_list:
  total += item
print(total) #55


#Range object 
for item in range(10):
  print(item) # will print 0 to 9

for _ in range(0,10,2):
  print(_) # will print 0,2,4,6,8

for _ in range(5):
  print(list(range(10)))
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

#Enumerate will give you an index in an enumerable item
for i,char in enumerate('Helllloooo'):
  print(i, char)
'''
0 H
1 e
2 l
3 l
4 l
5 l
6 o
7 o
8 o
9 o
'''

for i, char in enumerate((list(range(100)))):
  if char == 50:
    print(i, char)

#while loop -> while a condition is true do something
i = 0
while i < 10:
  print(i)
  i = i + 1

# while True:
#   response = input("say something: ")
#   if (response == "bye"):
#     break

picture = [ 
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
]

# iterate over picture
  # if 0 -> print " "
  # if 1 -> print *

for row in picture:
  for pixel in row:
    if (pixel == 1):
      print("*", end=" ")
    else:
      print(" ", end=" " )  
  print(" ") #need a new line after every row
'''
      *        
    * * *      
  * * * * *    
* * * * * * *  
      *        
      *  
'''

#Find duplicates
some_list = [
  'a','b','c','b','c','m','n','n'
]
duplicates = []
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)
print(duplicates)