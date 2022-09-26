from bottle import get, request, view, response, redirect
import g
import jwt

#########################

@get("/tweets_feed")
#last thing read
@view("tweets_feed")

def _(): 

    if len(g.SESSIONS) < 1 :
        response.status = 400
        redirect ("/signUp")

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/signUp")
    
    encoded_jwt = request.get_cookie("jwt") 
    userSession = jwt.decode(encoded_jwt, "theSecret", algorithms="HS256")

    
        
    return dict(tweets=g.TWEETS, user_id = userSession["user_id"])