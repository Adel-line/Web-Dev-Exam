from bottle import run, get, post, view, static_file, request, redirect, default_app

######################################################

import login_get
import login_post
import logout_get
import signup_get
import signup_post
import admin_panel_get
import tweets_feed_get
import add_tweet_post
import delete_tweet
import global_users_get
import admin_login_get
import admin_login_post
import admin_panel_get
import tweet_update_put
import follow_user_post
import send_email
######################################################

######################################################

@get("/")
@view ("index.html")

def _():
    return

######################################################
@get("/images/one.png")
def _():
    return static_file("one.png", root=".")

######################################################
@get("/validator.js")
def _():
    return static_file("validator.js", root=".")

######################################################
@get("/app.js")
def _():
    return static_file("app.js", root=".")

######################################################
@get("/app.css")

def _():
    return static_file("app.css", root=".")
##########################################################
@get("/images/<image>")
def _(image):
    return static_file(image, root="./images")
#####################################

try:
    import production
    application = default_app()
except Exception as ex:
    print("Server running on development")
    run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")
