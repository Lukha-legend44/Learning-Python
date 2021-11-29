# Lecture 190-198

# Lecture 190 notes:
# Alright, so we've seen how to keep our data and code separate,
# and we'll do that again for this program
# Alright, so the first thing we're going to do in this new program is to import the dictionaries from the last lecture
# We've seen an import like that previously, in the simple jukebox program,
# back in the Lists and Tuples section
# By importing the dictionaries from content.py ,
# they become availible in this program
# Next we need to present the recipes to the user so that they can choose one
# Once again, we're not learning how to write a menu
# We're learning how to transform data
# We display it in a menu, because that lets us see what we've done to it
# Just printing it out would serve the same purpose, but it's more interesting if there's a use for the transformed data
# So how do we transform the data?
# We need to transform the recipes dictionary into something that resembles the following:
# Please choose your recipe
# --------------------------
# 1 - Butter chicken
# 2 - Chicken and chips
# 3 - Egg sandwich
# ...
# In Python, that's easy. In fact we can do it with 1 line of code
# Because that would use something we'll be covering later, we're going to use 3 lines of code instead
# Let's see the more naive way of transforming our recipes into something we can display to the user
# We're going to iterate over the dictionary and use the keys to create a new one
# Because we're using that new dictionary to display the menu to the user, we're going to cll it display_dict
# Now we used the enumerate function, when we were working with lists
# If you checked the documentation for enumerate, you'll have seen that it can be used with any iterable
# Alright, so we're iterating over the tuples that the enumerate function produces
# Each tuple wil contain an index, and the key from the dictionary
# If you're thinking hang on, dictionaries don't have index numbers, you're right - they don't
# They use the keys to index into a dictionary
# The enumerate function creates the index numbers for us,
# it iterates over an iterable, and generates an index number for each item it finds, starting at zero
# It then return tuples, containing the index and value for each item in the iterable
# So we unpacking each tuple in turn, in the for loop,
# to get the index numbers for each entry in the dictionary
# We're going to display our menu repeatedly in a loop, so we'll store these values in our display_dict dictionary,
# instead of printing them
# Our display_dict dictionary has numeric characters as its keys, and recipes as its values
# What may not be obvious, is that its values are actually the keys from the recipe's dictionary
# We've transformed the data, so that the keys from recipes become the values in display_dict
# All the values in the display_dict dictionary are valid keys in the recipe dictionary
# That means we can use those values to access items in the recipes dictionary
# If the user chooses option 3 for a pizza, we can look up pizza in the recipes,
# to get the list of ingredients for a pizza
# We'll see that working in the next lecture

# Lecture 191 notes:
# Alright back to our meal planner code
# It's time to make these dictionaries work together
# At the moment, our code creates the display_dict dictionary, and uses it to print the menu
# Now we getting input from the user, but only checking for zero at the moment
# If the user enters zero, we break out of the loop
# If they enter something else, we'll start by making sure it's a valid choice
# Note that the values in the display_dict dictionary are the keys in the recipes dictionary
# We're going to switch back to the contents.py program
# Alright, so the values we chose from the display_dict dictionary,
# can be used to get the list of ingredients from the recipes dictionary
# We are now going to retrieve the list from the recipes dictionary
# eg. You select option 4
# So after the you've selected egg sandwich message, we've got "Checking ingredients",
# and we can also see our list of ingredients
# The next step is to link in the pantry dictionary

# Lecture 192 notes:
# At the moment, the program just prints out the list
# We've got egg, butter and bread in the output
# The next step i to check our pantry dictionary
# If you want to make an egg sandwich,
# then we'll need all these 3 ingredients; egg, bread and butter
# All we have to do is iterate over this list, and see if each item is in the pantry dictionary
# Alright, so this program is very good at telling us what we don't have,
# but not very good at telling us what to do about it
# It also doesn't check how much of an ingredient we have, nor how much we need
# We'll continue developing this program
# In the next lecture, we'll start by checking how much of each item, a recipe needs

# Lecture 193 notes:
# At the end of the last video, we mentioned that our program doesn't tell us how much of each ingredient we need
# The problem is the recipes dictionary
# Lets have a look at that, in contents.py

# Lecture 194 notes:
# Alright, so we've now got quantities in our pantry, so we know how much of each item we've got
# We need to change the code in meal_planner.py, to check those quantities
# Before we do, remember that we might not have that ingredient at all
# It might not exist in the dictionary
# If we try to retrieve the quantity, using the ingredient name as a key, we'll get an exception in that scenario,
# and we saw that right at the start of this section
# This a good chance to see when you'd want to use .get(), rather than indexing into the dictionary
# We are going to start by changing the last for loop
# So after making the changes lets run the program now, and we'll start off by choosing 1: Butter chicken
# As you can see, the messages are more useful now
# This tells us how much chicken to buy, and how much ginger and tomato puree we need as well
# Alright, we're now starting to get a useful program
# But it only produces output on the screen
# Our cook will either have to write things down, or print the output
# That's just not good enough, these days. Users expect more from their technology
# Our program could order items from an online food store, or send the details to a mobile phone
# That would be what modern users expect
# We're not going to do all of that straight away, but you will do the first step
# Whatever we decide to get the program to do, it's going to need the data in a more usable form
# So it's time for a challenge

# Lecture 194 challenge:
# Modify the program, so that it puts the items we need to buy into some sort of data structure
# It's entirely up to you what type of structure you use
# You may decide to create some sort of list, or a dictionary
# The important thing is, that you must produce something that can be iterated over,
# to retrieve the ingredient and quantity
# Hint: We did something similar with the buy_computer_dict program, earlier in this section
# Another hint: Whatever data structure you choose, use a function to add items to it

# My solution to Lecture 194 notes:
# Created an empty dictionary, then added items to the dictionary when they were missing in the pantry
# The issue with my solution is as follows:
# When you want to cook to recipes, and in those recipes you are missing the same item,
# the quantity of said items do not stack,
# instead the key value is updated to reflect the last chosen recipe missing item

# Lecture 195 notes:
# Our solution may be different to the Python masterclass solution - there's no right or wrong here
# The important thing is that you get something you can iterate over, to get the ingredients and quantities
# We could use a dictionary, or a list of tuples for the lecture 194 challenge
# This section is about dictionaries, and a dictionary would be a good choice
# But often, you'll need to mix different data structures
# We don't want to give the impression that you can only use dictionaries with dictionaries
# So we going to create a list of tuples in the Python masterclass solution
# And we're going to find out that it wasn't the best choice
# We've mentioned, a few times, that you'll soon find out if you make the "wrong" choice
# We've also said not to worry too much about getting it wrong
# But that doesn't necessarily stop students from worrying
# This is a good chance to see what happens if you get it wrong, and why it doesn't have to be a big deal
# In either case, we'll start by creating an empty dictionary, or an empty list
# Now we suggested that you use a function, to add items to your shopping data
# What we going to do is to define our function at the start of the program, right after the import
# It's not a very complicated function, and you may be wondering why we've bothered defining it
# We'll come back to that once we've seen it being used
# What we'll do is call the function in the else block, when we've identified an item that the cook needs to buy
# If you haven't spotted the problem yet, don't worry
# We'll see the problem that using a list of tuples is going to cause, once we start testing the program
# Alright, so what we going to do now is print the list, to check what's being produced
# We going to do that outside of the loop
# We've go the data in a list, but we can pass that list to some other function
# That function might order the items online, or send them to a mobile phone, or whatever
# Now let's see the problem we've got
# When we select two recipes, that have the same item missing from the pantry,
# The item will crop up twice with the respective amounts required,
# rather than appearing once with the cumulative amount needed
# Also note, that our program doesn't update the pantry once recipes have been selected
# Overall our shopping list will work, but it's a bit annoying
# We'll examine the problem in more detail, and fix it, in the next video

# Lecture 196 notes:
# In this video, we'll examine the problem with our shopping list
# We'll look at why we've got a problem, but more importantly perhaps, how to fix it
# Our add_shopping_item() function can check if the list already contains an item, and update the quantity if it does
# We decided to use a list of tuples, and searching through the list is going to be a bit tricky
# We saw how to use the index method of a list, to find an item, but we don't know what item to search for
# Items in the list are in two parts; an ingredient and a quantity
# We know the ingredient part that we want, but we don't know what quantity it'll have, if it's already in the list
# That means we can't search for a specific tuple
# We'd have to iterate over the list, and compare the first item in each tuple
# That means we can't search for a specific tuple
# We'd have to iterate over the list, and compare the first item in each tuple
# Choosing a list of tuples, instead of a dictionary, wasn't the best decision here
# But it's not the end of the world
# Our program isn't as easy to modify as it could, but we produced something that works
# Alright so time to fix the problem
# We now want a dictionary for shopping_list, instead of a list
# We should now change our function, changing the annotations, docstring etc.
# Our change in the function code is fairly straight forward
# If the item is in the dictionary, we're using augmented assignment to increase it's vale by amount
# Otherwise, using the else, we store the amount using item as the key. This adds the entry to the dictionary
# In the next lecture, we'll look at an alternative function code for add_shopping_item()

# Lecture 197 notes:
# In the last video, we mentioned that there's a more concise way to write our add_shopping_item() function
# So having a look at the function code, we check to see if the item's in the dictionary
# If it is, we add amount to the current value
# We've used augmented assignment to do that - augmented assignment works fine with values in a dictionary
# Otherwise, we store amount in the dictionary, creating a new entry with the key item
# That sort of code is so common, that Python's dictionaries provide a way to help
# What we gonna do is comment out out these four lines, and use the set default method (.setdefault()) instead
# The set default value returns the value from the dictionary, if the key exists
# If the key doesn't exist, it creates a new entry for the key, assigns the default value to it,
# which is zero in this case, and then returns that default value
# We add amount to the value returned, then store the value back to the dictionary
# So looking back at the code, the new line of code is doing the same job as the previous four lines,
# but is much more concise
# It's also less obvious what it's doing, but don't let that put you off using it
# Using .setdefault() is a useful tool in your toolkit
# Some more examples will help with understanding what it does
# Lets create a new Python file now
# We're going to call this one dict_defaults

# Lecture 198 notes: (Video only) (API nd mobile phone demo)
# At the end of the last video, we mentioned that we could do something more useful with our shopping list
# If we print it out, our cooks will have to write the list down before they go shopping
# If we store it in some kind of data structure, as we've done, we can do something more exciting with it
# We not going to show the code for this, nor will it be made availible in the resources for this lecture
# This is purely a demonstration of what's possible
# At this point in the course, we haven't learnt enough to be messing with your Google accounts
# It's possible, if you attempt too many logins too quickly, or get the authentication wrong,
# that Google will lock you out of your account
# Another reason why this code won't be made availible, is that it uses an unofficial API
# We'll see the demo, then we'll talk a bit about APIs
# We have to run this demo from a terminal, rather than from IntelliJ's Run pane
# That's because we're using the Python getpass module
# The getpass function is similar to input, but it doesn't echo the input to the console
# If Tim used the input function here, his username and password would be visible on the video,
# which obviously isn't a good thing
# If you use getpass in your code, be aware that it doesn't work in the IntelliJ Run pane
# It does work in the IntelliJ terminal, as well as a normal terminal and windows command prompt
# In the video we see the items needed, transferred from the Python application (run in the IntelliJ terminal),
# to the phone application
# In the video Tim could check off the things he buys,
# but it wouldn't be hard to use the same API to read the note and update the pantry, with items bought
# Microsoft have published an API for OneNote, allowing you to use that instead of Google Keep, if you prefer
# There's also a Google Drive API, if you want to create  document on Google Drive and open that on your phone
# A bit of googling will find APIs for Evernote, and the Apple iCloud as well
# So what is an API?
# Well API is an acronym for Application Programming Interface
# It defines object and functions that are made availible, and how to use them
# We've already used a lot of APIs in this course
# For example, we used the list API when we worked with lists
# The documentation described the list object, and methods we can use to manipulate lists
# Shortly, we'll look at the documentation for Python's dict API
# You wouldn't find programmers referring to these as APIs, but that's really what they are
# If you create a system that other programmers will find useful, you may decide to create an API for that system
# For example, Google make all sorts of data availible
# Raw data can be useful, but providing a way to interact with that data is even better
# Google provide a YouTube API that lets you query YouTube, to get statistics on your YouTube channels
# Those statistics are availible when you log into the YouTube website,
# but you might want to write your own program to analyse the statistics
# Their Channels API lets you do that, from your Python code
# Students sometimes ask how they can allow a user to log in, with a password, before being granted access to a program
# Our advice is don't
# Authenticating users is extremely difficult to get right, and comes with all sorts of problems
# You may be aware of websites getting hacked, and all their customers' passwords being stolen
# If you need to perform authentication, let someone else handle it
# Google, Apple and Facebook, to name a few, spend a lot of money on their authentication systems
# They have the resources to make them secure, and the money to spend on the development and testing
# An official API is supported by whoever created it
# More importantly, there's an implicit guarantee that the API won't be changed in a way that breaks client code
# If you write code that uses a Google API, for example,
# then Google will make sure that any changes they make won't cause your code to break
# The Google Keep API that is used in the video is an unofficial one
# A programmer called Kai created a module to use that API, and has made it availible
# But if Google change the way Keep works, any code using Kai's API might break
# If you're new to programming,
# it's a bit early in the course to be experimenting with your live Google or Microsoft accounts
# By the end of the course, you'll be able to make sense of published APIs, and use them in your programs
# With a bit of extra code, in the video, our simple meal planner program became a lot more useful
# Now if you think of something you'd like to do, google for it -
# it's very likely that you'll find at least one Python module that will help
# Alright, so let's end the lecture here, and in the next one, we'll have a look at the dict API -
# the documentation for dictionaries


from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dict."""
    # data.append((item, amount))
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


# print(pantry)
# print(recipes)

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)},
# The one liner that we spoke of earlier, just to show the optimal way of doing things
# It's called a dictionary comprehension

display_dict = {}
for index, key in enumerate(recipes):
    # print(index, key)
    display_dict[str(index + 1)] = key
    # So we've added one to each index because we don't want the menu to start at zero

# shopping_list = {}   Part of my solution to lecture 194 challenge
# shopping_list = []
shopping_list = {}

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)      # Prints the dictionary, which is the value for the key in the recipes dictionary
        # for food_item in ingredients:   # Iterating over the keys in the aforementioned printed dictionary
        #     if food_item in pantry:
        #         print(f"\t{food_item} OK")
        #     else:
        #         print(f"\tYou don't have a necessary ingredient: {food_item}")
        for food_item, required_quantity in ingredients.items():
            # So what we're doing here is we're iterating over the items, and unpacking the key and value
            # That'll give us the quantity for each ingredient. Remember ingredients is now a dictionary
            quantity_in_pantry = pantry.get(food_item, 0)       # 0 is the default value
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                # shopping_list[food_item] = quantity_to_buy    # Part of my solution to lecture 194 challenge
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

# print(shopping_list)      # Part of my solution to lecture 194 challenge
for things in shopping_list.items():
    print(things)
