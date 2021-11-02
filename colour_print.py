# Lecture 164 - 169
# Lecture 175

import colorama  # Note that it is the convention to leave a blank line after an import

# Lecture 164 notes:
# We've been running our code in an IDE, which is a slightly artificial environment
# When you distribute your programs to your users, they won't be running in an IDE
# They'll run your code from a command prompt on Windows, or a Terminal session on Linux and Mac
# Sometimes that can lead to different behaviour, and our next example wil demonstrate that
# Most terminals will respond to certain character sequences, to perform actions rather than printing
# We've seen two such sequences already; backslash n causes the terminal to start a new line,
# rather than printing characters. Backslash t advances to the next tab stop
# Back in the day (old teletype) terminals needed both a carriage return and line feed key, to start a new line
# Carriage return took the print head back to the left hand side, and line feed moved the paper up a line
# Obviously, that slowed they typist down on this particular terminal -
# they had to press two keys to start each new line
# Device drivers for Unix started including carriage return automatically,
# which meant software only had to send a line feed
# That's why you sometimes don't get correct line breaks, if you open a Linux file on a Windows computer
# Windows uses carriage return and line feed, to indicate a new line
# It also explains something that confused a few students. When they compare two files,
# they notice that the contents appear identical, but the Windows file has a larger size
# That's because of the extra carriage return character, at the end of each line
# Once screens where a thing, there wasn't a standard way to control the cursor position
# Eventually, a standard did emerge - ANSI sequence. ANSI is the American National Standards Institute
# We're going to use ANSI escape sequences, to change the colour of the text that we print

# Lecture 165 notes:
# In this video we're going to create a function that'll let us print text with different effects
# We'll have included the escape codes for the main colours, as well as bold, underline and inverted text

# Some ANSI escape sequences for colours and effects

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


# So the escape sequences are defined in a series of Python constants
# We can define them once and then use the friendlier names
# The escape character, by the way, is ASCII character 27. That's 1B in hex,
# and it's easier to include the characters using the hexadecimal unicode character
# This is slightly confusing, because the backslash character is also called the escape character, in Python -
# and a few other languages
# It was called the escape character because it changes the meaning of what comes next
# When a TTY terminal received an escape character, it knew that it should interpret the next few characters differently
# The backslash, in Python strings, does the same thing
# It tells Python that it should interpret what comes next in a special way
# The above ANSI sequences, start with an escape code, followed by an opening square bracket
# So that tells the terminal that the next few characters will be special commands, that it should perform
# # # All you have to do to use these escape sequences is print them to a terminal, that understands the ANSI sequences
# The good news is that the IntelliJ run window does understand them
# Using ANSI sequence:

# print(RED, "this will be in red")
# print("and so is this")
# Note if you're using Windows, and are using a different IDE, you may not see the colour change
# If you're running your code in a Windows command prompt, then you probably won't get red text
# That might change, as Microsoft replace the command prompt with Windows Terminal, but at the time of writing,
# Windows doesn't recognise ANSI escape sequences by default
# We will cover how to make this work soon however

# So our text is in red in our run window terminal. What's not obvious, is that all output is now red,
# Check the run window
# The changes we make to the colours, etc, will stay in effect until we cancel them
# Now we can reset the text effects, by printing the reset sequence
# It's going to get a bit tedious doing that everytime, so this sounds like a good use for a function:

# Lecture 166 notes:
# Re watch lectures to see what to do on Linux or Mac
# Note to self: Spend some time learning how to use the windows file system,
# file paths and how to use the windows command prompt
# We are going to run our program like a user would
# In the IntelliJ IDE right click on the colour_print.py file in the project pane,
# then click on "open in terminal"
# We will see that IntelliJ has opened a terminal in the directory that contains our colour_print file
# We don't want to run the program in this terminal.
# The whole point of this video is to run the program like our users will, and they're very unlikely to be using an IDE
# But the good new is that we get the full path appearing
# It's got a greater than symbol appearing after it, which can make the path a bit error prone
# If you on windows: type the command 'cd' and press 'enter',
# This will print the full path to our file
# Now copy the file path to our clipboard, then open up the command prompt in windows by typing cmd in the search bar
# Now press cd (the command to change directory), and then paste in the path from our clipboard
# We are now in our project directory, now start by checking the version of Python installed
# Type in python, space, --version, and press 'enter'
# Make note of the version number that appears (Make sure its a Python 3. something)
# The type in the command python space, and then colour_print.py, then press enter and our program runs
# The program looks awful on windows, we will cover how to fix that in the next lecture
# The reason why the output looks awful is cause in windows the command prompt doesn't understand ANSI escape sequences
# This demonstrates why you should test your programs in a command prompt, before installing it for your users to use


# def colour_print(text: str, effect: str) -> None:
#     """
#     Print `text` using the ANSI sequences to change colour, etc.
#
#     :param text: The text to print.
#     :param effect: The effect we want. One of the constants
#         defined at the start of this module.
#     """
#     output_string = "{0}{1}{2}".format(effect, text, RESET)
#     print(output_string)


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc.

    :param text: The text to print.
    :param effects: The effects we want. Zero or more of the
        constants defined at the start of this module.
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
colour_print("Hello, Red", RED)
colour_print("Hello, Red in bold", RED, BOLD)
# test that the colour was reset
print("This should be the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello Blue reversed", BLUE, REVERSE)
colour_print("Hello Bleu reversed and underlined", BLUE, REVERSE, UNDERLINE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Yellow bold", YELLOW, BOLD)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)
colorama.deinit()

# Lecture 167 notes:
# Before we get into the code, what we're going to do is install a package called Colorama
# This is a package that's going to  solve the issue with ANSI escape sequences,
# so that we can get it working properly on windows
# Note that this video will also cover how to install a package that we've downloaded
# Colorama is an open source package, and we will be using a python masterclass modified version
# (due to bugs in the latest open source copy)
# After we've downloaded the Colorama package, open the terminal
# The bit in parenthesis is the name that we used for our virtual environment,
# it appears when you have a python virtual environment activated,
# and shows that we working with that virtual environment
# The latest versions of IntelliJ and PyCharm automatically activate the virtual environment for us
# In the terminal type in the command we need: "pip install" followed by the full path to the package wheel file
# Note when typing the file path (In a terminal or command prompt), the tab key will complete file names for you
# Once done, then press enter to install the package
# In the next lecture we'll see how to install the colorama package from the Python Package Index
# Basically: go to file, select project structure, select SDK, then select packages

# Lecture 168 notes:
# Colorama is a Python package that allows ANSI codes to work on the Windows command prompt
# To find documentation on Python packages check PyPI (the Python Package Index) or on github
# To install packages on IntelliJ and PyCharm do the following: (Continuing from the select packages window)
# On the Packages tab we can add and update Python packages
# IntelliJ and PyCharm use pip to install packages, its a good idea to keep pip up to date
# If there's an update availible for a package you'll see an upwards pointing triangle,
# click the matching icon to update the package
# Most packages will generally update successfully
# Some packages will fail though, so when that happens don't worry about it
# If it's a package you need, then you might need to install an earlier version of Python to use it,
# but 'pip' should always update successfully
# To install a new Python package, click on the plus icon, type the name of the package in the search field,
# then click on the package and click on install package
# Importing the Colorama package into our Python file
# The Colorama package basically enables ANSI in a Windows command prompt,
# then directs all print statements to the Windows API
# To use Colorama, we need to call the init function it provides,
# there's also a deinit, that we should call to tidy up when we're finished
# Our program now should work on all 3 operating systems
# The Colorama package is now installed in our Python virtual environment - or virtualenv, or even venv
# A Python virtual environment is an isolated installation of Python, separate from your main installation
# If you have a program that works with a particular version of a package, it might break when you upgrade that package
# If you install new versions into your main Python installation, you could break a program that you rely on
# eg. Parts of the Linux and Mac OS rely on python script, broken programs due to updates could cause a lot of issues
# For windows, simply delete and reinstall python
# Using a virtual environment simply saves you from the hassle
# A Python virtual environment contains a copy of your main Python installation
# If you ticked the box to 'use site packages',
# when you created your virtualenv, the environment will also have access to any packages in your main installation
# In addition, you can install packages into the virtualenv, without affecting your main installation
# If you install something that doesn't work, or upgrade something to a later version that doesn't work,
# you won't break important programs that rely on your main Python installation
# At worst, you can delete the virtualenv and create a new one
# There are other ways to isolate Python - Conda environments, for example. But we'll use Python virtual environments

# Lecture 169 notes:
# We've seen that we can have a Python installation that's separate from our main installation
# So how do we know which Python will be used when we run our program?
# Our main installation will be used by default
# This is clear when we run our program in the Windows command prompt,
# the program crashes because the main python installation is being used and we only installed Colorama in the venv
# When we run our programs in an IDE, the IDE activates the virtual environment for us,
# when we running from a command prompt we have to activate the virtual environment for ourselves
# To activate the venv in the windows command prompt do the following:
# In the IDE run the program and go the run pane
# The first line in the run pane shows the complete path to the Python interpreter (Which is what we want to activate)
# Copy the path (stopping just before the python.exe part)
# In the windows command prompt (after typing in the command to get to the python file path)
# Paste in the copied path to the venv, then add a backslash and type in activate
# Once we have done that we will be using the python installation for the venv
# (The prompt will have the venv name in parenthesis)
# Now we run the Python program
# Once we've finished using our venv, type in deactivate, to deactivate the venv
# What we have done here, is tested the environment that our code will be running in

# Lecture 175 notes:
# We've seen how to allow a function to accept a variable number of arguments, now we'll put that into practice
# We are gonna change our colour_print function
# We are going to improve our function by allowing it to apply a variable amount of effects
# We are improving our function, by allowing more than one ANSI sequence to be passed, for the effect parameter
# We accomplish this by doing the following:
# add * to the left of effect, and rename effect to effects
# Change the doc string to account for added functionality
# So we were getting a single string passed into our function, now we'll be given a tuple of strings
# To deal with that, we can join them up into a single string
# After the docstring adding; effect_string = "".join(effects)
# Remember that join will take any iterable, as long as each item is a string
# Our effects tuple will contain zero or more strings, and we join them using an empty string, as you can see there
# effect_string now contains all the ANSI escape sequences that were passed to the function, joined into one string
# Printing that will cause all the effects to be used in the output, so let's change effect to effect_string
# The lines with more than one effect are were we test our new and improved function
# In one of the tests, we've passed 3 different effects to the function
# The three arguments - BLUE, REVERSE and UNDERLINE - are packed into our effects tuple
# Now we can check that by setting a break point, and running the program in the debugger
