# Lecture 91-93
# Lecture 94-96

# Lecture 91 notes:
# So we going to look at appending items to a list. For this example,
# we'll allow customers to choose which parts they need when buying a computer
# First we need to initialize a couple of variables, we need a variable to store the customers choice,
# as well as an empty list to add items to

availible_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
# Note the following, there are two sequences in a list, the list itself is a sequence, and so is each item.
# To find the first character in the 2nd item of the list the code bellow is used:
# print(availible_parts[1][0]) , the second index is for the character in the item, which is a string.
# valid_choices = [str(i) for i in range(1, len(availible_parts)+1)]  # This is a comprehension (haven't learnt it yet)
valid_choices = []
for i in range(1, len(availible_parts) + 1):  # This for loop block accomplishes the same feat as the commented out code
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []     # create an empty list
# enumerate function returns each item, with its index position
while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice)-1   # converting current_choice into an index value, as index starts from 0 not 1
        chosen_part = availible_parts[index]  # recall what we learnt about indexing and slicing from helloWorld project
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}.".format(computer_parts))
    else:
        print("Please add options from the list below:")
        # for part in availible_parts:
        #     print("{0}: {1}".format(availible_parts.index(part) + 1, part))
        # above method is inefficient, and that's because Python has to look up each item in the list,
        # in order to get its index position
        # In the above code, we've got a for loop that assigns each of the values in our list,
        # to a variable called part
        # In the print line, the availible_parts list has to be searched, to get the index position of each part
        # If the list was sorted, we could use a binary search, but our list isn't in order
        # Python has to check each item, to see if it equals part
        # The first part will be found straight away
        # The second part will take a bit longer,
        # Python will check if monitor equals computer parts, then go on to check the second item in the list
        # That matches, so it can return an 1 as the index value
        # If there are hundreds or thousands of items, finding the index positions will take a while
        # This result is a consequence of using the method to find the index position
        # This is a very common thing to have to do, and Python provides a much more efficient way of doing it
        # that's the enumerate function
        # enumerate returns each item, with its index position
        # So this is a more efficient way of getting the return value and it's associated index position
        # When we discussed for for loops in section 4, we said that a for loop starts with the word for,
        # and then the names of one or more variables
        # If the object that's iterated over contains more than one value,
        # you can use more than one variable in the for loop
        # enumerate returns pairs of values - we get the index position and the item, as a pair of values
        # The first value is the index position and the second value is the item
        # We can use enumerate with any iterable type
        for number, part in enumerate(availible_parts):     # Watch lecture 94 for explanation of line 33 for loop
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()
# A for loop starts with the name for and then the names of 1 or more variables
# If the object that's iterated over contains more than 1 value,
# you can use more than one value in the for loop, and that's whats done in line 33
# enumerate function returns pairs of values, we get the index position and the item as a pari of values
# In our for loop number will be our index position and part will be the item in the list
# We can use enumerate with any iterable type
print(computer_parts)
