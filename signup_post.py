from urllib import response
from bottle import post, redirect, request
import g
import uuid
import re

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


    user = {"user_id": user_id, "user_firstname": user_firstname, "user_lastname": user_lastname, "user_email": user_email, "user_password": user_password}
        

    g.USERS.append(user)
        

    
    redirect("/login")

    
