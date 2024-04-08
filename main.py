from flask import Flask, render_template, request, flash


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/products")
def products_page():
    return render_template("products.html")

@app.route("/product/<item_id>")
def product_page(item_id):

    return render_template("product.html")

if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python main.py
"""