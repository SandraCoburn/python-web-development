#OOP - Object Oriented Programming Paradigm

class BigObject: #Class
  pass

obj1 = BigObject() #instantiate -> an instance of BigObject


class PlayerCharacter:
  #classs object attribute is not dynamic, it's static
  membership = True

  #Constructor function
  def __init__(self, name='anonymous',age=0):
    self.name = name #attribute
    self.age = age
 
  def run(self):
    if self.age > 18: 
      print("Welcome to the game")
    else:
      print("You are not old enough to play")
    return "Game started"

  
  def shout(self):
    print(f'my name is {self.name}')

player1 = PlayerCharacter("JRyan",14)
print(player1.name)
print(player1.run()) #run done
print(player1.membership) #True
print(player1.shout())
player2 = PlayerCharacter("Jackie", 19)
player2.shout()
print(player2.run())

'''
help(PlayerCharacter)

class PlayerCharacter(builtins.object)
 |  PlayerCharacter(name, age)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  run(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
'''


#Given the below class:
class Cat:
  species = 'mammal'
  def __init__(self, name, age):
      self.name = name
      self.age = age
    
   
# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Nala", 5)
cat2 = Cat("Milky", 2)
cat3 = Cat("Mishy", 8)

print(cat1.name)
# 2 Create a function that finds the oldest cat
def older(cat1, cat2,cat3):
  older = max(cat1.age, cat2.age, cat3.age)
  return older

x = older(cat1, cat2,cat3)
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {x} years old ')