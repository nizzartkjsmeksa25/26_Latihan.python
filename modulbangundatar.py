#Modul Luas Persegi Panjang
def hitung_luas_persegi_panjang(c):
    while True:
        angkapjg = int(input("Panjang = "))
        angkalbr = int(input("Lebar = "))
        print(f"{angkapjg}cm * {angkalbr}cm = {angkapjg * angkalbr} cm")
        print(f"jadi luas persegi panjangmu adalah {angkapjg * angkalbr}cm atau {angkapjg * angkalbr / 100}m")
        
        # Hentikan program jika pengguna mengetik 'tidak'    
        pilihan = input("mau lanjut? (ya/tidak): ")   
                
        if pilihan == 'tidak':
            print("Program selesai.")
            break
        
#Modul Keliling Persegi Panjang
def hitung_keliling_persegi_panjang(c):
    while True:
        angkapjg = int(input("Panjang = "))
        angkalbr = int(input("Lebar = "))
        print(f"2 * {angkapjg}cm * {angkalbr}cm = {2 * angkapjg * angkalbr} cm")
        print(f"jadi luas persegi panjangmu adalah {2 * angkapjg * angkalbr}cm atau {2 * angkapjg * angkalbr / 100}m")
        
        # Hentikan program jika pengguna mengetik 'tidak'    
        pilihan = input("mau lanjut? (ya/tidak): ")   
                
        if pilihan == 'tidak':
            print("Program selesai.")
            break
        
#Modul Luas Jajar Genjang
def hitung_luas_jajar_genjang(c):
    while True:
        angkaals = int(input("Alas = "))
        angkatgi = int(input("Tinggi = "))
        print(f"{angkaals}cm * {angkatgi}cm = {angkaals * angkatgi} cm")
        print(f"jadi luas jajar genjangmu adalah {angkaals * angkatgi}cm atau {angkaals * angkatgi / 100}m")
        
        # Hentikan program jika pengguna mengetik 'tidak'    
        pilihan = input("mau lanjut? (ya/tidak): ")   
                
        if pilihan == 'tidak':
            print("Program selesai.")
            break
