import smtplib
from email.message import EmailMessage

email_subject = "Email test Pythonist"
while True:
    sender_email_address = input("kirjuta teie email adress: ")
    if "@" not in sender_email_address or "." not in sender_email_address:
        print("Palun sisesta kehtiv emaili aadress.")
    else:
        try:
            receiver_email_address = "jaroslavbaka25@gmail.com"
            email_password = input("Sisesta oma emaili rakenduse parool: ")
            print("Proovin saata emaili...")
            break
        except Exception as e:
            print("Tekkis viga:", e)

# qztk ogxx duva gvez
email_smtp = "smtp.gmail.com"
message = EmailMessage()

with open('message.html', 'r', encoding='utf-8') as file:
 file_content = file.read()
message.set_content(file_content, subtype='html')

with open('Python-logo-notext.svg.png', 'rb') as file:
 image_data = file.read()
message.add_attachment(image_data, maintype='image', subtype='png', filename='Python-logo-notext.svg.png')

message['Subject'] = email_subject
message['From'] = sender_email_address
message['To'] = receiver_email_address


server = smtplib.SMTP(email_smtp, '587')

server.ehlo()

server.starttls()

server.login(sender_email_address, email_password)

server.send_message(message)


server.quit()



