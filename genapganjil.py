for i in range(5):
    bilangan = int(input("Masukkan bilangan: "))

    if bilangan % 2 == 0:
        print(bilangan, "adalah bilangan genap")
    else:
        print(bilangan, "adalah bilangan ganjil")
        
    # Perulangan akan terus berjalan selama variabel lanjut bernilai 'y' atau 'Y'
    while lanjut.lower() == "y":
        # 1. Input bilangan dari pengguna
        bilangan = int(input("\nMasukkan sebuah bilangan: "))
    
        # 2. Logika Modulus (sisa pembagian dengan 2)
        if bilangan % 2 == 0:
            print(f"--> {bilangan} adalah bilangan GENAP")
        else:
            print(f"--> {bilangan} adalah bilangan GANJIL")
    
        # 3. Menanyakan apakah pengguna ingin mengulang atau keluar
        lanjut = input(
            "\nApakah ingin mengecek bilangan lain? (y/n untuk keluar): "
        )
    
    print("\nProgram selesai. Terima kasih!")
