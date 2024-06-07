print("Verify which year is a leap year!")
year = int(input("Please enter the year you want to confirm: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is an leap yaer")
        else:
            print(f"The year {year} is not a leap yaer")
    else:
        print(f"The year {year} is an leap yaer")
else:
    print(f"The year {year} is not a leap yaer")
