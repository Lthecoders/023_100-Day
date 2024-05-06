

print("\033[35m","              Replit Login System", "\033[0m")
print("\033[31m","           ---------------------------\n", "\033[0m")


def login_system():

  user_name = input("\nEnter Username -----> ")
  password = input("\nEnter Password -----> ")
  if user_name == "Nikhil" and password == "123@Nik":
    print("\033[32m", "\n\nWelcome back Nikhil to Replit!!🥳", "\033[0m")
    print("\033[32m", "\nle's get started to work on code.....", "\033[0m")
  # elif user_name != "Nikhil" and password== "123@Nik":
  #   print("Whoops! I don't recognize that username or password. Try again!")
  else:
    print("\033[31m",
          "\nWhoops! I don't recognize that username or password. Try again!",
          "\033[0m")

login_system()