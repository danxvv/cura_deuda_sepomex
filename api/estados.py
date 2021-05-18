import sqlite3
from flask import Blueprint, jsonify


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


estados_BP = Blueprint('estados', __name__)


@estados_BP.route('/api/estados', methods=['GET'])
def get_estados():
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    estado = cur.execute("""
    SELECT nombre_estado from estados;
    """).fetchall()
    return jsonify(estado)


@estados_BP.route('/api/estado/<nombre>', methods=['GET'])
def get_estado(nombre):
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    name = ''.join([str(elem) for elem in nombre])
    estado = cur.execute("""
    SELECT nombre_estado from estados where nombre_estado like ?
    """, ['%' + name + '%']).fetchall()
    return jsonify(estado)
