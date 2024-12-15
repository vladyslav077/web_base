from flask import Flask, render_template, request, flash


app = Flask(__name__)
database = [
    (0, "Iphone 15 Pro", "деякий опис", 10, 41000, "Телефон", "img.png"),
    (1, "Iphone 14 Pro", "деякий опис2", 15, 40000, "Телефон", "img_1.png"),
]

a = [43, 12, 32]
print(a[0])
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", products=database)

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/products")
def products_page():
    return render_template("products.html", items=database)

@app.route("/product/<item_id>")
def product_page(item_id):
    print(item_id)
    return render_template("product.html", item=database[int(item_id)])

if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python main.py
"""