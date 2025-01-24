import sys 
import mysql.connector
from tabulate import tabulate

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
            
            statement = '''
            SELECT * FROM BUKU
            '''
            
            cur.execute(statement)
            
            header = ["KODE", "JUDUL", "PENERBIT", "TAHUN_TERBIT", "HARGA"]
            hasil = cur.fetchall()

       except ValueError as e:
           print(f'Data gagal di ditampilkan: {e}')
           koneksi.rollback()
           sys.exit(1)

       else :
           koneksi.commit()
           
           print(tabulate(hasil, headers=header, tablefmt='grid'))
           print('\nData berhasil di ditampilakan')
           
      
   except mysql.connector.Error as e:
       print('Error :', e)
       
   else:
       # menutup koneksi dan kursor
       cur.close()
       koneksi.close()

if __name__ == "__main__":
    main()  