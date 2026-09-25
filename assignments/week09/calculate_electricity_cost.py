print("=== โปรแกกรมคำนวณค่าไฟ ===")
while(True):
    print("1. คำนวณค่าไฟฟ้า")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")

    if choice == "1":
        units = int(input("กรอกจำนวณหน่วยไฟฟ้า: "))
        calculate_electricity_cost(units)
    elif choice == "2":
        break
    else:
        print("เมนูไม่ถูกต้อง")
        