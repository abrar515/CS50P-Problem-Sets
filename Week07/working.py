import re


def main():
        print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(?P<h1>1[0-2]|0?[1-9])(?P<m1>\:[0-5][0-9])? (?P<AMPM1>AM|PM) to (?P<h2>1[0-2]|0?[1-9])(?P<m2>\:[0-5][0-9])? (?P<AMPM2>AM|PM)$"
    match = re.search(pattern, s)

    try:
        h1 = converthour(match.group("h1"), match.group("AMPM1"))
        h2 = converthour(match.group("h2"), match.group("AMPM2"))

        m1 = isminutes(match.group("m1"))
        m2 = isminutes(match.group("m2"))
    except:
        raise ValueError
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def converthour(h, AMPM):
    if int(h) == 12:
        return 0 if AMPM == "AM" else 12
    else:
        return int(h) if AMPM == "AM" else int(h)+12

def isminutes(m):
    if m:
        return int(m.rsplit(":")[1])
    else:
        return 0


if __name__ == "__main__":
    main()



