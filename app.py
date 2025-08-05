from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/menu">메뉴로 이동</a>'

@app.route('/menu')


if __name__ == '__main__':
    app.run(debug=True)