"""
def calculate_damage(sword, arrow, spear, dagger, fire):
    total_damage = sword + arrow + spear + dagger + fire
    average_damage = total_damage/5
    return total_damage,average_damage

def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score
    pass
"""
def get_hurt(current_health, damage):
    current_health -= damage
    #alternatively we can do this
    #current_health = current_health - damage
    return current_health
    pass

