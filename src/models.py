from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    coordinate_center_x = db.Column(db.Float, nullable=False)
    coordinate_center_y = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Galaxy %r>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,

        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(240))
    population = db.Column(db.Integer, default=0)

    # OBLIGATORIO para establecer la relación
    galaxy_id = db.Column(db.Integer, db.ForeignKey(
        'galaxy.id'), nullable=False)

    # OPCIONAL para poder acceder a los campos del planeta relacionado
    galaxy = db.relationship('Galaxy')

    def __repr__(self):
        return '<Planet %r>' % self.name
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "population": self.population,
            
        }
    




class FavoritePlanet(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False, primary_key=True)
    insertion_date = db.Column(db.Date, default=datetime.datetime.now())
  
    planet = db.relationship('Planet', backref="favorite_planets")
    user = db.relationship('User', backref="favorite_planets")

    def __repr__(self):
        return f'<Planet {self.user.email} likes {self.planet.planet_name} on date {self.insertion_date}>'
    
class FavoritePeople(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False, primary_key=True)
    insertion_date = db.Column(db.Date, default=datetime.datetime.now())
  
    people = db.relationship('People', backref="favorite_people")
    user = db.relationship('User', backref="favorite_people")

    def __repr__(self):
        return f'<People {self.user.email} likes {self.people.name} on date {self.insertion_date}>'    
