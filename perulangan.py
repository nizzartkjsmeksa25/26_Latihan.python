# ALAT PENGHITUNG ANGKA GANJIL DAN GENAP

while True:
    print("\n=== PENGECEKAN GANJIL / GENAP ===")
    print("Ketik 'q' untuk keluar dari program.")

    X = input("Masukkan Angka : ")

    # Tombol keluar
    if X.lower() == "q":
        print("Program selesai. Terima kasih!")
        break

    # Memastikan input berupa angka
    try:
        X = int(X)

        # LOGIKA PENGHITUNGAN
        if X % 2 == 0:
            print("Angka", X, "Termasuk Bilangan Genap")
        else:
            print("Angka", X, "Termasuk Bilangan Ganjil")

    except ValueError:
        print("Input tidak valid! Masukkan angka atau 'q' untuk keluar.")
