from flask import Flask, render_template

app = Flask(__name__)

productos = [
    {
        "id": 1,
        "nombre": "Nike Hoodie",
        "precio": 1200,
        "imagen": "img/hoodie.jpg"
    },
    {
        "id": 2,
        "nombre": "Jordan T-Shirt",
        "precio": 850,
        "imagen": "img/shirt.jpg"
    },
    {
        "id": 3,
        "nombre": "Denim Jacket",
        "precio": 1600,
        "imagen": "img/jacket.jpg"
    }
]

@app.route("/")
def inicio():
    return render_template("index.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)