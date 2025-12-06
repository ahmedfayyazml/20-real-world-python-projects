import smtplib,ssl
import  os

class SendEmail:
    def send_email(self,message):
        host= "smtp.gmail.com"
        port = 465


        username = "babaralihaider74@gmail.com"
        password = "cxlm olpn woct dlxm"

        reciever = "babaralihaider74@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host,port,context=context) as server:
            server.login(username,password)
            server.sendmail(username,reciever,message)