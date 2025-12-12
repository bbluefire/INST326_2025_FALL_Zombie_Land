import random


starter_weapon = {
  
"Rusty Knife": 5
}

Random_Loot = {
    "BaseBall Bat": 10,
    "Pistol": 12,
    "Shotgun": 18,
    "RayGun": 25
}
print("\n\n====================================")
print(" Welcome to ZOMBIE LAND ")
print(" Your mission is to survive the zombie attacks.")
print(" Good luck, soldier.")
print("====================================\n\n")


class Player:

  def __init__(self, health, strength):
    
    self.health = health
    self.strength = strength
    self.max_health = health
    
    self.inventory = {"weapons": [], "healthkits": []}
    self.inventory["weapons"].append("Rusty Knife")
    self.inventory["healthkits"].append("healthkit")
    self.inventory["healthkits"].append("healthkit")
    print(f"You start with a Rusty Knife (+{starter_weapon['Rusty Knife']} strength)")
    print("You start with 2 Healthkits (+20 health each).")
    print(f"You start with 100HP. Make your next decison wisely.")

    
  def isalive(self):
    return self.health > 0

class Zombie:
  
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength
  
  def isalive(self):
    return self.health > 0
  
def use_item(player):
    """ A function that allows the player to choose one of three options: use a weapon, use a healthkit, use neither.

    Args:
        player(obj): an instance of the Player class

    Returns:
        int: returns the bonus damage for the player if the choice is a weapon
        None: returns none if the choice is healthkit or neither

    Author: Ryan Money
    Technique: f-string containing expression
    """
    print("Before combat choose: (1) Weapon (2) Healthkit (3) None")

    choice = input("Your choice: ").strip().lower()

    if choice in ("1", "weapon"):
        if player.inventory["weapons"]:
            # auto-equip the strongest weapon
            _, bonus = auto_equip_strongest(player)
            return bonus
        else:
            print("You have no weapons. Time to use your fists.")
            return None

    elif choice in ("2", "healthkit"):
        if player.health == player.max_health:
            print("You're at max health, You cannot use a healthkit.")
        else:
            if player.inventory["healthkits"]:
                player.inventory["healthkits"].pop(0)
                player.health += 20
                if player.health > player.max_health:
                    player.health = player.max_health
                print(f"You used a health kit for + 20 health, new health is {player.health}")
            else:
                print("You have no healthkits")

        print("Before combat choose: (1) Weapon (2) Healthkit (3) None")

        choice2 = input("Your choice: ").strip().lower()

        if choice2 in ("1", "weapon"):
            if player.inventory["weapons"]:
                # auto-equip strongest weapon here as well
                _, bonus = auto_equip_strongest(player)
                return bonus
            else:
                print("You have no weapons. Time to use your fists.")
                return None

        elif choice2 in ("2", "healthkit"):
            if player.health == player.max_health:
                print("You're at max health, You cannot use a healthkit.")
            else:
                if player.inventory["healthkits"]:
                    player.inventory["healthkits"].pop(0)
                    player.health += 20
                    if player.health > player.max_health:
                        player.health = player.max_health
                    print(f"You used a health kit for + 20 health, new health is {player.health}")
                else:
                    print("You have no healthkits")
            return None
        else:
            print("You fight normally.")
            return None

    else:
        print("You fight normally.")
        return None

  
    

def zombie_interaction(player, zombie, new_strength):
    """
    Handles a zombie encounter where the player can choose to attack or flee.

    Args:
        player (dict): Information about the player (health and damage)
        zombie (dict): Information about the zombie (health and strength)
        new_strength (int): new player damage

    Returns:
        tuple: Updated player dictionary, updated zombie dictionary, and a summary string describing the outcome
        
    Author: Mariam Sanni
    Technique: Conditional expressions
    
    """
    print("Choose Action: Press (1) to Attack or (2) to Flee:")
    choice = input("Your Choice: ").strip()
    
    if choice in ("1", "weapon"):
        zombie.health -= new_strength
        # Conditional expression to track zombie status
        zombie_status = "dead" if zombie.health <= 0 else "alive"
        
        if zombie.health <= 0:
            zombie.health = 0
            print(f"You attacked the zombie for {new_strength} damage. Zombie is {zombie_status}!")
            return True, False, False
    
        player.health -= zombie.strength
        # Conditional expression to track player status
        player_status = "dead" if player.health <= 0 else "alive"

        print(f"You attacked the zombie for {new_strength} damage. Zombie attacks back for {zombie.strength} damage.")
        print(f"Your health is now at {player.health} ({player_status}).")
        print(f"Zombie health is now at {zombie.health} ({zombie_status}).")
        
        if player.health <= 0:
            player.health = 0
            print("The zombie has killed you!")
            return False, True, False
        return True, True, False  
    
    # Flee choice
    elif choice in ("2", "flee"):
        success = random.choice([True, False])
        if success:
            stamina += 1
            print("You successfully fled from the zombie!")
            return True, zombie.isalive(), True
        else:
            player.health -= zombie.strength
            # Conditional expression to track player status after failed flee
            player_status = "dead" if player.health <= 0 else "alive"

            print(f"You tried to flee but failed. Zombie attacks for {zombie.strength} damage.")
            print(f"Your health is now at {player.health} ({player_status}).")
            
            if player.health <= 0:
                print("You died while fleeing!")
                return False, True, False
        
            return True, zombie.isalive(), True
        
    # Return the updated info
    print("You can't do that! You lose the current turn.")
    return True, zombie.isalive(), False



def generate_item(player):
  """function for generating either a healthkit or weapon

  Args:
      player (obj): an instance of the Player class
      
  Returns:
  N/a
  
  Author: Ryan Money
  Technique: use of a key function with the .keys and list
  """
  #section for generating random loot with random benefits
  loot_type = random.choice(["weapon", "healthkit"])
  
  if loot_type == "weapon":
    weapon = random.choice(list(Random_Loot.keys()))
    if player.inventory["weapons"]:
        dropped_weapon = player.inventory["weapons"].pop(0)
        print(f"You found a new {weapon}!(+{Random_Loot[weapon]} strength). You dropped your {dropped_weapon}.")
    else:
        print(f"You found a new {weapon}!(+{Random_Loot[weapon]} strength).")
    player.inventory["weapons"].append(weapon)
  else:
    print("You found a healthkit")
    player.inventory["healthkits"].append("healthkit")
    
#User's strongest weapon
def strongest_weapon(player, show=False):
    """
    Find and return the player's strongest weapon.

    Args:
        player (Player): The player with weapons in their inventory.
        show (bool, optional): If True, prints the strongest weapon. Defaults to False.

    Returns:
        tuple: (weapon_name, strength) or (None, 0) if no weapons.
        
   Author: Mariam Sanni
   Technique: Use of max() key function
   
    """
    weapon_name = max(player.inventory["weapons"], key=lambda w: Random_Loot.get(w, starter_weapon.get(w, 0)), default=None)
    strength = Random_Loot.get(weapon_name, starter_weapon.get(weapon_name, 0)) if weapon_name else 0
    if show and weapon_name:
        print(f"Your strongest weapon is {weapon_name} (+{strength} strength)")
    return weapon_name, strength
  
def auto_equip_strongest(player):
    """
    Automatically equips the strongest weapon from the player's inventory.

    Args:
        player (Player): The player object.

    Returns:
        tuple: (weapon_name, bonus_strength) of the equipped weapon, or (None, 0) if no weapons.

    Side effects:
        Removes the equipped weapon from inventory.
        Prints a message showing the equipped weapon.
        
    Author: Mariam Sanni
    """
    weapon_name, bonus = strongest_weapon(player)
    if weapon_name:
        # Remove the weapon from inventory immediately
        player.inventory["weapons"].remove(weapon_name)
        print(f"Auto-equipped {weapon_name} (+{bonus} strength)!")
        return weapon_name, bonus
    return None, 0



  
##determining zombie spawn after a round
def spawn_zombies(round_num, final_round, start_health=50, start_strength=10, 
                  strength_increase=5):
    """ 
    Spawn a zombie each round that gets stronger as the game progresses.
    
    Args: 
    round_num(int): The current round number.
    start_health(int): The start health of a zombie.
    start_strength(int): The start strength.
    strength_increase(int): The strenght increase of the zombie.
    
    Retuns:
    Zombie: A new instance of a zombie.
    
    Author: Kritagya Ghimire & Bethany Cruz
    """
    health = start_health + round_num * 5 # Zombies health increases 
    strength = start_strength + round_num * strength_increase #attack power increases
    #boss zombie chance only in final round
    is_boss = False
    if round_num == final_round and random.random() < 0.5:  #50% chance
            health *= 3
            strength *= 3
            is_boss = True
            print("!WARNING! BOSS ZOMBIE SPAWNED!")
    print (f"New Zombie Alert! Zombie Health = {health} Zombie Strength = {strength}.") # New zombie
    return Zombie(health, strength)



##what happens in each round
def play_round(player, round_num, final_round=5):
    """ 
    Function to handle the logic of a single round in the game.
    Args:
        player (Player): An instance of the Player class representing the 
            player.
        round_num (int): The current round number.
    
    Returns:
        tuple: A tuple containing three boolean values:
            - player_alive: True if the player is alive after the round, 
                False otherwise.
            - killed_zombie: True if the zombie was killed, False 
                otherwise.
            - player_ran: True if the player ran away, False otherwise.
    Author: Bethany Cruz
    """
    zombie = spawn_zombies(round_num, final_round)
    boosted_strength = use_item(player)
    new_strength = player.strength + (boosted_strength or 0)
    #here will have choice to use an item
    while True:
        player_alive, zombie_alive, player_ran = zombie_interaction(player, 
        zombie, new_strength)
        if not player_alive:
            return False, False, False
        
        if player_ran:
            return True, False, True
        
        if not zombie_alive:
            generate_item(player)
            return True, True, False
 


##running the game on x rounds
def run_game(rounds=5):
  """Function to run the game for a set number of rounds
      Args:
        rounds(int): number of rounds to play the game for
      Returns:
        score(int): final score of the player after all rounds
    Author: Bethany Cruz
  """
  player = Player(health=100, strength=20)
  score = 0
  
  print("\n--- GAME START ---\n")
  for round_num in range(1, rounds + 1):
    print(f"\n===== ROUND {round_num} =====\n")
    player_alive, killed_zombie, player_ran = play_round(player, round_num)
    
    if not player_alive:
        print (f"You lost, final score: {score}")
        return
    
    if killed_zombie:
      score += 1
      print (f"Zombie killed score = {score}")
      
    if player_ran:
      print("you ran away, round over")
  print (f"Game over, you survived {rounds}'s with a score of {score}")
  return score


if __name__ == "__main__":
    """ Runs the game, and asks player if they want to keep playing or exit.
    
    Author: Kritagya Ghimire
    
    """
    while True:
      final_score = run_game() 
    
      print("Hey Soldier, would you want to play again?")
      choice = input("(1) to play again or (2) Leave: ").strip().lower()
    
      if choice in ("1", "yes", "y"):
        print("Restarting New Game...")
        continue
      else:
        print("Thanks for playing soldier!")
        break


              
