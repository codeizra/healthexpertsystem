import main
from services import db

def add():
    id_pasien = int(input('id pasien: '))
    nama_pasien = input('nama pasien: ')
    usia = input('usia: ')
    jenis_kelamin = input('jenis kelamin: ')
    alamat = input('alamat: ')

    db.insert_item(id_pasien, nama_pasien, usia, jenis_kelamin, alamat)
    print("Data berhasil disimpan")


def start():
    while True:
        print('Menu:')
        print('1. Tambah Data Pasien')
        print('2. Lihat Data Pasien')
        print('3. Keluar')
        menu = int(input('Pilih menu: '))
        
        if menu == 1:
            add()
        elif menu == 2:
            # Logic to view patient data
            pass
        elif menu == 3:
            print('Terima kasih telah menggunakan layanan kami.')
            break
        else:
            print('Menu tidak valid. Silakan pilih menu yang benar.')

        play_again = input('Kembali ke menu utama? [y/n]: ')
        if play_again.lower() != "y":
            break

if _name_ == '_main_':
    start()