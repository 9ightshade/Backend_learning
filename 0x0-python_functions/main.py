"""
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same,is_alphonse_edward_same,is_winry_alphonse_same
    pass

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    if number_of_swords != number_of_soldiers:
        return "incorrect amount"

    pass
def check_high_score(player_name, high_scoring_player_name,
                     low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
    pass
"""
def does_attack_hit(attack_roll, armor_class):
    if ((attack_roll != 1) and (attack_roll >= armor_class)):
        return True
    elif attack_roll == 20:
        return True
    else:
        return False
    pass

