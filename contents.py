# Lecture 189
# Lecture 191
# Lecture 193

# Lecture 189 notes:
# Now we'll start using dictionaries for more interesting things
# If you've got $8000 to spare, you could buy yourself a smart fridge
# They keep track of the food in them, and let you know what you can make for tea
# We're going to use some Python dictionaries to do something similar
# The first dictionary is called pantry, and it contains food items and ingredients that we've got availible
# The dictionary contains the names of foods items and ingredients
# They're the key, and the values are how much of each one we've got
# The next dictionary contains the ingredients for some recipes
# The keys are the names of the meals
# The meals get easier to cook as you get further down the dictionary
# We mention that because this is the order that we'll be presenting the meals, to start with
# We'll then sort the keys in a dictionary, so that we can present the meals in alphabetical order
# Before we start using these dictionaries, take a closer look at recipes
# The keys are the names of each recipe, or meal
# The values are lists
# Although there are restrictions on what you can use as a dictionary key (which we'll talk about soon),
# you can use any Python object as a value
# You can store tuples in a dictionary, or even other dictionaries
# Dictionary values can be anything that Python knows about
# Our values are lists - specifically, lists of the ingredients that we need for each recipe
# If we want, we could extend that to also include the recipe instructions
# the first ingredient for Butter Chicken is chicken
# chicken is the key to the pantry dictionary
# Data that's organised like this is very common - and incredibly useful
# It's common to have something like a list, that contains keys in a dictionary
# You might also have one dictionary, whose values are keys in another dictionary (like we have here)
# That would be useful here, in fact
# Our recipes are a bit useless, because they don't specify how much chicken we need
# We'll extend this data soon and address that problem
# In the next video, we'll start to make use of these two dictionaries

# Lecture 191 notes:
# IntelliJ has a useful feature that can make it easier to work with large data structures
# So notice that each of the recipe keys has a little minus button, just on the margin
# Clicking that button collapses the entry
# The button then changes to a little plus, which will expand the entry again
# Note that the line numbers in the margins remain correct

# Lecture 193 notes:
# So each recipe contains a list of ingredients
# However, as you can see, there's no quantities
# Adding the quantities is easy -  it's just a bit of typing
# Deciding how to add them is harder
# So how are we going to store the recipe items, if we want to include the quantities
# There are two obvious options; we could store them as tuples; or as key value pairs - a dictionary, in other words
# We'll open a new python file called recipe_options.py
# we're back
# Lets look at the pantry dictionary
# When we tell the program that we're going to make a recipe,
# the program will subtract the amount of each ingredient used
# We are going to be updating the values in pantry
# Using tuples here wouldn't work, because tuples are immutable
# But our recipes, when including the quantities, we can use either
# Now this is a section on dictionaries, so the obvious one for us to choose is a dictionary

pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": {
        "chicken": 750,
        "lemon": 1,
        "cumin": 1,
        "paprika": 1,
        "chilli powder": 2,
        "yogurt": 250,
        "oil": 50,
        "onion": 1,
        "garlic": 2,
        "ginger": 3,
        "tomato puree": 240,
        "almonds": 25,
        "rice": 360,
        "coriander": 1,
        "lime": 1,
    },
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
    "Pizza": {
        "pizza": 1,
    },
    "Egg sandwich": {
        "egg": 2,
        "bread": 80,
        "butter": 10,
    },
    "Beans on toast": {
        "beans": 1,
        "bread": 40,
    },
    "Spam a la tin": {
        "spam": 1,
        "tin opener": 1,
        "spoon": 1,
    },
}

