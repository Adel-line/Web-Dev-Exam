from bottle import get, request, view

#########################

@get("/admin_login")
@view("admin_login")

def _(): 
    error = request.params.get("error") 
    
    return dict(error=error) 