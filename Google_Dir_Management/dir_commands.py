import os 

print("You are HERE ===>", os.getcwd())

os.rmdir("nuevo_directorio")

os.mkdir("nuevo_directorio") #Creamos un nuevo directorio

os.chdir("nuevo_directorio") #entramos en él

print("HERE now:" ,os.getcwd()) #obtenemo su ubicación

