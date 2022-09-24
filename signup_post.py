from bottle import post, redirect, request
import g
import uuid

####################

@post("/signUp")

def _():
    user_firstname = request.forms.get("user_firstname")
    user_lastname = request.forms.get("user_lastname")
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    user_id = str(uuid.uuid4())
    user = {"user_id": user_id, "user_firstname": user_firstname, "user_lastname": user_lastname, "user_email": user_email, "user_password": user_password}
    g.USERS.append(user)
    #return redirect(f"/signUpverified?user_firstname={user_firstname}")
    return redirect("/login")
