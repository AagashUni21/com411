"""We wish to create a program to determine the ASCII character represented by an ASCII code.
The program should start by displaying the message "Program Started!".
The program should start by displaying the message "Please enter an ASCII code:".
The program should then read in the user's response which should be a positive integer.  You can can use the built-in functions abs() and int() to convert the input appropriately.
The program should then check that the number is in the range 32 - 126 (inclusive) i.e. the printable characters.  You should use the keyword in and the built-in function range to help you with this.
If the number in within the range then the program should
    determine the ASCII character from the number using the built-in function chr().
    display the message "The character represented by the ASCII code {code} is {character}." where {code} is the number entered by the user and {character} is the ASCII character represented by the number.
Otherwise, if the number is within the range then the program should
    display a suitable error message
Finally, the program should display the message "Program Ended!"."""

print("\nprogram started!")
print("\nplease enter and ASCII code!\n")
code= input()
code= abs(int(code))
if code in range(32, 127):
  print(f"the character represented by the ASCII code {code} is {chr(code)}")
else:
  print("no possible scenario")
print("\n\n program ended")




