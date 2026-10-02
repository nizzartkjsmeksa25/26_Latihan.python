# Modul Hitung Bangun Datar
def hitung_luas_persegi_panjang(panjang, lebar):
    luas_cm = panjang * lebar
    luas_m = luas_cm / 100
    return f"Luas: {luas_cm} cm² ({luas_m} m²)"

def hitung_keliling_persegi_panjang(panjang, lebar):
    kel_cm = 2 * (panjang + lebar)
    kel_m = kel_cm / 100
    return f"Keliling: {kel_cm} cm ({kel_m} m)"

def hitung_luas_jajar_genjang(alas, tinggi):
    luas_cm = alas * tinggi
    luas_m = luas_cm / 100
    return f"Luas Jajar Genjang: {luas_cm} cm² ({luas_m} m²)"
