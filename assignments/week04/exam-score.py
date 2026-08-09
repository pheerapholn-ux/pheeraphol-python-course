# โปรแกรมเพื่อการตรวจสอบผลการสอบ
scores = []

print("Enter Student Score: ")
for i in range(5):
    score = int(input(f"Student No. {i+1}: "))
    scores.append(score)

print("Check Result...")

for index, score in enumerate(scores):
    
    if score >= 50:
        print(f"Student No. {index+1}  {score} : ผ่าน")
    else:
        print(f"Student No. {index+1}  {score} : ไม่ผ่าน")
        