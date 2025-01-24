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
            
            data = [

                    ('BK06', 'Legend of Ambatron', 'Gramedia', 1788, 135_000), 
                    ('BK07', 'Para pencari tuhan', 'Gramedia', 2011, 254_000),
                    ('BK08', 'C++ cheat sheat', 'Gramedia', 2023, 568_000)

                ]
            
            statement_dml = '''
            INSERT INTO BUKU VALUES(%s, %s, %s, %s, %s)
            '''
            
            # eksekusi statemen dml dan 3 data sekaligus
            cur.executemany(statement_dml, data)
           
            
       except mysql.connector.DatabaseError as e:
           print(f'Data gagal ditambahkan: {e}')
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