# Lecture 279-287

# Lecture 279 notes:
# So we are gonna leave geometric functions where we left in the previous videos but we gonna carry on working with
# Tkinter to produce a very simple card game. Now there's a couple of things that we haven't fully explored with
# functions yet and as Tim mentioned earlier there's another reason why IntelliJ warns about shadowing variables in the
# outer scope. This game is gonna give us a way to look at that in more detail. Now blackjack itself is quite a simple
# card game, the aim is for players to get a higher score or higher total than the dealer without going above the score
# of 21. Now if the total value of the cards in a hand comes to more than 21 then the player is said to have bust or
# to have busted and that is game over. Now there's variations on the way the game is played,
# as Tim mentioned our game is gonna be a simple version and will have the following conditions. The dealer deals one
# card to each player then to himself, each player but not the dealer then gets a second card, the players then decide
# whether to stick with a total they have or hit, which means to get another card. Now a player can hit as many times as
# they like but a soon as their total goes above 21 they're bust. The cards that a players hold when they go finishes
# is called their hand. Once all the players have either stuck or bust, the dealer gets a second card and the dealer
# then decides whether to stick or hit. This works the same as for the players and if the dealer has over 21 they bust,
# then all the players that haven't bust effectively win.There is another constraint to the dealer though, the dealer
# cannot stick on less than 17. So in our version of the game we will also play the dealer must stick if they have 17 or
# more. Now once the dealer has finished any player whose total is more than the dealer wins and any player with a
# smaller total losses. So if the dealer and the player have the same scores then they draw. So to keep it simple we
# gonna play with a single player but you can add more players yourself once the game is working. Now in case for anyone
# who isn't familiar with Western playing cards. There's 13 cards in each of 4 suites and that makes a total of 52 cards
# in the pack effectively. The first 10 cards are 1 to 10 and then there are 3 face cards called jack, queen and king,
# each also having a value of 10 in this game. In other games the queen will rank higher than the jack and king higher
# than a queen. So suits are called hearts, clubs, diamonds and spades. Now there is one final complication to make
# things interesting. The ace which is the card with the value 1 can also have the value 11, then the player can decide
# which of the two values it should take so they get the best total in their hand. Now before we start we gonna show the
# cards on the screen rather than printing "3 of spades", "queen of heart" etc. So we we are gonna draw it, so to do
# that we need some graphics for the cards, and there is a very good collection created by David Bellot.
# (Watching Tim's screen in the video). So the images are licensed under the GNU LGPL Lesser General Public License,
# so that basically allows you to do what you want with it as long as anyone you give or sell your program to also has
# the same rights, but keep in mind if you are gonna use this in a program that you need to give people the same rights
# and those rights include full access to the source code. So if you were releasing an app you have to give that source
# code access, that's what you're giving up for this particular type of licensing. By Tim giving us the link to download
# these images he is complying with the LGPL and if you create and distribute a program using these images, read the
# license carefully and make sure that you actually comply. So all 52 cards plus 2 jokers and an image of the reversal
# are in a single .svg file, so it's possible to leave them in that format and to extract the individual images as the
# program runs, there are libraries to help with this, but to make life easier though what Tim has done is extract all
# the images and you can download them from the link in the lecture at the end of the course to get all the images in
# .png and .ppm format. Now interesting thing to keep in mind with Tkinter that support for .png files was added into
# Tkinter 8.6, so if you are using an earlier version, then you need to use the .ppm files. Alright that's enough
# talking, we've talked quite a bit, let's actually get into starting some coding.But before we enter any code we need
# to extract the cards folder from the zip file and place it in the same directory as the blackjack.py. Now you can put
# it somewhere else if you prefer but the path you'll be using to find the coded images will then be changed to reflect
# your actual location.
# Ok so we are gonna start the program by importing Tkinter as normal and because this is a card game and we need a
# degree of randomness to make it interesting we are gonna also import the random module.
# Now the program needs to have space for the dealer's and the player's cards and some way to display the result,
# and also buttons for the player to choose hit or stick. So we can change the captions for the buttons later but while
# we're developing the program we are going to use one button to deal cards to the player and another to deal to the
# dealer. The game is going to look like this (refer to the image presented at 7:50), so that's what our screen is gonna
# look like. So the main window has got 3 widgets; a label at the top to display the result and two frames, one below
# the other. The top most of the two frames is going to contain the cards and scores for the dealer and player,
# and the one below will hold the buttons as you can see on the screen there. Now the card frame will itself contain two
# other frames, one for the dealer and one for the player, as well as labels to hold the name as well as the score.
# So let's start typing a bit of code in to start building this interface.
# So we still got some more typing to do so what we gonna do is stop this video now and in the next video we'll continue
# on. We still need to add the embedded frame to hold the card images, and the buttons.

# Lecture 280 notes: Load cards
# Ok so moving on with our blackjack program, we about to do the player card frame now.
# Alright so next is the buttons.
# Alright so that's the basic code done. So the main window's got 3 widgets, the label at the top to display the result,
# and 2 frames one below the other. The topmost of the 2 frames is gonna contain the cards and as well as the scores for
# the dealer and player. The bottom frame will hold the buttons. The card frame itself will contain two other frames,
# one for the dealer and one for the player, as well as labels to hold the name as well as the score. So the card frame
# as we said will contain 2 frames that will hold the cards, and by putting the card images into separate frames
# starting a new game is easier because we just have to destroy the entire frame rather than trying to find out each of
# the cards in it and destroy them separately, note this will make more sense when we come to do it so let's move onto
# loading the card images. So the file names of the individual images are quite well formed and made up of the card's
# value and suite followed by and underscore. It means we can pragmatically load these in pretty easily. So for the
# cards from 1 to 10 we can actually load that with a simple loop to load them all in. Now the face card images can be
# retrieved using a second loop that runs through a list of names (jack, king and queen) and by wrapping all that in
# another loop that runs through the list of suite names, all 52 card images can be loaded. Now this is something that
# the program will only have to do once but we still going to create a function to do it. By placing this code in it's
# own function the main program is going to be far less cluttered and more readable as a result. So let's go ahead and
# do that. So we've now got our load images function written and that should now be able to retrieve all those images we
# need for our game into memory. So the cards list should after this contain a list of tuples, each tuple storing the
# value and image for each one of the 52 cards. And the images have been loaded into Tkinter photo image objects, which
# are fairly basic but do all images to be displayed easily and that's what we wanted to do here. And what we're going
# to do is right on the bottom add some code to just test that this actually works. So if we run this now we should be
# able to get something, it won't be very exciting but we can at least demonstrate that things are actually working. If
# we go to our interface its obviously not working yet because we haven't actually added the cards, so we can close that
# down. But we should be able to confirm that we've got our various objects in here and you can see there is multiple
# objets that are loaded, so it seems that it has worked, we'll just have to print out the cards or display them we
# should say to confirm that they've been loaded, but it seems to have loaded into the list which is good. So a new deck
# of cards can be created from the cards list now that we've imported them and then we can shuffle them using the
# shuffle function from the random module that we imported. So the program will also need to store the cards dealt to
# each player, so before we start creating the functions to make all of this work we going to initialise a dealer hand
# and player hand list.
# So we going to finish the video here, now in the next video we're gonna go ahead and write some code to deal the
# cards. We are gonna deal cards to the players each time the button is clicked, so we need a function called deal_card
# and we'll work on that in the next video.

# Lecture 281 notes: Deal Cards
# So moving on we now need to start creating some functions that will ultimately drive the game. So we are gonna start
# out by just dealing cards to the players each time the button is clicked. So we need a function called deal_card after
# the load images functions, so lets do that. So the function has got a single parameter and that's the frame the image
# should be displayed on. Now up until now we placed all the widgets using the grid manager, when it comes to adding
# card images, a pack manager is a much simpler one to use, as you add new ones to the left they just stack up against
# the ones already there, so in this case for cards it's obviously perfect because everytime we add a card it's gonna
# be stacked. Now generally speaking it's a very bad idea to mix grid and pack in the same window and the Python 3
# compiler will give an error if you try, but its ok to use the pack manager in it's own window. Now as every widget is
# a window, packing the images into into this frame is fine as long as we don't try add anything else to the frame using
# grid. Now we had a good look at lists in one of the earlier sections but we didn't look at the pop method that we are
# using. Now pop is a way to retrieve an item from a list, that also removes it from the list at the same time. So think
# about it as the opposite of append. Now append adds an item to the end of the list, pop takes an item from the
# specified position in the list, defaulting to the end if the position to be taken from is not specified. By
# specifying position 0 we can take cards from the start of the deck. Both append and pop can also be used with an index
# to add an item at the specified position, or remove one from the specified position, but if we started popping cards
# from the middle of the deck the players will not be very happy with the dealer. Once the next card has been retrieved
# from the deck the function creates a Tkinter label in the frame that's passed into the function and sets its image to
# the photo image stored in the next card tuple. The label is then packed against the left side of the frame so that all
# cards should stack up against each other from left to right as they are being added. So the newest one will be to the
# left. Now the function then returns the next card tuples so that whatever is calling it can also check the face value
# of the card. So that's the function to deal a card. We also now need to link up the function to the buttons.
# Now we briefly saw this in the videos introducing Tkinter, but the only button we actually got working was the cancel
# button. Now a function is associated with a widget using the command property, so it might be tempting to come down
# here to the dealer button code and add command=deal_card(dealer_card_frame). So in a earlier tkinter video Tim
# mentioned to you that you have to be very careful when setting up the command property of widgets, the value that
# you assign has to be the function you want to be executed when the button is clicked. Now you definitely don't want
# to call the function instead of assigning it to the command, and that's actually what we've done by typing
# command=deal_card(dealer_card_frame), by attempting to pass the frame to the function at the same time as assigning
# the function of the button. So the actual correct code would be command=deal_card.
# But of course that's now introduced another problem because there's now no way to specify the frame parameter that the
# function actually actually needs, and in fact that's true there's really no way to pass a parameter when a assigning
# a function in this way. So if you include the parentheses after the function name,
# then what you're doing is you're assigning the result of calling the function rather than assigning the function
# itself, and obviously we want to assign the function here so that it's actually executed or called when the button is
# clicked. Now if you don't use parentheses then you can't specify an argument to a function. So it sounds like a catch
# 22. Well the thing is we've only got two buttons so the approach that we're going to take here is to create one
# function for the dealer and one for the player, and assign them to the corresponding button. Now this is not the only
# approach, and for something like the calculator that's got loads of buttons it wouldn't be a suitable solution, it
# wouldn't be practical and we'll be looking at other ways to deal with this later in the course, but for now what we
# gonna do is just create two functions. So we gonna put these after the code that we've just added to deal a card.
# So let's do it.
# So you can see basically what we've done there is we've just created another function that's gonna call the function
# that we need with the required parameter being the dealer or the player card frame, depending on which method we
# actually called, either deal_dealer or deal_player. So no that we've actually done that we can actually connect the
# buttons. So we come back to the dealer and player button code and add the commands. So now that we've done that the
# program should run. Now let's try giving it a go. You can see it is working. One thing we haven't done is change the
# minimum and maximum size, at the moment it's actually going a lot wider than what we would normally like it to be,
# but we'll look at fixing that in the next video, for now the code is actually working and it's actually adding a new
# card everytime you click on it which is pretty awesome. If we kept adding cards actually, if we did get to 52 the
# program will end up creating an error when there's no mare cards left, because of course it can't deal anymore cards
# if there is no more left in the deck, and that's because attempting to pop an item from an empty list isn't allowed.
# Now the maximum number of cards a player can be dealt without going bust is 11, we ordinarily in a single game don't
# need to worry about all the cards being dealt and so we can actually ignore that error for now. Next thing we want to
# do is calculate the players score and display it in the frame and we'll look at doing that in the next video.

# Lecture 282 notes: Global variables
# Ok so moving on with our blackjack program, now just before we continue there is a few items of housekeeping that
# we need to go through first. When we actually run the app, Tim mentioned before that it wasn't sort of looking the
# the best, so if we have a look and run it you can see that there's a lot of white space and obviously as we start
# using it, it gets better and the cards get dealt and it's starting to take up some space so probably the easiest thing
# to fix right now is just to change this background. So what we gonna do is change the background so it's green. So
# that's number one. Let's go ahead and do that. And where we would do that would be just under the two lines that set
# the window title and the geometry. So now if we run that we've got a green window that's going to look a bit better
# once we get some cards in there. So again that's number one, that has made our application look a little bit nicer
# and bearing in mind that we haven't got any text showing here in the results label but that will be coming. But the
# other issue we need to fix is the line of code where we create the main window, it's really in the wrong position,
# that should really be after all the functions and we'll be actually dealing with talking about this a little bit
# later, we're going to talk about an idea of a main function to put the code that's not directly in functions, but we
# will be doing that a little bit later. Lastly in the deal card function you may recall that we talked in the previous
# video about making sure when we're actually grabbing cards that we don't pop the cards off the end of the list, and
# that's what we did. So we gonna change next_card = deck.pop() to next_card = deck.pop(0), so we don't grab a card
# from the bottom of the deck. So now that we've done that, we've finished off that bit of housekeeping the next thing
# we really need to do is calculate the players score and to display it in the frame. Now we want to demonstrate the
# other reason why IntelliJ gives warnings about local variables shadowing those from the main program, and of course we
# talked about shadowing in the previous videos and so the the first attempt at running this function isn't going to be
# the final one, so although we'll be replacing this first line of code the technique used is sometimes necessary,
# so it's really important to understand it and the reason for these warnings. So in terms of the players score, the
# sensible place to calculate the total is just after each card has been dealt. So what we gonna do is modify the
# deal_player function. So the face value of the card can be obtained from the tuple returned by the deal_card function,
# so that can be used to update the players total. Now the code also has to deal with the two values that an ace can
# represent, so in blackjack that's not actually too difficult luckily because no matter how many aces a player has,
# only one of them at most can have the value 11, or of course the player will be bust, because the maximum score is 21.
# So the technique used here is to give the first ace the value 11 and give any subsequent ones the value of 1.
# Now if the player goes bust by holding at least one ace then 10 is subtracted from the total and a check for being
# bust is performed again. So that way it will actually give the player the option to treat an ace as one instead of 11.
# So in order to do all this we actually really need two more variables, one to store the players total and another to
# track whether or not the player holds an ace that has the value 11. So let's go ahead and add those. Just after the
# player_score_label we gonna add the variables there. Now this a new term but variables that are defined in the main
# part of the program rather than in a function are called global variables and variables that only exist inside a
# function are called local variables. So in the case where we actually added these 2 global variables, by putting
# them here outside of a function we're making them global variables. Ok so now that we've actually got those 2
# variables set up we can go back to our deal_player function and start using it. So we gonna start typing some code in
# deal_player. So at this stage the only information we can get on the outcome of the game is if the player goes bust
# and that's because the dealer will not get anymore cards until the player has finished his/her go. So we can set the
# result to the dealer winning if the player goes bust, but any other outcome will have to wait until the dealer is
# getting cards. Now before going any further we going to run the program and you can see that it sort of behaves but
# there is a subtle bug there. Ok so we'll just have a look at this running now. So if we click on player notice that
# the score is being updated, but if we click it again notice that it's only storing the last value. So it's not
# actually calculating the total  and the reason for that is going to probably be pretty obvious if we actually close
# this and have a look. This bug is occurring because we used a local and overrode the global variable and set it to
# a value of 0. So consequently the player_score is only going to ever be the total of the last card that was actually
# drawn. Now just before we go ahead and actually remove that and fix that error, if we just have a look at the error,
# "shadow name player_score from outer scope" or "shadows name player_score from outer scope", the shadowing of
# player_score is an error but why don't we get the same warning about player_ace, because both variables are defined
# in the main program but IntelliJ is really only warning about player_score in the deal_player function. The answer
# is that the value of player_ace is used in the comparisons but the difference between that and the player_score
# variables is that the function doesn't attempt to assign a new value to player_ace but player_score is assigned new
# values. It's because of this difference in the way that they are used that Python treats the variables differently
# inside the function, so IntelliJ is just reporting here it's Python that's actually making the rules. So we can
# confirm that there is a difference by using ctrl click. So if we ctrl click on player_score in the function other than
# the definition, it's obviously staying within the function. Whereas if we ctrl click on the player_ace in the same
# function, it goes back to our definition in our main program outside the function. So that was just a quick way to
# determine a local or global variable. So when you use the name of a global variable in a function Python assumes that
# you want to use the global variable and will happily let you until you try change its value, that's the key point
# there. So as soon as you assign a new value to a global within a function Python then creates a local variable with
# the same name and your code no longer refers to the global variable. So once you understand this behaviour it actually
# does make sense and it actually saves you from introducing hard to spot bugs, but it can be an unexpected behaviour
# until you do understand that and we can see that in action in our deal_player function obviously there now. So at the
# moment we've used the variable name player_score and assigned new values to it, so as a result Python's created a new
# local variable called player_score and IntelliJ's complaining by giving us a warning that it shadows the global
# variable. So it is important to pay attention to those warnings as they are the only clue that we really not in fact
# changing the global variable player_score. Also inside the deal_player function we use the variable name player_ace
# but we haven't assigned any new values to it so as a result Python let's us refer to the global variable and
# consequently there's no warning bells from IntelliJ about shadowing because we in fact not doing that, because we are
# not saving a value and essentially not creating a local variable. So we gonna end this video here, now in the next
# video we'll continue our discussion about this and then move on and get this deal_player function working correctly
# in calculating the score for the entire hand the player's got rather than just the last card.

# Lecture 183 notes: Global keyword
# Ok so moving on what we'll do in the deal_player function is we'll just add that command that we saw in the previous
# videos to print all the local variables just so we're 100% clear on which variables are local to the deal_player
# function. And this will print out a list of all the local variables. So if we run the program now and start clicking
# the player button, and you can see card_value which has a value of 10 and player_score which also has a value of 10,
# they are the only 2 local variables in this function. So it can be really useful if there is any confusion in your
# programs to use this locals function to call just so you are aware fully which variables are local. Ok and it just
# bares repeating the rule again one more time, when you use the name of global variable inside a function, Python is
# going to use the global variable as long as you don't assign a new value to it, as soon as you add code that tries to
# change the value, the variable itself becomes local and shadows the global variable with the same name. So because
# the function assigns the value in this case 0 to player_score, player_score becomes local to the function and because
# no values were assigned to player_ace, we've only used the value we haven't actually stored anything in there, it
# refers to the global variable. That also means that you can have a function that's happily using a global variable but
# will suddenly switch to being local if you happen to add code to change the value of the variable, and that can be
# really a gotcha there that will start potentially unpredictable things, or giving you unpredictable results in your
# program. Now the deal_player function really provides a good way to see this in action because we should actually
# change the value of player_ace and looking at the code in the deal_player function, the card value is set to 11 if
# this is the first ace dealt, so if that is the case then what we really should be doing is setting player_ace the
# the variable to True so that we know that there is an ace with the value 11 so similarly it should also be set to
# False when we subtract 10 from score. So if we go ahead and add player_ace = True in the deal_player function after
# the first ace has been dealt, immediately we get an error. Well 2 things actually happen when we do that. So the
# one error is in the if statement, "unresolved reference player_ace", and this can be a little confusing, you probably
# thinking hang on player_ace is a global variable why isn't that working? Well again because we've assigned a value
# what's actually happened is it's now being converted into a local variable for this function and when we're doing the
# test for the value it hasn't been initialized and such it doesn't exist, so that's why it's coming and saying
# "unresolved reference to player_ace". And the other error in terms of the shadowing name, we've talked about that
# extensively, we know why that's coming up and that's just because we using the same variable name of the global
# variable. So deal_player was a working working but as soon as a perfectly valid assignment was actually added then we
# started getting an error. Now before you actually went through this video, this type of error would probably have
# driven you nuts, now though you can see why IntelliJ warnings come up and immediately know what's going on. So in a
# while what we gonna do is rewrite the function so that it doesn't try make use of global variables, ideally a function
# should be self contained and not make changes to anything outside itself. Now when a function does change things like
# global variables the changes are known as side effects and it should be really avoided wherever possible, but with
# that said sometimes side effects are necessary so they are allowed but are discouraged. Python automatically when
# changing a global variable to local when you try change it is Python's way of discouraging us from doing that. Now
# because they are occasionally necessary Python does provide a way to make changes to global variables within a
# function because of course this is what the problem is here, we actually here want to change the value of a global
# variable and it's not allowing us to do that because as soon as we type in the same name and type in an assignment to
# save a value to that variable it's created a local variable and then consequently in this case we got an error saying
# that the variable didn't exist in the if statement. So how do we go about changing a global variable, well the way to
# do that is to specify that you intend to use a global variable by using the global keyword, but before doing that
# let's get rid of the erroneous line that sets player_score to 0 everytime the function is called, because that
# shouldn't be there, because we really do want to get the score actually saved globally, so let's go ahead and comment
# that out. And as soon we've done that you can see there are other errors, there's now errors relating to player_score.
# So by removing the assignment that we did when we commented out player_score = 0, player_score now doesn't have a
# value as far as this function is concerned and this is just primarily because we're trying to save a value into
# player_score. So player_score doesn't exist as a variable because of the shadowing functionality that Python does. The
# local variable hasn't been initialized and that's why we are getting those errors again. Similarly to what was
# happening with player_ace. And specifically the augmented assignment requires that the variable already has a value
# and of course because of the shadowing technique Python knows that we're using a variable of the same name and it
# would normally create a local variable but we haven't initialized that variable at this point in time. So because
# they're assignments, player_score is still a local variable but of course we just commented out the line that gave it
# a value. Ok so enough talk, so how in other words do we get the function in this case to use the global variables of
# the same name. Well to tell Python we want to use the global variables we jut use the global keyword at the start of
# the function, so let's do that. What that immediately tells the function to use, is to use the global versions of
# those variables and not trying to create a local variable of the same name and consequently all the errors disappear
# at that point in time and also the warnings about shadowing have also disappeared as well because in fact we're not
# shadowing anymore because the global keyword essentially is really telling the function to use the global variables
# from this point forward in that function. Note we need to make another change in the function, player_ace = False.
# When we are deducting 10 from ace if you recall we need to actually say player_ace = False. So now we should be able
# to run this. And now when we run it we click on player you can see it's actually working, if the player score exceeds
# 21 we also see the result that dealer wins. Note that if we get blackjack i.e 21 the player wins but we haven't got a
# calculation in the code to actually check for blackjack as we only doing a score check for if the player's score is
# greater than 21. So what we've determined now is that Python does allow global variables to be modified inside a
# function because of course that was the problem. So the function is now working as we saw when we ran the game but if
# if this function's modifying the 2 global variables player_score and player_ace, how can we really be sure that some
# other function isn't also changing them and it's quite possible in a game that could happen, and if something else
# does change them then the deal_player function is no longer going to work correctly because it really is assuming that
# it's got full control over those variables or the way that the code has been written. This is the main reason why
# side effects are discouraged and why functions really should only modify variables in the outer scope i.e globally,
# if there's really no other way to perform the functionality that you are creating and usually there is actually a way
# around. So before we write in the function to remove side effects it is actually worth revisiting the design. So the
# deal_player gets a new card and maintains the total by adding the value of that card to it's tally and that tally is
# now stored in player_score as a global variable. And we gonna have to do the same thing for the dealer so it may make
# sense to create a function that returns a score if it's given a list of cards, so what we gonna do is we are going to
# add a score_hand function and it's purpose is to do that, to look at a hand and calculate a score based on that hand.
# So we are gonna create that under deal_cards, so let let's do it. So given a list containing tuples were the first
# item in the tuple is the value, the function is going to add up all the values and return the score. And as we
# mentioned the first ace will have the value 11 rather than 1 and if the total score goes above 21 and there is at
# least one ace then the total has decreased by 10 and hopefully the player won't have busted, but in any case we are
# going going to return the score. So that is pretty much the same as what we're doing when dealing the card and it now
# goes through the entire hand rather than the single card at a time. So now that we've done that we can actually
# implement this in deal_player, and before calling it the card just dealt is added to the list that contains the
# player's hand. So going back to deal_player, obviously our design has changed dramatically, so what we gonna do here
# is we are going to comment out this the function, and create a new version of deal_player, so let's do that.
# So basically what we're doing now is, what we've done is we've rewritten the deal_player function to call the logic
# that we've just created in the score_hand and we are still getting this warning about shadowing, but we no longer need
# these global variables so we are going to comment out player_score = 0 and player_ace = False.
# So we gonna stop this video here and in the next video when we come back we're going to look at the deal_dealer
# function because that is now very similar to the deal_player, but obviously we need to do a test to see whether the
# player wins and etc.

# Lecture 184 notes: Test blackjack game
# So what we need to do now is implement the deal_dealer function. Now this turns out to be very similar to the
# deal_player function but because the player's turn has finished by the time the dealer gets more cards what we can do
# here in this function is we can add a bit of extra code to check to see who has actually won the game because of
# course the only check we got at the moment is in the deal_player function where we check to see if the player went
# bust resulting in the dealer winning. So we need to see whether the player wins as well, we also need more detail in
# addition to that because at the moment we are only really basically checking to see at the moment if the payer has
# busted, if the score is greater than 21. There could be a situation of course where both a dealer and the player got
# cards less than 21, we need to that check as well, as well as checking to see whether the dealer has busted.
# So let's make a start by working on the deal_dealer function. So that should be our method. So it's really quite
# simple no matter what the dealer_score is, if the player went bust then the dealer wins. So that's the first condition
# tested. If the player's not bust, the player wins if their score is higher than the dealer, or the dealer went bust.
# And obviously we get down to that last else, any other outcome means a draw. Alright so we should have the basis for
# a game here. So let's run this and see what it does. So let's see whether it actually works. We'll click player
# first, the player's got an 11, an ace which is scored 11 which is correct for the first ace. We click dealer next,
# it's got a 10 and according to this the player has won. And we continue on, we click player then dealer, and it's
# still not quite working at this stage, but we've got the basis on here, it's actually doing some basic calculation
# but obviously we need to do a bit of work here because when we first started it, and we'll just run it again, click
# player then dealer, we are getting a message immediately that the dealer wins because the score was greater than the
# players. So it's a little bit disconcerting that because that message shouldn't really be appearing until the dealer
# has finished playing or the player has gone bust, so it's correct it's actually processing this function correctly but
# we need to put an extra condition in to have the game go as far as it can before it actually starts showing who is
# winning. So if we run the program again and click player then dealer, we guess it'd be more accurate to say that
# dealer is winning so far at this point in time in the present game. If we click on player again the result window
# still hasn't changed, as the deal_player unction only directly affects the result window when the player goes bust,
# otherwise it works indirectly through the deal_dealer function. Obviously we got a bit of work here to do still,
# so let's go ahead and continue looking at this. So one advantage of creating functions that perform specific tasks is
# that they can be used whenever you need the functionality that they provide and we saw an example of that with
# score_hand which we used in a number of places which is pretty handy that we only written that code once and we are
# able to call it multiple times. So in the main program we really don't want the dealer to play their turn as
# the initial cards are dealt, we just want them to deal a card and store it in their hand. So what we gonna do is make
# a change there, go down to the bottom, so after the deal_hand. If we run that again let's see what that looks like.
# So it's definitely getting better. Now we haven't got any initial scores showing up, we correctly showing the player
# score to be 13. We got a problem here though, the dealer score is showing 0 for some reason (Note I already fixed
# that, code is just commented out), it could be a bug or something that we've introduced there because the dealer score
# should be calculated and it should actually initially be 9. So it's getting better but it's still not correct yet
# because the person playing the game has to click the button for each of the dealer's cards and once we clicked it then
# correctly it does the score though it didn't do that initially, but we wouldn't ordinarily want that to happen.
# The computer should really play the part of the dealer and all the player should do is click their own button for more
# cards or the click dealer button once they want to stick. So the deal_dealer function that's called when the dealer's
# button is clicked will need to score the dealer's hand, which only has a single card to begin with and then
# automatically keep dealing more cards until the dealer score is greater than or equal to 17 or the dealer goes bust,
# and once that has happened the scores are then checked and the results are displayed, so let's go back and make a
# change to the code for that. So basically what happened is when we go to deal_dealer it should automatically keep
# dealing cards for us until it gets to a score of 17 or higher and obviously it could still bust and the the rest of
# the code will be executed and we can establish whether there's been a win or a loss. And the reason in the function we
# now start with dealer_score = score_hand(dealer_hand), where we actually calculating the score, is we are dealing
# with the score for the card that's initially dealt when we first start, because you saw that when we ran this the
# previous time the dealer score was showing us a 0, so that's why we are calculating that score first and then we're
# actually adding the score each time another card is dealt. So looking down, the code we've got down here now,
# so we got deal_player() which draws the player card, dealer_hand.append(deal_card(dealer_card_frame)) which
# actually called the deal_card function to deal the first card of the dealer and then we deal the card for the player
# again. So basically what should happen now is that we'll see two cards for the player and two cards or more for the
# dealer depending on what the score was. So let's try running the program and see what happens.
# So now when we click dealer you notice how it went through and automatically selected the extra cards, it basically
# won the game at that point and we got no play again button at the moment so we need to stop and start it again.
# So basically the program is now playing a reasonable game of black jack and all dealing is being taken care of by the
# computer.

# Lecture 285 notes: Blackjack challenge
# So talking a little bit about the challenge, it's going to be quite simple because just looking at where we're at
# with the game now it plays a reasonably good game of blackjack and all the dealing is now taken care of by the
# computer, so we only need to click on the dealer once we are finished with our turn and the rest of the game finishes
# and the deal_dealer function sort of handles that functionality to play the game as far as the computer is concerned.
# It is a bit annoying though, which we have seen Tim having to close the window and run the program again for a new
# game. As Tim mentioned in the last video it's time for a challenge. Just before that one final comment about global
# variables, you probably sick about it now but we are harping on about it because it's really important that you
# understand this and get into the right mind set about how to use them so you are aware of the limitations. You might
# be wandering why the variables player_hand and dealer_dealer are not triggering warnings about a local variable
# shadowing the global ones because both the deal_player function and deal_dealer function, if we go back and have a
# look, those are both appending new cards to the corresponding list, so wouldn't that count as modifying the global
# variable which would make them local, because we talked about that in the previous videos. Well the answer is that
# neither variable is modified, they're initialised as lists towards the end of the program, and continue to reference
# same lists as long as the program runs. So adding items to a list or removing items from it is not modifying the
# list variable, it always has the same value, which is a list, and the contents of a list can change. Now adding items
# to a global list is still a side effect but it's not considered as dangerous as changing the list that the variable
# holds for example. Lists exist to have items added and removed and so consequently this is acceptable behaviour and
# that's why IntelliJ is not actually warning us of that, so it would still probably be better to pass the lists
# as arguments to the functions but as we can't provide parameters to functions that are used as button commands we
# really don't have any choice here but to use global lists, so that's of course why we went ahead and did that.
# Ok so moving on now the challenge, and it's going to be quite a simple one, the challenge is to add a new button to
# the program with the text, "new game". Now the button should call a function that clears the cards from the screen,
# it resets the players and dealers hands and then starts a new game. Now the easiest way to clear the contents of a
# frame is to destroy the frame and create new one with the same name,
# and in fact that's why the program has a player_card_frame and dealer_card_frame inside the card frame itself.So
# that's it, go away and create a new button with the text new game and again the functionality clears the cards from
# the screen and resets the player and dealer hands and then starts a new game.
#
# Python masterclass solution:
# Ok so hopefully you managed to figure it out and have a pretty good go at getting it working. So let's go through
# what the Python masterclass solution is to implement this, and what we're going to do is create a new function called
# new_game. Now the thing to remember here is that most of the initialization code is in the main program concern
# setting up the GUI, and so consequently we don't need to repeat all of that every time a new game is started, but the
# dealer_card_frame and player_card_frame will need to be cleared, so calling the destroy method will do that, and once
# that is done the lists holding the hands will need to be cleared, and then the first 3 cards dealt, and we can also
# make a start on that now so let's do that. Now creating the button itself is pretty easy, we already have a frame in
# place so let's add that down below the initialization code. And just the other thing we can do because you've noticed
# we've got a lot of code there that's being used, so we can actually call the new game function after we initially
# create the dealer and player hand variables (comment out the code dealing the first 3 cards, this will now be handled
# by the new_game function). We can actually call the new_game function and what we're trying to do is avoid duplication
# of code because we had that initial code now in the new_game function. So basically at the start of the game we can go
# through and just actually run this and we have actually got a frame we are destroying, technically destroying a frame
# we just created and creating it again, but what we are doing is avoiding this duplication of the code and not running
# it sort of in 2 places, so the idea is to put the code and only execute it only once. So let's try running that and
# see whether it works. And so far so good, we've now got a button for a new game. So it's working well but we are
# gonna have a problem with this and if we keep playing we should eventually get an error. So why has it crashed?
# The reason it crashed is that we ran out of cards, remember we created the deck of cards initially and we're not
# refreshing those. Now there are many ways to solve this, but the obvious one would be to create a new deck list
# everytime a new game has started by just copying the 2 lines where we initially created the deck and adding them to
# the new_game function. The obvious approach would to everytime we create a new game we basically execute the lines of
# code which create and shuffle the deck, so that each game has a new deck. So that would be one way and we could
# actually put that code in the new_game function (approach used in my solution), but we're gonna take a slightly
# different approach here, so what we gonna do is everytime a new card is dealt it is going to be put back at the
# bottom/start of the deck, in other words you reusing the same deck continually. So in Python terms the object is going
# to be appended back to the list, so we want to do that in the deal_card function. So let's do it. So that should be
# all we need to do, so this is actually more realistic because it's like a real game and that's because when you
# normally play a game of blackjack you don't start with a brand new deck for every single game.
# Note added random.shuffle(deck) because if we didn't add it then if someone was paying attention to each card dealt
# they would eventually be able to work out the order of the cards after enough games have been played. Now there are
# many other improvements we could make to the game. If a new deck is not created for each new game, then the game could
# have an option to shuffle, and let's add that as well, so you can randomly click on a button and have it do a shuffle
# for us. Ok so let's run that just to make sure that it is working. Ok we now got a shuffle button, so we just click on
# shuffle, we are not getting any indication that it's working but it's also not crashing which is good. So that's good,
# that's all working nicely and perhaps another final thing we could do if we want is to add a score of how many games
# each player has won and display the tally at the top of the screen. We gonna finish the video here now because it's
# getting very long, but there is one last final mini challenge, and that's how would you change the program to play the
# game with several packs of cards, in other words just assuming you're adding 2 or 3 packs of cards and you got one
# deck that contains 2 or 3 packs, how would you actually do that? Ok so the solution to that, where we initialise the
# deck you can see deck = list(cards), that's one deck of cards. So we could simply just put
# deck = list(cards) + list(cards) + list(cards), and effectively you've got 3 packs of cards now that are being put
# into our overall deck.
#
# My challenge solution:
# I firstly created a new function called new_game.
# The function deletes the player and dealer card frames then immediately recreates the new frames to reset the game.
# The function then proceeds to clear both the dealer and player hands.
# The function also deletes and recreates the deck for the new game so the deck doesn't contain fewer cards each game.
# Lastly the function also deals the first set of cards automatically like the first game.
# Note my solution doesn't follow best practices as I am using global variables to give the application this
# functionality thus creating side effects, ideally I should find an alternative method if possible.
# I placed the new game button in the same frame as the dealer and player buttons as well.

# Lecture 286 notes: Importing techniques
# So after working through the last set of videos we've now got a working blackjack game that we can actually run
# whenever we want to, either from the IDE or ultimately from the command line as well. The one thing we can't do is
# include the blackjack module in another program. Well actually we can but the results are probably not going to be
# what we wanted. So to see this what we going to do is create anther py file and call it import_test.py.
# Go to import_test.py to continue the lecture.
#
# Let's go to our shuffle method, just after the last of the methods, and type in print(__name__). So we've now put that
# in the code, so if we then run this, so we actually running the blackjack game again just to confirm. So if we
# actually run it we should see the output on the screen, and there's __main__, and obviously the game itself is
# actually running as well so that's good. Go back to import_test.py.
#
# we are going to replace the print statement we just added and we are going to change it and instead of printing we
# gonna put "if __name__ == '__main__':" (note the exact number of underscores is also obviously important here, so make
# sure you get those right). So basically we are doing a test here to see that we're actually in the right scope,
# so we are doing that test to see whether name is equal to main, and if that's the case, note that we indent all the
# code that follows. So that code is now only executed if that's the case, if __name__ is equal to __main__. Ok so
# that's that. Go back to import_test.py.
#
# However we then go back to blackjack.py itself and actually run it from within there, we find that the game is running
# and that's because we specifically said we want to run the game as opposed to importing it. So again the big
# distinction there is we're running this file directly, we are actually telling the IDE IntelliJ IDEA to execute the
# code and it's being executed just fine and so therefore the code we added ends up being true because we are running in
# __main__. Go back to import_test.py.
#
# The initialisation, we still want to actually execute that at the time it gets imported, but we only want the code
# that actually runs the game to be executed when we specifically called the play function. So how do we do that?
# Well we create a new function and we're gonna call it play. Let's do that. Now if we run this you should find it
# works. So it's working and that's good. So now let's go back and check to see whether import_test.py is working.
#
# One last thing we can add to this before we actually finish of the blackjack game and it relates to the code we
# duplicated to create the play function. So it's probably not a good idea, we need to execute this code for dealing a
# new card for the player, one for the dealer and another for the player each time we are invoking a new game, and
# likewise when we are gonna play for the first time we need to do that as well, and we don't want to actually put all
# this code and only execute the new game method the first time when we play because we basically deleting the frame and
# recreating it again. So what we going to do is just create one final method and put this code that is going to be
# executed in 2 places in there so that we're not duplicating our code, because it's nearly always a idea to fix the
# issue if you duplicating code anywhere. So let's do that. So what's happening now is that we haven't got any code
# duplicated and if by any chance we decided to change the code to that initial_deal, we could still modify it in one
# place namely the initial_deal and it's still gonna work. So let's check that it does work, and it's still working.

# Lecture 287 notes: Underscores in Python
# So lets refactor deal_card().Go back to import_test.py.
#
# Just below the play method what we gonna do is change __name__ to __main__. So obviously this is something you
# shouldn't be doing, we just making the point that these two underscores at the start and end of the variable names is
# Python's way of saying you should never change this, but we are just doing this to see what happens. Go back to
# import_test.py.
#
# So before moving on we just gonna comment out that offending line of code where we change the __name__ variable,
# because that shouldn't be there. So we just about done here and what we going to leave you with now is one more use of
# the underscore that we'll quickly go through, so a variable that's just named underscore with nothing else indicates
# a throwaway value. So underscore by itself is a valid variable name and rather than thinking of a name for something
# that's not gonna be used, the convention is to call it either underscore or underscore underscore. So examples of
# things you might have to access but are not going to use include tuples, we want to use some of the values of a tuple,
# but not all of them. Go back to import_test.py.

import random

try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # For each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards_png\\cards\\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        # Next the face cards
        for card in face_cards:
            name = 'cards_png\\cards\\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def _deal_card(frame):
    # Pop the next card off the top of the deck
    # next_card = deck.pop()
    next_card = deck.pop(0)
    # And add it to the back of the pack (note append defaults to adding to the end)
    deck.append(next_card)
    # Add the image to a ;abel and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # Note that next card is a tuple where the 1st item in the tuple is the value and the second is the image object
    # Now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all the cards in the list.
    # Only one ace can have the value 11, and this will reduce to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    # deal_card(dealer_card_frame)

    # dealer_hand.append(deal_card(dealer_card_frame))
    # dealer_score = score_hand(dealer_hand)
    # dealer_score_label.set(dealer_score)

    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
        # Note we have already done this check in the deal_player function
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


# def deal_player():
#     deal_card(player_card_frame)

# def deal_player():
#     global player_score
#     global player_ace
#     # player_score = 0
#     card_value = deal_card(player_card_frame)[0]
#     # We are actually obtaining the result from the deal_card function and then we need to do a bit of checking.
#     if card_value == 1 and not player_ace:
#         player_ace = True
#         card_value = 11
#         # So by default an ace has got the value of 1 and what we're saying here is if an ace was drawn from the card
#         # from the deck and the player hasn't already got an ace in their hand then we are going to assign 11 to this
#         # particular card.
#         # Note something needs to set player_ace to True after the ace has been added because the program as presently
#         # constructed will continuously add card value=11 if next card is an ace because player_ace is set to False in
#         # the main part of the program
#     player_score += card_value
#     # If we would bust, check if there is an ace and subtract 10
#     if player_score > 21 and player_ace:
#         # So if we are bust and the player already has an ace in their hand
#         player_score -= 10
#         player_ace = False
#     player_score_label.set(player_score)
#     if player_score > 21:
#         result_text.set("Dealer wins!")
#     print(locals())


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")


# My solution function:
# def new_game():
#     global dealer_card_frame
#     global player_card_frame
#     global deck
#
#     dealer_card_frame.destroy()
#     dealer_card_frame = tkinter.Frame(card_frame, background="green")
#     dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
#
#     player_card_frame.destroy()
#     player_card_frame = tkinter.Frame(card_frame, background="green")
#     player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
#
#     dealer_hand.clear()
#     player_hand.clear()
#
#     dealer_score_label.set(0)
#     player_score_label.set(0)
#
#     del deck
#     deck = list(cards)
#     random.shuffle(deck)
#
#     result_text.set("")
#
#     deal_player()
#     dealer_hand.append(deal_card(dealer_card_frame))
#     dealer_score_label.set(score_hand(dealer_hand))
#     deal_player()


# Python master class solution function:
def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # Embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    # embedded frame to hold the card image
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")

    # Create the list to store dealer's and player's hands
    random.shuffle(deck)
    dealer_hand = []
    player_hand = []

    # deal_player()
    # dealer_hand.append(deal_card(dealer_card_frame))
    # dealer_score_label.set(score_hand(dealer_hand))
    # deal_player()
    # Ok so obviously we've cleared the player hand and the dealer hand now and we deal a new card, and we will also
    # deal a new card for the dealer and another card for the player again as we've done previously. And obviously
    # because looking at the code we also need to declare that we want to use the global objects rather than creating
    # local variables and that's why we used the global keyword. Now in Python 3 the 2 lists holding the hands could be
    # cleared using their .clear method and that just removes all the items for them, but it doesn't create new lists
    # so we could access the global variables without declaring them in the function, however we've also written
    # blackjack to work with Python 2 so instead of that approach (the approach I used in my solution) what we've done
    # is we assigned empty lists to the 2 variables and that means they do have to be declared as global in the function
    # for that to actually work.
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    # deal_player()
    # dealer_hand.append(deal_card(dealer_card_frame))
    # dealer_score_label.set(score_hand(dealer_hand))
    # deal_player()
    initial_deal()

    mainWindow.mainloop()


# __name__ = "__main__"
# print(__name__)
# if __name__ == "__main__":

mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False
# Note player_ace is a boolean variable that that  tells us whether or not the player has an ace in his hand.
# player_ace is initially set to zero because prior to the games start the player has no ace in his/her hand.

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# dealer_button = tkinter.Button(button_frame, text="Dealer")
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card(dealer_card_frame))
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card)
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card)
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

# player_button = tkinter.Button(button_frame, text="Player")
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# My solution New game button solution:
# new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
# new_game_button.grid(row=1, column=0, columnspan=2, sticky="ew")

# Python masterclass New game button solution:
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

# Shuffle button
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)
# Load cards
cards = []
load_images(cards)
print(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
# deck = list(cards) + list(cards) + list(cards)
# We used the list function to create a new list from the cards and if we did something different, for example if we
# had the code deck = cards, deck would then be exactly the same list as cards. So that's not necessarily a problem
# when just shuffling but as the cards are dealt they will be removed from the list which could cause problems.
# So every game will then have fewer and fewer cards until there are none left to create a new deck from. So we
# definitely don't want to do it that way, we want to create a new and separate list which is the way we've done
# here.
# random.shuffle(deck)
# It's gonna sort of shuffle them in a random order which is obviously what we want.
shuffle()
# Instead of using random.shuffle(deck), we simply using our created shuffle function which accomplishes the same
# thing.

# Create the list to store dealer's and player's hands
dealer_hand = []
player_hand = []

# deal_player()
# So the player gets the first card automatically
# dealer_hand.append(deal_card(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# Recall that if we use deal_dealer function it will accomplish the above two lines of code but it will also declare
# a winner prematurely which isn't what we want.
# deal_player()
# So we want to deal player again. Basically the player is gonna get two cards which is how black jack works,
# and the dealer is going to have one.

# new_game()
if __name__ == "__main__":
    play()

# mainWindow.mainloop()
