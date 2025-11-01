import sys

def main():
    while True:
        try:
            fraction = convert(input("Fraction: "))
        except (ValueError, ZeroDivisionError):
            pass
        except (EOFError):
            sys.exit("")
        else:
            break

    print(gauge(fraction))


def convert(fraction):
    a, b = fraction.split ("/")
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroDivisionError
    elif a > b or a < 0 or b < 0:
        raise ValueError
    return (a/b)*100

def gauge(percentage):
    percent = int(round(percentage))
    if percent <= 1:
        return "E"
        #print("E")
    elif percent >= 99:
        return "F"
        #print("F")
    else:
        return f"{percent}%"
        # print(f"{percent}%")


if __name__ == "__main__":
    main()
