# Lecture 128-129
# Have a list containing 4 tuples, each of which contain 4 items, with one of those items being a list of song tuples
albums = [
    ("Welcome to my nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady Love"),
         (3, "Ready Steady"),
         (4, "Don't Let me Down"),
         (5, "Bad Company"),
         (6, "The Way I choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda", 2011,
     [
         (1, "Pulling the rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# for name, artist, year, songs in albums:
#     print("Album: {}, Artist: {}, Year: {}, Songs: {}"
#           .format(name, artist, year, songs))
#
# print()
#
# album = albums[3]   # This will give you the 3rd album, in the list
# print(album)
#
# songs = album[3]    # This will give you the 4th item in the Album tuple, which is the list of songs
# print(songs)
#
# song = songs[2]     # This will give you the 2nd song in the list on song tuples
# print(song)
# print(song[1])      # This will give you the title of the song
#
# # Nested indexing
# mayhem = albums[3][3][2][1]
# print(mayhem)
#
# # Showing what code 60 does in a step wise fashion
# print(albums[3])
# print(albums[3][3])
# print(albums[3][3][2])
# print(albums[3][3][2][1])
