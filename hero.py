# hero.py
import random
from ability import Ability
from armor import Armor 

class Hero:
  def __init__(self, name, starting_health=100):
    # Abilites and armors don't have starting values, and are set to empty lists on initialization
    self.abilities = list()
    self.armors = list()
    # We know the name of our hero, so we assign it here
    self.name = name 
    # Similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # When a hero is created, their current health is always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health

  def add_ability(self, ability):
    """Add ability to abilities list"""
    # Using the append method we add ability objects to our list.
    self.abilities.append(ability)
  
  def attack(self):
    """Return the sum of all the abilities attack damage"""
    total_damage = 0
    # Loop through all of our hero's abilities
    for ability in self.abilities:
      # Add the damage of each Ability() attack to our running total 
      total_damage += ability.attack()
    return total_damage
  
  def add_armor(self, armor):
    """Add armor to armors list"""
    # Using the append method we add armor objects to our 'self.armors' list.
    self.armors.append(armor)

  def defend(self):
    """Calculate the total block amount from all armor blocks."""
    total_block = 0
    # Loop through all of our hero's armors
    for armor in self.armors:
      # Add the block of each Armor() block to our total block
      total_block += armor.block()
    return total_block

  def take_damage(self, damage):
    """Updates self.current_health to reflect the damage minus the defense."""
    damage_after_defense = damage - self.defend()
    self.current_health -= damage_after_defense

  def is_alive(self):
    if self.current_health <= 0:
      return False
    else:
      return True

  def fight(self, opponent):
    """Current Hero will take turns fighting the opponent hero passed in."""
    if not self.abilities and not opponent.abilities:
      print("Draw!")

    while self.is_alive() and opponent.is_alive():
      # opponent taking damage
      taken_damage = self.attack()
      opponent.take_damage(taken_damage)
      # self taking damage
      opponent_damage = opponent.attack()
      self.take_damage(opponent_damage)
      print(self.current_health)

    if not self.is_alive() and not opponent.is_alive():
      print("Draw!")
    elif not self.is_alive():
      print(f"{opponent.name} won!")
    elif not opponent.is_alive():
      print(f"{self.name} won!")
    else:
      raise ValueError("Impossible values!")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

