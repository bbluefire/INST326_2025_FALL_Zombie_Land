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
    print f"Choose Action: (1) attack or (2) flee"
    choice = input("Your Chouce: ").strip()
    # Attack choice
    if choice == "attack":
        zombie.health -= player.strength
        if zombie.health <= 0:
            zombie.health = 0
            print f"You attacked the zombie for {player.strength} damage. Zombie is dead!"
            return True, False, False
        else:
            player.heatlh -= zombie.strength
            print f"You attacked the zombie for {player.strength} damage. Zombie attacks back for {zombie.strength} damage."
            if player.heatlh < 0:
                player.heatlh = 0
                print("The zombie has killed you!")
                return False, True, False
            return True, True, False  
    # Flee choice
    elif choice == "flee":
        success = random.choice([True, False])
        if success:
            print f"You successfully fled from the zombie!"
        else:
            player.health -= zombie.strength
            if player.health < 0:
                player.health = 0
            print f"You tried to flee but failed. Zombie attacks for {zombie.strength} damage."
        return True, zombie.isalive(), True
    
    # Return the updated info
    return player, zombie, summary
def spawn_zombies(round_num, start_health=50, start_strength=10, strength_increase=5):
  health = start_health + round_num * 5
  strength = start_strength + (round_num * strength_increase)
  print f"New Zombie Alert! Health = {health} Strength = {strength}"
  return Zombie(health, strength)

def play_round(player, round_num):
  zombie = spawn_zombies(round_num)
  while True:
     print f"Choose Action: (1) attack or (2) flee"
     choice = input("Your Chouce: ").strip()
     player_alive, zombie_alive, player_ran = zombie_interaction(player, zombie, choice)
     if not player_alive:
       return False, False, False
     if player_ran:
       return True, False, True
     if not zombie_alive:
       return True, True, False

def run_game(rounds=5):
  player = Player(health=100, strength=20)
  score = 0
  print("Game Start!")
  for round_num in range(1, rounds + 1):
    print f"Round {round_num}"
    player_alive, killed_zombie, ran = play_round(player, round_num)
    if killed_zombie:
      score += 1
      print f"Zombie killed score = {score}"
      if not player_alive:
        print f"You lost, final score: {score}"
        return
      if ran:
        print("you ran away, round over")
  print f"Game over, you survived {round}'s with a score of {score}"

  
