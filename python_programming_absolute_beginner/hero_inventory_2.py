# Hero's Inventory 2.0
# Demonstrates tuples

# Create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print('Your items: ')
for item in inventory:
    print(item)
input("\nPress the ENTER key to continue.")

# Get the length of the tuple
print("You have, {} items in your inventory".format(len(inventory)))
input("\nPress the ENTER key to continue.")

# Test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# displaying one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index: {}, is item: {}".format(index, inventory[index]))
