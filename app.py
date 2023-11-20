from flask import Flask
from modules.categoria.controller import categoria_controller
from modules.marca.controller import marca_controller
from modules.produto.controller import produto_controller
from service.connect import Connect

app = Flask(__name__)
app.register_blueprint(marca_controller)
app.register_blueprint(categoria_controller)
app.register_blueprint(produto_controller)
Connect().init_database('v2')
app.run(debug=True)
