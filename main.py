print("\033[35m", "\n            Replit Login System", "\033[0m")
print("\033[31m", "        ----------------------------\n", "\033[0m")


def login_system():

  while True:
    user_name = input("Enter Username -----> ")
    password = input("\nEnter Password -----> ")

    if user_name == "Nikhil" and password == "123@Nik":
      print("\033[32m", "\n\nWelcome back Nikhil to Replit!!!🥳", "\033[0m")
      print("\033[32m", "\nlet's get you started.....\n", "\033[0m")
      break

    print(
        "\033[31m",
        "\nWhoops! I don't recognize that username or password 😕😕. Try again!\n\n\n",
        "\033[0m")


login_system()
