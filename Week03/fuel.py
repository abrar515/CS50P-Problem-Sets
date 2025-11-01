while True:
    try:
        fraction = input("Fraction: ")
        a, b = fraction.split ("/")
        a = int(a)
        b = int(b)
        if a > b or a < 0 or b < 0:
            continue
        percent = (a/b)*100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

percent = int(round(percent))
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")
