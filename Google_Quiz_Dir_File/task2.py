#importamos librería requerida: os
import os 

#Creamos función de creación de directorios y archivos
def create_directory(directory, filename):
    
    #Asegurarse de que el directorio nuevo no exista:
    if os.path.exists(directory) == False:
        os.mkdir(directory) #Creamos el nuevo directorio mediante os.mkdir()
        print("New Directory {} Has Been Created!".format(directory))

    os.chdir(directory) #nos ubicamos dentro del nuevo directorio mediante os.chdir()
    with open(filename, "w") as file: #indicamos que queremos crear un archivo dentro de nuestro directorio
        file.write('''
                    The new_directory function creates a new directory inside the current working directory, 
                    then creates a new empty file inside the new directory,
                    and returns the list of files in that directory. 
                    Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".
                ''')
    print(file.read())
    return os.listdir(directory)

print(create_directory("NewPyDir", "pytext.txt"))

