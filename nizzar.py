import tkinter as tk
from tkinter import messagebox, ttk
import modulmath
import modulbangundatar
import database

class AplikasiNizzar:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Modul & Matematika - Nizzar")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Inisialisasi Tampilan Login / Input User
        self.tampilan_login()

    def tampilan_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="LOGIN / INPUT DATA SISWA", font=("Helvetica", 14, "bold")).pack(pady=15)

        tk.Label(self.root, text="Nama :", font=("Helvetica", 10)).pack(anchor="w", padx=40)
        self.ent_nama = tk.Entry(self.root, width=35)
        self.ent_nama.pack(pady=5)

        tk.Label(self.root, text="Kelas :", font=("Helvetica", 10)).pack(anchor="w", padx=40)
        self.ent_kelas = tk.Entry(self.root, width=35)
        self.ent_kelas.pack(pady=5)

        tk.Label(self.root, text="Password :", font=("Helvetica", 10)).pack(anchor="w", padx=40)
        self.ent_pass = tk.Entry(self.root, width=35, show="*")
        self.ent_pass.pack(pady=5)

        tk.Button(self.root, text="Simpan & Masuk Menu", bg="#27ae60", fg="white", font=("Helvetica", 10, "bold"),
                  command=self.proses_login).pack(pady=20)

    def proses_login(self):
        nama = self.ent_nama.get()
        kelas = self.ent_kelas.get()
        password = self.ent_pass.get()

        if not nama or not kelas or not password:
            messagebox.showwarning("Peringatan", "Semua data wajib diisi!")
            return

        timer = database.simpan_data(nama, kelas, password)
        messagebox.showinfo("Sukses", f"Data berhasil disimpan!\nWaktu: {timer}")
        self.tampilan_menu_utama(nama)

    def tampilan_menu_utama(self, nama):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Selamat Datang, {nama}!", font=("Helvetica", 12, "bold"), fg="#2c3e50").pack(pady=10)

        # Tab Menu Modul
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # TAB 1: Ganjil Genap
        frame_gg = ttk.Frame(notebook)
        notebook.add(frame_gg, text="Ganjil Genap")
        
        tk.Label(frame_gg, text="Masukkan Angka:").pack(pady=10)
        ent_gg = tk.Entry(frame_gg)
        ent_gg.pack(pady=5)
        lbl_hasil_gg = tk.Label(frame_gg, text="", font=("Helvetica", 10, "bold"))
        
        def cek_gg():
            try:
                val = int(ent_gg.get())
                lbl_hasil_gg.config(text=modulmath.cek_ganjil_genap(val))
            except ValueError:
                messagebox.showerror("Error", "Masukkan angka yang valid!")

        tk.Button(frame_gg, text="Cek", command=cek_gg, bg="#3498db", fg="white").pack(pady=10)
        lbl_hasil_gg.pack(pady=10)

        # TAB 2: Aritmatika (Perkalian & Pembagian)
        frame_math = ttk.Frame(notebook)
        notebook.add(frame_math, text="Aritmatika")

        tk.Label(frame_math, text="Angka 1:").pack()
        ent_a1 = tk.Entry(frame_math)
        ent_a1.pack()
        
        tk.Label(frame_math, text="Angka 2:").pack()
        ent_a2 = tk.Entry(frame_math)
        ent_a2.pack()

        lbl_hasil_math = tk.Label(frame_math, text="", font=("Helvetica", 10, "bold"))

        def hitung_kali():
            try:
                a, b = int(ent_a1.get()), int(ent_a2.get())
                lbl_hasil_math.config(text=modulmath.hitung_perkalian(a, b))
            except ValueError:
                messagebox.showerror("Error", "Masukkan angka yang valid!")

        def hitung_bagi():
            try:
                a, b = int(ent_a1.get()), int(ent_a2.get())
                lbl_hasil_math.config(text=modulmath.hitung_pembagian(a, b))
            except ValueError:
                messagebox.showerror("Error", "Masukkan angka yang valid!")

        btn_frame = tk.Frame(frame_math)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Perkalian (*)", command=hitung_kali, bg="#e67e22", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Pembagian (/)", command=hitung_bagi, bg="#e74c3c", fg="white").pack(side="left", padx=5)
        lbl_hasil_math.pack(pady=10)

        # TAB 3: Bangun Datar
        frame_bd = ttk.Frame(notebook)
        notebook.add(frame_bd, text="Bangun Datar")

        tk.Label(frame_bd, text="Panjang / Alas (cm):").pack()
        ent_p = tk.Entry(frame_bd)
        ent_p.pack()

        tk.Label(frame_bd, text="Lebar / Tinggi (cm):").pack()
        ent_l = tk.Entry(frame_bd)
        ent_l.pack()

        lbl_hasil_bd = tk.Label(frame_bd, text="", font=("Helvetica", 10, "bold"))

        def proses_luas_pp():
            try:
                p, l = float(ent_p.get()), float(ent_l.get())
                lbl_hasil_bd.config(text=modulbangundatar.hitung_luas_persegi_panjang(p, l))
            except ValueError:
                messagebox.showerror("Error", "Input tidak valid!")

        def proses_kel_pp():
            try:
                p, l = float(ent_p.get()), float(ent_l.get())
                lbl_hasil_bd.config(text=modulbangundatar.hitung_keliling_persegi_panjang(p, l))
            except ValueError:
                messagebox.showerror("Error", "Input tidak valid!")

        def proses_luas_jg():
            try:
                p, l = float(ent_p.get()), float(ent_l.get())
                lbl_hasil_bd.config(text=modulbangundatar.hitung_luas_jajar_genjang(p, l))
            except ValueError:
                messagebox.showerror("Error", "Input tidak valid!")

        tk.Button(frame_bd, text="Luas Persegi Panjang", command=proses_luas_pp).pack(pady=2)
        tk.Button(frame_bd, text="Keliling Persegi Panjang", command=proses_kel_pp).pack(pady=2)
        tk.Button(frame_bd, text="Luas Jajar Genjang", command=proses_luas_jg).pack(pady=2)
        lbl_hasil_bd.pack(pady=10)

        tk.Button(self.root, text="Keluar / Ganti User", command=self.tampilan_login, bg="#7f8c8d", fg="white").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiNizzar(root)
    root.mainloop()
