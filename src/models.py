from flask_sqlalchemy import SQLAlchemy

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


    favorites = db.relationship('Favorite', backref='users')

    def __repr__(self):
        return '<User %r>' % self.username

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
    height = db.Column(db.Integer, unique=False, nullable= False)
    mass = db.Column(db.Integer, unique=False, nullable= False)

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
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'), nullable=False)

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
    

# Va a albergar tanto favoritos de Planets como de People
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
   
    #TODO: Tendreis que establecer esta relacion con la tabla People
    #people_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)

    planet = db.relationship('Planet')

    def __repr__(self):
        return f'<Favorite {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'planet': self.planet.serialize() if self.planet else None,
        }


        