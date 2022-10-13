from flask_app import app 
from time import gmtime, strftime

#importacion controllers para poder usar las rutas
from flask_app.controllers import users_controller
from flask_app.controllers import recipes_controller


if __name__== "__main__": #ejecución del programa
    app.run(debug=True)