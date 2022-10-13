from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask import flash #para mandar mensajes de validación
from datetime import datetime
from flask import jsonify

from flask_bcrypt import Bcrypt # 1ero importamos Bcrypt
# 2do estamos creando un objeto llamado bcrypt,que se realiza invocando la función Bcrypt
# con nuestra aplicación como argumento
bcrypt = Bcrypt(app)

from flask_app.models.users import User
from flask_app.models.recipes import Recipe

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    #validamos la info que recibimos
    if not User.valida_usuario(request.form):
        return redirect('/')
    # generamos la password encryptada
    pwd = bcrypt.generate_password_hash(request.form['password'])
        # poner pw_hash en el diccionario de datos
    #creamos un usuario con los datos del request.form mas la password segura
    formulario = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password" : pwd
    }
    # llama al @classmethod de guardado en Users
    id = User.save(formulario) #recibir el id del nuevo usuario
    # almacenar id de usuario en la sesión
    session['id'] = id  #guardamos en sesion el identificador del usuario
    return redirect("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    #Verificamos que el email exista en la Base de datos
    user = User.get_by_email(request.form) #Recibimos una instancia de usuario O False
    if not user: #Si user = False
        #flash('E-mail no encontrado', 'login')
        #return redirect('/')
        return jsonify(message="Email no encontrado")
    #user es una instancia con todos los datos de mi usuario
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        #flash('Password incorrecto', 'login')
        #return redirect('/')
        return jsonify(message="Password incorrecta")
    session['user_id'] = user.id #se abre session! queda en session y puede ser utilizado en dashboard, por ejemplo
    #return redirect('/dashboard')
    return jsonify(message="correcto")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}
    
    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID
    
    # lista con lass recetas publicadas
    todas_recetas = Recipe.get_all(formulario)
    
    return render_template('muro.html', user=user, recipes=todas_recetas)
    

@app.route('/logout')
def logout():
    session.clear() #cerrar sessión
    return redirect('/')

