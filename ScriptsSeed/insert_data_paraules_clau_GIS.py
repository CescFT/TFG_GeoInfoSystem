import MySQLdb

datos = ['localhost', 'root', '', 'GIS_DB']
conn = MySQLdb.connect(*datos)
conn.set_character_set('utf8')
cursor = conn.cursor()
cursor.execute("SET NAMES UTF8;")

# Per si mai haig de tornar a executar, aquestes fer-les de forma manual a la db
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Latitud','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('longitud','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('punt','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Punt','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Punts','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('punts','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('interès','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Sistema','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('sistema','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Informació','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('informació','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Geogràfica','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('geogràfica','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Motor','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('motor','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Importació','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('importació','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Dades','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('dades','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Nom','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Usuari','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('local','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('locals','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('GIS','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('sistema GIS','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('mapa','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Mapa','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Nom del local','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Categoria','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Superfície','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Província','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Localitat','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Estat de Conservació','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Any de Construcció','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Fotografia del local','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Actiu','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Coordenades','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Descripció','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Localització','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Insereix foto del local','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Treball Fi de Grau','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Informació Geogràfica','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Informació específica del local','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Nous Punts','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Dades Importades','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Contrasenya','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Correu electrònic','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Nom','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Cognom','ca')")
conn.commit()
cursor.execute("INSERT INTO geoinfosystem_paraulesclaugis (paraula, idioma) VALUES ('Inicia la sessió','ca')")
conn.commit()