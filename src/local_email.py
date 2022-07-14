#python -m smtpd --nosetuid --class DebuggingServer localhost:8025
import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Hello Python World!'
msg['From'] = 'kiateamscommunications@gmail.com'
msg['To'] = 'jerzarq@gmail.com'
msg.set_content("""Hello World,
    I am writing to tell you that I am alive!

Yours very truly,
Johnny B. Goode
""")

smtp = smtplib.SMTP('localhost:8025')
smtp.send_message(msg)
smtp.quit()

print(msg)
