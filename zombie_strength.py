


def zombie_strength (round_num):
    """ The Zombie Strength multiplier
    Attributes: 
        round_num(int): The number of rounds played.

    Return:
        strength(float): The increased power of the zombie.
        
    """
    base_power = 5
    strength_multiplier = 1.05
    
    ## Strength Multiplier
    for num in range(2, round_num + 1):
        
        base_power *= strength_multiplier
    
    strength = base_power
    return strength

