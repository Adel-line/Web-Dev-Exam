from bottle import get, request, view, redirect, response
import g
import jwt

#########################

@get("/global_users")
@view("global_users")

def _(): 
    if len(g.SESSIONS) < 1 :
        response.status = 400
        redirect ("/login")

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/login")
    error = request.params.get("error") 

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/login")

    try : 
        #decoding the cookie
        encoded_jwt = request.get_cookie("jwt")
        userSession = jwt.decode(encoded_jwt, "theSecret", algorithms="HS256")
        
        return dict(users=g.USERS, sessionID=userSession["user_id"], followees=g.FOLLOWEES, tweets=g.TWEETS) 

    except Exception as ex : 

        print(ex)
        print("#"*60)
        response.status = 500
        return {"info":"sorry, something went wrong. try again"}