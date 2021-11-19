from flask import Flask, render_template

# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Index page (now using the index.html file)
@app.route('/')  #Mainpage
def index():
    return render_template('index.html')


@app.route('/shop/')  #Shop page
def shop():
    return render_template('shop.html')


@app.route('/about-me/')  #About me page
def aboutme():
    return render_template('aboutme.html')


@app.route('/cart/')  #Cart page
def cart():
    return render_template('cart.html')


@app.route('/shop/item/')  #Item page
def item():
    return render_template('item.html')


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)

    # To open website localhost:8080
