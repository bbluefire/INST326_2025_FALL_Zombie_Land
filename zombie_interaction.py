import random

def zombie_interaction(player, zombie, choice):
    # Use item
    if choice == "use item":
        if player["inventory"]:
            item = player["inventory"][0]
            player["health"] += 20
            player["inventory"].pop(0)
            summary = f"You used {item} and healed 20 HP."
        else:
            summary = "You have no items to use!"

    # Attack
    elif choice == "attack":
        zombie["health"] -= player["damage"]
        if zombie["health"] <= 0:
            zombie["health"] = 0
            summary = f"You attacked the zombie for {player['damage']} damage. Zombie is dead!"
        else:
            player["health"] -= zombie["strength"]
            if player["health"] < 0:
                player["health"] = 0
            summary = f"You attacked for {player['damage']} damage. Zombie attacks back for {zombie['strength']} damage."

    # Flee
    else: 
        chance = random.choice([True, False])
        if chance:
            summary = "You have successfully fled from the zombie, how lucky!"
        else:
            player["health"] -= zombie["strength"]
            if player["health"] < 0:
                player["health"] = 0
            summary = f"You tried to flee but failed. Zombie attacks for {zombie['strength']} damage."

    # Return updated player info
    return player, zombie, summary

         
    