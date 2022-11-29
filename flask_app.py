##requirement python run dependence & making server ready
from flask import Flask
import os
PORT = os.environ.get("PORT",5000)

server = Flask(__name__)

@server.route("/home",methods=["GET"])
def home():
    return {"message":"Hello world!"}
@server.route("/contact",methods=["GET"])
def contact():
    return {"message":"Welcome Ment360!"}

#Main URL Page
@server.route("/",methods=["GET"])
def root():
    return {"message":"Demo Test"}

#Wellcome
server.run("0.0.0.0",PORT)
