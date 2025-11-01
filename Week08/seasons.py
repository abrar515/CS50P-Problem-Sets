from datetime import date
from re import search
import sys
import inflect
p = inflect.engine()


def main():
    dob = input("Date of Birth: ")
    try:
        dob = convert_to_date(dob)
    except (ValueError, AttributeError):
        sys.exit("Invalid Date")


    minutes = dob - date.today()
    print(p.number_to_words(minutes.days*-24*60, andword="").capitalize()+" minutes")


def convert_to_date(s):
    if s := search(r"(\d{4})-(\d{2})-(\d{2})", s):
        return date(int(s.group(1)), int(s.group(2)), int(s.group(3)))
    else:
        raise ValueError



if __name__ == "__main__":
    main()
