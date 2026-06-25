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
│   └── .gitkeep
├── accounts.txt          # Plain text database storing account variables (auto-generated)
├── transactions.txt      # Log file containing audit history (auto-generated)
├── bankgui.py            # Primary application source file containing layout and logic
└── README.md             # Project documentation
