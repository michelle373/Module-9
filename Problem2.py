# Michelle Patlan
# 8/31/2022
# Using a while loop, create a list called L that contains the numbers 10 to 20. On each
# iteration, the loop should append the current value of a counter variable to the list and then
# increase the counter by 1. The while loop should stop once the counter variable is greater than
# 20.

L = []
i = 10
while i <= 20:
    L.append(i)
    i = i + 1
print(L)
