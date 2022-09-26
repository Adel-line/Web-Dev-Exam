from csv import DictReader
from bottle import put, redirect, request, response
import g
import jwt

@put("/update")

def _():
    if not request.forms.get('updated_tweet_text'):
        response.status = 400
        return redirect("/tweets_feed")
    if not request.forms.get('tweet_id'):
        response.status = 400
        return redirect("/tweets_feed")

    if request.forms.get("image_check"):
        delete_tweet_image = request.forms.get("image_check")


    tweet_id = request.forms.get('tweet_id')
    updated_text = request.forms.get('updated_tweet_text')

    print("#"*40)
    print(tweet_id, updated_text)

    if not (updated_text):
        response.status = 400
        return redirect("/tweets_feed")
    
    try : 
        encoded_jwt = request.get_cookie("jwt")
        userSession = jwt.decode(encoded_jwt, "theSecret", algorithms="HS256")

        for tweet in g.TWEETS: 
            if tweet["id"] == tweet_id:
                tweet["text"] = updated_text
                if not delete_tweet_image == "false" :
                    tweet["image"] = ""
                print(tweet)

        response.status = 200
        return dict( user_id = userSession["user_id"], tweets = g.TWEETS)


    except Exception as ex:
        print(ex)
        print("#"*60)
        response.status = 500
        return {"info":"upsss.... something went wrong"}