#This program asks the user to input a string and for the characters in it they would like to make disappear

#Adding features to the messages
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#Getting the initial sentence from the user
magic_string = input("What sentence you would like to try my magical powers on? ")
# wanna_trick = input("And would you like to see some of its characters vanished? (Y/N)")

#Getting the characters to disappear from the user
disappearing_chars = []
i = 0
print(f"\nPlease insert the characters below or type {BOLD}{UNDERLINE}{RED}READY{WHITE} for the magic to begin!")
while True:
     wanna_trick = input("Character {}: ".format(i + 1))
     if wanna_trick.lower() != 'ready':
          disappearing_chars.append(wanna_trick)
          i += 1
     else:
          break

#Replacing characters in the original sentence
new_string = magic_string
for i in range(i):
     new_string = new_string.replace(disappearing_chars[i], '')

#Printing the new sentence
print(f"\nThe magic sentence is: {BOLD}{UNDERLINE}{new_string}")
