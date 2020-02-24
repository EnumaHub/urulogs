from flask import Flask
import pymongo

def create_app():
	conn = pymongo.MongoClient(
            'localhost',
            27017
        )

	app = Flask(__name__, static_url_path="/static", static_folder='static')
	app.register_blueprint(errors)

	return app