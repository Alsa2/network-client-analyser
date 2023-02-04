from flask import Flask, render_template, request, make_response
import datetime

STATIC_FOLDER = 'templates/assets'
app=Flask(__name__, static_folder=STATIC_FOLDER) #initiating flask object

@app.route("/",methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        # checking if there is a agreement cookie
        if request.cookies.get('agreement') == 'yes':
            return render_template("index.html", agreed = True)
        else:
            return render_template("index.html", agreed = False)
    elif request.method == 'POST':
        if request.form['agreement'] == 'on':
            # setting the cookie
            resp = make_response(render_template("index.html", agreed = True))
            resp.set_cookie('agreement', 'yes', expires=datetime.datetime.now() + datetime.timedelta(days=365))
            return resp

@app.route("/cookie",methods = ['POST', 'GET'])
def cookie():
    pass

@app.route("/test", methods = ['POST', 'GET'])
def test():
    if request.method == 'GET':
        return render_template("index.html", agreed = False)
    elif request.method == 'POST':
        return request.form['agreement']

@app.route("/test2", methods = ['POST', 'GET'])
def test2():
    if request.method == 'GET':
        return  request.cookies.get('agreement')





if __name__ == "__main__":
    app.debug=True #setting the debugging option for the application instance
    app.run(host='0.0.0.0', port=80) #launching the flask's integrated development webserver