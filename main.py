from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About')
def about():
    return 'About page'

@app.route('/Contact')
def contact():
    return 'Contact Page'

if __name__ == '__main__':
    app.run(debug=True)
