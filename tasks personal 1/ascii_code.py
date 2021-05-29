"""
We wish to create a program that determines the ASCII code for a character.

The program should start by displaying the message "Program Started!".
The program should start by displaying the message "Please enter a standard character:".
The program should then read in the user's response which should be a single character.
The program should then check that a single letter has been entered using the built-in function len(). 
If the length is 1 then the program should
    determine the ASCII code of the character using the built-in function ord().
    display the message "The ASCII code for {letter} is {value}." where {letter} is the letter entered by the user and {value} is the ASCII code as a number.
Otherwise, if the length is not 1 then the program should
    display a suitable error message
Finally, the program should display the message "Program Ended!"."""



print("\nProgram started!")
print("\nplease enter a standard character\n")
letter = input()
if len(letter)==1:
  print(f"\nthe Ascii code for {letter} is {ord(letter)}.")
else:
  print("This program does not accept more than 1 character dumbass!")

print("\n\n the program has ended")