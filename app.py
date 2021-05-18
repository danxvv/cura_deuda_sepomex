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
