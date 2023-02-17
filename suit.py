import re
import os

def condition_check():
    valid_response = ['ya','tidak']
    while True:
        try:
            response = input("Apakah kamu ingin bermain lagi? (Ya or Tidak): ")
            if response.lower() not in valid_response:
                raise ValueError("Jawaban hanya Ya atau Tidak")
            elif response.lower() == "ya":
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Terima Kasih telah bermain!")
                exit()
        except ValueError as err:
            print(err)
def play_suit():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Permainan Gajah, Manusia , Semut, Dimulai! ")

        print("Jagoan yang dapat kamu gunakan "
            "[G]ajah, [M]anusia, [Semut]")

        player1 = input("Pilih Jagoanmu : ")

        if not re.match("[GgMmSs]", player1):
            print("Masukkan pilihan dengan benar!")
            print("[G]ajah, [M]anusia, [Semut] : ")
            continue
        print('Pemain pertama memilih: ', player1.upper())
        
        player2 = input("Pilih Jagoanmu : ")

        if not re.match("[GgMmSs]", player2):
            print("Masukkan pilihan dengan benar!")
            print("[G]ajah, [M]anusia, [Semut] : ")
            continue
        print('Pemain kedua memilih: ', player2.upper())
        

        if player1.upper() == player2.upper():
            print("Seri!")
            play = condition_check()
        elif player1.upper() == "G" and player2.upper() == "M":
            print("Gajah berhasil mengalahkan manusia, Pemain pertama menang!")
            play = condition_check()
        elif player1.upper() == "M" and player2.upper() == "S":
            print("Manusia berhasil mengalahkan semut, Pemain pertama menang!")
            play = condition_check()
        elif player1.upper() == "S" and player2.upper() == "G":
            print("Semut berhasil mengalahkan gajah, Pemain pertama menang!")
            play = condition_check()
        else:
            if player2.upper() == player1.upper():
                print("Seri!")
                play = condition_check()
            elif player2.upper() == "G" and player1.upper() == "M":
                print("Gajah berhasil mengalahkan manusia, Pemain kedua menang!")
                play = condition_check()
            elif player2.upper() == "M" and player1.upper() == "S":
                print("Manusia berhasil mengalahkan semut, Pemain kedua menang!")
                play = condition_check()
            elif player2.upper() == "S" and player1.upper() == "G":
                print("Semut berhasil mengalahkan gajah, Pemain kedua menang!")
                play = condition_check()

if __name__ == '__main__':
    play_suit()
