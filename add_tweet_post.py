from bottle import post, request, redirect, get, response, view
import uuid
import g
import jwt
import time

@post("/post_tweet") 
def _():   
    print("#"*30)
    

#VALIDATE SESSION

    if len(g.SESSIONS) < 1 :
        response.status = 400
        redirect ("/signUp")

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/signUp")

#VALIDATE TEXT
    #tweet_text = request.forms.get("tweet_text")
    #tweet_image = request.forms.get("tweet_image")
    
    # if not request.forms.get("tweet_text"):
    #     response.status = 400
    #     return redirect ("/tweets_feed")

    # if len(tweet_text) < 1 or len(tweet_text) > 400:
    #     response.status = 400
    #     return "you have entered too many of no charaters"


    print("adadadadadadaa")

    try : 
        print("adadadadadadaa")
        encoded_jwt = request.get_cookie("jwt") 
        print("adadadadadadaaX2")
        tweet_text = request.forms.get("tweet_text")
        userSession = jwt.decode(encoded_jwt, "theSecret", algorithms="HS256")
        generated_time = time.ctime(int(time.time()))
        print(userSession["user_session_id"])
        tweet_id = str(uuid.uuid4())
        tweet = {
            "user_id": userSession["user_id"],
            "id": tweet_id,
            "user_firstname": userSession["user_firstname"],
            "user_lastname": userSession["user_lastname"],
            "user_email": userSession["user_email"],
            "text": tweet_text,
            "iat": generated_time
        }
        

        g.TWEETS.append(tweet)

        #RESPONSE
        return dict(tweet = tweet, tweet_image = "false")

    except Exception as ex:
        print(ex)
        print("#"*60)
        response.status = 500
        return {"info":"upsss.... something went wrong"}

    #QUERY
    # tweet_id = str(uuid.uuid4())
    # tweet = {
    #     "id": tweet_id,
    #     "user_firstname": user_firstname,
    #     "user_lastname": user_lastname,
    #     "user_name": user_name,
    #     "text": tweet_text
    # }

    # g.TWEETS.append(tweet)
    #RESPONSE
    # return tweet_id