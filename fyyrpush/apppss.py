from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:postgres@localhost:5432/hello' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # postgresql+pyscopyg. up it uses it by default
app.config['SQLALCHEMY_ECHO'] =True                                             
db=SQLAlchemy(app)
migrate =Migrate(app,db)

class Person(db.Model):
     __tablename__ = "persons"
     
     id = db.Column(db.Integer, primary_key=True, autoincrement =True)
     name = db.Column(db.String(100), nullable=False)
     
     def __str__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'
   
db.create_all() 
db.session.commit()

   
@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello' + ' ' + person.name
    
    
    
    
if __name__ == "__main__" :
    app.run(debug=True)
   