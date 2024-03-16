print("Learning functions")

"""
We need to calculate the size of a weapon's "attack area". With a 1.0 meter sword, for example, a player can attack in an area of 3.14 square meters around them. You can use the area_of_circle function to do that calculation.

The spear_area variable should be set to the result of calling the area_of_circle function with the given spear_length as input.


"""
#function to calculate area of circle
def area_of_circle(r):
    pi=3.14
    result = pi * r * r
    return result
    


sword_len = 1.0
spear_len = 2.0


spear_area = area_of_circle(spear_len)
sword_area = area_of_circle(sword_len)

print(f"Sword attack area: {sword_area}")
print(f"Spear attack area: {spear_area}")

#subtraction of two numbers
def subtract(a, b):
    diff = a - b
    print(f"difference between {a} and {b} is {diff}")

subtract(12,42)

#calculate damage function
dmg_one = 2
dmg_two = 4
dmg_three = 3
dmg_four = -1
dmg_five = 10
dmg_six = 5

# Don't touch above this line


def calculate_damage(opening_attack, core_damage, finishing_move):
    triple_attack_combo = opening_attack + core_damage + finishing_move
    return triple_attack_combo


# Don't touch below this line

print("Getting damage for", dmg_one, dmg_two, "and", dmg_three, "...")
print(calculate_damage(dmg_one, dmg_two, dmg_three), "points of damage dealt!")
print("=====================================")

print("Getting damage for", dmg_four, dmg_five, "and", dmg_six, "...")
print(calculate_damage(dmg_four, dmg_five, dmg_six), "points of damage dealt!")
print("=====================================")


#function to convert temp in farenhiet to celsuis
def to_celsuis(f):
    celsuis = 5/9 * (f-32)
    print(f"temp in celsuis: {celsuis}")
    return celsuis

to_celsuis(100)

print("=======================================")

def hours_to_seconds(h):
    seconds = h*120
    print(f"{h} hours to {seconds}secs")

hours_to_seconds(20)

print("=========================================")

first_name = "9ightshade"
last_name = " Shadow mage"
power = 1000

def become_warrior(first_name, last_name, power):
    title = first_name + last_name + " the Warrior"
    return title, power + 1

title, power = become_warrior(first_name, last_name, power)
print(f"9ightshade power level: {power}")
print("=======================")
print(title)

print("================================================")

#health and armor variables
health = 1000
armor = 20

#if armor is not passed to function at point of calling, set to default of 0 and getting slashed does 100 damage.
#damage should subtract from armor and then health
def get_slashed(health, armor=0):
    return health + armor - 100

#getting punched does 50 damage
def get_punched(health, armor= 0):
    return health + armor -50
