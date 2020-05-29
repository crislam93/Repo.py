import re 
import datetime
import shutil

#Variables:
regex = r"\[(\d+)\]"
disk = shutil.disk_usage("/")
disk_used = disk.used
hoy = datetime.date.today()
sqr_brackets = [20665634]
log = f"Date: {hoy} \n Disk Used: {disk_used} \n Random: {sqr_brackets}"


def square_brackets_pattern(item):       #función para buscar solo [dígitos] entre corchetes
    tracker  = re.search(regex, item)     #captura solo la primera coincidecia 
    tracker1 = re.findall(regex, item)   #captura todas las coincidencias 
    return tracker, tracker1

print(square_brackets_pattern(log))
print(square_brackets_pattern("there are 99 elephants in a [cage]"))

