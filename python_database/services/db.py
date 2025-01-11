import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'Ridz-data', 
    password = 'tokisaki123',
    database = 'mini_market'
)

def insert_item(kode_barang, nama_barang, stok_barang, harga_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, stok_barang, harga_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, stok_barang, harga_barang))
    db.commit()
    
    if cursor.rowcount > 0:
        print("Data berhasil ditambahkan")
    else:
        print("Data gagal ditambahkan")
        
def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()
