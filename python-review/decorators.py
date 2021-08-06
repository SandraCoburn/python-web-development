# DECORATORS have the @ before variable -> functions act like variables in memory -> decorators super charge our functions
# wraps another function and enhances it
#Higher Order Functions -> a function that accepts another option in its parameters -> or a function that returns another function
def greet(func):
  func()

def greet2():
  def func():
    return 5
  return func

#decorator pattern

def my_decorator(func):
  def wrap_func():
    print("***********")
    func()
    print("***********")
  return wrap_func

@my_decorator
def hello():
    print("helllloooo!")

hello() #***********
        #helllloooo!
        #***********

#Deorator with parameters
def my_decorator2(func):
  def wrap_func(x):
    print("***********")
    func(x)
    print("***********")
  return wrap_func

@my_decorator2
def hello2(greeting):
    print(greeting)

hello2("hiiii")

#Several arguments decotarors
def my_decorator3(func):
  def wrap_func(*args, **kwargs):
    print("***********")
    func(*args, **kwargs)
    print("***********")
  return wrap_func

@my_decorator3
def hello3(greeting, emoji=";)"):
    print(greeting, emoji)

hello3("hiiii", ":-)")

#performance decotaror
from time import time

def performance(fn):
  def wrapper(*args, **kawrgs):
    t1 = time()
    result = fn(*args, **kawrgs)
    t2 = time()
    print(f'took {t2-t1} s')
    return result
  return wrapper

@performance
def long_time():
  for i in range(10000):
    i*5

long_time()