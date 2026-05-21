import sys

class BankingSystem:
    def __init__(self):
        # Nested dictionary simulating a relational database schema
        # Schema: { account_number: { "name": str, "pin": str, "balance": float } }
        self.database = {
            "1001": {"name": "Syam Sandeep", "pin": "1234", "balance": 5000.0},
            "1002": {"name": "Rahul", "pin": "5678", "balance": 1500.0}
        }
        self.current_user = None

    def authenticate_user(self):
        print("\n--- SECURE USER LOGIN ---")
        acc_num = input("Enter Account Number: ").strip()
        pin = input("Enter 4-Digit PIN: ").strip()

        # Validation logic to prevent unauthorized access
        if acc_num in self.database and self.database[acc_num]["pin"] == pin:
            self.current_user = acc_num
            print(f"\n[SUCCESS] Authentication successful. Welcome, {self.database[acc_num]['name']}!")
            return True
        else:
            print("\n[ERROR] Invalid Account Number or PIN access denied.")
            return False

    def check_balance(self):
        balance = self.database[self.current_user]["balance"]
        print(f"\nYour current available balance is: ${balance:,.2f}")

    def deposit_funds(self):
        try:
            amount = float(input("\nEnter amount to deposit: "))
            if amount <= 0:
                print("[ERROR] Deposit amount must be positive.")
                return
            
            # Update state integrity
            self.database[self.current_user]["balance"] += amount
            print(f"[SUCCESS] ${amount:,.2f} deposited successfully.")
            self.check_balance()
        except ValueError:
            print("[ERROR] Invalid numeric input transaction cancelled.")

    def transfer_funds(self):
        print("\n--- SECURE INTER-BANK TRANSFER ---")
        target_acc = input("Enter Recipient Account Number: ").strip()

        if target_acc == self.current_user:
            print("[ERROR] Cannot transfer funds to your own account system loop blocked.")
            return

        if target_acc not in self.database:
            print("[ERROR] Recipient account routing node not found.")
            return

        try:
            amount = float(input("Enter transfer amount: "))
            if amount <= 0:
                print("[ERROR] Transfer amount must be positive.")
                return

            # Conditional safety gate check to prevent overdraft anomalies
            current_balance = self.database[self.current_user]["balance"]
            if amount > current_balance:
                print(f"[DENIED] Insufficient funds. Overdraft prevented. Maximum available: ${current_balance:,.2f}")
                return

            # Atomic transaction block executing state updates across nodes
            self.database[self.current_user]["balance"] -= amount
            self.database[target_acc]["balance"] += amount
            print(f"\n[SUCCESS] Transaction Complete! ${amount:,.2f} routed securely to {self.database[target_acc]['name']}.")
        except ValueError:
            print("[ERROR] Invalid numeric input transaction cancelled.")

    def logout(self):
        print(f"\nSession closed securely for user node: {self.current_user}")
        self.current_user = None

def main():
    bank = BankingSystem()
    
    while True:
        print("\n====================================")
        print("  AUTOMATED DATA BANKING INTERFACE  ")
        print("====================================")
        print("1. Access Secure User Login")
        print("2. Exit Application Terminal")
        
        choice = input("Select operation routing switch (1-2): ").strip()
        
        if choice == "1":
            if bank.authenticate_user():
                # Post-authentication multi-tier system dashboard
                while bank.current_user is not None:
                    print("\n--- USER CORE OPERATION PANEL ---")
                    print("1. Query Available Balance")
                    print("2. Execute Cash Deposit Pipeline")
                    print("3. Execute Secure Fund Transfer Routing")
                    print("4. Secure System Logout")
                    
                    sub_choice = input("Select operations node (1-4): ").strip()
                    
                    if sub_choice == "1":
                        bank.check_balance()
                    elif sub_choice == "2":
                        bank.deposit_funds()
                    elif sub_choice == "3":
                        bank.transfer_funds()
                    elif sub_choice == "4":
                        bank.logout()
                    else:
                        print("[ERROR] Invalid terminal instruction selection.")
        elif choice == "2":
            print("\nShutting down core database application loops cleanly. Goodbye!")
            sys.exit()
        else:
            print("[ERROR] System command unrecognized.")

if __name__ == "__main__":
    main()
