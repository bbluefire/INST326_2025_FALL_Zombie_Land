import math
import random

def zombie_spawns(round_num, player_position, zombie_spawn_points, 
                  current_zombies, max_zombies, min_player_distance = 5.0, 
                  boss_probability = 0.10):
    
    
    """ Decides how many zombies to spawn, their type, and where they appear.
    Args:
        round_num(int): the current round number
        player_position(tuple): the (x, y) position of the player
        zombie_spawn_points(list): possible spawn points for zombies
        current_zombies(int): number of zombies already on the map
        max_zombies(int): the maximum number of zombies allowed at once
        min_player_distance(float): the minimum distance from player to spawn
        boss_probability(float): the chance that a zombie is a boss

    Returns:
        list[dict]: A list of zombie dictionaries that include
                    "id", "type", "hp", and "pos".
                    Returns [] if there are no valid spawn points. """


    #starts off with 1 zombie and increases by 1 every 3 rounds (max 10)
    base_count = min(10, 1 + round_num // 3)

    #makes sure the number of zombies does not exceed the max limit
    remaining_capacity = max(0, max_zombies - current_zombies)
    if remaining_capacity == 0:
        return []
    target_count = min(base_count, remaining_capacity)

    #makes sure zombies spawn far enough away from the player
    px, py = player_position
    valid_points = []
    for (x, y) in zombie_spawn_points:
        distance = math.hypot(x - px, y - py)
        if distance >= min_player_distance:
            valid_points.append((x, y))

    #if there are no valid spawn points then stop spawning
    if not valid_points:
        return []

    #spawns zombies at random valid points
    spawns = []
    for zombie_id in range(target_count):
        pos = random.choice(valid_points)
        #decides if the zombie is a boss or a normal zombie
        if random.random() < boss_probability:
            spawns.append({"id": zombie_id, "type": "boss", "hp": 250, 
                           "pos": pos})
        else:
            spawns.append({"id": zombie_id, "type": "normal", "hp": 100, 
                           "pos": pos})

    #returns the list of zombies that spawned
    return spawns
