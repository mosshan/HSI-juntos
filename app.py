# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('signin.html')  # return a string


@app.route('/signin', methods=['GET'])
def signin():
    error = None
    return render_template('signin.html')  # render a template


@app.route('/signup')
def signup():
    return render_template('signup.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)