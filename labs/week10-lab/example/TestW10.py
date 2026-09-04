# เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ Strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว, มีตัวเลข, มีตัวอักษร
#
# ตัวอย่างหน้าจอ
# Insert your password: Boonchoo
# Your password is not strong!
# 
# Insert your password: Test@123
# Your password is strong!

password = input("Your password: ")
lenght = len(password)
word = password.split('@')

if len(word) > 1:
    left = word[0].isalnum()
    right = word[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and len(word) == 2 and left == True and right == True:
    print("Your password is strong!")
else:
    print("Your password is not strong!")
