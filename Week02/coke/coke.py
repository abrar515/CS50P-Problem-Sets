due = 50
while 0 < due:
    while True:
        print("Amount Due: " + str(due))
        coin = int(input("Insert Coin: "))
        match coin:
            case 25 | 10 | 5:
                break
            case _:
                continue
    due -= coin
print("Change owed:", -due)
