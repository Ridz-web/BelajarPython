import sys 
import mysql.connector

def main():
    
   kode = input('masukkan kode yang akan dihapus: ')

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
            DELETE FROM BUKU WHERE KODE = %s 
            '''
            
            cur.execute(statement_dml, (kode,))

       except mysql.connector.DatabaseError as e:
           print(f'Data gagal di dihapus: {e}')
           koneksi.rollback()
           sys.exit(1)

       else :
           koneksi.commit()
           print('Data berhasil di dihapus')
           
      
   except mysql.connector.Error as e:
       print('Error :', e)
       
   else:
       print('koneksi berhasil')
       # menutup koneksi dan kursor
       cur.close()
       koneksi.close()

if __name__ == "__main__":
    main()  