from bottle import post, request, redirect, response
import g
import jwt

@post("/follow")

def _(): 
    print ("alalalalallaa")

    if not request.forms.get("followee_id"):
        return redirect ("/login?error=followee_id")

    if not (request.get_cookie("jwt")) : 
        response.status = 400
        redirect("/login")

    if not request.forms.get("followee_name"):
        return redirect ("/login?error=followee_name")

    try : 
        #decoding the cookie
        encoded_jwt = request.get_cookie("jwt")
        userSession = jwt.decode(encoded_jwt, "theSecret", algorithms="HS256")
        followee = request.forms.get("followee_id")
        followeeName = request.forms.get("followee_name")
        #create object
        relation = {
            "followee": followee, 
            "followee_name": followeeName
        }
        for user in g.USERS: 
            if user["user_id"] == userSession["user_id"]:
                user["followees"].append(relation)
                userSession["followees"].append(relation)
                print(user)

        encoded_jwt = jwt.encode(userSession, "theSecret", algorithm="HS256")
        response.set_cookie("jwt", encoded_jwt)
        return dict(sessoins=userSession)

    except Exception as ex : 

        print(ex)
        print("#"*60)
        response.status = 500
        return {"info":"sorry, something went wrong. try again"}