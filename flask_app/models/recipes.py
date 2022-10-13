from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.under_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image=data['image'] #agregado para almacenar imagenes en bd

#(left join) 1 propiedades extras - Sender name, reiceiver name --> left join
        self.first_name = data['first_name']

    @staticmethod
    def valida_receta(formulario):
        es_valido = True
        if len(formulario['name']) <3:
            flash('El nombre de la receta debe tener al menos 3 caracteres','receta')
            es_valido = False
        if len(formulario['description']) <3:
            flash('La descripción de la receta debe tener al menos 3 caracteres','receta')
            es_valido = False
        if len(formulario['instructions']) <3:
            flash('Las instrucciones de la receta deben tener al menos 3 caracteres','receta')
            es_valido = False
        if formulario['date_made'] == '':
            flash('Ingrese una fecha de creación de receta','receta')
            es_valido = False
        return es_valido

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO recipes(name, description, instructions, date_made, under_30,user_id, image) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30)s,%(user_id)s, %(image)s)" #interpolacion
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result #regresa el ID de la nueva receta que se ingreso

    @classmethod
    def get_all(cls,formulario):
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id=recipes.user_id;"
        results = connectToMySQL('recetas').query_db(query)
        return results #regresa lista de recetas (diccionarios)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def get_recipe(cls,formulario):
        #formulario = {id:1}
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id=recipes.user_id WHERE recipes.id=%(id)s;"
        result = connectToMySQL('recetas').query_db(query,formulario) #al hacer un select recibimos una lista
        recipe= cls(result[0]) #result[0] = diccionario con todos los datos de la receta; cls() creamos la insyantancia en bd a ese diccionario
        return recipe #regresa la receta q se quiere editar

    @classmethod
    def update(cls, formulario):
        query = "UPDATE recipes SET name = %(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_30=%(under_30)s, image=%(image)s WHERE id=%(recipe_id)s" #recipe_id debe concordar con el formulario
        result = connectToMySQL('recetas').query_db(query,formulario) #al hacer un select recibimos una lista
        return result

    @classmethod
    def delete(cls,formulario):
        #formulario = {id:1}
        query = "DELETE FROM recipes WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query,formulario) #al hacer un select recibimos una lista
        return result
    

