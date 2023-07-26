from flask import Flask
from app.routes import contacts_blueprint

app = Flask(__name__)

app.register_blueprint(contacts_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
