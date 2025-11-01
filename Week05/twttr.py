def main():

    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    vowels = ["a","e","i","o","u"]
    for v in vowels:
        word = word.replace(v, "")
        word = word.replace(v.upper(), "")
    return word



if __name__ == "__main__":
    main()


#for s in word:
    #    match s.lower():
    #        case "a" | "e" | "i" | "o" | "u":
    #            print("", end="")
    #        case _:
    #            print(s, end="")
