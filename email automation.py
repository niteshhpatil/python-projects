import smtplib
from email.message import EmailMessage

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()


server_login_mail = "automail.patil.nitesh9@gmail.com"
server_login_password = "Niteshprakash92"

server.login(server_login_mail,server_login_password)

email = EmailMessage()

email['From'] = server_login_mail
email['To'] = "patil.nitesh9@gmail.com"
email['Subject'] = "hii this is subject"
email.set_content("hii this is message")

server.send_message(email)
