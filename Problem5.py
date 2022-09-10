# Michelle Patlan
# 8/31/2022
# Write a program that reads a word and prints the word in reverse. For example, if
# the user provides the input “Harry”, the program prints “yrraH”


word = input('enter a word: ')

reverse_word: str = ""

for char in word:
    reverse_word = char + reverse_word

print(reverse_word)

#You can make the word in reverse using slice operator
Reversed_word = word[::-1]
