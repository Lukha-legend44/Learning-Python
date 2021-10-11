# Lecture 130-137
# Python lets us import things from other Python files,
# which can be a great way to share data between different programs.
# Importing data from nested_data python file

# Lecture 133 notes:
# Constants in Python
# Now this is gonna be a short program, but often you'll be working with hundreds,
# or even thousands of lines of program code
# With large programs, it can be very difficult to remember what everything is
# In this code for example we have to remember that the list of songs is at index position 3 in albums
# That would be a lot easier if we gave 3 a more meaningful name. We could call it SONGS_LIST
# Now we can use the variable, instead of remembering that we want the value 3
# The problem with that is, the value must always be 3
# It's a constant that refers to the fourth item in the list
# If you go changing in the value that SONGS_LIST is bound to, our code won't do what we expect
# We want SONGS_LIST to represent a constant value
# A constant is a fixed value that doesn't change
# Constants must never be changed
# Looking at our code, we've assigned songs_list
# That's not good and it will cause our code to break
# So many languages have some way of marking a value as constant
# The keyword const, is used in C, for example. In Java, the keyword is final
# Python, on the other hand, doesn't have any way of preventing us from changing the value of a constant
# Instead, there's a convention that constants should have names that are in all capitals, hence SONGS_LIST
#  Whenever you see a name that's all in capitals, that means it represents a constant and you shouldn't change it
# Now you'll find that convention is in the Python Style sheet
# Note that this is only a convention, though. The Python compiler won't stop reassigning a constant -
# it's ultimately your responsibility to make sure that you don't do that
# Python 3.8 adds a final annotation, and a final qualifier to the typing module
# However, the compiler still doesn't prevent you from changing the value of a constant, s
# o pay attention to this convention
# Use uppercase for the names of your constants, and don't change any variable that's in uppercase
# Because variable names are case sensitive, SONGS_LIST represents a different value to songs_list
# If you want to be even clearer, you could refactor SONGS_LIST, and change it to SONGS_LIST_INDEX
# So that's constants in Python. There's nothing special about them - they're just variables
# The compiler doesn't treat them any differently, to any other variable
# We write them in capitals to let other humans know, that they represent a value that shouldn't be changed

# Lecture 137 notes:
# Some advantages of tuples are that they use less memory,
# protect against unintended changes to your data and help prevent bugs in your program

from nested_data import albums
# Note when you run this file with the imported data,
# it runs all the code in the file where the imported data originates
# To deal with this issue we commented out the code we don't need

SONGS_LIST_INDEX = 3  # Whenever you see a variable name written in all capitals(uppercase),
# it represents a constant and you shouldn't change it
SONG_TITLE_INDEX = 1

# while True:
#     print("Please choose your album (invalid choice exits):")
#     for index, (title, artist, year, songs) in enumerate(albums):
#         print("{}: {}".format(index + 1, title))
#     # for index, value in enumerate(albums):
#     #     title, artist, year, songs = value      # Lines 19 & 18 accomplish the same thing as line 15
#     #     # The tuple is just unpacked in the same line as the for loop
#     #     print(index, title, artist, year, songs)
#     choice = int(input())
#     if 1 <= choice <= len(albums):
#         songs_list = albums[choice - 1][SONGS_LIST_INDEX]
#     else:
#         break
#     print("Please choose your song:")
#     for index, (track_number, song) in enumerate(songs_list):
#         print("{}: {}".format(index + 1, song))
#
#     song_choice = int(input())
#     if 1 <= song_choice <= len(songs_list):
#         title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#     else:
#         break
#     print("Playing {}".format(title))
#     print("=" * 40)

# Challenge: alter the program so that when an invalid number is chosen in the song selection stage,
# the code doesn't break but prints out the list of albums and the user has to the select the album
# and return to the song selection stage
# My solution:
while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break
    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    else:
        print("Invalid choice, returning to album selection")
    print("=" * 40)

# Python Masterclass solution:
# while True:
#     print("Please choose your album (invalid choice exits):")
#     for index, (title, artist, year, songs) in enumerate(albums):
#         print("{}: {}".format(index + 1, title))
#     choice = int(input())
#     if 1 <= choice <= len(albums):
#         songs_list = albums[choice - 1][SONGS_LIST_INDEX]
#     else:
#         break
#     print("Please choose your song:")
#     for index, (track_number, song) in enumerate(songs_list):
#         print("{}: {}".format(index + 1, song))
#
#     song_choice = int(input())
#     if 1 <= song_choice <= len(songs_list):
#         title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#         print("Playing {}".format(title))
#     print("=" * 40)

