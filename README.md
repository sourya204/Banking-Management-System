# 🏦 Banking Management System

> A simple command-line banking system built with pure beginner Python — no libraries, no frameworks, just core concepts from scratch.

---

## 📖 About the Project

This is my **first Python project**, built while learning programming for the very first time.

The idea was simple — instead of just reading theory, I wanted to build something that *feels* real. A banking system uses almost every basic Python concept in one place, so it was the perfect beginner project to really understand how programs work.

Built and tested entirely in **IDLE (Python 3)**.

---

## ✨ Features

- 🆕 **Create Account** — opens a new bank account with a name and opening deposit
- 💰 **Deposit Money** — add money to any account
- 💸 **Withdraw Money** — withdraw with balance validation
- 📊 **Check Balance** — view current account balance
- 🔁 **Fund Transfer** — transfer money between two accounts
- 🧾 **Transaction History** — view last 10 transactions
- 🔐 **Change PIN** — update your 4-digit PIN securely
- 💾 **File Handling** — all data is saved to a `.txt` file so it persists after closing

---

## 🧠 Python Concepts Used

| Concept | Where it's used |
|---|---|
| `variables` | storing name, balance, account number |
| `dictionary` | storing all account data |
| `while loop` | main menu + PIN attempts |
| `for loop` | reading file line by line |
| `if / elif / else` | menu choices, validation, error handling |
| `functions (def)` | each feature is its own function |
| `file handling` | saving and loading accounts from `.txt` |
| `try / except` | catching invalid number inputs |
| `string methods` | splitting and parsing file data |

---

## 🚀 How to Run

No installations needed. Just make sure Python 3 is installed.

**In IDLE:**
1. Open `bank.py` in IDLE
2. Press `F5` to run
3. Use the menu in the Shell window

**In Terminal:**
```bash
python bank.py
```

---

## 📂 Files in This Project

```
📁 banking-system/
├── 🐍 bank.py           ← main program
├── 📄 accounts.txt      ← created automatically when you run
├── 📄 transactions.txt  ← created automatically when you run
└── 📘 README.md
```

> `accounts.txt` and `transactions.txt` are created automatically the first time you run the program. You don't need to create them manually.

---

## 🖥️ Sample Output

```
--- BANK MENU ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Fund Transfer
6. Transaction History
7. Change PIN
8. Exit

Choose: 1
Enter your name: Rohit Kumar
Opening deposit amount (min ₹500): 5000

✅ Account created!
Your account number is: 1001
```

---

## 🗺️ How I Built It (Stage by Stage)

I didn't write the whole program at once. I built it in stages:

```
Stage 1 → Menu with while loop
Stage 2 → Dictionary to store accounts
Stage 3 → Create account function
Stage 4 → Deposit and withdraw
Stage 5 → Check balance
Stage 6 → File handling (save and load data)
Stage 7 → PIN authentication
Stage 8 → Transfer + transaction history
```

Each stage taught me something new. By the end, all the stages connected into one working program.

---

## 📚 What I Learned

- How `while True` loops work and why `break` is important
- Why dictionaries are better than multiple variables for storing structured data
- How RAM (temporary) vs hard disk (permanent) storage works in programs
- Why data needs to be saved to a file — variables reset every time the program restarts
- How to validate user input so the program doesn't crash
- How to split a big program into small functions

---

## 🙋 Who is this for?

Anyone who is **learning Python for the first time** and wants a real project to practice with. Feel free to fork it, improve it, or use it as a reference!

---

## 🌱 Future Improvements

- [ ] Add admin login with password
- [ ] Add interest calculation for savings accounts
- [ ] Store data in a proper database (SQLite)
- [ ] Add a GUI using Tkinter

---

*Built with 🐍 Python 3 | Tested on IDLE | First project ever* 🎉
