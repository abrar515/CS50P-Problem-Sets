answer = input("File name: ")

answer = answer.replace(" ", "")
answer = answer.lower()

if answer.endswith((".jpeg", ".jpg")):
    print("image/jpeg")
elif answer.endswith(".pdf"):
    print("application/pdf")
elif answer.endswith(".gif"):
    print("image/gif")
elif answer.endswith(".png"):
    print("image/png")
elif answer.endswith(".txt"):
    print("text/plain")
elif answer.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
