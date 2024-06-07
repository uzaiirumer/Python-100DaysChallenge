import random
your_number = int(input('Please Choose and number "0 for Heads" and "1 for Tails" \n'))
rand_num = random.randint(0, 1)
your_number
if your_number == rand_num and rand_num == 0:
    print("Congratulation! You won, It's Head")
elif your_number == 1 and rand_num == 1:
        print("Congratulation! You won, It's Tails")
else:
    print("You loss the toss")