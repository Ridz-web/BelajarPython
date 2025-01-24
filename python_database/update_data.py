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
            
            statement_dml = '''
            UPDATE BUKU SET TAHUN_TERBIT = 1992 WHERE KODE = "BK03"
            '''
            
            cur.execute(statement_dml)

       except mysql.connector.DatabaseError as e:
           print(f'Data gagal di update: {e}')
           koneksi.rollback()
           sys.exit(1)

       else :
           koneksi.commit()
           print('Data berhasil di update')
           
      
   except mysql.connector.Error as e:
       print('Error :', e)
       
   else:
       print('koneksi berhasil')
       # menutup koneksi dan kursor
       cur.close()
       koneksi.close()

if __name__ == "__main__":
    main()