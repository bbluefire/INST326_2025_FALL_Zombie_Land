#different classes we will use in our program
import random

class Player:
  
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength
    ##here will be the self.inventory which will be a dictionary of weapons with certain damage and healthkit which will add certain amount of health
    self.inventory = {"weapons": [], "healthkits": []}
    
  def isalive(self):
    return self.health > 0

class Zombie:
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength
  def isalive(self):
    return self.health > 0
  
def use_item(player):
  print("Before combat choose: (1) Weapon (2) Healthkit (3) None")
  choice = input("Your choice: ").strip()
  if choice in ("1", "weapon"):
    if player.inventory["weapons"]:
      player.inventory["weapons"].pop(0)
      print("You used a weapons for + 10 strength")
      return 10
    else:
      print("You have no weapons")
      return 0

  elif choice in ("2", "healthkit"):
    if player.inventory["healthkits"]:
       player.inventory["healthkits"].pop(0)
       player.health += 20
       print (f"You used a health kit for + 20 health, new health is {player.health}")
       return 0
    else:
      print("You have no healthkits")
      return 0 
  else:
    print("You fight normally")
    return 0
    

def zombie_interaction(player, zombie, new_strength):
    """
    Handles a zombie encounter where the player can choose to attack or flee.

    Args:
        player (dict): Information about the player (health and damage)
        zombie (dict): Information about the zombie (health and strength)
        new_strength (int): new player damage

    Returns:
        tuple: Updated player dictionary, updated zombie dictionary, and a summary string describing the outcome
    """
    print (f"Choose Action: press 1 to attack or 2 to flee")
    choice = input("Your Choice: ").strip()
    
    # Attack choice
    if choice in ("1", "weapon"):
        zombie.health -= player.strength
        if zombie.health <= 0:
            zombie.health = 0
            print (f"You attacked the zombie for {player.strength} damage. Zombie is dead!")
            return True, False, False
        else:
            player.health -= zombie.strength
            print (f"You attacked the zombie for {player.strength} damage. Zombie attacks back for {zombie.strength} damage.")
            if player.health < 0:
                player.health = 0
                print("The zombie has killed you!")
                return False, True, False
            return True, True, False  
    
    # Flee choice
    elif choice in ("2", "flee"):
        success = random.choice([True, False])
        if success:
            print (f"You successfully fled from the zombie!")
        else:
            player.health -= zombie.strength
            if player.health < 0:
                player.health = 0
            print (f"You tried to flee but failed. Zombie attacks for {zombie.strength} damage.")
        return True, zombie.isalive(), True
    # Return the updated info
    return player, zombie, summary


def generate_item(player):
  #section for generating random loot with random benefits
  loot_type = random.choice(["weapon", "healthkit"])
  if loot_type == "weapon":
    print("You found a weapon")
    player.inventory["weapons"].append("weapon")
  else:
    print("you found a healthkit")
    player.inventory["healthkits"].append("healthkit")
  
##determining zombie spawn
def spawn_zombies(round_num, start_health=50, start_strength=10, strength_increase=5):
  health = start_health + round_num * 5
  strength = start_strength + (round_num * strength_increase)
  print (f"New Zombie Alert! Health = {health} Strength = {strength}")
  return Zombie(health, strength)



##what happens in each round
def play_round(player, round_num):
  zombie = spawn_zombies(round_num)
  boosted_strength = use_item(player)
  new_strength = player.strength + boosted_strength

  #here will have choice to use an item
  while True:
     player_alive, zombie_alive, player_ran = zombie_interaction(player, zombie, new_strength)
     print (f"Choose Action: (1) attack or (2) flee")
     choice = input("Your Choice: ").strip()
     player_alive, zombie_alive, player_ran = zombie_interaction(player, zombie, new_strength)
     if not player_alive:
       return False, False, False
     if player_ran:
       return True, False, True
     if not zombie_alive:
       return True, True, False


##running the game on x rounds
def run_game(rounds=5):
  player = Player(health=100, strength=20)
  score = 0
  print("Game Start!")
  for round_num in range(1, rounds + 1):
    print (f"Round {round_num}")
    player_alive, killed_zombie, ran = play_round(player, round_num)
    if killed_zombie:
      score += 1
      print (f"Zombie killed score = {score}")
      if not player_alive:
        print (f"You lost, final score: {score}")
        return
      if ran:
        print("you ran away, round over")
  print (f"Game over, you survived {rounds}'s with a score of {score}")


if __name__ == "__main__":
    run_game()
