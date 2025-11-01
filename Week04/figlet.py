from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

fontsList = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fontsList)

elif (len(sys.argv) < 4) and (sys.argv [1]== "-f" or sys.argv [1]== "--font") and (sys.argv [2] in fontsList):
    font = sys.argv [2]
else:
    sys.exit("Invalid usage")

input = input("Input: ")
figlet = Figlet(font)
print("Output: ")
print(figlet.renderText(input))
