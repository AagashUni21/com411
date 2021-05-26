picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for y in picture:
  for x in y:
    if x==0:
      print(" ",end="")
    else:
      print("*", end="")
  print('')
#[print("*") for "1" in picture]
#[print(" ") for "0" in picture]
#check :Something on the line .... where it is 0 the program needs to print an empty space, where it is 1 the program needs to print a *"""