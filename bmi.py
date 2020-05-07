from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost/height_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)
    weight_=db.Column(db.Integer)

    def __init__(self, email_, height_, weight_):
        self.email_= email_
        self.height_= height_
        self.weight_= weight_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
     email=request.form["email_name"]
     height=request.form["height_name"]
     weight=request.form["weight_name"] 
     if db.session.query(Data).filter(Data.email_==email).count()==0:
         data=Data(email, height, weight)  
         db.session.add(data)
         db.session.commit()
         avg_h=db.session.query(func.avg(Data.height_)).scalar()
         avg_h=round(avg_h)
         avg_w=db.session.query(func.avg(Data.weight_)).scalar()
         avg_w=round(avg_w,2)
         send_email(email, height, weight, avg_h, avg_w)
         return render_template("success.html")

     return render_template('index.html',text="Email Address already exists ! . Please Enter New Email ")
 

if __name__== '__main__':
    app.debug=True
    app.run()    