def menu():

  print("Please choose an option from the menu:\n\nLoad Data\n\nProcess Data\n"
  "\nVisualise Data\n\nSave Data\n\nExit\n")
  option = input()
  x = int(input())

  if option == "Load Data":
    x = 1
  elif option == "Process Data":
    x = 2
  elif option == "Visualise Data":
    x = 3
  elif option == "Save Data":
    x = 4
  elif option == "Exit":
    x = 5
  else:
    print("\nThe Option is not Available")

  return x

menu()