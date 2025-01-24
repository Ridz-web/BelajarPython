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
            
            data1 = ('BK01', 'Learn Python Mysql', 'Python', 1995, 450_000)
            data2 = ('BK02', 'Java for beginner', 'Java', 1987, 175_000)
            
            statement_dml = '''
            INSERT INTO BUKU VALUES(%s, %s, %s, %s, %s)
            '''
            # eksekusi statemen dml
            cur.execute(statement_dml, data1)
            cur.execute(statement_dml, data2)
            
       except mysql.connector.DatabaseError:
           print('Data gagal ditambahkan')
           koneksi.rollback()
           sys.exit(1)

       else :
           koneksi.commit()
           print('Data berhasil ditambahkan')
           
      
   except mysql.connector.Error as e:
       print('Error :', e)
       
   else:
       print('koneksi berhasil')
       # menutup koneksi dan kursor
       cur.close()
       koneksi.close()

if __name__ == "__main__":
    main()