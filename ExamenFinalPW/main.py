from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ""
    total_sin_descuento = 0
    descuento = 0
    total_con_descuento = 0

    if request.method == 'POST':

        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        total_sin_descuento = tarros_pintura * 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

    return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=total_sin_descuento * descuento, total_con_descuento=total_con_descuento)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje_bienvenida = ""

    if request.method == 'POST':

        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'juan' and contrasena == 'admin':
            mensaje_bienvenida = "Bienvenido administrador juan"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje_bienvenida = "Bienvenido usuario pepe"
        else:
            mensaje_bienvenida = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje_bienvenida=mensaje_bienvenida)

if __name__ == '__main__':
    app.run(debug=True)