from flask import Flask, render_template, request, flash


app = Flask(__name__)
items = [
    (1, "Браслет", 15, "img.png"),
    (2, "Наліпки", 25, "img_1.png"),
    (3, "Ручки", 25, "img_2.png"),

]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/products")
def products_page():
    return render_template("products.html", items=items)

@app.route("/product/<item_id>")
def product_page(item_id):
    item = items[int(item_id)-1]
    return render_template("product.html", item=item)

if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python app.py
"""