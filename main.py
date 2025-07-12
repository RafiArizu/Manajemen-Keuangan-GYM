import pandas as pd
import modular_class as mc


def menu(self):
    while True:
        print("\n=== Menu Manajemen Keuangan Gym ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Simpan ke CSV")
        print("6. Laporan bulanan")
        print("7. Laporan Tahunan")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == '1':
            mc.ManajemenKeuanganGym.tampilkan_data(self)
        elif pilihan == '2':
            mc.ManajemenKeuanganGym.tambah_data(self)
        elif pilihan == '3':
            mc.ManajemenKeuanganGym.ubah_data(self)
        elif pilihan == '4':
            mc.ManajemenKeuanganGym.hapus_data(self)
        elif pilihan == '5':
            mc.ManajemenKeuanganGym.simpan_ke_csv(self)
        elif pilihan == '6':
            mc.ManajemenKeuanganGym.laporan_bulanan(self)
        elif pilihan == '7':
            mc.ManajemenKeuanganGym.laporan_tahunan(self)
        elif pilihan == '8':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    app = mc.ManajemenKeuanganGym('data_gym.csv')
    menu(app)
