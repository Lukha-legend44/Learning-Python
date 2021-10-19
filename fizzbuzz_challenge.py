# Lecture 172 - 173

# Lecture 172 notes: (Using the code from coding exercise 17)
# For this challenge, replace the loop from the coding exercise with a loop that will play the game
# The computer will start with the value 1
# The player and the computer will then take turns
# The player will type in their response, and the computer will print out its next value, and so on.
# The game ends when the player makes a mistake, or gets to 100
# If the player gets it wrong, he/she loses
# Pseudocode is code that you write in a simplified language -  usually a simple version of your native language
# Think of the biology practical methodologies in high school, mapping out how the code is going to work

# Challenge Pseudocode:
# 1) calculate the computer's "number"
# 2) Print the computer's response
# 3) calculate the player's correct answer
# 4) get input from the player
# 5) compare the correct answer to the player's input
# 6) repeat, until the player makes a mistake, or we reach 100
# 7) Print suitable message: "Congratulations" or "Wrong"

# Refining Pseudo code:
# 1) call fizz_buzz() and print the result
# (We'll need a variable to pass to fizz_buzz)
# 2) calculate the player's correct answer
# (Increment the variable that was previously passed to fizz_buzz, and use it again here)
# 3) get input from the player
# 4) check the player's input against the correct answer
# 5)If it's not correct, break out of the loop. Print "Wrong" message
# 6) repeat until we reach 100
# 7) print suitable congratulations message


def fizz_buzz(start: int) -> str:
    """
    The function checks whether the integer after
    the starting integer is divisible by 3, 5 or both.

    :param start: The starting integer.
    :return: fizz is returned if the integer is divisible by 3,
        buzz is returned if the integer is divisible by 5,
        and fizz buzz is returned if the integer is divisible by
        both 3 and 5. If none of the conditions are met, the
        integer is returned as a string literal
    """
    if start % 3 == 0 and start % 5 == 0:
        return "fizz buzz"
    elif start % 3 == 0:
        return "fizz"
    elif start % 5 == 0:
        return "buzz"
    else:
        return str(start)


# My solution: (worked perfectly)

game_round = 1
user_correct_answer = 2
computer_choice = 1
while game_round < 51:
    # fizz_buzz(computer_choice)
    print(fizz_buzz(computer_choice))
    computer_choice += 2
    user_choice = input("Your turn mate: ").casefold()
    # user_choice = fizz_buzz(user_correct_answer)      # Run when you want to see what happens if you win the game
    # print(user_choice)
    if user_choice != fizz_buzz(user_correct_answer):
        print("Game over mate, you lose")
        break
    user_correct_answer += 2
    game_round += 1
else:
    print("Congrats you win")

# Python masterclass solution:

# input("Play Fizz Buzz.  Press ENTER to start")
# print()
#
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_answer = fizz_buzz(next_number)
#     player_answer = input("Your go: ")
#     # player_answer = correct_answer      # Run when you want to see what happens if you win the game
#     if player_answer != correct_answer:
#         print("You lose, the correct answer was {}".format(correct_answer))
#         break
# else:
#     print("Well done, you reached {}".format(next_number))
