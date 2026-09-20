import csv
import sys

def main():
    n = len(sys.argv)
    if n > 2:
        sys.exit("Too many arguments have been given")
    elif n < 2:
        try:
            sys.exit("Not enough arguments have been given")
        except:
            sys.exit("Something went wrong :( please check up the names off the given files")

    list_good, list_bad = clearing(sys.argv[1])
    finalising(list_good, list_bad)



def clearing(f):
    wrong_emails = []
    ok_emails = []
    with open(f) as file:
        data = csv.DictReader(file)
        for i, line in enumerate(data, start=1):
            
            line["first_name"] = line["first_name"].title()
            line["last_name"] = line["last_name"].title()

            line["phone"] = line["phone"].replace("-", "").replace(" ", "")

            if "@" in line["email"]:
                ok_emails.append(line)
            else:
                wrong_emails.append(line)
    return ok_emails, wrong_emails





def finalising(list_g, list_b):
    with open("New_users.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id","first_name","last_name","email","phone"])
        writer.writeheader()
        writer.writerows(list_g)

    with open("No_emails_users.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id","first_name","last_name","email","phone"])
        writer.writeheader()
        writer.writerows(list_b)

if __name__ == "__main__":
    main()
