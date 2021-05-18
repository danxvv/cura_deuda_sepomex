import sqlite3
from flask import Blueprint, jsonify


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


colonia_BP = Blueprint('colonia', __name__)


@colonia_BP.route('/api/colonias', methods=['GET'])
def get_colonias():
    conn = sqlite3.connect('../example.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    colonia = cur.execute("""
    SELECT colonias.nombre_colonia FROM colonias;
    """).fetchall()
    return jsonify(colonia)


@colonia_BP.route('/api/colonia/<nombre>', methods=['GET'])
def get_colonia(nombre):
    conn = sqlite3.connect('../example.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    name = ''.join([str(elem) for elem in nombre])
    colonia = cur.execute("""
    SELECT colonias.nombre_colonia, estados.nombre_estado
    FROM colonias
    JOIN estados ON estados.id = colonias.id_estado
    WHERE colonias.nombre_colonia LIKE ?
    """, ['%' + name + '%']).fetchall()
    return jsonify(colonia)
