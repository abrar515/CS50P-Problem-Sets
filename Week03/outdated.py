months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            mm, dd, yyyy = date.split("/")
            mm, dd, yyyy = int(mm), int(dd), int(yyyy)

        elif "," in date:
            mm, dd, yyyy = date.replace(",", "").split()
            mm = months.index(mm) + 1
            dd, yyyy = int(dd), int(yyyy)
        else:
             continue

        if not (1 <= mm <= 12 and 1 <= dd <= 31):
            continue
    except (ValueError, IndexError):
            continue
    else:
        break
print(f"{yyyy}-{mm:02}-{dd:02}")

