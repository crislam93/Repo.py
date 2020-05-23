import os

#os.remove("filename.extension")
#os.rename("filename.extension")

file_path = "Google_File_Management/texto.txt"

print(os.path.exists(file_path))

print("file size is: {}".format(os.path.getsize(file_path))+" Kbs")

print("The file has been modified: {}".format(os.path.getmtime(file_path)))

import datetime

timestamp = os.path.getmtime(file_path)
print(datetime.datetime.fromtimestamp(timestamp)) #fecha en que fue modificado este archivo por última vez

print(os.path.abspath("texto.txt")) #muestra la ruta absoluta del archivo seleccionado


