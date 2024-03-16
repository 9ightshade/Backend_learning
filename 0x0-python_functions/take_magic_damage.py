"""parameters include
health,resist, amp,spell power

function takes these arguments and prints magic_damage to console
"""
health = 2000
resist = 4
amp = 2
spell_power = 28

def take_magic_damage(health, resist, amp, spell_power):
    return health - ((spell_power*amp)-resist)

#calling function now
print(f"magic damage: {take_magic_damage(health, resist, amp, spell_power)}")
