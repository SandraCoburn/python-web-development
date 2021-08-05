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

  def run(self):
    print("run really fast")

  def attack(self):
      print(f'attacking with arrows, arrows left:  {self.num_arrows}')

class HybridBorg(Wizard,Archer):
  def __init__(self, name, power, arrows, email):
    Archer.__init__(self,name, arrows, )
    Wizard.__init__(self,name,power)

hb1 = HybridBorg("borg1", 50,100, "test@email.com")
print(hb1.run())
print(hb1.attack())

wizard1 = Wizard("Merlin", 50, "merlin@wizard.com")
archer1 = Archer("Robin", 100, "robin@archers.com")

print(isinstance(wizard1, User)) #True

print(wizard1.sign_in())
wizard1.attack()
archer1.attack()
print(wizard1.email)
print(archer1.email)

