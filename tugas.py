import tkinter as tk
from tkinter import messagebox

database_kerusakan = {
    "Baterai Drop/Rusak": ["baterai_cepat_habis", "mati_saat_cabut_charger", "persentase_loncat"],
    "Keyboard Konslet": ["tombol_macet", "ngetik_sendiri", "bunyi_beep_panjang"],
    "Kipas Pendingin Mati": ["suara_kipas_hilang", "bodi_sangat_panas", "mati_saat_berat"],
    "Kabel Fleksibel Layar Rusak": ["layar_berkedip", "layar_putih_saat_digerakkan", "warna_layar_pudar"],
    "Terinfeksi Virus/Malware": ["kinerja_lambat_tanpa_sebab", "banyak_popup_iklan", "file_terkunci"]
}

semua_gejala = [
    ("baterai_cepat_habis", "Apakah daya baterai sangat cepat habis saat digunakan?"),
    ("mati_saat_cabut_charger", "Apakah laptop langsung mati jika charger dicabut?"),
    ("persentase_loncat", "Apakah indikator persentase baterai sering meloncat tiba-tiba (misal dari 50% langsung 10%)?"),
    ("tombol_macet", "Apakah ada tombol di keyboard yang tidak merespon saat ditekan?"),
    ("ngetik_sendiri", "Apakah laptop seperti mengetik huruf sendiri tanpa Anda tekan?"),
    ("bunyi_beep_panjang", "Apakah terdengar bunyi beep panjang yang tidak wajar saat baru dinyalakan?"),
    ("suara_kipas_hilang", "Apakah suara hembusan kipas di dalam laptop tidak terdengar sama sekali?"),
    ("bodi_sangat_panas", "Apakah bodi laptop terasa jauh lebih panas dari biasanya?"),
    ("mati_saat_berat", "Apakah perangkat sering mati mendadak saat membuka aplikasi berat (seperti game/edit video)?"),
    ("layar_berkedip", "Apakah tampilan di layar sering berkedip (flickering)?"),
    ("layar_putih_saat_digerakkan", "Apakah layar menjadi blank/putih saat engsel monitor digerakkan?"),
    ("warna_layar_pudar", "Apakah warna pada layar terlihat pudar, aneh, atau tidak wajar?"),
    ("kinerja_lambat_tanpa_sebab", "Apakah perangkat terasa sangat lambat padahal tidak sedang membuka aplikasi?"),
    ("banyak_popup_iklan", "Apakah sering muncul iklan pop-up atau jendela aneh dengan sendirinya?"),
    ("file_terkunci", "Apakah ada file data yang tiba-tiba tidak bisa dibuka atau berubah formatnya?")
]

class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Kerusakan Laptop")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0


        self.label_tanya = tk.Label(root, text="Selamat Datang di Sistem Pakar", font=("Arial", 12))
        self.label_tanya.pack(pady=20)

        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, command=lambda: self.jawab('t'))
        
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil = []
        for kerusakan, syarat in database_kerusakan.items():
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(kerusakan)

        kesimpulan = ", ".join(hasil) if hasil else "Tidak terdeteksi kerusakan"
        
        messagebox.showinfo("Hasil Diagnosa", f"Berdasarkan gejala Anda:\n\n{kesimpulan}")

        # reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x250") 
    app = AplikasiPakar(root)
    root.mainloop()