from flask import Flask, render_template

# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Index page (now using the index.html file)
@app.route('/')  #Mainpage
def index():
    return render_template('index.html')


@app.route('/FAQ/')  #FAQ page
def FAQ():
    return render_template('FAQ.html')


@app.route('/about/')  #About me page
def about():
    return render_template('about.html')


@app.route('/cart/')  #Cart page
def cart():
    return render_template('cart.html')


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)

    # To open website localhost:8080
