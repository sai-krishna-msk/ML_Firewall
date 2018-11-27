import flask
from flask import Flask
from flask import Flask, render_template,  request
from flask_uploads import UploadSet, configure_uploads, ALL
import os
import sqlite3
import simplejson
import query as q


app =Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/read"  , methods=["GET" , "POST"])
def read():
    if(request.method=="GET"):
        return "Server is working but this link is funcitonal for only post request"

    if(request.method=="POST"):
        query = request.form["query"]
        result =q.fetchContent(query)
        return simplejson.dumps(result)


@app.route("/write" , methods=["GET", "POST"])
def write():
        if(request.method=="GET"):
            return "Server is working but this link is funcitonal for only post request"

        if(request.method=="POST"):
            query = request.form["query"]
            result =q.writeContent(query)
            return simplejson.dumps(result)



@app.route("/update" , methods=["GET", "POST"])
def update():
    if(request.method=="GET"):
        return "Server is working but this link is funcitonal for only post request"

    if(request.method=="POST"):
        query = request.form["query"]
        result =q.updateContent(query)

        return simplejson.dumps(result)



@app.route("/delete" , methods=["GET", "POST"])
def delete():
    if(request.method=="GET"):
        return "Server is working but this link is funcitonal for only post request"

    if(request.method=="POST"):
        query = request.form["query"]
        result =q.deleteContent(query)

        return simplejson.dumps(result)






if __name__ == "__main__":
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'college.db')
    sqlite3.connect(DATABASE_PATH)
    
    #app.run(host='0.0.0.0', port=80, debug=True)
    app.run(debug=True)
