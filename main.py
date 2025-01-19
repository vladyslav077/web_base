from flask import Flask, render_template

app = Flask(__name__)

# Список кросівок
products = [
    {"id": 1, "name": "Nike Air Max 90", "price": 6500, "category": "Nike", "description": "Легендарні кросівки з відмінною амортизацією.", "image": "tcross01.jpg"},
    {"id": 2, "name": "Adidas Ultraboost", "price": 7200, "category": "Adidas", "description": "Ідеальні для бігу та активного способу життя.", "image": "tcross02.jpg"},
    {"id": 3, "name": "Puma RS-X", "price": 5800, "category": "Puma", "description": "Стильний вибір для повсякденного носіння.", "image": "tcross03.jpeg"},
    {"id": 4, "name": "Nike Air Force 1", "price": 7000, "category": "Nike", "description": "Класика стилю з 1982 року.", "image": "tcross04.png"},
    {"id": 5, "name": "Adidas NMD_R1", "price": 7500, "category": "Adidas", "description": "Сучасний дизайн і комфорт.", "image": "tcross05.jpg"},
    {"id": 6, "name": "Saucony Progrid Omni 9 Disrupt", "price": 4399, "category": "Saucony", "description": "Стиль та перевага у зручності.", "image": "tcross06.jpg"},
    {"id": 7, "name": "Nike Air Monarch Iv", "price": 3474, "category": "Nike", "description": "Демісезон, Шкіра /Синтетика.", "image": "tcross07.jpg"},
    {"id": 8, "name": "Adidas Originals Campus", "price": 3897, "category": "Nike", "description": "Демісезон, Шкіра /Синтетика.", "image": "tcross08.jpg"},
]

# Унікальні категорії
categories = list(set(product["category"] for product in products))

@app.route("/")
def index():
    """Головна сторінка з переліком усіх товарів."""
    return render_template("index.html", products=products, categories=categories, site_name="KRASTY CROSS")

@app.route("/product/<int:product_id>")
def product(product_id):
    """Сторінка з детальною інформацією про продукт."""
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template("product.html", product=product, categories=categories, site_name="KRASTY CROSS")

@app.route("/purchase/<int:product_id>")
def purchase(product_id):
    """Обробка покупки товару."""
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return f"<h1>Дякуємо за покупку! Ви купили: {product['name']} за {product['price']} грн!</h1>"

@app.route("/category/<string:category_name>")
def category(category_name):
    """Сторінка категорії з товарами, що належать до неї."""
    filtered_products = [p for p in products if p["category"] == category_name]
    return render_template(
        "category.html",
        products=filtered_products,
        category_name=category_name,
        categories=categories,
        site_name="KRASTY CROSS"
    )

if __name__ == "__main__":
    app.run(debug=True)