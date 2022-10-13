from flask import Flask


app = Flask(__name__) #inicializamos la app



#declarar la llave secreta, aqui usaremos session..por lo que se requiere declarar la key secreta
app.secret_key="bootcamp"

app.config['UPLOAD_FOLDER'] = 'flask_app/static/img'