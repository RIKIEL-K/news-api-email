import smtplib
import ssl


def send_email(message,receiver_email):
    host= "smtp.gmail.com"
    port = 465

    username= "elrik4448@gmail.com"
    password = "jqwa glad gfeg wzaz"


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver_email,message)
