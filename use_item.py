def use_item(item, target):
  """ Item use function that will be called in other areas like during a zombie interaction in order to do damage
  Args:
      item(obj): an item that has either a heal amount or a damage amount based on what the item is
      target(obj): Either an instance of a player class or a zombie class
  Returns:
    None: nothing will be return, the effect will just happen and the game will continue
  
  """
  if target == user:
    if item = health:
      player.health += item
    elif item == food:
      player.hunger += item
    else:
      print(f"item can not be used on player")
  elif target == zombie:
    if item = weapon:
      zombie.health -= item
    else:
      print(f"item can not be used on zombie")
  elif target == environment:

  else:
    print(f"An item can not be used on that target")
return None
    
