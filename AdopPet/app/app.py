import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS

from modelos.Usuario import Usuario
from modelos.Mascota import Mascota

from controlles.UsuarioController import UsuarioController
from controlles.MascotaController import MascotaController

#app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
#app = Flask(__name__, template_folder="../templates/")
app = Flask(__name__)
CORS(app) 



#EndPoints Para usuarios
app.route('/usuarios/crear', methods=['POST'])(UsuarioController.crear_usuario)
app.route('/usuarios/validar/<string:email>/<string:contrasenia>', methods = ['GET'])(UsuarioController.validar_usuario)
app.route('/usuarios/obtener/<int:id_usuario>', methods = ['GET'])(UsuarioController.obtener_usuario)
app.route('/usuarios/obtener', methods = ['GET'])(UsuarioController.obtener_usuarios)
app.route('/usuarios/obtener/mascotas/<int:id_usuario>', methods = ['GET'])(UsuarioController.validar_usuario)

#EndPoints Para mascotas
app.route('/mascotas/obtener/perros', methods = ['GET'])(MascotaController.obtener_perros)
app.route('/mascotas/agregar',  methods = ['POST'])(MascotaController.agregar_mascota)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)