# Pickle It
# Demonstrates pickling and shelving data

import pickle
import shelve

print("Pickling lists")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

# open a file to store the pickled lists
pickle_file = open("pickles1.dat", "wb")

# pickle and store the lists
pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)
pickle_file.close()

# Unpickling
print("\nUnpickling Lists.")
pickle_file = open("pickles1.dat", "rb")
variety = pickle.load(pickle_file)
shape = pickle.load(pickle_file)
brand = pickle.load(pickle_file)
print(variety)
print(shape)
print(brand)
pickle_file.close()

# Using a shelf to store pickled data
print("\nShelving Lists.")
pickle_shelve = shelve.open("pickles2.dat")

pickle_shelve["variety"] = ["sweet", "hot", "dill"]
pickle_shelve["shape"] = ["whole", "spear", "chip"]
pickle_shelve["brand"] = ["Claussen", "Heinz", "Vlassic"]

pickle_shelve.sync()

# Using a shelf to retrieve pickled data
print("\nRetrieving lists from a shelved file: ")
print("brand - ", pickle_shelve["brand"])
print("shape - ", pickle_shelve["shape"])
print("variety - ", pickle_shelve["variety"])

pickle_shelve.close()

input("\n\nPress the ENTER key to exit.")
