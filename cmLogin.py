def askUser():
    username = raw_input("Enter your Username: ")
    password = raw_input("Enter your Username: ")
    checkpass(username, password)
    return

def checkpass(user, pwd):
    if user == "user"and pwd == "password":
        login(user)
    else:
        print("Your username and/or password is incorrect")
        askuser()

def login(user):
    print("Welcome " + user)
    print("You have successfully login in!")
    askcom()

def askcom():
    command = raw_input("Enter your command: ")
    if command = "quit" or "Quit":
        username = ""
        password = ""
        print("Logged Off")
        askUser()
    else:
        print("Unknown Command")
        askcom()

askUser()
