import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^(((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])|([0-9]))\.){3}((25[0-5])|(2[0-4][0-9])|(1[0-9]{2})|([1-9][0-9])|([0-9]))$", ip):
        #print("Valid")
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()





#^[0-2]?[0-9]?[0-9]\.[0-2]?[0-5]?[0-6]\.[0-2]?[0-5]?[0-6]\.[0-2]?[0-5]?[0-6]
