nama_file = "catatan_belanja.txt"

with open(nama_file, 'w') as file:
    print(f"File '{nama_file}' telah dibuka dalam mode 'append'...")

    # Menulis baris pertama ke file
    file.write("Daftar Belanja Bulanan\n")
    file.write("----------------------\n")

    # Menulis beberapa item
    jumlah = file.write("1. Apel\n")
    file.write("2. Roti Gandum\n")
    file.write("3. Susu UHT\n")

    print("Berhasil menulis 3 item ke file.")
    print(jumlah)

print(f"File '{nama_file}' telah ditutup secara otomatis.")
