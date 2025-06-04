print("Welcome to the world of Alanoth!")
# Name
name = input("What is your name, brave adventurer? ")
print(f"Greetings, {name}! Tell me about yourself.")
# Class
print("\nChoose your class:")
print("1. Warrior - Strong and brave, skilled in melee combat.")
print("2. Mage - Wise and powerful, master of the arcane arts.")
print("3. Rogue - Stealthy and cunning, expert in deception and agility.")
choice = input("Enter 1, 2, or 3: ")
if choice =="1":
    player_class = "Warrior"
    health = 120
    attack = 8
    magic = 2
elif choice == "2":
    player_class = "Mage"
    health = 70
    attack = 3
    magic = 10
elif choice =="3":
    player_class = "rogue"
    health = 90
    attack = 6
    magic = 4
else:
    player_class = "peasant"
    health = 50
    attack = 2
    magic = 1
    print("You have entered an invalid choice. You must be a peasant.")
# Backstory
print("\nChoose your backstory:")
print("1. Orphan raised by monks in the mountains.")
print("2. Former noble who lost their title and wealth.")
print("3. Escaped prisoner seeking redemption.")
backstory_choice = input("Enter 1, 2, or 3: ")
if backstory_choice == "1":
    backstory = "Orphan raised by monks in the mountains."
elif backstory_choice == "2":
    backstory = "Former noble who lost their title and wealth."
elif backstory_choice == "3":
    backstory = "Escaped prisoner seeking redemption."
else:
    backstory = "Aimless wanderer who can't follow instructions."
# Traits
print("\nChoose TWO personality traits (separated by a comma):")
print("Brave, Cunning, Kind, Wise, Hot-Headed, Greedy")
traits_input = input("Enter TWO traits: ")
traits = [trait.strip().capitalize() for trait in traits_input.split(",")][:2]
# Trait Effects
if "Brave" in traits:
    health += 5
if "Cunning" in traits:
    attack += 2
if "Kind" in traits:
    print("Your kindness may earn you allies later.")
    attack -= 1
if "Wise" in traits:
    magic += 2
if "Hot-Headed" in traits:
    attack += 1
    health -= 5
if "Greedy" in traits:
    print("You start with 50 extra gold.")
    gold = 60
else:
    gold = 10
# Character Summary
print(f"\nCharacter Created!")
print(f"Name: {name}")
print(f"Class: {player_class}")
print(f"Backstory: {backstory}")
print(f"Personality Traits: {traits[0]} and {traits[1] if len(traits) > 1 else 'None'}")
print(f"Stats - Health: {health}, Attack: {attack}, Magic: {magic}")
print("\nPrepare for your adventure in Alanoth!")