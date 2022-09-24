from bottle import get, request, view, redirect, response
import g

#########################

@get("/global_users")
@view("global_users")

def _(): 
    if len(g.SESSIONS) < 1 :
        response.status = 400
        redirect ("/signUp")

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/signUp")
    error = request.params.get("error") 

    return dict(users=g.USERS, tweets=g.TWEETS) 