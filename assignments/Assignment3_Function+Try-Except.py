def deposite(money):
    balance = 1000
    print(f"Opening Balance: {balance} Bath")

    try:
        amount = float(input("Enter deposit amount:"))
        
        if amount <= 0:
            raise ValueError("The deposit amount must be greater than 0.")

    except ValueError as e:
        if str(e) == "The deposit amount must be greater than 0.":
            print(f"\nAn error occurred")
        else:
            print("\nAn error occurred: Please enter the correct number")

    else:
        balance = balance + amount
        print("\nDeposit successful")
        print(f"Balance: {balance:.2f} Bath")

    finally:
        print("Deposit Completed")

#เรียกใช้ฟังก์ชัน
deposite(1000)
        