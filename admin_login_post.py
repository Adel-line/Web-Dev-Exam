from bottle import post, redirect, request, response, get
import re
import g
import uuid
import time
import jwt

@post("/admin_login")

def _(): 

    if not request.forms.get("admin_email"):
        return redirect ("/login?error=user_email")
    if not request.forms.get("admin_email"):
        return redirect ("/login?error=user_email")
    user_email = request.forms.get("admin_email")

    if not request.forms.get("admin_password"):
        return redirect (f"/login?error=admin_password&user_email={user_email}")
    if len(request.forms.get("admin_password")) < 6:
        return redirect (f"/login?error=admin_password&user_email={user_email}")
    if len(request.forms.get("admin_password")) > 15:
        return redirect (f"/login?error=admin_password&user_email={user_email}")
    admin_password = request.forms.get("admin_password")

    if user_email == "admin@gmail.com" and admin_password == "admin123":
        print("dadadadadadada")
            ###############################
        user_session_id = str(uuid.uuid4())
        session = {"user_session_id": user_session_id, "user_id": "adminIDWOWSOSECURE123", "user_firstname": "Secret", "user_lastname": 'hacker :0', "user_email": user_email, "iat": int(time.time())}
        g.SESSIONS.append(session)
        print(g.SESSIONS)

            ###############################
        encoded_jwt = jwt.encode(session, "theSecret", algorithm="HS256")
        response.set_cookie("jwt", encoded_jwt)

        return redirect ("/admin_panel")
            
            ###############################