pizza_price = 0


print("Thank you for choosing PYTHON PIZZA DELIVERIES")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S" or size == "s":
    pizza_price = 15
    if add_pepperoni == "Y" or add_pepperoni =="y":
        pizza_price += 2
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_price += 1
    print(f"Your final bill is: £{pizza_price}")
elif size == "M" or size == "m":
    pizza_price = 20
    if add_pepperoni == "Y" or add_pepperoni =="y":
        pizza_price += 3
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_price += 1
    print(f"Your final bill is: £{pizza_price}")
elif size == "L" or size == "l":
    pizza_price = 25
    if add_pepperoni == "Y" or add_pepperoni =="y":
        pizza_price += 3
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_price += 1
    print(f"Your final bill is: £{pizza_price}")