answer = input("Expression: ")

x, y, z = answer.split(" ")

if y == "+":
	end = float(x) + float(z)
elif y == "-":
	end = float(x) - float(z)
elif y == "/":
	end = float(x) / float(z)
elif y == "*":
	end = float(x) * float(z)
print(round(end, 2))
