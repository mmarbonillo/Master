from flask import Flask,render_template

#unix/mac
#export FLASK_APP="app.py"
#export FLASK_ENV="development" #entorno de desarrollo

#windows
#set "FLASK_APP=app.py"
#set "FLASK_ENV=development" #entorno de desarrollo


#crear la aplicación
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html",mensaje="Hello world")

@app.route('/about')
def my_about():
    return "Esta es la página de about"

@app.route("/post/<string:titulo>/")
def mostrar_post(titulo):
    return render_template("post_view.html",post_id=titulo)