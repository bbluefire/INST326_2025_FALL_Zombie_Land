# INST326_2025_FALL_Zombie_Land
## Concept of the game
Zombie-Land is our text-based zombie survival game where players navigate 
randomized events, manage hit points, and make strategic choices. Players can 
pick up and use items, like weapons, to gain advantages against zombies. Each 
decision (attack, flee, or use an item) impacts health, survival chances, and 
available resources as they progress through the game. 

## HOW TO PLAY
1. Run zombie_land.py file using python zombie_land.py
2. Respond to command-line prompts with a single digit suggested by the prompt.
    - Responses outside of the expected numbers will be given a warning.
3. Choose the best options based on information given.
    - Players will be prompted to choose actions such as attacking, fleeing, 
        or using items. Combat affects both player and zombie health. If the 
        player’s health reaches zero, the game ends. Defeating zombies 
        increases the score and may generate more items.
4. Try to win and have fun!

## Difficulties that we faced
We did have some issues including: overlap in functions, different schedules 
and time conflicts, meeting function requirements, and slight changes of our
original idea.

In the end, we made a fun and easy to use text-based game that focuses on 
surviving the zombie apocalypse, finding resources, and fighting. 

No information outside of the INST326 course materials.


## Purpose of Each File
- README.md serves as an explination of game, an explanation of how to plat the 
    game difficulties that we faced along the way, 
- zombie_land.py contains the Player and Zombie classes, game logic, combat 
    mechanics, item generation, zombie spawning, and the main game loop. 

## Attribution
--------------------------------------------------------------------------
| Method/Function    | Student Name     | Techniques Demonstrated        |
| ------------------ | ---------------- | ------------------------------ |
| play_round         |                  | Tuple Unpacking/               |
| run_game           |  Bethany Cruz    | Conditional Logic              |
| __init__ (player)  |                  |                                |
|------------------------------------------------------------------------|
| spawn_zombies/     |                  | Default Argument Values/       |
| if main            | Kritagya Ghimire | User input handling +          |
| isalive (player)   |                  | normalization                  |
| isalive (zombie)   |                  |                                |
|------------------------------------------------------------------------|
| use_item/          |                  | F-String Containing Expression/| 
| generate_item      | Ryan Money       | use of a key function with the |
| __init__ (zombie)  |                  |  .keys and list                |
|------------------------------------------------------------------------|
| zombie_interaction/|                  |  Conditional Expressions/      |
| strongest_weapon/  |  Mariam Sanni    |  Use of max() key function     |
| auto_equip         |                  |                                |
--------------------------------------------------------------------------


