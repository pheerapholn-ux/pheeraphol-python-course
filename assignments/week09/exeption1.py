"""
1.โจทย์คำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
- ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
- ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise ValueError
- ผู้ใช้พยายามหารด้วย 0 #ZerodivisionError
- โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย Finally
"""
try :
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+ - * /): ")
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น + - * / เท่านั้น")
    print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("กรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้") 

except Exception:
    print("ทำบางอย่างไม่ได้ไม่แน่ใจว่าอะไร")

else:
    print("คำนวณข้อมูลเรียบร้อย")

finally:
    print("จบการทำงาน") 
           