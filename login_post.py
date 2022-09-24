from bottle import post, redirect, request, response, get
import re
import g
import uuid
import time
import jwt

@post("/login")

def _(): 
    if not request.forms.get("user_email"):
        return redirect ("/login?error=user_email")
    if not re.match( g.regex_email, request.forms.get("user_email")):
        return redirect ("/login?error=user_email")
    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
        return redirect (f"/login?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) < 6:
        return redirect (f"/login?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) > 15:
        return redirect (f"/login?error=user_password&user_email={user_email}")
    user_password = request.forms.get("user_password")

    for user in g.USERS:
        if user_email == user["user_email"] and user_password == user["user_password"]:
            ###############################
            user_session_id = str(uuid.uuid4())
            session = {"user_session_id": user_session_id, "user_id": user["user_id"], "user_firstname": user["user_firstname"], "user_lastname": user["user_lastname"], "user_email": user["user_email"], "iat": int(time.time())}
            g.SESSIONS.append(session)

            ###############################
            encoded_jwt = jwt.encode(session, "theSecret", algorithm="HS256")
            response.set_cookie("jwt", encoded_jwt)

            return redirect ("/tweets_feed")
            
            ###############################
    return redirect ("/login")