import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tabel_pasien_balita'
)

def insert_item(id_pasien, nama_pasien, usia, jenis_kelamin, alamat):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO tbl_pasien_balita (id_pasien, nama_pasien, usia, jenis_kelamin, alamat) VALUES (%s, %s, %s, %s, %s)", (id_pasien, nama_pasien, usia, jenis_kelamin, alamat))
        db.commit()
        if cursor.rowcount > 0:
            print("Data berhasil dimasukkan")
            return True
        else:
            print("Data gagal diinsert")
            return False
    except mysql.connector.Error as error:
        print("Error:", error)
        return False