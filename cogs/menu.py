def menu ():
  print("Welcome to Diskrypt v0.01!\n")
  print("Developed by Nate Holcomb in Python 3.\n")

  #================================================

  while True:
    try:
      print ("Menu \n")
      print ("1 - Encrypt Mode\n")
      print ("2 - Decrypt Mode\n")
      print ("3 - Quit\n")
      userNum = int(input("Enter choice: "))
    except ValueError:
      print ("Invalid entry. Please try again.\n")

  return userNum