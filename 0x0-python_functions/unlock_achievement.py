#unlock_achievement function
#parameters before_xp, ach_xp, ach_name
before_xp = 200
ach_xp = 100
ach_name = "novice"

def unlock_ach(before_xp, ach_xp, ach_name):
    print(f"Achievement Unlocked: {ach_name}")
    return before_xp + ach_xp

#function call
unlock_ach(before_xp, ach_xp, ach_name)

print("=====================create status message==============")
def create_stats_message(strength = 100, wisdom = 200, dexterity = 150):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    print(msg)
    return msg

create_stats_message()

