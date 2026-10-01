from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from config import app_active, app_config

config = app_config[app_active]

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, template_folder="templates")

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def index():
        return "Meu primeiro run."

    @app.route("/login/")
    def login():
        return "Aqui entrará a tela de login."

    @app.route("/recovery-password/")
    def recovery_password():
        return "Aqui entrará a tela de recuperar a senha."

    @app.route("/profile/<int:id>/action/<action>/")
    def profile(id, action):
        if action == "action1":
            return f"Ação {action} do usuário de ID {id}"
        elif action == "action2":
            return f"Ação {action} do usuário de ID {id}"
        elif action == "action3":
            return f"Ação {action} do usuário de ID {id}"

    @app.route("/profile", methods=["POST", "GET"])
    def create_profile():
        # if request.method == "POST":
        #     return "Método POST sendo requisitado"
        # elif request.method == "GET":
        #     return "Método GET sendo requisitado"
        username = request.form["username"]
        password = request.form["password"]

        return f"Essa rota possui um método POST e criará um usuário com os dados de usuário {username} e senha {password}"

    @app.route("/profile/<int:id>", methods=["PUT"])
    def edit_total_profile(id):
        username = request.form["username"]
        password = request.form["password"]

        return f"Essa rota possui um método PUT e editirá o nome do usuário para {username} e a senha para {password}"

    return app
