from flask import Flask,jsonify,request
from flask.json.tag import JSONTag
from data import data

# creating flask app
app= Flask(__name__)

# 1st route
@app.route("/")
def value():
    return jsonify({
        "data":data,
        "message":"success"
    }),200


@app.route("/planet")
def planet():
    name=request.args.get("name")
    planetname=next(item for item in data if item["name"]== name)
    return jsonify({
        "data":planetname,
        "message":"success"
    }),200

# to run the app
if __name__ == '__main__':
    app.run(debug=True,port=5000,host="localhost")

