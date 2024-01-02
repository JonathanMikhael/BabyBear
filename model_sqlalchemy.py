from email.policy import default
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    namalengkap = db.Column(db.String(50))
    email = db.Column(db.String(50))
    username = db.Column(db.String(25), primary_key = True)
    password = db.Column(db.String(30))

    def __init__(self, namalengkap, email, username, password):
        self.namalengkap = namalengkap
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '[%s,%s,%s, %s]' % \
            (self.namalengkap, self.email, self.username, self.password)

class Products(db.Model):
    id = db.Column(db.String(50), primary_key = True)
    kategori = db.Column(db.String(25))
    gambar = db.Column(db.String(255), default='image.jpg')
    nama_produk = db.Column(db.String(255))
    deskripsi = db.Column(db.Text)
    harga_jual = db.Column(db.Integer)

    def __init__(self, kategori, gambar, nama_produk, deskripsi, harga_jual):
        self.kategori = kategori
        self.gambar = gambar
        self.nama_produk = nama_produk
        self.deskripsi = deskripsi
        self.harga_jual = harga_jual

    def __repr__(self):
        return '[%s,%s,%s,%s,%s]' % \
            (self.kategori, self.gambar, self.nama_produk, self.deskripsi, self.harga_jual)