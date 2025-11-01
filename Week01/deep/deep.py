answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

answer = answer.replace(" ", "")
answer = answer.lower()

match answer:
	case "42" | "fortytwo" | "forty-two":
		print("Yes")
	case _:
		print("No")
