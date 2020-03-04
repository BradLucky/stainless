"""Main Flask entry point."""
from flask import Flask

from general.general import general_bp
from config import Config

from models import init_db


app = Flask(__name__)
app.config.from_object(Config)

# register blueprints
app.register_blueprint(general_bp)

db_session = init_db(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
