##requirements python run dependence & making server is  ready
##used Flash requried for  Frame Works to implement  Urls & import
##OS Handshake Window b/w Pycharm
##Port will set URl HTTP from OS get CMD 5000 to use

from flask import Flask
import os
PORT = os.environ.get("PORT",5000)

server = Flask(__name__)

@server.route("/home",methods=["GET"])
def home():
    return {"message":"Hello world!"}
@server.route("/contact",methods=["GET"])

# 1st step displaying after URL's generation main root page
def contact():
    return {"message":"Welcome Ment360!"}

#Main URL Page
@server.route("/",methods=["GET"])
def root():
    return {"message":"Rocks"}

#if click on this port it will run this code
server.run("0.0.0.0",PORT)
