import smtplib  # Standard lib to send emails. Lecture 218
import ssl
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('PASSWORD_GMAIL'))


def send_email(message):
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    username = os.getenv('USERNAME_GMAIL')
    password = os.getenv('PASSWORD_GMAIL')

    reciever = 'marcin.karbowniczyn@gmail.com'

    context = ssl.create_default_context()  # Nie wiem co to, mogę później poszukać
    with smtplib.SMTP_SSL(host, port, context=context) as server:  # Musimy dać "as" bo otwieramy funkcję która zwraca zmienną na której są metody
        server.login(username, password)
        server.sendmail(username, reciever, message)
