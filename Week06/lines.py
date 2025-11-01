import sys

#check command line arguments
if len(sys.argv) == 2:
    filename = sys.argv[1]
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

#check the file extension
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

#get the list of lines from the file
try:
    with open(filename, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

#Go over lines and count lines with code
i = 0
for line in lines:
    if not (line.lstrip().startswith("#") or len(line.strip()) == 0):
        i += 1

print(i)
#print(f"the {filename} contains {i} lines of code")
