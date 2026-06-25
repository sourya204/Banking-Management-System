import tkinter as tk
from tkinter import messagebox, simpledialog
def create_account():
    name=simpledialog.askstring("Input","Enter your name : ")
    if not name: return
    while True:
        try:
            deposit=simpledialog.askfloat("Input","Enter your deposit (minimum = Rs. 500) : ")
            if deposit is None: return
            if deposit<500 :
                messagebox.showerror("Error","Minimum deposit is Rs. 500")
            else :
                break
        except ValueError:
            messagebox.showerror("Error","Please enter a number.")

    if(len(accounts)==0):
        acc_no="100001" #we could have used a counter variable=1001 instead of this if else but Counter resets to 1001 every time you restart the program
    else :
        last=max(accounts.keys())
        acc_no=str(int(last)+1)

    while True :
        pin=simpledialog.askstring("Input","Set a 4 digit PIN : ",show="*")
        if pin is None: return
        if pin.isdigit() and len(pin)==4 :
            break
        else :
            messagebox.showerror("Error","PIN must be exactly 4 digits.")
            
    accounts[acc_no]={"name":name , "balance": deposit , "pin": pin}
    save_accounts()
    messagebox.showinfo("Success","Account created! Your account number is "+ acc_no)


def deposit():
    acc_no=simpledialog.askstring("Input","Enter account number : ")
    if not acc_no: return
    if acc_no not in accounts:
        messagebox.showerror("Error","Account not found!")
        return

    if authenticate(acc_no)==False :
        return
    while True:
        try:
            amt=simpledialog.askfloat("Input","Enter deposit amount : ")
            if amt is None: return
            if amt<=0 :
                messagebox.showerror("Error","Please enter positive amount.")
            else :
                break
        except ValueError:
            messagebox.showerror("Error","Please enter a valid number.")

    accounts[acc_no]["balance"]+=amt
    save_accounts()
    log_transaction(acc_no, "DEPOSIT", amt)
    messagebox.showinfo("Success","Deposit successful\nNew balance : "+str(accounts[acc_no]['balance']))
    

def withdraw():
    acc_no = simpledialog.askstring("Input","Enter account number : ")
    if not acc_no: return

    if acc_no not in accounts:
        messagebox.showerror("Error","Account not found!")
        return

    if authenticate(acc_no)==False :
        return
    
    while True:
        try:
            amt = simpledialog.askfloat("Input","Enter withdrawal amount : ")
            if amt is None: return
            if amt <= 0:
                 messagebox.showerror("Error","Amount must be positive.")
            elif amt > accounts[acc_no]["balance"]:
                messagebox.showerror("Error","Insufficient balance!\nAvailable balance:" +str(accounts[acc_no]['balance']))
            else:
                break
        except ValueError:
             messagebox.showerror("Error","Please enter a valid number.")

    accounts[acc_no]["balance"] = accounts[acc_no]["balance"] - amt
    save_accounts()
    log_transaction(acc_no, "WITHDRAWAL", amt)

    messagebox.showinfo("Success","Withdrawal successful!\nRemaining balance : " +str(accounts[acc_no]['balance']))


def check_balance():
    acc_no = simpledialog.askstring("Input","Enter account number : ")
    if not acc_no: return

    if acc_no not in accounts:
        messagebox.showerror("Error","Account not found!")
        return

    if authenticate(acc_no)==False :
        return

    messagebox.showinfo("Balance Info","Account Holder : "+accounts[acc_no]['name']+"\nBalance : "+str(accounts[acc_no]['balance']))
    

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
        pin = simpledialog.askstring("Security", "Enter PIN (" + str(attempts) + " attempts left): ", show="*")
        if pin is None: return False

        if pin == accounts[acc_no]["pin"]:
            return True
        else:
            attempts = attempts - 1
            messagebox.showwarning("Warning", "Wrong PIN. " + str(attempts) + " attempt(s) left.")

    messagebox.showerror("Error","Too many wrong attempts!")
    return False

def transfer():
    from_acc=simpledialog.askstring("Input","Enter account number : ")
    if from_acc not in accounts :
        if not from_acc: return
        messagebox.showerror("Error","Account not found!")
        return

    if authenticate(from_acc)==False :
        return
    
    to_acc = simpledialog.askstring("Input","Recipient account number: ")
    if to_acc not in accounts:
        if not to_acc: return
        messagebox.showerror("Error","Recipient account not found!")
        return

    if from_acc == to_acc:
        messagebox.showerror("Error","Cannot transfer to the same account!")
        return

    while True:
        try:
            amount = simpledialog.askfloat("Input","Enter transfer amount: ")
            if amount is None: return
            if amount <= 0:
                messagebox.showerror("Error","Amount must be positive.")
            elif amount > accounts[from_acc]["balance"]:
                messagebox.showerror("Error","Insufficient balance!")
            else:
                break
        except ValueError:
           messagebox.showerror("Error", "Please enter a valid number.")

    accounts[from_acc]["balance"] = accounts[from_acc]["balance"] - amount
    accounts[to_acc]["balance"]   = accounts[to_acc]["balance"] + amount
    save_accounts()
    log_transaction(from_acc, "TRANSFER OUT to " + to_acc, amount)
    log_transaction(to_acc, "TRANSFER IN from " + from_acc, amount)
    messagebox.showinfo("Success","Transfer successful!\nYour new balance: "+str(accounts[from_acc]['balance']))

def log_transaction(acc_no,action,amount):
    file=open("transactions.txt","a")
    file.write(acc_no+"|"+action+"|"+str(amount)+"\n")
    file.close()
    
def transaction_history():
    acc_no=simpledialog.askstring("Input","Enter account number : ")
    if not acc_no: 
        messagebox.showerror("Error","Account not found!")
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
               messagebox.showinfo("History","No transactions found.")
        else:
            output=""
            for record in history:
                parts = record.split("|")
                output+=parts[1]+ "→ Rs."+ parts[2]+"\n"
            messagebox.showinfo("Transaction History", output)
    except FileNotFoundError:
        messagebox.showinfo("History","No transactions found.")
    
accounts={}
load_accounts()


root=tk.Tk()
root.title("Bank Menu")
root.geometry("300x420")
root.configure(bg="#1e293b")

BTN_BG = "#3b82f6"      
BTN_FG = "#ffffff"      
EXIT_BG = "#ef4444"     
TEXT_COLOR = "#f8fafc"  


label=tk.Label(
    root, 
    text="BANKING SYSTEM", 
    font=("Helvetica", 14, "bold"), 
    bg="#1e293b", 
    fg=TEXT_COLOR
)
label.pack(pady=(25, 20))

def style_button(btn, bg_color=BTN_BG):
    btn.configure(
        font=("Helvetica", 10, "bold"),
        width=24,
        bg=bg_color,
        fg=BTN_FG,
        activebackground="#1d4ed8",
        activeforeground="#ffffff",
        bd=0,
        relief="flat",
        cursor="hand2"
    )
    btn.pack(pady=6, ipady=4) 

cr_acc=tk.Button(root,text="1. Create Account",command=create_account)
style_button(cr_acc)

dep_acc=tk.Button(root,text="2. Deposit Money",command=deposit)
style_button(dep_acc)

with_acc=tk.Button(root,text="3. Withdraw Money",command=withdraw)
style_button(with_acc)

ch_acc=tk.Button(root,text="4. Balance Inquiry",command=check_balance)
style_button(ch_acc)

tr_acc=tk.Button(root,text="5. Transfer Money",command=transfer)
style_button(tr_acc)

th_acc=tk.Button(root,text="6. Transaction History",command=transaction_history)
style_button(th_acc)

ex_acc=tk.Button(root,text="7. Exit Application",command=root.destroy)
style_button(ex_acc, bg_color=EXIT_BG)


root.mainloop()
    
