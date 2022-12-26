# Assign a list that contains the atomic numbers and the names of the six alkaline earth metals---barium (56), beryllium (4), calcium (20), magnesium (12), radium (88), and strontium (38)---to a variable called alkaline_earth_metals.

# 1. Write a one-liner that returns the highest atomic number in alkaline_earth_metals.
# 2. Using one of the list methods, sort alkaline_earth_metals in ascending order (from the lightest to the heaviest).
# 3. Transform the alkaline_earth_metals into a dictionary using the name of the metals as the dictionary's key.
# 4. Create a second dictionary containing the noble gases -- helium (2), neon (10), argon (18), krypton (36), xenon (54), and radon (86) -- and store it in the variable noble_gases.
# 5. Merge the two dictionaries and print the result as couples (name, atomic number) sorted in ascending order on the element names.
# Note that Python's dictionaries neither preserve the insertion order nor are sorted in some way.

alkaline_earth_metals = [("barium", 56), ("beryllium", 4), ("calcium", 20), ("magnesium", 12), ("radium", 88), ("strontium", 38)]

max_atomic_number = max(alkaline_earth_metals, key = lambda item : item[1])
print(f"The highest atomic number in alkaline earths metals is {max_atomic_number}")

sorted_alkaline_list = sorted(alkaline_earth_metals, key = lambda item : item[1])
print(f"Alkaline list order from lightest to heavier is {sorted_alkaline_list}")

alkaline_earth_metals_dictionary = {key: item for key,item in alkaline_earth_metals}
print(f"The alkaline earth metals dictionary is {alkaline_earth_metals_dictionary}")

noble_gases = {"helium": 2, "neon": 10, "argon": 18, "krypton": 36, "xenon": 54, "rabon": 86}
merged_dictionary = alkaline_earth_metals_dictionary | noble_gases
couples_string = ""
for key in sorted(merged_dictionary):
    couples_string += f"({key}, {merged_dictionary[key]}) "
print("The couples list of alkaline earth metals and noble gases is:\n\t" + couples_string)