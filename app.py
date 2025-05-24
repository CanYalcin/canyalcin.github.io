from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/projects.html')
def more():
    return render_template('projects.html')

@app.route('/vrdevelopment.html')
def vrdev():
    return render_template('vrdevelopment.html')

@app.route('/gamedevelopment.html')
def gamedev():
    return render_template('gamedevelopment.html')

@app.route('/aimusic.html')
def aimusic():
    return render_template('aimusic.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/privacy.html')
def privacy():
    return render_template('/privacy.html')

@app.route('/terms.html')
def terms():
    return render_template('/terms.html')

if __name__ == '__main__':
    freezer.freeze()