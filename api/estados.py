import sqlite3
from flask import Blueprint, jsonify, request
from .auth import auth


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


estados_BP = Blueprint('estados', __name__)


@estados_BP.route('/api/estados', methods=['GET'])
@auth.login_required()
def get_estados():
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    estado = cur.execute("""
    SELECT nombre_estado, capital from estados;
    """).fetchall()
    return jsonify(estado)


@estados_BP.route('/api/estado/<nombre>', methods=['GET'])
@auth.login_required()
def get_estado(nombre):
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    name = ''.join([str(elem) for elem in nombre])
    estado = cur.execute("""
    SELECT nombre_estado, capital from estados where nombre_estado like ?
    """, ['%' + name + '%']).fetchall()
    return jsonify(estado)


@estados_BP.route('/api/estado', methods=['POST'])
@auth.login_required()
def add_estado():
    datos = request.get_json(force=True)
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    print(datos)
    print(type(datos))
    estado = datos[0]
    capital = datos[1]
    add_datos = cur.execute("""
    INSERT INTO estados (nombre_estado, capital) VALUES (?, ?)
    """, [estado['estado'], capital['capital']])
    conn.commit()
    return jsonify(True)
