from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route("/lang")
def check():
    languge=request.args.get("sneha")
    return ' <h1>"Langue is :{}" </h1>'.format(languge)

if __name__ =='__main__':
    app.run(debug=True)