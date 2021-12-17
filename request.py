from flask import Flask,jsonify,request
# create the Flask app
app = Flask(__name__)

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    framework= request.args.get("framework")
    return '''<h1>The language value is: {}</h1>
    <h1>The Framework value is: {}</h1>
    
    '''.format(language,framework)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

    # query-example?language=Python