def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(","🙁")
    return text
def main():
    print(convert(input()))

main()
