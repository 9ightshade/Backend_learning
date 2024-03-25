def printsm():
    fruits = ["apple", "orange", "banana"]
    return "banana" in fruits
# Prints: True

print(f"return value: {printsm()}")

print("================================================")

stronghold = [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
            ]

def trim(stronghold):
    del stronghold[0]
    new_hold = stronghold
    del new_hold[-2:]
    return new_hold

print(stronghold)
print(f"first stronghold deleted: {trim(stronghold)}")

                    
