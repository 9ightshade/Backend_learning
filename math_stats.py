"""
sum = a + b
difference = a - b
product = a * b
quotient = a / b
"""
player_health = 1000
armor_multiplier = 2

armored_health = player_health*armor_multiplier
print(armored_health)

#when player walks thru poision, health reduce by 20
poison = 20
poison_health = player_health - poison
print("player is poisoned:")
print(poison_health)

# * and + operations with strings
first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name) # prints "Lane Wagner"

first_name = "Bruce "
last_name = "Wayne "

full_name = first_name + last_name * 2
print(f"I am BATMAN, OH Wait {full_name}")

