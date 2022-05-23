from setup import db, app

class Person(db.Model):
     __tablename__ = "persons"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(), nullable=False)
   
with app.app_context():
 db.drop_all()
 db.create_all()    
 db.session.commit()