from flask import Flask
app = Flask(__name__)         # __name__ is set to __main__
print(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'