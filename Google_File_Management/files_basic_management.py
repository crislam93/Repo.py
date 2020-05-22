
#el modo "r" está implícito
with open("Google_File_Management/texto.txt") as file:
    print(file.read())
    print(type(file))

#"w" overwrite content, y si el documento no existe Pyrthon lo creará
with open("write_txt") as new_file:
    print(new_file.read())

#"r+" read and write

#"a" agrega contenido 