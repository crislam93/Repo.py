import re 

texto = "One. Two! Three? Four: Five"

regex = r"[.!?:]" #el corchete contiene los símbolos que indicarán donde "cortar" 
rgx = r"([.!?:])"

print(re.split(regex, texto)) #OUTPUT: ['One', ' Two', ' Three', ' Four', ' Five']
print(re.split(rgx, texto)) #OUTPUT: ['One', '.', ' Two', '!', ' Three', '?', ' Four', ':', ' Five'] 


regex1 = r"(\w*\W*@.*.com)"
'''
1)(\w)alfanuméricos (*) todos los que hayan
2)(\W)los NO alfanuméricos (*) todos los que hayan
3)@ delimita el antes y el después del mail 
4)(.*) admite todo tipo de caracteres (alfanumérico y especiales)
5)(.com) que lleve .com al final 
'''
change = "[USER_MAIL]"

print(re.sub(regex1, change, "Mail from cristhianlam_93@my.samplemail.com has been received"))
#formato sustitución: re.sub(criterios de cambio, contenido que quieres agregar, contenido que quieres cambiar)
