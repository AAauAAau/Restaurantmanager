
from Restaurant import db


class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    menuItems = db.relationship('MenuItem', backref='restaurant', lazy=True)

    def __repr__(self):
        return f"Restaurant('{self.name}','{self.id}')"


class MenuItem(db.Model):

    name = db.Column(db.String(20), unique=False, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurant.id'), nullable=False)

    def __repr__(self):
        return f"MenuItem('{self.name}', '{self.description}', '{self.id}', '{self.price}','{self.course}')"
