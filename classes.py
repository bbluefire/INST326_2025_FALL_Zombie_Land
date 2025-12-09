#different classes we will use in our program

class PLayer:
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength
  def isalive(self):
    retrun self.heatlh > 0

class Zombie:
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength
  def isalive(self):
    return self.health > 0
  



