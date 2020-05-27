import datetime
import shutil
import re


error = "ERROR: [404]"
error2 = "[123456]"

x = shutil.disk_usage("/")
free_disk  = round((x.free/10000000),2)
total_disk = round((x.total/10000000),2) 

current_date = datetime.date.today()

info = "Total Disk Usage = {} \n Free Disk = {} \n Today: {} \n {} \n{}".format(total_disk, free_disk, current_date, error, error2)

regex = "\[(\d+)\]"

result = re.search(regex, info) 

print(result)
