import re

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

'''
^ = que el texto empiece con letras de la a-z, A-Z o _  [a-zA-Z_]
el resto de la variable puede contener cadenas alfanuméricas o _ [a-zA-Z0-9_]

'''

print(re.search(pattern, "_this_is_a_text_with_underscore_symbol")) #match
print(re.search(pattern, "@hotmail.com"))       #None
print(re.search(pattern, "12345_abcde!!"))      #None
print(re.search(pattern, "abc_@hotmail.com"))   #None
print(re.search(pattern, "abc_1234"))           #match

