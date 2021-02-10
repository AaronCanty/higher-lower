import random


def my_guess():

    have_a_guess = int(input("What number am I thinking of? "))

    randomnumber = random.randrange(1,10)
    while randomnumber != have_a_guess:
        if randomnumber < have_a_guess:
            print("No bueno, think lower")
        elif randomnumber > have_a_guess:
            print("Think higher")
        have_a_guess = int(input("Let's try that again - what number am I thinking of? "))
        if randomnumber == have_a_guess:
            answer = input("Fantastic! Got it in one. Wanna try again? ")
            if answer.lower().__contains__("y"):
                have_a_guess = int(input("What number am I thinking of? "))
                randomnumber = random.randrange(1,10)
            elif answer.lower().__contains__("n"):
                print("Shame! Thanks for playing. ")
                break
def main():
    my_guess()

main()