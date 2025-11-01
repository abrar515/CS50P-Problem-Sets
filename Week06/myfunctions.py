import sys

#check command line arguments
def checkargs(argno):
    if len(sys.argv) == argno:
        filename = sys.argv[1]
    elif len(sys.argv) > argno:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


#check the file extension
def checkextension(ext):
    if not filename.endswith(ext):
        sys.exit(f"Not a {ext} file")


def hello():
    print("hello")

#get the rows from the file
def later():
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            table = []
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers="keys", tablefmt="grid"))
