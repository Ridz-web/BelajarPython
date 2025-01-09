from game import cuypy_game
from tools import warung_mini

def option() :
    while True :
        try :
            menu = int(input('pillih menu program:\n1.game cuypy\n2.warung mini\n3.keluar\npilihan anda: '))
            if menu == 1 :
                cuypy_game.start()
            elif menu == 2 :
                warung_mini.warung()
            elif menu == 3 :
                exit()
            else :
                print('silahkan pilih menu yang tersedia\n')
                continue
        except ValueError :
            print('silahkan pilih menu yang tersedia\n')
            continue

if __name__ == '__main__' :
    option()