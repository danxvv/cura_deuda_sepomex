import flask
from api.codigo_postal import codigo_postal_BP
from api.estados import estados_BP
from api.colonias import colonia_BP
from api.municipios import municipio_BP

app = flask.Flask(__name__)

app.register_blueprint(codigo_postal_BP)
app.register_blueprint(estados_BP)
app.register_blueprint(colonia_BP)
app.register_blueprint(municipio_BP)

@app.route("/api")
def welcome():
    return """
        <h1>END POINTS</h1>
        
        <p>/api/cp - Nos devuelve todos los codigos postales del pais (tarda un poco en cargar todos)</p>
        <p>/api/cp/{numerocp} - Al poner un codigo postal valido, nos devolvera Codigo Postal - Nombre Colonia - Nombre Estado - Tipo Colonia - Tipo Zona</p>
        <p>/api/estados - Devuelve los estados con su numero de estado y su capital</p>
        <p>/api/estado/{estado} - Busca en los estados si hay alguno que coincida con el endpoint</p>
        <p>/api/municipios - Devuelve los municipios del pais y el estado al que pertencen</p>
        <p>/api/municipio/{municipio} Busca en los municipios si hay alguno que coincida con el endpoint</p>
        <p>/api/colonias/ Devuelve todas las colonias del pais</p>
        <p>/api/colonia/{colonia} Busca en las colonias si hay alguno que coincida con el endpoint</p>
        
    """

@app.after_request
def after_request(response):
    response.headers[
        "Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, " \
                                          "Authorization "
    return response


if __name__ == "__main__":
    app.run(debug=True)
