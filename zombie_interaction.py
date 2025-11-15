import random

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
        zombie["health"] -= player["damage"]
        if zombie["health"] <= 0:
            zombie["health"] = 0
            summary = f"You attacked the zombie for {player['damage']} damage. Zombie is dead!"
        else:
            player["health"] -= zombie["strength"]
            if player["health"] < 0:
                player["health"] = 0
            summary = f"You attacked the zombie for {player['damage']} damage. Zombie attacks back for {zombie['strength']} damage."
    
    # Flee choice
    elif choice == "flee":
        success = random.choice([True, False])
        if success:
            summary = "You successfully fled from the zombie!"
        else:
            player["health"] -= zombie["strength"]
            if player["health"] < 0:
                player["health"] = 0
            summary = f"You tried to flee but failed. Zombie attacks for {zombie['strength']} damage."
    
    # Return the updated info
    return player, zombie, summary
    