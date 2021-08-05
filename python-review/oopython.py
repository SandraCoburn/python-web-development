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

  #Decorator -> with a class method, it can be called even if the class is not instantiated first
  @classmethod
  def adding_things(cls, num1, num2):
    return num1 + num2

  @staticmethod #we don't get access to the class parameters cls method
  def adding_things2(num1,num2):
    return num1, num2

print(PlayerCharacter.adding_things(4,5))
player1 = PlayerCharacter("JRyan",14)
print(player1.adding_things(2,3))
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

#FOUR PILLARS OF OOP
#Encapsulation is the binding of data and functions that manipulates that data -> bluprint to pass on to instances of that object
# Abstraction is getting access to only what is needed
#PRIVATE attributes: self._name -> the underscores let other developers know it's a private variable


#INHERITANCE
class User:
  def __init__(self,email):
    self.email = email

  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self, name, power,email) -> None:
      User.__init__(self, email)
      
      self.name = name
      self.power = power

  def attack(self):
      print(f'attacking with power of:   {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows, email) -> None:
      super().__init__(email)
      self.name = name
      self.num_arrows = num_arrows
  def attack(self):
      print(f'attacking with arrows, arrows left:  {self.num_arrows}')


wizard1 = Wizard("Merlin", 50, "merlin@wizard.com")
archer1 = Archer("Robin", 100, "robin@archers.com")

print(isinstance(wizard1, User)) #True

print(wizard1.sign_in())
wizard1.attack()
archer1.attack()
print(wizard1.email)
print(archer1.email)

#Polymorphism -> we can modify our classes when needed
def player_attack(char):
  char.attack()

player_attack(wizard1)
player_attack(archer1)
print("*****************************************")
for char in [wizard1,archer1]:
  char.attack()

#Instrospection -> the ability to determine the type of an object at runtime -> dir
print(dir(wizard1))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
   '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']
'''