class Animal:
  def __init__(self, name):
    self.name = name
  
  def eat(self):
    print(f"{self.name} is eating")

  def drink(self):
    print(f"{self.name} is drinking")

class Frog(Animal):
  def __init__(self, name):
    super().__init__(name)

  def jump(self):
    print(f"{self.name} is jumping")

eddy = Animal("Edison")
frog = Frog(eddy)
frog.eat()
frog.jump()