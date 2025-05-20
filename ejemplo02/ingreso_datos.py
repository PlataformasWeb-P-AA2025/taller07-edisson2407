from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

#conexion a la base de datos
Session = sessionmaker(bind=engine)
session = Session()

#se lee y guarda los clubes desde el archivo txt.
with open("/home/edisson/Documentos/web/sem07/taller07-edisson2407/ejemplo02/data/datos_clubs.txt", "r", encoding="utf-8") as f:
        for l in f:
                nombre, deporte, fundacion = l.strip().split(";")
                club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
                session.add(club)
session.commit() #cconfirmacion de cambios para que los clubes esten disponibles

#se traen todos los clubes para relacionarlos con los jugadores
clubes = {c.nombre: c for c in session.query(Club).all()}

with open("/home/edisson/Documentos/web/sem07/taller07-edisson2407/ejemplo02/data/datos_jugadores.txt", "r", encoding="utf-8") as f:
        for l in f:
                try:
                        club_nombre, posicion, dorsal, nombre = l.strip().split(";")
                        jugador = Jugador (
                                nombre=nombre,
                                dorsal=int(dorsal),
                                posicion=posicion,
                                club=clubes[club_nombre] #uso del nombre del club como llave
                                )
                        session.add(jugador)
                except:
                        pass


# se confirma las transacciones
session.commit()
