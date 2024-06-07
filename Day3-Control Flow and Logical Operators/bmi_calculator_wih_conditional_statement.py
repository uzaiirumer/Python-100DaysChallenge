print("Enter your height in meters e.g: 1.65 \n")
height = float(input())
print("Enter your weight in kilograms e.g: 72 \n")
weight = float(input())


bmi = weight / (height * height)

print(f"Your BMI is: {round(bmi, 2)}")

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You have normal weight")
elif bmi >= 25 and bmi < 30:
    print("You have slightly over-weight")
elif bmi >=30 and bmi < 35:
    print("You are over-weight")
elif bmi >= 35:
    print("You are clinically obese")

