import csv
import os

hosts = [["works_tation.local","192.168.0.1"],["remote_station","10.2.5.6"]]

with open("Google_CSV_Management/hosts.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(hosts)
    
    


