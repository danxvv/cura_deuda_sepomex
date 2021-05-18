import sqlite3
from flask import Blueprint, jsonify
from .auth import auth


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


municipio_BP = Blueprint('municipio', __name__)


@municipio_BP.route('/api/municipios', methods=['GET'])
@auth.login_required()
def get_municipios():
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    municipios = cur.execute("""
    SELECT nombre_municipio from municipios;
    """).fetchall()
    return jsonify(municipios)


@municipio_BP.route('/api/municipio/<nombre>', methods=['GET'])
@auth.login_required()
def get_municipio(nombre):
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    name = ''.join([str(elem) for elem in nombre])
    municipio = cur.execute("""
    SELECT municipios.nombre_municipio, estados.nombre_estado
    FROM municipios
    JOIN estados on estados.id = municipios.id_estado
    WHERE municipios.nombre_municipio LIKE ?
    """, ['%' + name + '%']).fetchall()
    return jsonify(municipio)
