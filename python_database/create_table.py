import sys 
import mysql.connector

def main():
   try:
       # membuat objek koneksi
       koneksi = mysql.connector.connect(
           user = 'Ridz-data',
           password = 'tokisaki123',
           host = 'Localhost',
           database = 'belajardb'
       )
       
       try:
           
       #membuat objek kursor/cursor
            cur = koneksi.cursor()
            
            statement_ddl = '''
            CREATE TABLE BUKU (
                KODE CHAR(6) NOT NULL PRIMARY KEY,
                JUDUL VARCHAR(50),
                PENERBIT VARCHAR(50),
                TAHUN_TERBIT INTEGER,
                HARGA INTEGER
            )
            '''
            # eksekusi statemen ddl
            cur.execute(statement_ddl)
            
       except:
           print('Tabel sql gagal dibuat')

       else :
           print('Tabel berhasil dibuat')
       
   except mysql.connector.Error as e:
       print('Error :', e)
    
   else:
       print('koneksi berhasil')
       # menutup koneksi
       koneksi.close()

if __name__ == "__main__":
    main()