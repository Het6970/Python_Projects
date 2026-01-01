'''/////------ROYAL BANK ACCOUNT------//////'''
accounts={}
INITIAL_BALANCE = 25000
MIN_BALANCE = 10000
current_user = None
OVERDRAFT_LIMIT = -5000

#Function for Open Account
def open_account():
    global accounts
    username = input("Enter new username : ")
    if username in accounts :
        print("Username is already exists, Try another.")
        return
    password = input("Enter New Password : ")
    accounts[username] = {
        "password" : password,
        "balance":INITIAL_BALANCE,
        "overdraft":False
    }
    print(f"Account created sucessfully for {username} with balance Rs.{INITIAL_BALANCE}")

#Function for Login
def login():
    global current_user
    username = input("Enter Username : ")
    password = input("Enter Password : ")
    if username in accounts and accounts[username]["password"] == password:
        current_user = username
        print(f"Welcome {username} , You're Logged in !")
    else:
        print("Invalid Username or password.")

#Function for deposit
def deposit():
    global accounts,current_user
    if current_user is None:
        print("You must login first.")
        return
    amount = int(input("Enter amount to deposit."))
    if amount > 0:
        accounts[current_user]["balance"] += amount
        print(f"Deposited Rs{amount}. New Balance : Rs.{accounts[current_user]['balance']}")
    else:
        print("Enter a valid amount.")

#Function for Withdrawn
def withdraw():
    global accounts,current_user
    if current_user is None:
        print("You must Login first !")
        return
    amount = int(input("Enter amount to withdraw : "))
    if amount <= 0:
        print("Enter a valid amount.")
        return
        
    bal = accounts[current_user]["balance"]
    od = accounts[current_user]["overdraft"]

    if od:
        if bal - amount >= OVERDRAFT_LIMIT:
            accounts[current_user]["balance"]-=amount
            print(f"Withdrawn Rs.{amount}.New Balance : Rs.{accounts[current_user]['balance']}")
        else:
            print(f"Cannot withdraw.Overdraft limit reached (Rs.{OVERDRAFT_LIMIT})")
    else:
        if bal - amount>=MIN_BALANCE:
            accounts[current_user]["balance"] -= amount
            print(f"Withdrawn Rs.{amount}.New Balance:Rs.{accounts[current_user]['balance']}")
        else:
            print(f"Cannot withdraw. Balance cannot below (Rs.{MIN_BALANCE})")

#Function for check balance
def checkBalance():
    global accounts,current_user
    if current_user is None:
        print("You must login First !")
        return
    print(f"Current Balance : Rs.{accounts[current_user]['balance']}")

#Function for Overdraft
def enable_overdraft():
    global accounts,current_user
    if current_user is None:
        print("You Must Login First.")
        return
    accounts[current_user]["overdraft"]=True
    print(f"Overdraft facility enabled for {current_user}.Limit:{OVERDRAFT_LIMIT}")

#Function for Logout
def logout():
    global current_user
    if current_user is None:
        print("No user is logged in.")
    else:
        print(f"{current_user} logged out.")
        current_user = None

#Main Program Loop
while True:
    print("1.Saving Account")
    print("2.Current Accont")
    print("3.Exit")
    choice = input("Enter choice : ")
    if choice == "1":
            while True:
                print("\n===Opening your Saving Account===")
                print("1. Open Account")
                print("2. Login")
                print("3. Deposit")
                print("4. Withdraw")
                print("5. Check Balance")
                print("6. Enable Overdraft")
                print("7. Logout")
                print("8. Exit")
                choice = input("Enter choice : ")            
                if choice == "1":
                    open_account()
                elif choice == "2":
                    login()
                elif choice == "3":
                    deposit()
                elif choice == "4":
                    withdraw()
                elif choice == "5":
                    checkBalance()
                elif choice == "6":
                    enable_overdraft()
                elif choice == "7":
                    logout()
                elif choice == "8":
                    print("Thank you for using Royal Bank,GoodBye !")
                    break
                else:
                    print("Invalid Choice , try again.")

    elif choice == "2":
            while True:
                print("\n===Opening your Current Account===")
                print("1. Open Account")
                print("2. Login")
                print("3. Deposit")
                print("4. Withdraw")
                print("5. Check Balance")
                print("6. Enable Overdraft")
                print("7. Logout")
                print("8. Exit")
                choice = input("Enter choice : ") 
                if choice == "1":
                    open_account()
                elif choice == "2":
                    login()
                elif choice == "3":
                    deposit()
                elif choice == "4":
                    withdraw()
                elif choice == "5":
                    checkBalance()
                elif choice == "6":
                    enable_overdraft()
                elif choice == "7":
                    logout()
                elif choice == "8":
                    print("Thank you for using Royal Bank,GoodBye !")
                    break
                else:
                    print("Invalid Choice , try again.")

    elif choice == "3":
         print("Thank you for using our Bank App ,GoodBye !")
         break
    
    else:
         print("Invalid Choice , try again.")
         break