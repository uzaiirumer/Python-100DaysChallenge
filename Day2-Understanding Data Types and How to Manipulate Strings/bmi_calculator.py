print("Enter your height in meters e.g: 1.65 \n")
height = float(input())
print("Enter your weight in kilograms e.g: 72 \n")
weight = float(input())


bmi = weight / (height * height)

print(round(bmi, 2))