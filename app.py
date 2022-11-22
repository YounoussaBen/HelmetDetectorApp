from flask import Flask, render_template, flash, redirect, url_for, request,session,logging
from flask_mysqldb import MySQL
from werkzeug.utils import redirect
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps


app = Flask(__name__)

# Config Mysql

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mouvement(125)'
app.config['MYSQL_DB'] = 'helmetDetector'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

# User login
@app.route('/',  methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", [username, password])
        account = cur.fetchone()
        if account:
            session['logged_in'] = True
            session['id'] = True
            session['username'] = account['username']
            flash('You are now logged in', 'success') 
            return redirect(url_for('home'))
        else:
            error = 'Incorrect Username Or Password'
            return render_template('login.html', error=error)  

    return render_template('login.html')
            
 
# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


@app.route('/home')
@is_logged_in
def home():
    return render_template('home.html')

@app.route('/dashboard')
@is_logged_in
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM drivers")
    data = cur.fetchall()
    cur.close()

    return render_template('dashboard.html', drivers=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        address = request.form['address']
        dateOfBirth = request.form['DateOfBirth']
        email = request.form['email']
        phone = request.form['phone']
        licensePlateNumber = request.form['licensePlateNumber']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO drivers (name, address, dateOfBirth, email, phone, licensePlateNumber) VALUES (%s, %s, %s, %s, %s, %s)", [name, address, dateOfBirth, email, phone, licensePlateNumber])
        mysql.connection.commit()
        return redirect(url_for('dashboard'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM drivers WHERE id=%s", (id_data,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dashboard'))


@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        address = request.form['address']
        dateOfBirth = request.form['DateOfBirth']
        email = request.form['email']
        phone = request.form['phone']
        licensePlateNumber = request.form['licensePlateNumber']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE drivers SET name=%s, address=%s, dateOfBirth=%s, email=%s, phone=%s, licensePlateNumber=%s
        WHERE id=%s
        """, [name, address, dateOfBirth, email, phone, licensePlateNumber, id_data])
        flash("Data Updated Successfully")
        return redirect(url_for('dashboard'))





if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
