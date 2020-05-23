import csv
import os
import datetime


file_path  = open("Google_CSV_Management/data.txt")

csv_reader = csv.reader(file_path)

for row in csv_reader:
    fullname, phone, role = row
    print("Name: {} || Phone: {} || Role: {}".format(fullname, phone, role))


def add_info(fullname, phone, role):
    fpath = "Google_CSV_Management/data.txt"
    with open(fpath, "a") as file:
        if fullname in fpath:
            print("Name {} Already Exists".format(fullname))
        else:
            file.writelines(fullname + ", ")
            file.writelines(phone + ", ")
            file.writelines(role + "\n")
            timestamp      = os.path.getmtime(fpath)
            modified_time  =  datetime.date.fromtimestamp(timestamp)
            return "Last update {}, Data added: {}, {}, {}".format(modified_time,fullname,phone,role)

print(add_info("...", "123-654-789","..."))

