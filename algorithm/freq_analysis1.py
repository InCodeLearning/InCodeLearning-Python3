# coding=utf-8
#  Crypto Analysis: Frequency Analysis
# To analyze encrypted messages, to find out information about the possible
# algorithm or even language of the clear text message, one could perform
# frequency analysis. This process could be described as simply counting
# the number of times a certain symbol occurs in the given text.
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only
# contains the lowercase letters a-z.
# As output you should return a list of the normalized frequency
# for each of the letters a-z.
# The normalized frequency is simply the number of occurrences, i,
# divided by the total number of characters in the message, n.

# A wrong way of doing it


def freq_analysis(message):
    total_number = len(message)
    ele = 0
    dis = []
    while ele < total_number:
        count = 0
        for i in message:
            if i == message[ele]:
                count = count + 1
        ele += 1
        frequency = float(float(count) / float(total_number))
        dis.append(frequency)
    left = 26 - total_number
    while left > 0:
        dis.append(left * 0.0)
        left -= 1
    return dis


# Tests

print(freq_analysis("abcd"))
# >>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]
print("""""")
print(freq_analysis("adca"))
# >>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]
print("""""")
print(freq_analysis('bewarethebunnies'))

# >>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]

print("""
 Seperate case line
 """)


# A more efficiency way to do it.
def freq_analysis2(message):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    freq_list = [0.0] * 26
    for i in message:
        freq_list[abc.find(i)] += 1.0 / len(message)
    return freq_list


print(freq_analysis2("abcd"))
# >>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]
print("""""")
print(freq_analysis2("adca"))
# >>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]
print("""""")
print(freq_analysis2('bewarethebunnies'))


#
