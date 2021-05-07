def run():
  print("Please enter the file path for a data file :\n")
  file_path = input()
    #we will use the enswith method returns True if the string ends with the specified value, otherwise False. 
  x = file_path.endswith(".csv")
  print (x)

  if x == True:
    return file_path
  else:
    print ("Sorry, the program only accepts .csv files")
    return None
run()