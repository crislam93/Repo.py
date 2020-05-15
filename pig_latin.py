def pig_latin(text):
    words = text.split(" ")
    pig   = "ay"
    lista = []
    for x in words:
        latin = (str(x[1:])+str(x[0]) +pig)
        lista.append(latin)
    return(" ".join(lista))


		
print(pig_latin("hello how are you"))
print(pig_latin("programming in python is fun"))