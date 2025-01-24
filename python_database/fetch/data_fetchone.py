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
            cur = koneksi.cursor(buffered=True)
            
            statement = '''
            SELECT * FROM BUKU
            '''
            
            cur.execute(statement)
            
            hasil = cur.fetchone()

       except ValueError as e:
           print(f'Data gagal di ditampilkan: {e}')
           koneksi.rollback()
           sys.exit(1)

       else :
           koneksi.commit()
           
           print(hasil)
           print('\nData berhasil di ditampilakan')
           
      
   except mysql.connector.Error as e:
       print('Error :', e)
       
   else:
       # menutup koneksi dan kursor
       cur.close()
       koneksi.close()

if __name__ == "__main__":
    main()  