from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/<404>')
def 404(404):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
