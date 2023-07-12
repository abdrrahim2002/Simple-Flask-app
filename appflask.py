from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/page2')
def lol():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')