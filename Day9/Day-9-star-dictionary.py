programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
# print(programming_dictionary["Function"])

# add bew items to dictionary
programming_dictionary["loop"] = "The loop of doing someting and over again"
# print(programming_dictionary)

# emoty dictionary
# empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "This is Bug"
# print(programming_dictionary)

# loop through dictionary
for key in programming_dictionary:
    print(key)  # key
    print(programming_dictionary[key])  # value
