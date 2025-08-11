# 'r' adalah mode untuk 'read' (membaca)
# Ini adalah mode default, jadi open('data.txt') sama saja dengan

# file_handle = open('siswa/data_siswa.txt', 'r')


# # file_handle.close()  # Jangan lupa ditutup!
# # print("--- Isi File ---")
# # print(seluruh_isi)
# # print("--- Tipe Data dan Panjang ---")
# # print(type(seluruh_isi))
# # print(f"Jumlah karakter (termasuk newline): {len(seluruh_isi)}")


# # Panggilan pertama membaca baris pertama
# baris_1 = file_handle.readline()
# print(f"Baris 1: {repr(baris_1)}")  # repr() untuk melihat karaktertersembunyi
# # Panggilan kedua membaca baris kedua
# baris_2 = file_handle.readline()
# print(f"Baris 2: {repr(baris_2)}")

# baris_3 = file_handle.readline()
# print(f"Baris 3: {repr(baris_3)}")

# baris_4 = file_handle.readline()
# print(f"Baris 4: {repr(baris_4)}")

# baris_5 = file_handle.readline()
# print(f"Baris 5: {repr(baris_5)}")

# baris_6 = file_handle.readline()
# print(f"Baris 6: {repr(baris_6)}")

# file_handle.close()

with open('siswa/data_siswa.txt', 'r') as file_handle:
    baris_1 = file_handle.readline()
    # repr() untuk melihat karaktertersembunyi
    print(f"Baris 1: {repr(baris_1)}")
    # Panggilan kedua membaca baris kedua
    baris_2 = file_handle.readline()
    print(f"Baris 2: {repr(baris_2)}")

    baris_3 = file_handle.readline()
    print(f"Baris 3: {repr(baris_3)}")

    baris_4 = file_handle.readline()
    print(f"Baris 4: {repr(baris_4)}")

    baris_5 = file_handle.readline()
    print(f"Baris 5: {repr(baris_5)}")

    baris_6 = file_handle.readline()
    print(f"Baris 6: {repr(baris_6)}")
