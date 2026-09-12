# เขียน function แปลงหน่วยสกุลเงิน 
# THB <-> USD .. 1 USD = 32 THB

#โดยใช้ชื่อและการใช้งาน 
#function convert_currency(100,USD)

def convert_currency(TH, US):
    if US == "USD":
        print(f"{TH} THB = {TH / 32.0} USD")
    else:
        print(TH, "USD = ", TH * 32.0, "THB")

convert_currency(500, "USD")
convert_currency(100, "THB")     
