# Michelle Patlan
# 8/31/2022
# Create a while loop that initializes a counter at 20 and will run until the counter
# reaches 70. If the value of the counter is divisible by 10, append the value to the list called tens.
# If the converted character of the counter number is one of vowels, append the vowel to the list
# called vowels. Confirm the two list results using a print statement.

counter = 20
tens = []
vowel = []

#You need a list of vowels for the converted character of the counter number to be compared with
vowel_List = "aeiouAEIOU"

while counter <= 70:
    if counter % 10 == 0:
        tens.append(counter)
    
    if chr(counter) in vowel_List: 
        vowel.append(chr(counter))
   
    counter = counter + 1

print(tens)
print(vowel)

'''
for i in tens:
    tens[0] = str('twenty')
    tens[1] = str('thirty')
    tens[2] = str('forty')
    tens[3] = str('fifty')
    tens[4] = str('sixty')
    tens[5] = str('seventy')

for chr in tens:
    if chr == 'a' or chr == 'e' or chr == 'i' or chr == 'o' or chr == 'u':
        print(tens)
'''
