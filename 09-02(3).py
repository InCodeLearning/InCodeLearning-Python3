
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# http://www.willprice.org/2012/11/19/CS101-Homework-4-splitting-strings.html
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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

                word_list.append(char)

                at_split = False
            else:

                word_list[-1] = word_list[-1] + char
    return word_list


out = split_string("This is a test-of the,string separation-code!", " ,!-")
print(out)
# >>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print(out)
# >>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,", ",")
print(out)
# >>>['First Name', 'Last Name', 'Street Address', 'City', 'State']
