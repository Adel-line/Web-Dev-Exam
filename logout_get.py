from bottle import get , request , redirect
import jwt
import g

@get("/logout")
def _():
    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theSecret" , algorithms="HS256") 
    session = user_info
    g.SESSIONS.remove(session)
    return redirect("/login")