from flask_app import app
from flask_app.controllers.user_controller import User


if __name__=="__main__":
    app.run(debug=True)