#!/bin/python3
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0]
number = int(position[1])
print(letter,number)
if letter == "A":
  letter_num = 0
elif letter == "B":
  letter_num = 1
else:
  letter_num = 2

print(letter_num)
print(letter)
if number == 1:
  line1[letter_num] = "X"
elif number == 2:
  line2[letter_num] = "X"
else:
  line3[letter_num] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")