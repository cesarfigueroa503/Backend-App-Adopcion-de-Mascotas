from flask import jsonify, request
from modelos.Usuario import Usuario
from peewee import IntegrityError

def toJson(obj):
        return {
            'idusuario' : obj.idusuario,
            'nombre' : obj.nombre,
            'apellido' :obj.apellido,
            'email' : obj.email,
            'contrasenia' : obj.contrasenia
        }


class UsuarioController:

    @staticmethod
    def crear_usuario():

        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no encontrados en la solicitud"}), 400

        nuevo_usuario = Usuario(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            email=data.get('email'),
            contrasenia=data.get('contrasenia')     
        )
        #print(nuevo_usuario.save())

        try:
        # Intentar guardar el nuevo usuario en la base de datos
            nuevo_usuario.save()
            
            return jsonify({"status": "Usuario creado exitosamente"}), 200
        except IntegrityError as e:
            # Manejar cualquier excepción que ocurra durante el proceso de guardado
            return jsonify({"error": str(e)}), 500


    @staticmethod
    def validar_usuario(email, contrasenia):
            
        return f"Aqui se validan las credenciales de los usuarios\n{email}\n{contrasenia}"
    
    @staticmethod
    def obtener_usuario(id_usuario):
        result = Usuario.get(Usuario.idusuario == id_usuario)
        result = toJson(result)
        return jsonify(result), 200
    
    @staticmethod
    def obtener_usuarios():
        result=[]
        usuarios = Usuario.select()

        for usuario in usuarios:
            result.append(toJson(usuario))

        return jsonify({'usuarios' : result }), 200
    
    
    
    