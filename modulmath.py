#Ganjil Genap#

#a = int(input("Angka: "))
#if a % 2 == 0:
    #print(f"{a} adalah bilangan GENAP")
#else:
    #print(f"{a} adalah bilangan GANJIL")
    
#b = int(input("Angka: "))
#if b // 2 * 2 == b:
    #print(f"{b} adalah bilangan GENAP")
#else:
    #print(f"{b} adalah bilangan GANJIL")
    
    
#Perulangan Ganjil genap#

#while True:
    
    #a = int(input("Angka: "))
    #if a % 2 == 0:
        #print(f"{a} adalah bilangan GENAP")
    #else:
        #print(f"{a} adalah bilangan GANJIL")
        
    #if a == 100:
        #break
    
#print("selesai")


#Modularitas

#Modul Ganjil_Genap
def ganjil_genap(a):
    while True:
        ank = int(input("angkamu = "))
        if ank % 2 == 0:
            print(f"{ank} adalah bilangan GENAP")
        else:
            print(f"{ank} adalah bilangan GANJIL")
            
        # Hentikan program jika pengguna mengetik 'tidak'    
        pilihan = input("mau lanjut? (ya/tidak): ")   
        
        if pilihan == 'tidak':
            print("Program selesai.")
            break
                
#Modul Perkalian
def perkalian(b):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("ingin dikali dengan = "))
        print(f"{angka} * {ank} = {angka * ank}")
        
        # Hentikan program jika pengguna mengetik 'tidak'    
        pilihan = input("mau lanjut? (ya/tidak): ")   
                
        if pilihan == 'tidak':
            print("Program selesai.")
            break
    
#Modul Pembagian
def pembagian(c):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("ingin dibagi dengan = "))
        print(f"{angka} / {ank} = {angka / ank}")
        
        # Hentikan program jika pengguna mengetik 'tidak'    
        pilihan = input("mau lanjut? (ya/tidak): ")   
                
        if pilihan == 'tidak':
            print("Program selesai.")
            break
