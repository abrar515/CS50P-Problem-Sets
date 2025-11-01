answer = input("Greeting: ")

answer = answer.replace(" ", "")
answer = answer.lower()

if answer.startswith("hello"):
	print("$0")
elif answer.startswith("h"):
	print("$20")
else:
	print("$100")
