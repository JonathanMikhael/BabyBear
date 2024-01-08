from flask import Flask, render_template, request, redirect, session, url_for
import sys

import secrets
from flask_mail import Mail, Message

import os

from model import Database

def currency_format(value):
    try:
        value = int(value)
    except ValueError:
        return value
    return "{:,.0f}".format(value)


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
app.jinja_env.filters['currency_format'] = currency_format

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
                    return redirect('/login')
                else:
                    return redirect('/register')
            else:
                return redirect('/register')
        else:
            return redirect('/register')

    return render_template('register.html', daftaractive=True)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
        if request.method == "POST":
            data = request.form

            return render_template('contact.html', data=data)
        return render_template('contact.html', conactive=True)

@app.route('/aboutus')
def aboutus():
        return render_template('aboutus.html', aboutactive=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if db.checklogin(request.form):
            session['username'] = request.form['username']
            session['role'] = db.checkRole(request.form)
            return redirect('/admin')
        else:
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
        return redirect('/')
    else:
        if session['role'] != "admin":
            return redirect('/')
        else:
            if request.method == 'POST':
                file = request.files['gambar']
                filename = save(file)

                if db.insert(request.form, filename):
                    save(request.files['gambar'])
                    return redirect('/admin')
                else:
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
    if session['role'] != "admin":
        return redirect('/')
    else:
        session['idProduct'] = idProduct
        return redirect('/halamanedit')

@app.route('/halamanedit', methods = ['GET', 'POST'])
def halamanedit():
    if session['role'] != "admin":
        return redirect('/')
    else:
        idProduct = session['idProduct']
        data = db.read(idProduct)
        if request.method == 'POST':
            if db.edit(idProduct, request.form):
                session.pop('idProduct', None)
                return redirect('/admin')
            else:
                return redirect('/admin')
        return render_template('edit.html', data=data)



@app.route('/product/<int:idProduct>')
def product(idProduct):
        session['idProduct'] = idProduct
        return redirect('/productpage')

@app.route('/productpage', methods = ['GET', 'POST'])
def productpage():
    idProduct = session['idProduct']
    data = db.read(idProduct)
    if request.method == 'POST':
        if session.get('role') != "user" and session.get('role') == None:
            return redirect('/login')
        else:
            if db.buy(idProduct, request.form):
                session.pop('idProduct', None)
                return redirect('/')
            else:
                return redirect('/')
    return render_template('halamanproduk.html', data=data)

@app.route('/hapus/<int:idProduct>')
def hapus(idProduct):
    if session['role'] != "admin":
        return redirect('/')
    else:
        if db.delete(idProduct):
            return redirect('/admin')
        else:
            return redirect('/admin')

@app.route('/admin')
def dataproduk():
    if session['role'] != "admin":
        return redirect('/')
    else:
        data = db.read(None)

        return render_template('dataproduk.html', dpactive = True, data=data)

@app.route('/order', methods=['GET', 'POST'])
def dataorder():
    if session['role'] != "admin":
        return redirect('/')
    else:
        data = db.readOrder(None)

        if request.method == 'POST':
            filterType = request.form['filter']
            categoryType = request.form['filterCategory']
            dateAwal = request.form['dateAwal']
            dateAkhir = request.form['dateAkhir']

            if filterType == 'Category':
                data = db.readCategory(categoryType)
                return render_template('order.html', orderactive = True, data=data)
                
            if filterType == 'Date':
                data = db.readDate(dateAwal, dateAkhir)
                return render_template('order.html', orderactive = True, data=data)

    return render_template('order.html', orderactive = True, data=data)

@app.route('/products')
def about():

    datapacifier = db.readpacifier(None)
    datarides = db.readrides(None)
    datacloth = db.readcloth(None)

    return render_template('products.html', prodactive = True, datapacifier=datapacifier, datarides=datarides, datacloth=datacloth)

@app.route('/email', methods=['GET', 'POST'])
def email():
    if session['role'] != "admin":
        return redirect('/')
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
                return redirect('/email')
            except:
                return redirect('/email')
        return render_template('email.html', emailactive = True, alluser=alluser, emailuser=emailuser)

@app.route('/update_delivery/<int:idOrder>', methods=['GET','POST'])
def updateStatus(idOrder):
    if session['role'] != "admin":
        return redirect('/')
    else:
        session['idOrder'] = idOrder
        return redirect('/update_delivery_status')

@app.route('/update_delivery_status', methods=['GET', 'POST'])
def update_delivery_status():
    if session['role'] != "admin":
        return redirect('/')
    else:
        idOrder = session['idOrder']
        if db.updateDeliveryStatus(idOrder):
            session.pop('idOrder', None)
            return redirect('/order')
        else:
            return redirect('/order')

@app.route('/myorder')
def myorder():
    if 'username' in session:
        username = session['username']
        datamyorder = db.readMyOrder(username)

        return render_template('myorder.html', orderactive = True, datamyorder=datamyorder)
    else:
        return render_template('login.html',)

@app.route('/filter', methods=['GET', 'POST'])
def filterOrder():
    if session['role'] != "admin":
        return redirect('/')
    else:
        filterType = request.form['filter']
        categoryType = request.form['filterCategory']
        dateAwal = request.form['dateAwal']
        dateAkhir = request.form['dateAkhir']

        if request.method == 'POST':
            if filterType == 'Category':
                data = db.readCategory(categoryType)
                return render_template('order.html', orderactive = True, data=data)
            else:
                data = db.readDate(dateAwal, dateAkhir)
                return render_template('order.html', orderactive = True, data=data)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    app.run(debug = True)