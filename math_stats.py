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
