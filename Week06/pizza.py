from tabulate import tabulate
import csv
import sys

#check command line arguments
if len(sys.argv) == 2:
    filename = sys.argv[1]
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")


#check the file extension
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")


#get the rows from the file
try:
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        table = []
        for row in reader:
            table.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table, headers="keys", tablefmt="grid"))
