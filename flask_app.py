from flask import Flask

app=Flask(__name__)

@app.route('/')
def home ():
    return "<p>New achievements</p>"

if __name__ == '__name__':
    app.run(port=5000,debug=True)