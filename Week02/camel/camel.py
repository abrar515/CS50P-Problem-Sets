camel = input("camelCase: ")

for i in camel:
    if i.isupper():
        print("_"+i.lower(), end="")
    elif i.lower():
        print(i, end="")
    else:
        break
