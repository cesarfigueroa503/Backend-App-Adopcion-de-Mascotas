from flask import jsonify, request
from psycopg2 import IntegrityError

from modelos.Usuario import Usuario
from modelos.Mascota import Mascota

def toJson(obj):
        return {
            'id_mascota' : obj.id_mascota,
            'nombre' : obj.nombre,
            'raza' :obj.raza,
            'categoria' : obj.categoria,
            'peso' : obj.peso,
            'edad':obj.edad
        }

class MascotaController:

    @staticmethod
    def obtener_perros():
        mascotas = Mascota.select().where(Mascota.categoria=="Perro" or Mascota.categoria=="perro")
        
        result = []
        
        for mascota in mascotas:
            result.append({
                'id_mascota': mascota.id_mascota,
                'nombre': mascota.nombre,
                'peso': mascota.peso,
                'edad': mascota.edad,
                'raza': mascota.raza,
                'categoria': mascota.categoria,
                'id_usuario': mascota.id_usuario_id  # Cambiar a 'id_usuario' si prefieres el nombre del campo
            })

        return jsonify({'mascotas': result})
    
    @staticmethod
    def obtener_gatos():
        mascotas = Mascota.select().where(Mascota.categoria=="Gato" or Mascota.categoria=="gato")
        
        result = []
        
        for mascota in mascotas:
            result.append({
                'id_mascota': mascota.id_mascota,
                'nombre': mascota.nombre,
                'peso': mascota.peso,
                'edad': mascota.edad,
                'raza': mascota.raza,
                'categoria': mascota.categoria,
                'id_usuario': mascota.id_usuario_id  # Cambiar a 'id_usuario' si prefieres el nombre del campo
            })

        return jsonify({'mascotas': result})    
    
    
    @staticmethod
    def adoptar_mascota(id_usuario, id_mascota):
        data = request.get_json()
        id_usuario = data.get("id_usuario")
        id_mascota = data.get("id_mascota")

        try:
            usuario = Usuario.get(Usuario.idusuario == id_usuario)
            mascota = Mascota.get(Mascota.id_mascota == id_mascota)
        except Usuario.DoesNotExist:
            return jsonify({
                "stado":"Error",
                "descripsion": f"No existe el usuario en la base de datos"
                })
        except Mascota.DoesNotExist:
            return jsonify({
                "stado":"Error",
                "descripsion": f"No existe la mascota en la base de datos"
                })


        mascota.id_usuario = usuario

        result = mascota.save()
        print (result)
        return jsonify({
            "stado":"Guardado exitosamente",
            "descripsion": f"Se agrego el usuario {usuario.email} como duenio de la mascota llamada {mascota.name}"
            })

    @staticmethod
    def agregar_mascota():
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no encontrados en la solicitud"}), 400

        nueva_mascota = Mascota(
            nombre=data.get('nombre'),
            peso=data.get('peso'),
            edad=data.get('edad'),
            raza=data.get('raza'),
            categoria=data.get('categoria'),
            dni_usuario = data.get('dni_usuario')
        )

        try:
        # Intentar guardar el nuevo usuario en la base de datos
            nueva_mascota.save()
            
            return jsonify({"status": "Usuario creado exitosamente"}), 200
        except IntegrityError as e:
            # Manejar cualquier excepción que ocurra durante el proceso de guardado
            return jsonify({"error": str(e)}), 500
        

    @staticmethod
    def obtener_mascotas_del_usuario(id_usuario):
        try:
            usuario = Usuario.get(Usuario.idusuario == id_usuario)
        except Usuario.DoesNotExist:
            print("no existe el usuario que solicito")

        mascotas = Mascota.select().where(Mascota.id_usuario == id_usuario)
        result = []
        for mascota in mascotas:
            result.append(toJson(mascota))

        return jsonify({'mascotas': result})
    