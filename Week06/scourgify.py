import sys
import csv

def main():

    #check command line arguments
    if len(sys.argv) == 3:
        oldfile = sys.argv[1]
        newfile = sys.argv[2]
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

    #check extension of existing file
    if not oldfile.endswith(".csv"):
            sys.exit(f"Not a .csv file")

    #open existing file, split name into first and last and append to the new file
    try:
        with open(oldfile, "r") as old, open(newfile, "w") as new:
            old = csv.DictReader(old)
            new = csv.DictWriter(new, fieldnames=["first", "last", "house"])
            new.writeheader()
            for row in old:
                last, first = row["name"].split(",")
                new.writerow({"first" : first.strip(), "last" : last.strip(), "house" : row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {oldfile}")

if __name__ == "__main__":
    main()



