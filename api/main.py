import flask
from routes.codigo_postal import codigo_postal_BP
from routes.estados import estados_BP
from routes.colonias import colonia_BP
from routes.municipios import municipio_BP

import routes

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(codigo_postal_BP)
app.register_blueprint(estados_BP)
app.register_blueprint(colonia_BP)
app.register_blueprint(municipio_BP)

app.run()
