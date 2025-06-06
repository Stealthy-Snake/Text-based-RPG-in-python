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
# Scene 1
print("\nYou arrive at the gates of the capital city of Alanoth.")
print("Two guards stop you, eyeing you suspiciously.")
print("\n Guard 1: 'State your business traveler.'")
print("\nWhat do you do?")
print("1. Be honest and tell them you're here to seek adventure.")
print("2. Lie and say you're a merchant.")
print("3. Offer a bribe of 10 gold to let you pass.")
choice = input("Enter 1, 2, or 3: ")
if choice == "1":
    if "Kind" in traits:
        print("\nYou speak honestly and with sincerity, the guards look at each other and nod.")
        print("Guard 1: 'You seem like a decent person. Alright, you can pass.'")
        print("Guard 2: 'Have a great day, traveler.'")
    else:
        print("\nYou tell them the truth, but they look at each other, clearly wary of your intentions.")
        print("Guard 1: 'We don't trust you. Leave now or we will arrest you.'")
        print("You have been denied entry to the city.")
elif choice == "2":
    if "Cunning" in traits:
        print("\nYou lie effortlessly, convincing the guards you're a merchant.")
        print("Guard 1: 'Alright, merchant. You can pass, but don't cause any trouble.'")
        print("Guard 2: 'Have a great day, merchant.'")
    else:
        print("\nYou try to lie, but the guard seems to see through your deception.")
        print("Guard 1: 'Alright, merchant. Show me your wares.'")
        print("You have nothing to show, and the guards are not impressed.")
        print("Guard 1: 'Get out of here before we arrest you.'")
        print("You have been denied entry to the city.")
elif choice == "3":
    if gold >= 10:
        gold -= 10
        print("\nYou hand the guard 10 gold coins.")
        print("Guard 1: 'Nice doing business with you. Hahaha!'")
    else:
        print("\nYou try to bribe the guard, but you don't have enough gold.")
        print("Guard 1: 'How dare you insult me! Get out of here before we arrest you.'")
        print("You have been denied entry to the city.")
else:
    print("\nYou stand there confused, the guards look at each other and shake their heads.")
    print("Guard 1: 'Get out of here before we arrest you.'")
    print("You have been denied entry to the city.")