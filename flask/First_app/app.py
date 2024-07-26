from flask import Flask, render_template

app = Flask(__name__)


@ app.route('/')
def index():
    introduction = ["TEST", "Address", "example@xxx.com"]
    return render_template('index.html', introduction=introduction)


if __name__ == '__main__':
    app.run(debug=True)
