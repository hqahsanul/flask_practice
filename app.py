import json
from flask import Flask,render_template,jsonify,request
import instaloader

IG = instaloader.Instaloader()


app = Flask(__name__)
IG.login("", "")
IG.save_session()
@app.route("/get-post",methods=["GET"])
def get_post():
    
    result = IG.get_stories(userids=38896206029)
    print(result)
    return jsonify({"msg":'success'}), 201

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/products")
def products():
    return "<p>This is a product page!</p>"

if __name__=="__main__":
    app.run(debug=True)
