#different classes we will use in our program
import random

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
  


def zombie_interaction(player, zombie, choice):
    """
    Handles a zombie encounter where the player can choose to attack or flee.

    Args:
        player (dict): Information about the player (health and damage)
        zombie (dict): Information about the zombie (health and strength)
        choice (str): Action the player takes ("attack" or "flee")

    Returns:
        tuple: Updated player dictionary, updated zombie dictionary, and a summary string describing the outcome
    """
    
    # Attack choice
    if choice == "attack":
        zombie.health -= player.strength
        if zombie.health <= 0:
            zombie.health = 0
            summary = f"You attacked the zombie for {player.strength} damage. Zombie is dead!"
        else:
            player.heatlh -= zombie.strength
            if player.heatlh < 0:
                player.heatlh = 0
            summary = f"You attacked the zombie for {player.strength} damage. Zombie attacks back for {zombie.strength} damage."
    
    # Flee choice
    elif choice == "flee":
        success = random.choice([True, False])
        if success:
            summary = "You successfully fled from the zombie!"
        else:
            player.health -= zombie.strength
            if player.health < 0:
                player.health = 0
            summary = f"You tried to flee but failed. Zombie attacks for {zombie.strength} damage."
    
    # Return the updated info
    return player, zombie, summary


