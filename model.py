"""Models for melon tasting app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=True)

    #Establishing relationships
    reservations = db.relationship("Reservation", back_populates="users")


class Reservation(db.Model):
    """Reservation Model"""

    __tablename__ = "reservations"

    res_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    res_date = db.Column(db.DateTime, nullable=False)
    res_time = db.Column(db.DateTime, nullable=False)
    
    #Establishing relationships
    users = db.relationship("User", back_populates="reservations")


def connect_to_db(flask_app, db_uri="postgresql:///tasting", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
