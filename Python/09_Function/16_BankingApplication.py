# Banking Application

balance = 0.0
kyc_document = {}

def check_balance():
    print(f"Your current balance is {balance}")
    print("=============================================")

    pass

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Cannot deposit a negative or zero amount")
    print("=============================================")

    pass

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot withdraw a negative or Zero amount")
        print("=============================================")

    elif amount > balance:
        print("Cannot withdraw. Insufficient balance.")
        print("=============================================")

    else:
        balance -= amount
    pass

def update_kyc(**docs):
    global kyc_document
    kyc_document.update(docs)
    pass

def check_kyc():
    if len(kyc_document) == 0:
        print(f"KYC not done")
        print("=============================================")
    else:
        for doc in kyc_document:
            print(f"{doc}: {kyc_document[doc]}")
        print("=============================================")


if __name__ == "__main__":
    print("=============================================")
    print("Welcome to ABC bank!!!")
    print("=============================================")


    while True:
        print("1. Check your balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = (input("Enter your choice (1-6) : "))
        print("=============================================")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter the amount to deposit: "))
            deposit(amt)
            print(f"Amount {amt} deposited successfully!")
        elif choice == '3':
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)
            print(f"Amount {amt} Withdrawn successfully!")
        elif choice == '4':
            check_kyc()

        elif choice == '5':
            kyc_docs = {}
            n_document = int(input("Enter the number of documents you want to add: "))
            for i in range(n_document):
                key = input("Enter the document type: ")
                value = input("Enter the document number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print(f"KYC updated!")
            print("=============================================")


        elif choice == '6':
            print("Quiting, have a nice day!!")
            break
        else:
            print("Invalid choice!!! Re-try.")
            print("=============================================")

    print("Thanks you for banking with us!")