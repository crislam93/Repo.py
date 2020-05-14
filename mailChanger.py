def changeMail(mail, old_domain, new_domain): #función cambiarEmail(correo,viejoDominio,nuevoDominio)

    if old_domain in mail:                    #si el @dominio_viejo está en tu correo_actual:

        index = mail.index(old_domain)        #variable1 = correo_actual.posición(del @dominio_viejo)

        print("posición: " + str(index) )     #Muestra en pantalla la posición del @dominio

        new_mail = mail[:index] + new_domain  #variable2 = correo_actual[:variable1] + @dominio_nuevo

        print("email has been changed successfully!")
        print("Old mail: "+mail)
        print("* New mail: "+new_mail+" * ")

changeMail("cristhianlam93@hotmail.com", "@hotmail.com", "@gmail.com")