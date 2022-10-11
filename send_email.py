# from bottle import post , request , response , run  , redirect
# import os
# import uuid
# import imghdr

# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# ##############################
# @post("/send_email")
# def _():
#     sender_email = "mem66267@gmail.com"
#     receiver_email = "mem66267@gmail.com"
#     password = "oiwildwsdbwwhgyi"

#     message = MIMEMultipart("alternative")
#     message["Subject"] = "My Company"
#     message["From"] = sender_email
#     message["To"] = receiver_email

#     # Create the plain-text and HTML version of your message
#     text = """\
#     Hi,
#     Thank you.
#     """

#     html = """\
#     <html>
#         <body>
#         <p>
#             Hi,<br>
#             <b>How are you?</b><br>
#         </p>
#         </body>
#     </html>
#     """

#     # # Turn these into plain/html MIMEText objects
#     part1 = MIMEText(text, "plain")
#     part2 = MIMEText(html, "html")

#     # # Add HTML/plain-text parts to MIMEMultipart message
#     # # The email client will try to render the last part first
#     message.attach(part1)
#     message.attach(part2)

#     # Create secure connection with server and send email
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        
#             print('iwork')
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, message.as_string())
#             return redirect("/login")
        