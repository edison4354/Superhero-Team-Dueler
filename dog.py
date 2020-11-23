# dog.py
class Dog:
  # Required properties are defined inside the __init__ constructor method
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("Dog Initialized!")
  
  def bark(self):
    print("Woof!")

  def sit(self):
    print(f"{self.name} sits!")