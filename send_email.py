from email.mime.text import MIMEText
import smtplib


def send_email(email, height, weight, avg_h, avg_w):
    from_email=
    from_password=
    to_email=email

    subject="Data Report"
    message="Hey there, Your Height is <strong>%s</strong>,Your Weight is <strong>%s</strong>.<br> The Average Value of Height out of 10 Values is <strong>%s</strong>, And weight out of 10 values is <strong>%s</strong>" %(height, weight, avg_h, avg_w)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

