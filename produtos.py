from flask import Flask, render_template
from flask import jsonify, request


productos = [
    {"id":"1","nombre":"manzana",
     "cantidad":12},
     {"id":"2","nombre":"pera",
     "cantidad":13},

]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/index.html")


@app.route("/productos", methods = ["GET"])
def getProductos():
    return jsonify(productos)

@app.route("/productos", methods=["POST"])
def postProductos():
    nuevoProducto = request.json
    productos.append(nuevoProducto)
    return "Producto creado correctamente!"


@app.route("/productos/<id>", methods=["DELETE"])
def deleteProductos(id):
    for prod in productos:
        if prod["id"]==id:
            productos.remove(prod)
            return f"Producto con id {id} borrado correctamente"


@app.route("/productos/<id>", methods=["PUT"])
def editProductos(id):
    nuevoProducto = request.json
    for prod in productos:
        if prod["id"] == id:
            idx = productos.index(prod)
            productos[idx] = nuevoProducto
            return "Producto editado correctamente"
    return "Producto no encontrado!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')