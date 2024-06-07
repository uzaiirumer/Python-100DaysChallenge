print("Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? £"))
tip = int(input("How much tip would you like to give in percentage? 10, 12, or 15? "))
number_of_persons = int(input("How many people to split the bill? "))

percentage_calculation = (total_bill * tip) / 100

bill_with_tip = (total_bill + percentage_calculation) / number_of_persons

print(f"Each person should pay: £{round(bill_with_tip, 2)}")
