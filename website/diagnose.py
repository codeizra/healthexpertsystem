
class Pengguna:
    def __init__(self, id_user, nama, usia, alamat):
        self.id_user = id_user
        self.nama = nama
        self.usia = usia
        self.alamat = alamat


class SistemLogin:
    def __init__(self):
        self.database_pengguna = []

    def tambah_pengguna(self, pengguna):
        self.database_pengguna.append(pengguna)

    def login(self, id_user):
        for pengguna in self.database_pengguna:
            if pengguna.id_user == id_user:
                print(f"Selamat datang, {pengguna.nama}!")
                print(f"Usia: {pengguna.usia}")
                print(f"Alamat: {pengguna.alamat}")
                return
        print("ID user tidak ditemukan.")
        tambah_baru = input("Apakah Anda ingin menambahkan pengguna baru? (ya/tidak): ").lower()
        if tambah_baru == "ya":
            nama = input("Masukkan nama: ")
            usia = int(input("Masukkan usia: "))
            alamat = input("Masukkan alamat: ")
            new_id = self.generate_new_id()
            self.tambah_pengguna(Pengguna(new_id, nama, usia, alamat))
            print("Silakan login kembali untuk menggunakan ID yang baru.")
            self.login(new_id)
        else:
            print("Terima kasih!")

    def generate_new_id(self):
        new_id = ''.join(random.choices('0123456789', k=5))
        while any(pengguna.id_user == new_id for pengguna in self.database_pengguna):
            new_id = ''.join(random.choices('0123456789', k=5))
        return new_id


class SistemPakar:
    def __init__(self):
        self.gejala = {
            'G1': 'Anak tidak bisa minum atau menyusu',
            'G2': 'Anak memuntahkan makanan yang dimakan',
            'G3': 'Anak menderita kejang',
            'G4': 'Anak tampak letargis atau tidak sadar',
            'G5': 'Napas Normal',
            'G6': 'Napas cepat',
            'G7': 'Tarikan dinding dada ke dalam',
            'G8': 'Stridor',
            'G9': 'Berak cair atau lembek',
            'G10': 'Mata cekung',
            'G11': 'Cubitan kulit perut kembali lambat',
            'G12': 'Gelisah, rewel/mudah marah',
            'G13': 'Haus, minum dengan lahap',
            'G14': 'Cubitan kulit perut sangat lambat',
            'G15': 'Anak tampak letargis atau tidak sadar',
            'G16': 'Tidak bisa minum atau malas minum',
            'G17': 'Diare 14 hari atau lebih',
            'G18': 'Ada darah dalam tinja',
            'G19': 'Suhu badan melebihi 37.5º C',
            'G20': 'Kaku kuduk (anak tidak bisa menunduk hingga dagu mencapai dada)',
            'G21': 'Ruam kemerahan di kulit',
            'G22': 'batuk pilek atau mata merah',
            'G23': 'Luka di mulut yang dalam atau luas',
            'G24': 'Kekeruhan pada kornea mata',
            'G25': 'Luka di mulut',
            'G26': 'Mata bernanah',
            'G27': 'Demam 2 - 7 hari',
            'G28': 'Demam mendadak tinggi dan terus menerus',
            'G29': 'Nyeri di ulu hati',
            'G30': 'bintik bintik merah',
            'G31': 'Muntah bercampur darah / seperti kopi',
            'G32': 'Tinja berwarna hitam',
            'G33': 'Perdarahan dihidung dan gusi',
            'G34': 'Syok dan gelisah',
            'G35': 'Infeksi',
            'G36': 'Pilek'
        }
        
        self.penyakit = {
            'P1': 'Tanda Bahaya Umum',
            'P2': 'Batuk',
            'P3': 'Pneumonia',
            'P4': 'Pneumonia Berat',
            'P5': 'Diare',
            'P6': 'Diare Dehidrasi Ringan',
            'P7': 'Diare Dehidrasi Berat',
            'P8': 'Diare Persisten',
            'P9': 'Diare Persisten Berat',
            'P10': 'Disentri',
            'P11': 'Demam',
            'P12': 'Demam dengan Tanda Bahaya Umum',
            'P13': 'Campak',
            'P14': 'Campak dengan komplikasi berat',
            'P15': 'Campak dengan komplikasi',
            'P16': 'Demam Mungkin DBD',
            'P17': 'DBD',
            'P18': 'Demam bukan DBD'
        }
    
    def aturan_inferensi(self, keluhan, gejala):
        penyakit_diduga = set()
        
        if keluhan in ['G1', 'G2', 'G3', 'G4']:
            penyakit_diduga.add('P1')
        
        elif keluhan == 'K1' and 'G5' in gejala:
            penyakit_diduga.add('P2')
        
        elif keluhan == 'K1' and 'G6' in gejala:
            penyakit_diduga.add('P3')
        
        elif keluhan == 'K1' and ('P1' in penyakit_diduga or 'G7' in gejala or 'G8' in gejala):
            penyakit_diduga.add('P4')
        
        elif keluhan == 'K2' and 'G9' in gejala:
            penyakit_diduga.add('P5')
        
        elif 'P5' in penyakit_diduga and 'G10' in gejala and ('G11' in gejala or 'G12' in gejala or 'G13' in gejala):
            penyakit_diduga.add('P6')
        
        elif 'P5' in penyakit_diduga and 'G10' in gejala and ('G14' in gejala or 'G15' in gejala or 'G16' in gejala):
            penyakit_diduga.add('P7')
        
        elif 'P5' in penyakit_diduga and 'G17' in gejala:
            penyakit_diduga.add('P8')
        
        elif 'P8' in penyakit_diduga and ('P6' in penyakit_diduga or 'P7' in penyakit_diduga):
            penyakit_diduga.add('P9')
        
        elif 'P5' in penyakit_diduga and 'G18' in gejala:
            penyakit_diduga.add('P10')
        
        elif keluhan == 'K3' and 'G19' in gejala:
            penyakit_diduga.add('P11')
        
        elif 'P1' in penyakit_diduga and ('P11' in penyakit_diduga or 'G20' in gejala):
            penyakit_diduga.add('P12')
        
        elif 'P11' in penyakit_diduga and ('G21' in gejala and 'G22' in gejala or 'G25' in gejala):
            penyakit_diduga.add('P13')
        
        elif 'P13' in penyakit_diduga and ('P1' in penyakit_diduga and ('G23' in gejala or 'G24' in gejala)):
            penyakit_diduga.add('P14')
        
        elif 'P13' in penyakit_diduga and ('G25' in gejala or 'G26' in gejala):
            penyakit_diduga.add('P15')
        
        elif 'P11' in penyakit_diduga and ('G27' in gejala and 'G28' in gejala and 'G29' in gejala or 'G30' in gejala):
            penyakit_diduga.add('P16')
        
        elif 'P11' in penyakit_diduga and ('G27' in gejala and 'G28' in gejala and 'G31' in gejala or 'G32' in gejala or 'G33' in gejala or 'G34' in gejala):
            penyakit_diduga.add('P17')
        
        elif 'P11' in penyakit_diduga and ('G35' in gejala or 'G36' in gejala):
            penyakit_diduga.add('P18')
        
        return penyakit_diduga

    
if __name__ == "__main__":
    sistem_login = SistemLogin()

    # Menambahkan beberapa pengguna
    sistem_login.tambah_pengguna(Pengguna("12345", "Choirunisa Syifa Amarta", 20, "Jalan Mushola Nurul Huda No. 12"))
    sistem_login.tambah_pengguna(Pengguna("67890", "Sindi Putri Setiawan", 19, "Jalan JatiKramat No. 22"))
    sistem_login.tambah_pengguna(Pengguna("11111", "Andina Wianie Zahra", 22, "Jalan Cilepuk 1 No. 90"))
    sistem_login.tambah_pengguna(Pengguna("22222", "Deizra Putri Kalika", 19, "Jalan Lubang Buaya No. 34"))
    sistem_login.tambah_pengguna(Pengguna("33333", "Revena Galuh", 22, "Jalan Raya Hankam No. 59"))
    sistem_login.tambah_pengguna(Pengguna("44444", "Ana Roina", 21, "Jalan Kalimalang No.41"))

    # Meminta pengguna untuk login
    id_user = input("Masukkan ID user: ")
    sistem_login.login(id_user)

    sistem_pakar = SistemPakar()

    valid_keluhan = False
    while not valid_keluhan:
        print("Silakan pilih keluhan atau masukkan 'Tidak Ada' jika tidak memiliki keluhan:")
        print("1. Batuk (K1)")
        print("2. Diare (K2)")
        print("3. Demam (K3)")
        keluhan = input("Masukkan pilihan keluhan (K1/K2/K3/Tidak Ada): ").upper()

        if keluhan in ['K1', 'K2', 'K3', 'TIDAK ADA']:
            valid_keluhan = True
        else:
            print("Keluhan tidak valid. Silakan coba lagi.")

    if keluhan == 'TIDAK ADA':
        print("\nAnda tidak memiliki keluhan. Silakan pilih gejala yang Anda alami:")
        valid_gejala = False
        while not valid_gejala:
            for kode, gejala in sistem_pakar.gejala.items():
                print(f"{kode}: {gejala}")
            gejala_input = input("Masukkan kode gejala (pisahkan dengan spasi jika lebih dari satu): ").split()

            if all(gejala in sistem_pakar.gejala for gejala in gejala_input):
                valid_gejala = True
            else:
                print("Salah satu atau lebih gejala yang dimasukkan tidak valid. Silakan coba lagi.")

        penyakit_diduga = sistem_pakar.aturan_inferensi(keluhan, gejala_input)

        if penyakit_diduga:
            print("\nPenyakit yang diduga berdasarkan gejala yang diberikan:")
            for penyakit in penyakit_diduga:
                print(f"- {sistem_pakar.penyakit[penyakit]}")
        else:
            print("\nTidak ada penyakit yang dapat diduga berdasarkan gejala yang diberikan.")
    else:
        print("\nSilakan pilih gejala:")
        valid_gejala = False
        while not valid_gejala:
            for kode, gejala in sistem_pakar.gejala.items():
                print(f"{kode}: {gejala}")
            gejala_input = input("Masukkan kode gejala (pisahkan dengan spasi jika lebih dari satu): ").split()

            if all(gejala in sistem_pakar.gejala for gejala in gejala_input):
                valid_gejala = True
            else:
                print("Salah satu atau lebih gejala yang dimasukkan tidak valid. Silakan coba lagi.")

        penyakit_diduga = sistem_pakar.aturan_inferensi(keluhan, gejala_input)

        if penyakit_diduga:
            print("\nPenyakit yang diduga berdasarkan keluhan dan gejala yang diberikan:")
            for penyakit in penyakit_diduga:
                print(f"- {sistem_pakar.penyakit[penyakit]}")
        else:
            print("\nTidak ada penyakit yang dapat diduga berdasarkan keluhan dan gejala yang diberikan.")
