# Banking Management System

A lightweight, secure Desktop Banking Application built using Python and Tkinter. The application offers a graphical user interface (GUI) allowing users to perform standard banking operations smoothly. Account information and transaction logs are persistently saved using flat text files.

## Features

* **Account Creation:** Generates a unique 6-digit account number automatically based on the last registered entry. Requires a secure 4-digit PIN and a minimum initial deposit of Rs. 500.
* **Secure Authentication:** Validates user transactions through PIN verification with a 3-attempt lock safeguard.
* **Deposits & Withdrawals:** Supports real-time balance updates with robust numeric validation (rejects negative numbers, alphabet strings, or empty fields).
* **Fund Transfers:** Allows safe balance transfers between two different registered accounts. Includes internal validation to ensure users cannot transfer money to themselves.
* **Balance Inquiry:** Fast lookup displays the current balance along with the account holder's name.
* **Transaction History:** Generates and presents structured logs of all deposits, withdrawals, and fund transfers.

---

## Folder Structure

```text
Banking-Management-System/
├── screenshots/          # Application UI previews and walk-throughs
├── accounts.txt          # Plain text database storing account variables (auto-generated)
├── bank.py               # Original core banking engine / CLI version
├── bankgui.py            # Primary desktop GUI application source file 
└── README.md             # Project documentation
```
---

## How to Run

Follow these steps to download and launch the application on your local machine:

1. **Clone the Repository:**
   Open your terminal or command prompt and run the following command to download the project files:
   ```bash
   git clone https://github.com/sourya204/Banking-Management-System.git
   ```
2. **Navigate to the Project Directory:**
  Change your working directory to the folder containing the repository files:
  ```bash
    cd Banking-Management-System
  ```
3. **Launch the Application:**
   Execute the main script using Python to start the Graphical User Interface (GUI):
   ```bash
   python bankgui.py
   ```
