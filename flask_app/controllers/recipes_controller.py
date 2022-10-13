from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importamos la clase Message
from flask_app.models.users import User
from flask_app.models.recipes import Recipe

#Importaciones para subir imágenes
from werkzeug.utils import secure_filename
import os


@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session: #comprobamos q se inicio sesion
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    return render_template('new_recipe.html', user=user)

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if 'user_id' not in session: #comprobamos q se inició sesión
        return redirect('/')
    #validamos la receta
    if not Recipe.valida_receta(request.form):
        return redirect('/new/recipe')

    #Validamos que haya subido algo
    if 'image' not in request.files:
        flash('No seleccionó ninguna imagen', 'receta')
        return redirect('/new/recipe') 

    image = request.files['image'] #Variable con imagen

    #Validamos que no este vacío
    if image.filename == '':
        flash('Nombre de imagen vacío', 'receta')
        return redirect('/new/recipe')

    #Generamos de manera segura el nombre de la imagen
    nombre_imagen = secure_filename(image.filename) 

    #Guardamos la imagen
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen))

    #diccionario con los datos del formulario, debemos crearlo pq el form no tiene ese nombre de variable de imagen
    formulario = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_made": request.form['date_made'],
        "under_30": int(request.form['under_30']),
        "image": nombre_imagen,
        "user_id": request.form['user_id']
    }


    #guardamos la receta
    Recipe.save(formulario)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session: #comprobamos q se inicio sesion
        return redirect('/')
    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #quien es el usuario? Recibo la instancia de usuario en base a su ID
    #buscar la receta q se debe desplegar en editar en base al id q recibimos en URL
    formulario_receta={"id":id}
    recipe = Recipe.get_recipe(formulario_receta)
    print(recipe)
    return render_template('edit_recipe.html', user=user, recipe=recipe)

@app.route('/update/recipe', methods=['POST'])
def update_recipe():
    #comprobamos q se inicio sesion
    if 'user_id' not in session: 
        return redirect('/')
    #validar datos correctos
    if not Recipe.valida_receta(request.form):
        #return redirect('/edit/recipe/' + request.form['recipe_id']) #redirige a la edicion de la receta q se está editamdo
        return redirect(f"/edit/recipe/{request.form['recipe_id']}") 
    #guardar cambios
    Recipe.update(request.form)
    #redireccionar a dashboard
    return redirect('/dashboard')

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    #1 comprobamos q se inicio sesion
    if 'user_id' not in session: 
            return redirect('/')
    #2 borramos
    formulario = {"id": id}
    Recipe.delete(formulario)
    # redigir a la pagina principal
    return redirect('/dashboard')

@app.route('/view/recipe/<int:id>')
def view_recipe(id):
    # 1 comprobamos q se inicio sesion
    if 'user_id' not in session: 
            return redirect('/')

    #2 saber cual el nombre del usuario del nombre que inicio sesion
    formulario = {"id": session['user_id']}
    user = User.get_by_id(formulario) #quien es el usuario? Recibo la instancia de usuario en base a su ID

    #3 saber la receta a desplegar
    formulario_receta={"id":id}
    recipe = Recipe.get_recipe(formulario_receta)

    #4 renderizar show_recipe.html
    return render_template('show_recipe.html', user=user, recipe=recipe)
