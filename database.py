import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import getpass
import os

# Pengaturan akses Google Sheets
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Membaca credentials
creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

# Login ke Google Sheets
client = gspread.authorize(creds)

# Membuka spreadsheet "database"
sheet = client.open("database").sheet1

# Membuat judul kolom
sheet.update("A1:D1", [["Nama", "Kelas", "Password", "Timer"]])

# Membersihkan terminal
os.system("cls")

# Input data
nama = input("Masukkan nama : ")
kelas = input("Masukkan kelas : ")
password = getpass.getpass("Masukkan password : ")

# Mengambil waktu saat data dimasukkan
timer = datetime.now().strftime("%H:%M:%S")

# Memasukkan data ke Google Sheets
sheet.append_row([nama, kelas, password, timer])

# Menampilkan hasil
print("\nData berhasil disimpan!")
print("Nama     :", nama)
print("Kelas    :", kelas)
print("Password :", "*" * len(password))
print("Timer    :", timer)