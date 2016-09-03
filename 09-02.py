# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:
#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

def check_sudoku(square):
    size = len(square)  # Check_the_#_of_sub_list_in_the list
    row = 0
    while row < size:
        num = 1
        while num <= size:
            if num not in square[row]:
                return False  # Check_this since at lease 1 will be in the single sublist
            num = num + 1
        row = row + 1
    # get column values
    col = 0
    mycol = []  # Note when you check a list the  procedure need to be carefully managed
    while col < size:  # Create an empty list and enumerate all elements into this list then creaat a standard to check it
        row = 0
        while row < size:
            mycol.append(square[row][col])
            row = row + 1
        num = 1
        while num <= size:
            if num not in mycol:
                return False
            num = num + 1
        mycol = []
        col = col + 1
    return True


print (check_sudoku(incorrect))
# >>> False

print (check_sudoku(correct))
# >>> True

print (check_sudoku(incorrect2))
# >>> False

print (check_sudoku(incorrect3))
# >>> False

print (check_sudoku(incorrect4))
# >>> False
print (check_sudoku(incorrect5))

#############################################


# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(num):
    hour = int(num / 3600)
    mins = int((num - hour * 3600) / 60)
    sec = round(num % 3600 % 60, 2)
    result = ""
    if hour == 1:
        result += "1 hour, "
    else:
        result += "%s hours, " % hour
    if mins == 1:
        result += "1 minute, "
    else:
        result += "%s minutes, " % mins
    if sec == 1:
        result += "1 second"
    else:
        result += "%s seconds" % sec
    return result


print (convert_seconds(3661))
# >>> 1 hour, 1 minute, 1 second

print
(convert_seconds(7325))
# >>> 2 hours, 2 minutes, 5 seconds

print(convert_seconds(7261.7))
# >>> 2 hours, 1 minute, 1.7 seconds


# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#参考这里的链接
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# http://www.willprice.org/2012/11/19/CS101-Homework-4-splitting-strings.html
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Unit4 知识难点
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def split_string1(source, splitlist):
    split_words = []
    word = ''
    for character in source:
        if character in splitlist:
            if word != '':
                split_words.append(word)
                word = ''
        else:
            word = word + character

if word != '':
    split_words.append(word)
    
    return split_words


def split_string(source, splitlist):
    word_list = ['']
    
    at_split = False
    for char in source:
        if char in splitlist:
            at_split = True
        else:
            if at_split:
                # We've now reached the start of the word, time to make a new element in the list
                word_list.append(char)  # This creates a new element in the array with the value of 'char'
                # Reset at_split so no more elements are created until we reach a new word
                at_split = False
            else:
                # Char is not in splitlist, and we're not at the start of a word, so simply concatenate
                # char with the last entry in word_list
                word_list[-1] = word_list[-1] + char

# Once we've filled word list, we'll want to return the list containing all the words
return word_list


out = split_string("This is a test-of the,string separation-code!", " ,!-")
print (out)
# >>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)
# >>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code", ",")
print (out)
# >>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']