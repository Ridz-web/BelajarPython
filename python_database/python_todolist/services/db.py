import mysql.connector
from datetime import date

# membuat objek koneksi
koneksi = mysql.connector.connect(
    user = 'Ridz-data',
    password = 'tokisaki123',
    host = 'Localhost',
    database = 'belajardb'
)
def add_list(id_list, todolist, tanggal):
    cur = koneksi.cursor()
    cur.execute('INSERT INTO todolist (id_list, todolist, tanggal) VALUES (%s, %s, %s)', (id_list, todolist, tanggal))
    koneksi.commit()
    
    if cur.rowcount > 0:
        print("Data berhasil ditambahkan")
    else:
        print("Data gagal ditambahkan")
        

def remove_list(id_list):
    cur = koneksi.cursor()
    cur.execute('DELETE FROM todolist WHERE id_list = %s', (id_list,))
    koneksi.commit()
    
    if cur.rowcount > 0:
        print("Data berhasil dihapus")
    else:
        print("Data gagal dihapus")
        


def fetch_item():
    cur = koneksi.cursor()
    cur.execute('SELECT * FROM todolist')
    return cur.fetchall()

