from pymongo import MongoClient  # Mengimpor MongoClient dari pustaka pymongo untuk menghubungkan aplikasi ke MongoDB
from datetime import datetime  # Mengimpor datetime untuk menambahkan timestamp

# Membuat koneksi ke MongoDB menggunakan URI koneksi
client = MongoClient("mongodb+srv://androidone252:p7wRtscSkaOTPJPu@cluster0.am62x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

try:
    # Mengakses database 'todo_app'
    db = client.todo_app
    # Mengakses koleksi 'task' di dalam database
    task_collection = db.task
except Exception as e:
    # Menangkap dan mencetak kesalahan jika terjadi masalah saat mengakses database atau koleksi
    print(f"terjadi kesalahan koneksi ke database dengan error: {e}")
finally:
    # Mencetak pesan bahwa koneksi ke database telah dibuat, terlepas dari apakah ada kesalahan atau tidak
    print("Database connection established")

# Fungsi untuk membuat tugas baru dengan judul, deskripsi, dan status
def add_task(title, description):
    try:
        # Membuat dokumen tugas baru dengan judul, deskripsi, status default "Belum Selesai", dan timestamp
        task = {
            "title": title,
            "description": description,
            "status": "Belum Selesai",
            "created_at": datetime.now()  # Menambahkan timestamp
        }
        # Menyisipkan dokumen tugas ke dalam koleksi 'task'
        task_collection.insert_one(task)
        # Memberikan umpan balik bahwa tugas berhasil ditambahkan
        print("tugas berhasil ditambahkan")
    except Exception as e:
        # Menangkap dan mencetak kesalahan jika terjadi masalah saat menambahkan tugas
        print(f"terjadi kesalahan saat menambahkan tugas dengan error: {e}")

# Fungsi untuk melihat semua tugas
def view_all_tasks():
    try:
        # Mengambil semua dokumen tugas dari koleksi
        view = task_collection.find()
        # Iterasi melalui setiap tugas dan mencetak detailnya
        for i in view:
            print(f"ID:{i['_id']}, Judul: {i['title']}, Deskripsi: {i['description']}, status : {i['status']}, created_at: {i.get('created_at', 'Tidak ada timestamp')}")

    except Exception as e:
        # Menangkap dan mencetak kesalahan jika terjadi masalah saat menampilkan tugas
        print(f"terjadi kesalahan saat menampilkan tugas dengan error: {e}")

# Fungsi untuk menghapus tugas berdasarkan ID
def delete_task(task_id):
    from bson.objectid import ObjectId  # Mengimpor ObjectId untuk mengonversi string ID ke tipe ObjectId
    try:
        # Menghapus tugas berdasarkan ID yang dikonversi ke ObjectId
        hapus = task_collection.delete_one({"_id": ObjectId(task_id)})
        # Memeriksa apakah ada dokumen yang dihapus dan memberikan umpan balik
        if hapus.deleted_count > 0:
            print("tugas berhasil dihapus")
        else:
            print("tidak ada tugas yang dihapus")
    except Exception as e:
        # Menangkap dan mencetak kesalahan jika terjadi masalah saat menghapus tugas
        print(f"error penghapusan data, please check {e}")

def main():
    while True:
        # Menampilkan menu opsi kepada pengguna
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")  # Meminta pengguna memilih opsi

        if pilihan == "1":
            # Meminta pengguna memasukkan detail tugas baru
            title = input("Masukkan Judul Tugas: ")
            description = input("Masukkan Deskripsi Tugas: ")
            status = input("Masukkan Status Tugas: ")  # Status diminta tetapi tidak digunakan dalam fungsi
            add_task(title, description)  # Menambahkan tugas baru
        elif pilihan == "2":
            view_all_tasks()  # Menampilkan semua tugas
        elif pilihan == "3":
            # Meminta pengguna memasukkan ID tugas yang ingin dihapus
            task_id = input("Masukkan ID Tugas yang ingin dihapus: ")
            delete_task(task_id)  # Menghapus tugas berdasarkan ID
        elif pilihan == "4":
            # Mengakhiri program dengan pesan terima kasih
            print("Terima kasih telah menggunakan aplikasi ini")
            break
        else:
            # Memberikan umpan balik jika pilihan tidak valid
            print("Pilihan tidak tersedia, silakan memilih menu yang tersedia")

if __name__ == "__main__":
    main()  # Memanggil fungsi utama untuk memulai program
