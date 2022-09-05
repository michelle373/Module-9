# Michelle Patlan
# 8/31/2022
# Using a while loop, ask the user to enter a number. Append each entered number
# to a list. Continue asking for a number until the sum of the list of numbers is greater than 100.

L = []
y = 100

while(sum(L) <= y):
    x = int(input('Enter a number: '))
    L.append(x)