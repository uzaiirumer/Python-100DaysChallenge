import random
names_string = ["Uzair", "Umer", "Umair",  "Sayyed",]

#names = [names_string.split(", ")]

num_of_names = len(names_string)
rand_choice =random.randint(0, num_of_names -1)

print(names_string[rand_choice])
