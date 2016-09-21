# Inventory Tracker RPG

#Player
#Inventory
#Items

player = {"inventory": {"red potion": {"quantity": 20}}}
player_name = input("Welcome Traveler! What is your name? ")
player["name"] = player_name
print(player)

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>")
    if choice == "a":
        item_name = input("What is the item name? ")
        item_quantity = int(input("How many? "))
        player["inventory"][item_name] = {"quantity": item_quantity}
    elif choice == "i":
        print("looking at inventory")
        for item in player["inventory"].keys():
            quantity = player["inventory"][item]["quantity"]
            print("{} - {}".format(item, quantity))
