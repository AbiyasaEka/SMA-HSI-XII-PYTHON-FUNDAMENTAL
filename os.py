import os

# 1. Mengecek Keberadaan File
nama_file = "catatan_belanja.txt"
if os.path.exists(nama_file):
    print(f"File '{nama_file}' ditemukan!")
else:
    print(f"File '{nama_file}' tidak ada.")

# 2. Mengecek Ukuran File (dalam bytes)
if os.path.exists(nama_file):
    ukuran = os.path.getsize(nama_file)
    print(f"Ukuran file: {ukuran} bytes")

# 3. Menghapus File
# Berhati-hatilah dengan perintah ini! File yang dihapus tidak masuk Recycle Bin.
file_untuk_dihapus = "test.txt"
# Buat file kosong dulu untuk contoh
with open(file_untuk_dihapus, 'w') as f:
    f.write("File ini akan dihapus.")

if os.path.exists(file_untuk_dihapus):
    print(f"\nMenghapus file '{file_untuk_dihapus}'...")
    os.remove(file_untuk_dihapus)
    print("File berhasil dihapus.")
else:
    print(f"File '{file_untuk_dihapus}' tidak ditemukan untuk dihapus.")

# 4. Membuat Direktori (Folder)
nama_folder = "data_output"
if not os.path.exists(nama_folder):
    print(f"\nMembuat folder '{nama_folder}'...")
    os.mkdir(nama_folder)
    print("Folder berhasil dibuat.")
else:
    print(f"Folder '{nama_folder}' sudah ada.")

# 5. Menghapus Direktori (Folder)
# Folder harus kosong untuk bisa dihapus dengan os.rmdir()
# if os.path.exists(nama_folder):
#     print(f"\nMenghapus folder '{nama_folder}'...")
#     os.rmdir(nama_folder)
#     print("Folder berhasil dihapus.")
