from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required, current_user

app = Flask(__name__)

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
            'G20': 'Dagu tidak bisa mencapai dada',
            'G21': 'Ruam kemerahan di kulit',
            'G22': 'Batuk pilek atau mata merah',
            'G23': 'Luka di mulut yang dalam atau luas',
            'G24': 'Kekeruhan pada kornea mata',
            'G25': 'Luka di mulut',
            'G26': 'Mata bernanah',
            'G27': 'Demam 2 - 7 hari',
            'G28': 'Demam mendadak tinggi dan terus menerus',
            'G29': 'Nyeri di ulu hati',
            'G30': 'Bintik-bintik merah',
            'G31': 'Muntah bercampur darah / seperti kopi',
            'G32': 'Tinja berwarna hitam',
            'G33': 'Perdarahan di hidung dan gusi',
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

        self.solusi = {
            'P1': 'Segera bawa ke fasilitas kesehatan terdekat.',
            'P2': 'Istirahat yang cukup dan minum banyak air.',
            'P3': 'Konsultasikan dengan dokter untuk pengobatan lebih lanjut.',
            'P4': 'Segera bawa ke rumah sakit untuk penanganan lebih lanjut.',
            'P5': 'Minum oralit untuk mencegah dehidrasi.',
            'P6': 'Pastikan anak minum cukup cairan dan konsultasikan dengan dokter.',
            'P7': 'Segera bawa ke fasilitas kesehatan untuk penanganan dehidrasi berat.',
            'P8': 'Konsultasikan dengan dokter untuk penanganan lanjutan.',
            'P9': 'Segera bawa ke fasilitas kesehatan untuk penanganan lebih lanjut.',
            'P10': 'Segera bawa ke dokter untuk mendapatkan pengobatan yang sesuai.',
            'P11': 'Istirahat yang cukup dan minum banyak air.',
            'P12': 'Segera bawa ke fasilitas kesehatan terdekat untuk penanganan.',
            'P13': 'Konsultasikan dengan dokter untuk pengobatan lebih lanjut.',
            'P14': 'Segera bawa ke rumah sakit untuk penanganan lebih lanjut.',
            'P15': 'Konsultasikan dengan dokter untuk pengobatan lebih lanjut.',
            'P16': 'Segera bawa ke fasilitas kesehatan untuk pemeriksaan lebih lanjut.',
            'P17': 'Segera bawa ke rumah sakit untuk penanganan lebih lanjut.',
            'P18': 'Konsultasikan dengan dokter untuk penanganan lebih lanjut.'
        }
    
    def aturan_inferensi(self, keluhan, gejala):
        penyakit_diduga = set()
        if keluhan in ['G1', 'G2', 'G3', 'G4']:
            penyakit_diduga.add('P1')

        if keluhan == 'K1' and 'G5' in gejala:
            penyakit_diduga.add('P2')

        if keluhan == 'K1' and 'G6' in gejala:
            penyakit_diduga.add('P3')

        if keluhan == 'K1' and ('P1' in penyakit_diduga or 'G7' in gejala or 'G8' in gejala):
            penyakit_diduga.add('P4')

        if keluhan == 'K2' and 'G9' in gejala:
            penyakit_diduga.add('P5')

        if 'P5' in penyakit_diduga and 'G10' in gejala and ('G11' in gejala or 'G12' in gejala or 'G13' in gejala):
            penyakit_diduga.add('P6')

        if 'P5' in penyakit_diduga and 'G10' in gejala and ('G14' in gejala or 'G15' in gejala or 'G16' in gejala):
            penyakit_diduga.add('P7')

        if 'P5' in penyakit_diduga and 'G17' in gejala:
            penyakit_diduga.add('P8')

        if 'P8' in penyakit_diduga and ('P6' in penyakit_diduga or 'P7' in penyakit_diduga):
            penyakit_diduga.add('P9')

        if 'P5' in penyakit_diduga and 'G18' in gejala:
            penyakit_diduga.add('P10')

        if keluhan == 'K3' and 'G19' in gejala:
            penyakit_diduga.add('P11')

        if 'P1' in penyakit_diduga and ('P11' in penyakit_diduga or 'G20' in gejala):
            penyakit_diduga.add('P12')

        if 'P11' in penyakit_diduga and ('G21' in gejala and 'G22' in gejala or 'G25' in gejala):
            penyakit_diduga.add('P13')

        if 'P13' in penyakit_diduga and ('P1' in penyakit_diduga and ('G23' in gejala or 'G24' in gejala)):
            penyakit_diduga.add('P14')

        if 'P13' in penyakit_diduga and ('G25' in gejala or 'G26' in gejala):
            penyakit_diduga.add('P15')

        if 'P11' in penyakit_diduga and ('G27' in gejala and 'G28' in gejala and 'G29' in gejala or 'G30' in gejala):
            penyakit_diduga.add('P16')

        if 'P11' in penyakit_diduga and ('G27' in gejala and 'G28' in gejala and 'G31' in gejala or 'G32' in gejala or 'G33' in gejala or 'G34' in gejala):
            penyakit_diduga.add('P17')

        if 'P11' in penyakit_diduga and ('G35' in gejala or 'G36' in gejala):
            penyakit_diduga.add('P18')
            
        return penyakit_diduga

sistem_pakar = SistemPakar()
