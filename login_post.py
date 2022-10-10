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
    
    user_email = request.forms.get("user_email")

    user_password = request.forms.get("user_password")
    #validation for password

    for user in g.USERS:
        if user_email == user["user_email"] and user_password == user["user_password"]:
            ###############################
            user_session_id = str(uuid.uuid4())
            session = {"user_session_id": user_session_id, "user_id": user["user_id"], "user_firstname": user["user_firstname"], "user_lastname": user["user_lastname"], "user_email": user["user_email"], "iat": int(time.time()),"followees": user["followees"]}
            g.SESSIONS.append(session)
            print("Do you load until here?")

            ###############################
            encoded_jwt = jwt.encode(session, "theSecret", algorithm="HS256")
            response.set_cookie("jwt", encoded_jwt)

            return redirect ("/tweets_feed")
            
            ###############################
    return redirect ("/login")