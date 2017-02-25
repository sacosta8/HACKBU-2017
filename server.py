from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
#Just basic example of home page
def hello_world():
    return current_app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
