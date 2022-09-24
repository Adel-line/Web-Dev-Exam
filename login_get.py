from bottle import get, request, view

#########################

@get("/login")
@view("login")

def _(): 
    error = request.params.get("error") 
    return dict(error=error) 