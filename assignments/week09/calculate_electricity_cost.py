def calculate_electricity_cost(units = 0):
    if units > 200:
        cost = (2.50 * 50) + (3.00 * 50) + (100 * 3.5) + ((units - 200)* 4.00) + 25
        print("1-50 units: 125.00 bath")
        print("51-100 units: 150 bath" )
        print("101-200 units: 350.00 bath")
        print(f"201-{units} units: {(units - 200)* 4.00} bath")
        print("ค่าบริการ: 25.00 bath")
        print("รวามค่าไฟทั้งสิ้น:", cost)
    elif units > 100:
        cost = (2.50 * 50) + (3.00 * 50) + ((units - 200)* 3.50) + 25
        print("1-50 units: 125.00 bath")
        print("51-100 units: 150 bath" )
        print(f"101-{units} units: {(units - 100)* 3.50} bath")
        print("ค่าบริการ: 25.00 bath")
        print("รวามค่าไฟทั้งสิ้น:", cost)
    elif units > 50:
        cost + (2.50 * 50) + ((units - 50)* 3.00) + 25
        print("1-50 units: 125.00 bath")
        print(f"51-{units} units: {(units - 50)* 2.50} bath")
        print("ค่าบริการ: 25.00 bath")
        print("รวามค่าไฟทั้งสิ้น:", cost)
    elif units >= 0:
        cost = (2.50 * units) + 25
        print(f"1-{units} units: {(2.50 * units)} bath")
        print("ค่าบริการ: 25.00 bath")
        print("รวามค่าไฟทั้งสิ้น:", cost)
    else:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")

print("=== โปรแกรมคำนวณค่าไฟฟ้า ===")
while(True):
    print("1. คำนวณค่าไฟฟ้า")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู")

    if choice == "1":
        units = int(input("กรอกจำนวนหน่วยไฟฟ้า:"))
        calculate_electricity_cost(units)
    elif choice == "2":
        break
    else:
        print("เลือกเมนูไม่ถูกต้อง")
        