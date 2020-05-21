import smtplib                                      #||Librería Protocolo Simple de Transferencia de Mails (Simple Mail Tranfer Protocol)||

receptor = str(input("Mail del destinatario: "))    #||Variable que solicita mail destinatario||

emisor   = str(input("Mail del emisor: "))          #||Variable que contiene mail del emisor||

password = str(input("Ingrese Password: "))         #||Variable que contiene el password||

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)    #||Variable que contiene la conexión con el servidor de gmail mediante el puerto 465||

server.login(emisor, password)                      #||Mail y password del emisor||

server.sendmail(
        emisor,                                     #||From:||
        receptor,                                   #||To:||
        "Mail Send From Python"                     #||Contenido del mensaje||
               )

server.quit() #||finaliZa la conexión con el servidor tras enviar el mail||



#fuente: https://www.afternerd.com/blog/how-to-send-an-email-using-python-and-smtplib/
''' 
You can use smtplib.SMTP or smtplib.SMTP_SSL to create the client object. 
The difference is that smtplib.SMTP_SSL uses a secure encrypted SSL protocol to connect to the SMTP server
while smtplib.SMTP doesn’t.
Línea 7 > server = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
'''

'''
OBSERVACIONES: Para que este código básico funcione,
la cuenta gmail del emisor debe tener habilitado el acceso a aplicaciones poco seguras:
Gmail > Gestionar Cuenta google > Seguridad > Acceso a Aplicaciones Poco Seguras (Activado)
'''