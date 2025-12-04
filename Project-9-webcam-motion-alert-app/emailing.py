import smtplib
import mimetypes
from email.message import EmailMessage

PASSWORD = "" # your email
SENDER = "" #sender email
RECIEVER = "" #reciever email
def send_email(image_path):

    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up"
    email_message.set_content("Hey we Just Saw a new Customer!")

    mime_type, _ = mimetypes.guess_type(image_path)

    main_type, sub_type = mime_type.split('/')

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype=main_type, subtype=sub_type)

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER,RECIEVER,email_message.as_string())
    gmail.quit()


    print("Email Sent")