from flask import Flask
app = Flask(_name_)

@app.route('/')
#Just basic example of home page
def hello_world():
    return "Hello, World"

@app.route('/test')
    def dying():
        return "OH MY GOD I'M ALREADY TIRED"
