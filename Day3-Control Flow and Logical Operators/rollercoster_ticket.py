print("Welcome to the rollercoster!")
bill = 0
height = int(input("What is your height in cm?"))

if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets £5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets £7.")
    else:
        bill = 12
        print("Adult tickets £12.")
    photo = input("Do you want photgraphy for the memory? Press Y or N: ")

    if photo == "y" or photo == "Y":
        bill = bill + 3
        print(f"Please pay £{bill}")
    elif photo != "y" or photo != "Y":
        print(f"Please Pay £{bill}")


else:
    print("Grow up first to ride the rollercoster")

