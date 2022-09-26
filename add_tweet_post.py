from bottle import post, request, redirect, get, response, view
import uuid
import g
import jwt
import time
import os

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

        if request.files.get("tweet_image") :
            image = request.files.get("tweet_image")
            #clean image name
            image_name = image.filename.strip().replace(" ", "-")
            #download image in images folder
            if image_name in os.listdir("./images"):
                print ("File successfully saved")
            else:
                print ("File not saved")
                image.save(f"images/{image_name}")



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
            "image": image_name,
            "text": tweet_text,
            "iat": generated_time
            }

            g.TWEETS.append(tweet)

            is_image = "true"
            response.status = 200
            return dict( tweet = tweet, is_image = is_image)



###########################################################################################

        print("adadadadadadaa")
        is_image = "false"
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
            "image": "",
            "iat": generated_time
        }
        

        g.TWEETS.append(tweet)

        #RESPONSE
        return dict(tweet = tweet, is_image = is_image)

    except Exception as ex:
        print(ex)
        print("#"*60)
        response.status = 500
        return {"info":"upsss.... something went wrong"}

