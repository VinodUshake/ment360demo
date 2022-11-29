
from flask import Flask
import os
PORT = os.environ.get("PORT",5000)

server = Flask(__name__)

@server.route("/home",methods=["GET"])
def home():
    return {"message":"Hello world!"}
@server.route("/contact",methods=["GET"])
def home():
    return {"message":"Welcome Ment360!"}


@server.route("/",methods=["GET"])
def root():
    return {"message":"You are on root page"}

# if __name__ == "__main__" :
server.run("0.0.0.0",PORT)
