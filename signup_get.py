from bottle import get, request, view

######################

@get("/signUp")
@view("signUp")

def _(): 
    error = request.params.get("error") 
    return dict(error=error)  
