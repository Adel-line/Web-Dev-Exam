import imp
from bottle import get, request, view, redirect, response
import g 

#########################

@get("/admin_panel")
@view("admin_panel")

def _(): 
    if len(g.SESSIONS) < 1 :
        response.status = 400
        redirect ("/signUp")

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/signUp")
    return 