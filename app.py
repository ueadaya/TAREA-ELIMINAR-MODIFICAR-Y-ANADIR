from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_connection

app = Flask(__name__)
app.secret_key = "clave_secreta"

# ================== PRODUCTOS ==================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/productos")
def productos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    data = cursor.fetchall()
    conn.close()
    return render_template("productos.html", productos=data)

@app.route("/crear", methods=["GET", "POST"])
def crear_producto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s,%s,%s)", 
                       (nombre, precio, stock))
        conn.commit()
        conn.close()
        flash("Producto creado con éxito")
        return redirect(url_for("productos"))
    return render_template("formulario.html")

@app.route("/editar/<int:id>", methods=["GET","POST"])
def editar_producto(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        cursor.execute("UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id_producto=%s", 
                       (nombre, precio, stock, id))
        conn.commit()
        conn.close()
        flash("Producto actualizado")
        return redirect(url_for("productos"))
    cursor.execute("SELECT * FROM productos WHERE id_producto=%s", (id,))
    producto = cursor.fetchone()
    conn.close()
    return render_template("editar.html", producto=producto)

@app.route("/eliminar/<int:id>")
def eliminar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id_producto=%s", (id,))
    conn.commit()
    conn.close()
    flash("Producto eliminado")
    return redirect(url_for("productos"))

# ================== CLIENTES ==================
@app.route("/clientes")
def clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    data = cursor.fetchall()
    conn.close()
    return render_template("clientes.html", clientes=data)

@app.route("/clientes/crear", methods=["GET", "POST"])
def crear_cliente():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nombre, apellido, correo, telefono) VALUES (%s,%s,%s,%s)",
                       (nombre, apellido, correo, telefono))
        conn.commit()
        conn.close()
        flash("Cliente registrado con éxito")
        return redirect(url_for("clientes"))
    return render_template("form_cliente.html")

@app.route("/clientes/editar/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        cursor.execute("UPDATE clientes SET nombre=%s, apellido=%s, correo=%s, telefono=%s WHERE id_cliente=%s",
                       (nombre, apellido, correo, telefono, id))
        conn.commit()
        conn.close()
        flash("Cliente actualizado")
        return redirect(url_for("clientes"))
    cursor.execute("SELECT * FROM clientes WHERE id_cliente=%s", (id,))
    cliente = cursor.fetchone()
    conn.close()
    return render_template("editar_cliente.html", cliente=cliente)

@app.route("/clientes/eliminar/<int:id>")
def eliminar_cliente(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id,))
    conn.commit()
    conn.close()
    flash("Cliente eliminado")
    return redirect(url_for("clientes"))

# ================== FACTURAS ==================
@app.route("/facturas")
def facturas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT f.id_factura, f.numero_factura, f.fecha, c.nombre, c.apellido FROM facturas f JOIN clientes c ON f.id_cliente = c.id_cliente")
    data = cursor.fetchall()
    conn.close()
    return render_template("facturas.html", facturas=data)

@app.route("/facturas/crear", methods=["GET", "POST"])
def crear_factura():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    if request.method == "POST":
        numero = request.form["numero"]
        fecha = request.form["fecha"]
        cliente = request.form["cliente"]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO facturas (numero_factura, fecha, id_cliente) VALUES (%s,%s,%s)",
                       (numero, fecha, cliente))
        conn.commit()
        conn.close()
        flash("Factura registrada con éxito")
        return redirect(url_for("facturas"))
    conn.close()
    return render_template("form_factura.html", clientes=clientes)

@app.route("/facturas/eliminar/<int:id>")
def eliminar_factura(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM facturas WHERE id_factura=%s", (id,))
    conn.commit()
    conn.close()
    flash("Factura eliminada")
    return redirect(url_for("facturas"))

if __name__ == "__main__":
    app.run(debug=True)
