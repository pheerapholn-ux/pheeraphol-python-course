height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilogram: "))

BMI = round(weight / height ** 2, 1)
print(f"Your BMI is: {BMI:.1f}")

if BMI < 18.5:
    print("Underweight")

elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal weight") 

elif BMI >= 25.0 and BMI <= 29.9:
    print("Overweight")

else:
    print("Obese")