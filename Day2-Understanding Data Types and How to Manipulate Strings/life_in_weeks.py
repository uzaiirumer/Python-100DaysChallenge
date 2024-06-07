print("Please enter your current age in years : \n")

age = int(input())

total_age_in_weeks = 90 * 52

#print(total_age_in_weeks)


your_age_in_weeks = age * 52
#print(your_age_in_weeks)

total_weeks_left = total_age_in_weeks - your_age_in_weeks

print(f"You have only {total_weeks_left} weeks left ")
