from bottle import get, request, view, response, redirect
import g

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
        
    return dict(tweets=g.TWEETS) 