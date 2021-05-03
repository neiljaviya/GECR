#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
#guess the number, then tell them whether they guessed too low, too high, or
#exactly right also perform following task.
#   • Keep the game going until the user types “exit”
#   • Keep track of how many guesses the user has taken, and when the game
#     ends, print this out.

import random
user_ans = input("Guess the number: ")
count = 0
tries = 0
while user_ans != "exit":
    user_ans = int(user_ans)
    random_no = random.randint(0,9)
    if user_ans == random_no:
        count += 1
        print("Yaay..!! You guessed it right")
    elif user_ans < random_no:
        print("Oops..!! You guessed it too less, it was %d"%(random_no))
    else:
        print("Oops..!! You guessed it too high, it was %d"%(random_no))
    tries += 1
    user_ans = input("Guess the number: ")

print("You've got %d right out of %d"%(count,tries))