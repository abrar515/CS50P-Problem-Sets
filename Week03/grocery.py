list = {}
while True:
    try:
        item = input().upper()
        list[item] = list.get(item, 0) + 1
    except EOFError:
        break
for item in sorted(list):
        print(list[item], item)
