from urllib import response
from bottle import post, redirect, request
import g
import uuid
import re

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


####################

@post("/signUp")

def _():

    if not request.forms.get("user_email"):
        return redirect ("/login?error=user_email")
    
    


    for user in g.USERS :
        if request.forms.get("user_email") == user["user_email"]:
            response.status = 400
            return redirect ("/login?error=user_email")



    if not request.forms.get("user_password"):
        return redirect (f"/login?error=user_password&user_email")
    if len(request.forms.get("user_password")) < 6:
        return redirect (f"/login?error=user_password&user_email")
    if len(request.forms.get("user_password")) > 15:
        return redirect (f"/login?error=user_password&user_email")


    

    user_email = request.forms.get("user_email")

    user_firstname = request.forms.get("user_firstname")

    user_lastname = request.forms.get("user_lastname")

    user_password = request.forms.get("user_password")

    user_id = str(uuid.uuid4())


    user = {"user_id": user_id, "user_firstname": user_firstname, "user_lastname": user_lastname, "user_email": user_email, "user_password": user_password ,"followees":[]}
        

    g.USERS.append(user)

    sender_email = "mem66267@gmail.com"
    receiver_email = "mem66267@gmail.com"
    password = "oiwildwsdbwwhgyi"

    message = MIMEMultipart("alternative")
    message["Subject"] = "My Company"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    Thank you.
    """

    html = """\
    <html>
        <body>
        <p>
            Hi,<br>
            <b>Welcome to tweeter. Sup?</b><br>
        </p>
        </body>
    </html>
    """

    # # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # # Add HTML/plain-text parts to MIMEMultipart message
    # # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        
            print('iwork')
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            return redirect("/login")
        

    
