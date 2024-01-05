from flask import Flask, render_template, request, flash, redirect, session, url_for
import sys

import secrets
from flask_mail import Mail, Message

import os

from model import Database

app = Flask(__name__)

UPLOAD_FOLDER = 'static/img'
ROWS_PER_PAGE = 5

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.secret_key = '@#$123456&*()'
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = Database()

@app.route('/')
def index():
    return render_template('index.html', homeactive=True)

@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form['password'] == request.form['konfirmasi']:
            if db.checkuser(request.form):
                if db.tambahuser(request.form):
                    flash('Data Berhasil Disimpan. Silahkan Anda Login.')
                    return redirect('/login')
                else:
                    flash('Data Gagal Disimpan. Ulangi lagi')
                    return redirect('/register')
            else:
                flash('Username yang dimasukkan sudah terdaftar, coba buat username lain')
                return redirect('/register')
        else:
            flash('Password yang dimasukkan tidak match')
            return redirect('/register')

    return render_template('register.html', daftaractive=True)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
        if request.method == "POST":
            data = request.form

            return render_template('contact.html', data=data)
        return render_template('contact.html', conactive=True)

@app.route('/aboutus')
def skating():
        return render_template('aboutus.html', aboutactive=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if db.checklogin(request.form):
            session['username'] = request.form['username']
            session['role'] = db.checkRole(request.form)
            return redirect('/admin')
        else:
            flash('Username dan Password salah')
            return redirect('/login')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect('/')
    
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/insert', methods=['GET', 'POST'])
def insert_data():
    if session['role'] != "admin":
        return render_template('index.html',)
    else:
        if request.method == 'POST':
            file = request.files['gambar']
            filename = save(file)

            if db.insert(request.form, filename):
                flash('Image successfully added into the database')
                save(request.files['gambar'])
                return redirect('/admin')
            else:
                flash('Image Failed to be added into the database')
                return redirect('/admin')
        else:
            return render_template('insert.html', manageactive = True)

@app.route('/save')
def save(file):
    hash_photo = secrets.token_urlsafe(10)
    _, file_extension = os.path.splitext(file.filename)
    filename = hash_photo + file_extension
    file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    file.save(file_path)
    return filename

@app.route('/edit/<int:idProduct>')
def edit(idProduct):
    session['idProduct'] = idProduct
    return redirect('/halamanedit')
    

@app.route('/halamanedit', methods = ['GET', 'POST'])
def halamanedit():
    idProduct = session['idProduct']
    data = db.read(idProduct)
    if request.method == 'POST':
        if db.edit(idProduct, request.form):
            flash('Data Berhasil Diubah')
            session.pop('idProduct', None)
            return redirect('/admin')
        else:
            flash('Data Gagal Diupdate')
            return redirect('/admin')
    return render_template('edit.html', data=data)

@app.route('/hapus/<int:idProduct>')
def hapus(idProduct):
    if db.delete(idProduct):
        flash('Data Berhasil Dihapus')
        return redirect('/admin')
    else:
        flash('Data Gagal Dihapus')
        return redirect('/admin')

@app.route('/admin')
def dataproduk():
    if session['role'] != "admin":
        return render_template('index.html',)
    else:
        data = db.read(None)

        return render_template('dataproduk.html', dpactive = True, data=data)

@app.route('/order')
def dataorder():
    if session['role'] != "admin":
        return render_template('index.html',)
    else:
        data = db.readOrder(None)

        return render_template('order.html', dpactive = True, data=data)

@app.route('/products')
def about():

    datapacifier = db.readpacifier(None)
    datarides = db.readrides(None)
    datacloth = db.readcloth(None)

    return render_template('products.html', prodactive = True, datapacifier=datapacifier, datarides=datarides, datacloth=datacloth)

@app.route('/email', methods=['GET', 'POST'])
def email():
    if session['role'] != "admin":
        return render_template('index.html',)
    else:
        alluser = db.readuser(None)
        
        emailuser = db.readuser(session['username'])
        if request.method == 'POST':
            email = request.form['email']
            apppassword = request.form['apppassword']
            to = request.form['emailkepada']
            subject = request.form['subject']
            emailmessage = request.form['emailmessage']
            app.config['MAIL_USERNAME'] = email
            app.config['MAIL_PASSWORD'] = apppassword
            if to == 'all':
                allemail=[]
                for i in alluser:
                    allemail.append(i[1])
                emailmessages = Message(subject, sender=email, recipients=allemail)
                emailmessages.body = emailmessage
            else:
                emailmessages = Message(subject, sender=email, recipients=[to])
                emailmessages.body = emailmessage
            try:
                mail = Mail(app)
                mail.connect()
                mail.send(emailmessages)
                flash('Email Berhasil Dikirim ke '+ to)
                return redirect('/email')
            except:
                flash('Email Gagal Dikirim ke '+ to)
                return redirect('/email')
        return render_template('email.html', emailactive = True, alluser=alluser, emailuser=emailuser)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    app.run(debug = True)