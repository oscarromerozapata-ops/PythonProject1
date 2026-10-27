mail = [".@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com", "asdf..@awe.com"
    , "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com" ,"awer@wer.com","awer@wer.commmm","..@wer.commmm"]

#crear lista con los mails correctos
indices_mails_correctos=[]
for i in range(len(mail)):
    #print(mail[i])
    mail_correcto=True
    if mail[i].count("@")!=1:
        mail_correcto=False
    else:
        usuario=mail[i][:mail[i].index("@")]
        dominio= mail[i][mail[i].index("@")+1:]
        # print(usuario)
        # print(dominio)
        usuario=usuario+"."
        dominio=dominio+"."
        inicio=0
        final=0
        for j in range(usuario.count(".")):
            if j==0:
                inicio=0
                final=usuario.find(".")
            else:
                inicio=final+1
                final=usuario.find(".",inicio)
            trozo_mail=usuario[inicio:final]
            #print(trozo_mail)
            if len(trozo_mail)==0:
                mail_correcto=False
            elif not trozo_mail.isalnum():
                mail_correcto=False
            else:
                inicio=0
                final=0
                for j in range(dominio.count(".")):
                    if j==0:
                        inicio=0
                        final=dominio.find(".")
                    else:
                        inicio=final+1
                        final=dominio.find(".",inicio)
                    trozo_mail=dominio[inicio:final]
                    if len(trozo_mail)==0:
                        mail_correcto=False
                    elif not trozo_mail.isalnum():
                        mail_correcto=False
        if mail_correcto==True:
            indices_mails_correctos.append(i)
print(indices_mails_correctos)
for i in indices_mails_correctos:
    print(mail[i])