from flask import Flask, render_template, Blueprint

app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    return render_template('home.html')

@app.route('/about')
def about():
    # Connecting to a template (html file)
    return render_template('about.html')

@app.route('/home')
def home():
    # Connecting to a template (html file)
    return render_template('home.html')

@app.route('/microgreens_section')
def microgreens_section():
    # Connecting to a template (html file)
    return render_template('home.html #Our microgreens section')


if __name__ == '__main__':
    app.run(debug=True)
