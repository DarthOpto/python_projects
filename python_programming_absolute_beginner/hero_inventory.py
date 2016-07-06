# Hero's Inventory
# Demonstrates tuple creation

# Create an empty tuple
inventory = ()

# Treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

input("\nPress the ENTER key to continue.")

# Create a tuple with some items in it
inventory = ("sword",
             "shield",
             "armor",
             "healing potion")

# Print the tuple
print("\nThe tuple inventory is: ")
print(inventory)

# print each element in the tuple
print("\nYour items are: ")
for item in inventory:
    print(item)

input("\n\nPress the ENTER key to exit.")
