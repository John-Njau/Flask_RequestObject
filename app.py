from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# connecting our app to the database
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer(), primary_key=True)
    # nullable is same to not null
    first_name = db.Column(db.String(50),unique=True, nullable=False)
    course = db.Column(db.String(30), nullable=False)
    
    
    
class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    
class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), nullable=False)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        addstudent = Student(first_name=form['name'], course=form['course'])
        db.session.add(addstudent)
        db.session.commit()
        return redirect(url_for('display'))
    return render_template ('index.html')

@app.route('/display')
def display():
    data = Student.query.all()
    return render_template('display.html', data=data)
    
if __name__ == '__main__':
    app.run(debug=True)