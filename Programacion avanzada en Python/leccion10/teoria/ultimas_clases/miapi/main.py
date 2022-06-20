from crypt import methods
from flask import Flask,jsonify, request
import personas_controlador
from db import create_db

app = Flask(__name__)

@app.route('/personas',methods=["GET"])
def get_people():
    people = personas_controlador.get_people()
    print(people)
    return jsonify(people)

@app.route('/persona',methods=['POST'])
def insert_person():
    person_data = request.get_json()
    nombre = person_data["nombre"]
    edad = person_data["edad"]
    salario = person_data["salario"]
    result = personas_controlador.insert_person(nombre,edad,salario)
    return jsonify(result)


if __name__ == "__main__":
    create_db()
    app.run(host='0.0.0.0',port=8000,debug=True)