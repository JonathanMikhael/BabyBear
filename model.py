from flask import request
import pymysql
from werkzeug.utils import secure_filename

class Database:
    def connect(self):

        return pymysql.connect(host='localhost', user='root', password='', database='babynbear', charset='utf8mb4')
    
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM products')
            else:
                cursor.execute('SELECT * FROM products where id = %s' ,(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readOrder(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM orders')
            else:
                cursor.execute('SELECT * FROM orders where id = %s' ,(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readpacifier(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM products WHERE kategori="Pacifier"')
            else:
                cursor.execute('SELECT * FROM products where id = %s AND kategori ="Pacifier"' ,(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readrides(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM products WHERE kategori="BabyRides"')
            else:
                cursor.execute('SELECT * FROM products where id = %s AND kategori ="BabyRides"' ,(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readcloth(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM products WHERE kategori="Clothings"')
            else:
                cursor.execute('SELECT * FROM products where id = %s AND kategori ="Clothings"' ,(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data, filename):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            file = request.files['gambar']
            cursor.execute('INSERT INTO products(kategori, gambar, nama_produk, deskripsi, harga_jual) VALUES(%s, %s, %s, %s, %s)',
                    (data['kategori'], filename, data['nama_produk'], data['deskripsi'], data['harga_jual'],))

            con.commit()
            return True
        except Exception as e:
            con.rollback()
            print(e)
            return False
        finally:
            con.close()
    
    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('DELETE FROM products where id = %s', (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def edit(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            file = request.files['gambar']
            cursor.execute('UPDATE products SET kategori = %s, gambar = %s, nama_produk = %s, deskripsi = %s, harga_jual = %s where id = %s',
                                    (data['kategori'], file.filename, data['nama_produk'], data['deskripsi'], data['harga_jual'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def checkuser(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM user where username = %s',(str(data['username']),))
            if len(cursor.fetchall()) == 0:
                return True
            else:
                return False
        except:
            return False
        finally:
            con.close()

    def tambahuser(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('INSERT INTO user(namalengkap, email, username, passwordl, userRole) VALUES(%s, %s, %s, %s, %s)',
                                (data['namalengkap'], data['email'], data['username'], data['password'], "user"))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def checklogin(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM user where username = %s and password = %s',(data['username'],data['password'],))
            if len(cursor.fetchall()) != 0:
                return True
            else:
                return False
        except:
            return False
        finally:
            con.close()

    def checkRole(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT userRole FROM user WHERE username = %s',(data['username'],))
            result = cursor.fetchone()
            return result[0] if result else None
        except:
            return "SQL erorr"
        finally:
            con.close()


    def readuser(self, username):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if username == None:
                cursor.execute('SELECT * FROM user')
            else:
                cursor.execute('SELECT * FROM user WHERE username = %s',(username,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

