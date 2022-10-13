from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #para mandar mensajes de validación

import re # importando expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,16}$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def valida_usuario(formulario):
        #formulario es un diccionario con los name del formulario
        es_valido = True
        #validamos que el nombre tiene al menos 3 caracteres
        if len(formulario['first_name'])<3:
            flash('Nombre debe tener al menos 3 caracteres','registro')
            es_valido = False
        #validamos que el nombre tiene al menos 3 caracteres
        if len(formulario['last_name'])<3:
            flash('Apellido debe tener al menos 3 caracteres','registro')
            es_valido = False
        
        #validamos que el password tiene al menos 6 caracteres
        #if len(formulario['password'])<6:
            #flash('Password debe tener al menos 6 caracteres','registro')
            #es_valido = False

        #validamos que el password cumpla el patron
        if not PASS_REGEX.match(formulario['password']):
            flash('Contraseña no válida: La contraseña debe tener al entre 8 y 16 caracteres, al menos un dígito, al menos una minúscula y al menos una mayúscula.', 'registro')
            es_valido = False

        #verificamos que las contraseñas coincidan
        if formulario['password'] != formulario['cpassword']:
            flash('Contraseñas no coinciden','registro')
            es_valido = False

        #validamos formato de email --> expresiones regulares
        if not EMAIL_REGEX.match(formulario['email']):
            flash('Email inválido','registro')
            es_valido = False
            
        #consultamos si existe el correo en la bd
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('recetas').query_db(query,formulario)
        if len(results) >= 1:
            flash('Email registrado previamente','registro')
            es_valido = False
        return es_valido

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO users(first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result #regresa el ID del nuevo registro que se realizó
        
    @classmethod
    def get_by_email(cls, formulario):
        #formulario = {email: elena@codingdojo.com, password: 123}
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('recetas').query_db(query, formulario) #SELECT me regresa una lista
        if len(result) < 1: #Significa que mi lista está vacía, entonces NO existe ese email
            return False
        else:
            #Me regresa una lista con UN registro, correspondiente al usuario de ese email
            #result = [
            #    {id: 1, first_name: elena, last_name:de troya.....} -> POSICION 0
            #]
            user = cls(result[0]) #User( {id: 1, first_name: elena, last_name:de troya.....})
            return user

    @classmethod
    def get_by_id(cls,formulario): #
        #formulario = {id:1}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario)
        user = cls(result[0]) #resul tendra 1 registro, por tanto posicion 0
        return user

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users ORDER BY first_name ASC"
        results = connectToMySQL('recetas').query_db(query) #Regresa una lista de diccionarios
        #results = [
        #   {id: 1, first_name: elena, last_name: de troya........}
        #   {id: 2, first_name: juana, last_name: de arco........}
        #]
        users = []
        for user in results:
            #user = {id: 1, first_name: elena, last_name: de troya........}
            users.append(cls(user)) #1.- cls(user) crea una instancia en base a el diccionario. 2.- users.append Agregando esa instancia a la lista users 
        return users









