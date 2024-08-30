from flask_mail import Message
from app import mail

def send_email(subject, recipent, body):
    msg =  Message(subject, recipients = [recipent])
    msg.body = body
    mail.send(msg)