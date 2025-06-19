import random
def roll_dice(sides=20):
    return random.randint(1, sides)
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
entered_city = False
print("\nYou arrive at the gates of the capital city of Alanoth.")
print("Two guards stop you, eyeing you suspiciously.")
print("\n Guard 1: 'State your business traveler.'")
print("\nWhat do you do?")
print("1. Be honest and tell them you're here to seek adventure.")
print("2. Lie and say you're a merchant.")
print("3. Offer a bribe of 10 gold to let you pass.")
print("4. Sneak past them.")
choice = input("Enter 1, 2, 3, or 4: ")
roll = roll_dice(20)
if choice == "1":
    if "Kind" in traits:
        print("\nYou speak honestly and with sincerity, the guards look at each other and nod.")
        print("Guard 1: 'You seem a decent person. Alright, you may pass.'")
        print("Guard 2: 'Have a great day, traveler.'")
        entered_city = True
    elif roll >= 5:
        print("\nYou tell them the truth, and they seem convinced.")
        print("Guard 1: 'Alright, you can pass. But don't cause any trouble.'")
        print("Guard 2: 'Have a great day, traveler.'")
        entered_city = True
    else:
        print("\nYou tell them the truth, but they look at each other, clearly wary of your intentions.")
        print("Guard 1: 'We don't trust you. Leave now or we will arrest you.'")
        print("You have been denied entry to the city.")
elif choice == "2":
    if "Cunning" in traits:
        print("\nYou lie effortlessly, convincing the guards you're a merchant.")
        print("Guard 1: 'Alright, merchant. You can pass, but don't cause any trouble.'")
        print("Guard 2: 'Have a great day, merchant.'")
        entered_city = True
    elif roll >= 10:
        print("\nYou lie convincingly, and the guards seem to buy your story.")
        print("Guard 1: 'Alright, merchant. You can pass, but don't cause any trouble.'")
        print("Guard 2: 'Have a great day, merchant.'")
        entered_city = True
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
        print("Guard 2: 'Have a great day, traveler.'")
        entered_city = True
    else:
        print("\nYou try to bribe the guard, but you don't have enough gold.")
        print("Guard 1: 'How dare you insult me! Get out of here before we arrest you.'")
        print("You have been denied entry to the city.")
elif choice == "4":
    if roll >= 15:
        print("\nYou successfully sneak past the guards unnoticed.")
        print("You enter the city of Alanoth, ready for your adventure.")
        entered_city = True
    else:
        print("\nYou try to sneak past, but the guards catch you.")
        print("Guard 1: 'Where do you think you're going?'")
        print("Guard 2: 'Get out of here before we arrest you.'")
        print("You have been denied entry to the city.")
else:
    print("\nYou stand there confused, the guards look at each other and shake their heads.")
    print("Guard 1: 'Get out of here before we arrest you.'")
    print("You have been denied entry to the city.")
# scene 2
if entered_city:
    print("\nYou have successfully entered the city of Alanoth!")
    print("You find yourself in a bustling marketplace filled with merchants and adventurers.")
    print("You see a notice board with various quests posted.")
    print("\nWhat would you like to do?")
    print("1. Help an old woman find her lost cat.")
    print("2. Explore the old mine.")
    print("3. Visit the blacksmith to buy gear.")
    quest = input("Enter 1, 2, or 3: ")
    if quest == "1":
        print("\nYou find the cat hiding in a tree.")
        if roll >= 5:
            print("You climb the tree and rescue the cat.")
            print("The old woman is grateful and rewards you with 20 gold coins.")
            gold += 20
        else:
            print("You try to climb the tree, but you slip and fall.")
            print("You take 5 damage and the cat runs away.")
    elif quest == "2":
        print("\nYou enter the old mine, it's dark and eerie.")
        print("You hear strange noises and see shadows moving.")
        if roll >= 10:
            print("You find a hidden treasure chest containing 50 gold coins!")
            gold += 50
        elif character_class == "Rogue":
            print("As a rogue, you easily spot the traps and get past them.")
            print("You find a hidden treasure chest containing 100 gold coins!")
            gold += 100
        else:
            print("You encounter a cave troll! You fight bravely but take 10 damage.")
            health -= 10
            print("You manage to escape, but you are injured.")
            if health <= 0:
                print("You have died in the mine. Game over.")
                exit()
    elif quest == "3":
        print("\nYou visit the blacksmith to buy gear.")
        if gold >= 30:
            print("You purchase a sturdy sword for 30 gold coins.")
            gold -= 30
        else:
            print("You don't have enough gold to buy anything.")
    else:
        print("\nYou stand there confused, not knowing what to do.")
        print("A thief sneaks up behind you and steals 5 gold coins.")
        gold -= 5
        print("You have been robbed! You now have", gold, "gold coins left.")
else:
    print("\nYou were turned away at the gates of the city.")
    print("You wander into the forest, unsure what lies ahead.")