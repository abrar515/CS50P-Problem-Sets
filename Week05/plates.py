def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not 2 <= len(s) <= 6:
        #print("vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.")
        return False
    elif not s[0:2].isalpha():
        #print("All vanity plates must start with at least two letters")
        return False
    elif not s.isalnum():
        #print("No periods, spaces, or punctuation marks are allowed.")
        return False
    else:
        j = 3
        for x in s[2:(len(s)-1)]:
            #print(x, s[j])
            if x.isdigit() and s[j].isalpha():
                #print("Numbers cannot be used in the middle of a plate")
                return False
            else:
                j += 1
        isdigit = False
        for x in s:
            if not isdigit:
                if x.isdigit():
                    isdigit = True
                    if x == "0":
                        #print("first num cant be zero")
                        return False
        return True

if __name__ == "__main__":
    main()
