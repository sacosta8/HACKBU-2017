from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
#Just basic example of home page
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
