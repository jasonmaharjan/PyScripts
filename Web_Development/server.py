from flask import Flask, render_template
app = Flask(__name__)         # __name__ is set to __main__

# create 'templates' folder for html and 'static' folder for css and js
@app.route('/')
def hello_world():
   return render_template('index.html')

