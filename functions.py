# Please note the backtick doesn't restructure text for me in my docstring for some reason
# Lecture 138-146
# Lecture 149
# Lecture 157 - 161

# Lecture 138 notes: Introduction
# A function that's bound to an instance of a class is called a method
# You define them in the same way as a function, and you'll learn more about them in the OOP section of this course
# You use methods in the same way as you use functions, but specify the object that they will act on, before the dot

# Lecture 161 notes:
# Talking about function annotation and type hints ( They aren't the same thing but terms commonly used interchangeably)
# Function annotations are basically a special case of type hints, applied to function parameters and return values
# They make it clearer what kinds of values your functions can accept, and what they return
# Adding annotations to the functions in this file
# Arrow indicates return type, and colon after parameter indicates parameter type
# This is why we didn't mention the type of the arguments and return values in Docstrings
# If you're not going to use function annotations, then your Docstring should mention the types
# The multiply function can be a little bit tricky:
# The parameters x & y, can either be ints or floats, when you come to annotate values like this, use float,
# as you can se an int whenever a float is needed
# Technically, we can pass any sequence type, as well as a number, for that second parameter,
# and there are ways to specify an annotation like that, but it's far more detail than I want to go into at the moment

# Not all functions return a useful value.
# Some functions, like 'print', and the '.sort' method of lists, perform and acton
# 'print' prints something out. When you use '.sort' it sorts the list. These functions don't return anything useful
# Other functions calculate a value, and return it for your main code to use.
# A function that's bound to an instance of a class is called a method.
# You define them in the same way as a function
# 'print' is a function, but '.sort' in my_list.sort() is a method
# You use methods in the same way as you use functions, but specify the object that they will act on, before the dot

# A python function definition starts with the keyword 'def'
# multiply is the name of our function, function names follow the same rules as variable names
# They're written in lowercase and mustn't start with a digit
# After the function name we have opening and closing parenthesis, and we end with a colon
# We can also define parameters inside the parentheses
# Our function starts a new block of code
# Inside the function, we write the code that we want to be executed, when the function is called
# Note the convention is to have two blank lines after a function,
# make sure to leave two blank lines before and after your functions

# def multiply():     # Indented block of code is part of the function
#     result = 10.5 * 4   # This just binds the variable result to the outcome of the calculation
#     # Our multiply function multiplies 10.5 by 4.
#     # So we can find out the value of our calculation, we tell the function to return the result,
#     # hence the return statement
#     return result


# answer = multiply()     # Calling the multiply function and binding its value to the variable answer
# print(answer)

# We are now going to go into more detail and see what happens when you call a function:
# Execution in the above code will jump to line 22 when we call the multiply function
# We will now be using the step into my code button in the debugger, to see what it does
# The step over button in the debugger executes a line, without stepping into any functions on that line
# When you press the step into my code button, the program execution jumps to line 22,
# and we have entered the code in our multiply function
# When you want to check the code in your functions, remember to use he step into my code button!
# Once you in the code of the function,
# using the step over function will execute the code in the function without stepping through it
# ( the step into button in this circumstance does the same thing as the step over button,
# and you won't see the difference until you start splitting your code into different modules)
# Line 22 is about to do a calculation and bind it to the variable result
# Introduction to the scope of variables, the variable result only exists inside the multiply function we created,
# you will see it vanish in the debugger when we leave the function
# All scope means, is where a variable exists
# In line 29 we bind the variable answer to the value returned by our multiply function

# Lecture 157-158 challenge:
# Create Docstrings for the three functions that we wrote, in the functions.py module

def multiply(x: float, y: float) -> float:     # Adding two parameters to our function
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence. If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    # Parameters are like placeholders for the real values that you'll pass to your function
    # They're just variables, but they're given a value when you call the function
    # May also be referred to as formal parameters
    result = x * y
    # Whatever values we provide for those parameters, will be used when we call the function
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]    # using slicing to reverse the string
    # return backwards == string  # testing to see if the reversed string is identical to the original string
    # (will return True or False)
    return string[::-1].casefold() == string.casefold()   # more concise way of writing above code


def palindrome_sentence(sentence: str) -> bool:    # Lecture 144 mini-challenge
    """
    Check if a sentence is a palindrome.

    The function ignores whitespaces, capitalization and
    punctuation in th sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for character in sentence:
        if character.isalnum():     # isalpha is a string method that returns true if character an alphabet letter
            # .isalnum is a string method that returns true if the character is a number or alphabet letter
            string += character
        # print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)    # Your functions can call other functions that you have written
    # above we have called the is_palindrome() function which we created earlier


# Lecture 159 notes:
# We will begin learning more about functions, specifically function annotations and type hints
# Before we do that we will be writing a few more functions, which will give us some functions to add type hints to
# The first function we will write is one to calculate Fibonacci numbers
# The Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1

# Lecture 160 notes:


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    # If we don't bind the variable result to None prior to the for loop we get the following warning:
    # Local variable 'result' might be referenced before assignment
    # In this case, the variable result won't be bound to a value, if the calling code passes a negative number
    # Our Docstring does however say that n should be positive, but we should still handle negative value in some way
    # If we essential don't initialize result, in the event that n is negative (despite the Docstring),
    # The result variable wil be referenced before it is assigned (which would cause an error or bug of some kind),
    # as the code would terminate immediately when it reaches the for loop as range is a negative integer
    # Negative integer in range results in the code immediately terminating from what I've observed
    # Note that reStructuredText doesn't allow partial highlighting of a word,
    # formatting characters such as the backtick can't be followed by an alphanumeric character
    # Note that a function can include more than 1 return statement as we have shown in this function

    for f in range(n - 1):  # Recall that Fibonacci sequence starts at 0
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

# word = input("Please enter a sentence to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# answer = multiply(10.5, 4)
# # The numbers in parenthesis in line 57 are arguments,
# # arguments are the values that will be used by formal parameters, when we call a function
# # Providing values as arguments is called passing the arguments
# # Note that some function parameters can have default values
# # Parameters are simply variables that only exist inside the function
# # The arguments in line 57 are called positional arguments
# # Positional arguments are assigned to parameters in the order they appear
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# # We can use a created function (like a regular function) anywhere that Python expects an expression
# # A function call is another type of expression
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
#
# # Another one of the debugger functions, upwards pointing arrow 'step out'
# Step out will execute the remainder of the code in the function, and return to the point where the function was called
#
# # A palindrome is a word that is the same when read backwards
# # Creating a function to detect palindromes

# All Python functions return a value. If you don't explicitly return something, then your function will return None.

# answer = multiply(18, 3)
# print(answer)

# Not all functions return something useful
# An example of this is the sort method
# The sort function didn't return anything useful, but it did perform a useful function - it sorted the list
