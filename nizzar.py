while True:
    import modulmath
    import modulbangundatar

    print("Menu Modul")
    print("1.Ganjil Genap\n2.Perkalian\n3.Pembagian\n4.Luas Persegi Panjang\n5.Keliling Persegi Panjang\n6.Luas Jajar Genjang")
    print("")
    a = int(input("No = "))
    if a == 1:
        print(modulmath.ganjil_genap(print("Ganjil Genap\nMasukkan angkamu")))
    if a == 2:
        print(modulmath.perkalian(print("Perkalian\nMasukkan Angkamu")))
    if a == 3:
        print(modulmath.pembagian(print("Pembagian\nMasukkan Angkamu")))
    if a == 4:
        print(modulbangundatar.hitung_luas_persegi_panjang(print("Hitung Luas Persegi Panjangmu\nMasukkan Angkamu")))
    if a == 5:
        print(modulbangundatar.hitung_keliling_persegi_panjang(print("Hitung Keliling Persegi Panjangmu\nMsukkan Angkamu")))
    if a == 6:
        print(modulbangundatar.hitung_luas_jajar_genjang(print("Hitung Luas Jajar Genjangmu\nMasukkan Angkamu")))
    pilihan = input("mau lanjut? (ya/tidak): ")   
                
    if pilihan == 'tidak':
        print("Program selesai.")
        break   
