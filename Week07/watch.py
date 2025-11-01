import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    m = re.search(r"\<iframe.+src\=\"(\S+)\"", s)

    if m:
        url = m.group(1)
        check = re.search(r"youtube\.com\/embed\/(\w+)", url)
        if check:
            embed = check.group(1)
            return f"https://youtu.be/{embed}"
        else:
            return check
    else:
        return None


if __name__ == "__main__":
    main()
