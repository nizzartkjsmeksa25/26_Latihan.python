# Modul Logika Dasar & Aritmatika
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return f"{angka} adalah bilangan GENAP"
    else:
        return f"{angka} adalah bilangan GANJIL"

def hitung_perkalian(a, b):
    return f"{a} x {b} = {a * b}"

def hitung_pembagian(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi 0!"
    return f"{a} / {b} = {a / b}"
