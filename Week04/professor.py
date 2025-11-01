import random


def main():
    level = get_level()

    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        wrong = 0
        while True:
            try:
                answer = int(input(str(f"{x} + {y} = ")))
                if answer == x + y:
                    score += 1
                    break
                else:
                    raise ValueError
            except(ValueError):
                wrong += 1
                print("EEE")
                if wrong == 3:
                    print(f"{x} + {y} = {x+y}")
                    break
                pass
    print(f"score: {score}")



def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1 or n > 3:
                continue
        except (ValueError):
            pass
        else:
            return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
