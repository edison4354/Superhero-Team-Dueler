# hero.py
import random


class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name 
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    '''Current Hero will take turns fighting the opponent hero passed in.'''
    # TODO: Fight each hero until a victor emerges.
    # Phases to implement:
    #1) randomly choose winner,
    #Hint: Look into random library, more specifically the choice method
    return random.choice([self.name, opponent.name])                

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    print(hero1.fight(hero2))

