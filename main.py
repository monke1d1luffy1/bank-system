user_credentials = {

}

user_balance = {

}

help_text = {
    "ca": "Create an account",
    "lta": "Login to your account",
    "looa": "Log out of Account",
    "da": "Delete your account",
    "dtb": "Deposit to your Balance",
    "wfb": "Withdraw from your balance",
    "cb": "Check your balance",
    "sht": "Show help text",
    "t": "Exit the program"
}

currentUser = ""

terminate = False

def createAccount():
    print("==> Create an account <==")
    username = str(input("Choose a username: "))
    password = str(input("Choose a password: "))
    if username not in user_credentials and username not in user_balance:
        user_credentials[username] = password
        user_balance[username] = 0
        print(f"Success: Created account '{username}'")
    else:
        print("Error: Username is not available")

def loginToAccount():
    global currentUser
    if currentUser == "":
        print("==> Login to your account <==")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in user_credentials and username in user_balance and user_credentials[username] == password:
            currentUser = username
            print(f"Success: Logged in as '{username}'")
        else:
            print("Error: Username or password invalid")
    else:
        print("Error: Someone is already logged in")

def logOutOfAccount():
    global currentUser
    if currentUser != "":
        print("==> Logout of your account <==")
        print(f"Logging user '{currentUser}' out...")
        currentUser = ""
        print(f"Success: Logged out of your account")
    else:
        print("Error: No user is currently logged in")

def deleteAccount():
    print("==> Delete your account <==")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_credentials and user_credentials[username] == password and username in user_balance:
        user_credentials.pop(username)
        user_balance.pop(username)
        print(f"Success: Deleted account '{username}'")
    else:
        print("Error: Username or password invalid")

def depositToBalance():
    global currentUser
    if currentUser != "":
        print("==> Add to your balance")
        amountToDeposit = int(input("Input amount to deposit: "))
        if amountToDeposit > 0:
            user_balance[currentUser] = user_balance[currentUser] + amountToDeposit
            print(f"Success: Deposited ${amountToDeposit} to your balance")
        else:
            print("Error: Amount cannot be 0 or negative")
    else:
        print("Error: No user is currenly logged in")

def withdrawFromBalance():
    global currentUser
    if currentUser != "":
        print("==> Withdraw from your balance")
        amountToWithdraw = int(input("Input amount to withdraw: "))
        if amountToWithdraw > 0:
            user_balance[currentUser] = user_balance[currentUser] - amountToWithdraw
            print(f"Success: Withdrawed ${amountToWithdraw} from your balance")
        else:
            print("Error: Amount cannot be 0 or negative")
    else:
        print("Error: No user is currenly logged in")

def checkBalance():
    global currentUser
    if currentUser != "":
        print("==> Checking your balance <==")
        print(f"Your balance is: ${user_balance[currentUser]}")
    else:
        print("Error: No user is currenly logged in")

def showHelpText():
    print(help_text)

print("==> Bank <==")
print("Execute command 'h' for help")

while not terminate:
    command = input(">_")
    if command == "ca":
        createAccount()
    elif command == "lta":
        loginToAccount()
    elif command == "looa":
        logOutOfAccount()
    elif command == "da":
        deleteAccount()
    elif command == "dtb":
        depositToBalance()
    elif command == "wfb":
        withdrawFromBalance()
    elif command == "cb":
        checkBalance()
    elif command == "h":
        showHelpText()
    elif command == "t":
        terminate = True
    else:
        print("Invalid command")