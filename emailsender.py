import smtplib

to=input('Enter a recepients Email :\n ')

content=input('Enter the content of an email :\n')

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.echlo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()

sendEmail(to,content)
