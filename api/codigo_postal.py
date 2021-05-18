import sqlite3
from flask import Blueprint, jsonify


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


codigo_postal_BP = Blueprint('codigo_postal', __name__)


@codigo_postal_BP.route('/api/cp/', methods=['GET'])
def get_cpall():
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_cp = cur.execute(
        """SELECT codigo_postal FROM colonias""").fetchall()
    return jsonify(all_cp)


@codigo_postal_BP.route('/api/cp/<cp>', methods=['GET'])
def get_cp(cp):
    conn = sqlite3.connect('sepomex.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    one_cp = cur.execute(
        """SELECT
    estados.nombre_estado,
    colonias.codigo_postal,
    colonias.nombre_colonia,
    colonias.tipo_colonia,
    colonias.tipo_zona
    FROM estados
    INNER JOIN colonias ON estados.id = colonias.id_estado
    WHERE codigo_postal = ?""", [cp]).fetchall()
    return jsonify(one_cp)
