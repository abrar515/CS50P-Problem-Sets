import random

def main():

    level = getpositive("Level: ")
    rand_n = random.randint(1, level)
    while True:
        guess = getpositive("Guess: ")
        if guess < rand_n:
            print("Too small!")
        elif guess > rand_n:
            print("Too large!")
        else:
            print("Just right!")
            break




def getpositive(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 1:               #zero is considered a nonpositive int in this code
                continue
        except (ValueError):
            pass
        else:
            return n
main()
