#!flask/bin/python
from flask import Flask

# This gets static pages
app = Flask(__name__,
            static_url_path='',
            static_folder='../')

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__' :
    app.run(debug= True)


# From this we can see that the forward slash will return hello world 
