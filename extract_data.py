import sqlite3
import xlrd


con = sqlite3.connect('sepomex.db')
curs = con.cursor()

'''
Elimina las tablas a usar por si llegaran a existir
'''
curs.execute("""DROP TABLE IF EXISTS estados""")
curs.execute("""DROP TABLE IF EXISTS municipios""")
curs.execute("""DROP TABLE IF EXISTS tempo""")
curs.execute("""DROP TABLE IF EXISTS colonias""")

'''
Crea las tablas que se usaran, estan relacionadas por el c_estado, que es el ID de cada estado
'''
curs.execute(
    """CREATE TABLE IF NOT EXISTS estados 
    (id INTEGER PRIMARY KEY NOT NULL , nombre_estado TEXT NOT NULL, capital TEXT);""")
curs.execute(
    """CREATE TABLE IF NOT EXISTS municipios
(nombre_municipio TEXT,id_estado INTEGER,FOREIGN KEY (id_estado) REFERENCES estados(id));""")
curs.execute(
    """CREATE TABLE IF NOT EXISTS colonias
    (codigo_postal TEXT, nombre_colonia TEXT, tipo_colonia TEXT, tipo_zona TEXT, id_estado INTEGER,
     FOREIGN KEY (id_estado) REFERENCES estados(id));
    """
)
sepomex_wb = xlrd.open_workbook("source/CPdescarga.xls")


def cargar_estados(book):
    '''
    Esta funcion se encarga de leer el libro, recorrer cada hoja y extrar nombre de cada estado asi como su capital y su id
    '''
    for index in range(1, book.sheet_names().__len__()):
        sheet = book.sheet_by_index(index)
        data_estado = []
        for i in [4, 5, 7]:
            data_estado.append(sheet.row(1)[i].value)
        curs.execute("""INSERT INTO estados (nombre_estado, capital, id) VALUES (?, ?, ?);""", data_estado)


def cargar_municipios(book):
    '''
    Esta funcion se encarga de leer el libro, recorrer y acceder cada estado para obtener sus colomunas y extrar mucipios y el id del estado
    '''
    for index in range(1, book.sheet_names().__len__()):
        sheet = book.sheet_by_index(index)
        for index_row in range(1, sheet.nrows):
            row = sheet.row(index_row)
            data = []
            for index_data in [3, 7]:
                data.append(row[index_data].value
            curs.execute("""INSERT INTO municipios (nombre_municipio, id_estado) VALUES (?, ?);""", data)
    curs.execute("""
              CREATE TABLE tempo(nombre_municipio TEXT, id_estado INTEGER, FOREIGN KEY (id_estado) REFERENCES estados(id));""")
    curs.execute("""INSERT INTO tempo
      SELECT DISTINCT nombre_municipio as nombre_municipio, id_estado FROM municipios;""")
    curs.execute("""DROP TABLE municipios;""")
    curs.execute("""ALTER TABLE tempo RENAME TO municipios;""")


def cargar_colonias(book):
    '''
    Esta funcion se encarga de cargar un libro, recorrer todas las hojas y acceder a ellas para extrar codigo postal,
    nombre de colonia, tipo de colonia, id estado y tipo de zona
    '''
    for index in range(1, book.sheet_names().__len__()):
        sheet = book.sheet_by_index(index)
        for index_row in range(1, sheet.nrows):
            row = sheet.row(index_row)
            data = []
            for index_data in [0, 1, 2, 7, 13]:
                data.append(row[index_data].value)
            curs.execute("""INSERT INTO colonias 
            (codigo_postal, nombre_colonia, tipo_colonia, id_estado, tipo_zona) VALUES (?, ?, ?, ?, ?);""", data)


cargar_estados(sepomex_wb)
cargar_municipios(sepomex_wb)
cargar_colonias(sepomex_wb)
con.commit() #Para guardar los datos en la DB.

