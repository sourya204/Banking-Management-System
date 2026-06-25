def create_account():
    name=input("Enter your name : ")
    while True:
        try:
            deposit=float(input("Enter your deposit (minimum = Rs. 500) : "))
            if deposit<500 :
                print("Minimum deposit is Rs. 500")
            else :
                break
        except ValueError:
            print("Please enter a number.")

    if(len(accounts)==0):
        acc_no="100001" #we could have used a counter variable=1001 instead of this if else but Counter resets to 1001 every time you restart the program
    else :
        last=max(accounts.keys())
        acc_no=str(int(last)+1)

    while True :
        pin=input("Set a 4 digit PIN : ")
        if pin.isdigit() and len(pin)==4 :
            break
        else :
            print("PIN must be exactly 4 digits.")
            
    accounts[acc_no]={"name":name , "balance": deposit , "pin": pin}
    save_accounts()
    print("Account created! Your account number is ", acc_no)


def deposit():
    acc_no=input("Enter account number : ")
    if acc_no not in accounts:
        print("Account not found!")
        return

    if authenticate(acc_no)==False :
        return
    while True:
        try:
            amt=float(input("Enter deposit amount : "))
            if amt<=0 :
                print("Please enter positive amount.")
            else :
                break
        except ValueError:
            print("Please enter a valid number.")

    accounts[acc_no]["balance"]+=amt
    save_accounts()
    log_transaction(acc_no, "DEPOSIT", amt)
    print("Deposit successful")
    print("New balance : ", accounts[acc_no]["balance"])


def withdraw():
    acc_no = input("Enter account number : ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    if authenticate(acc_no)==False :
        return
    
    while True:
        try:
            amt = float(input("Enter withdrawal amount : "))
            if amt <= 0:
                print("Amount must be positive.")
            elif amt > accounts[acc_no]["balance"]:
                print("Insufficient balance!")
                print("Available balance: ", accounts[acc_no]["balance"])
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    accounts[acc_no]["balance"] = accounts[acc_no]["balance"] - amt
    save_accounts()
    log_transaction(acc_no, "WITHDRAWAL", amt)

    print("Withdrawal successful!")
    print("Remaining balance : ", accounts[acc_no]["balance"])


def check_balance():
    acc_no = input("Enter account number : ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    if authenticate(acc_no)==False :
        return

    print("Account Holder : ", accounts[acc_no]["name"])
    print("Balance : ", accounts[acc_no]["balance"])

def save_accounts():
    file=open("accounts.txt","w")
    for acc_no in accounts:
        line=acc_no+"|"+accounts[acc_no]["name"]+"|"+str(accounts[acc_no]["balance"])+"|"+accounts[acc_no]["pin"]
        file.write(line+'\n')
    file.close()

def load_accounts():
    try:
        file=open("accounts.txt","r")
        for acc in file:
            acc=acc.strip()
            parts=acc.split("|")
            acc_no=parts[0]
            name=parts[1]
            balance=float(parts[2])
            pin=parts[3]
            accounts[acc_no]={"name":name , "balance":balance , "pin":pin}
        file.close()
    except FileNotFoundError:
        pass

def authenticate(acc_no):
    attempts = 3

    while attempts > 0:
        pin = input("Enter PIN: ")

        if pin == accounts[acc_no]["pin"]:
            return True
        else:
            attempts = attempts - 1
            print("Wrong PIN.", attempts, "attempt(s) left.")

    print("Too many wrong attempts!")
    return False

def transfer():
    from_acc=input("Enter account number : ")
    if from_acc not in accounts :
        print("Account not found!")
        return

    if authenticate(from_acc)==False :
        return
    
    to_acc = input("Recipient account number: ")
    if to_acc not in accounts:
        print("Recipient account not found!")
        return

    if from_acc == to_acc:
        print("Cannot transfer to the same account!")
        return

    while True:
        try:
            amount = float(input("Enter transfer amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            elif amount > accounts[from_acc]["balance"]:
                print("Insufficient balance!")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    accounts[from_acc]["balance"] = accounts[from_acc]["balance"] - amount
    accounts[to_acc]["balance"]   = accounts[to_acc]["balance"] + amount
    save_accounts()
    log_transaction(from_acc, "TRANSFER OUT to " + to_acc, amount)
    log_transaction(to_acc, "TRANSFER IN from " + from_acc, amount)
    print("Transfer successful!")
    print("Your new balance: ", accounts[from_acc]["balance"])

def log_transaction(acc_no,action,amount):
    file=open("transactions.txt","a")
    file.write(acc_no+"|"+action+"|"+str(amount)+"\n")
    file.close()
    
def transaction_history():
    acc_no=input("Enter account number : ")
    if acc_no not in accounts :
        print("Account not found!")
        return

    if authenticate(acc_no)==False :
        return
    try:
        file=open("transactions.txt","r")
        history=[]
        for line in file :
            if line.startswith(acc_no+"|"):
                history.append(line.strip())
        file.close()
        if len(history)==0:
               print("No transactions found.")
        else:
            print("\n--- TRANSACTION HISTORY ---")
            for record in history:
                parts = record.split("|")
                print(parts[1], "→ Rs.", parts[2])

    except FileNotFoundError:
        print("No transactions found.")
    
accounts={}
load_accounts()
while True:
    print("\n\tBank Menu\t")
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Balance")
    print("5.Transfer Money")
    print("6.Transaction History")
    print("7.Exit")
    choice = input("Choose (1-7): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        transfer()
    elif choice == "6":
        transaction_history()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!! Try again.")




    
