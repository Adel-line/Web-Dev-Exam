from traceback import print_last
from bottle import get, request, view, redirect, response
import g 
import jwt
import imp

#########################

@get("/admin_panel")
@view("admin_panel")

def _(): 
    print('hahahahahahah')

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/signUp")
    encoded_jwt = request.get_cookie("jwt") 
    userSession = jwt.decode(encoded_jwt, "theSecret", algorithms="HS256")

    print(userSession)
    #Only admin can access the admin panel
    if not (userSession["user_id"] == "adminIDWOWSOSECURE123"):
        return redirect ("/login")
    return dict(users=g.USERS, tweets=g.TWEETS) 