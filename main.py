from config import Config, db
from flask import Flask
from views import init_views
from models import User








def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    init_views(app)
    return app

app = create_app()





print("works")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
