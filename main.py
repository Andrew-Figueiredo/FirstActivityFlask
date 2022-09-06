from flask import Flask, render_template

app = Flask(__name__)


# Página Principal
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/result')
def equal():
    return 'page result'


app.run(host='0.0.0.0', port=81)
