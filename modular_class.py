import main

class ManajemenKeuanganGym:
    def __init__(self, nama_file):
        self.nama_file = nama_file

        # Baca data dari file CSV ke list dictionary
        try:
            self.data = main.pd.read_csv(nama_file).to_dict(orient='records')
        except FileNotFoundError:
            self.data = []

    def tampilkan_data(self):
        print("\n=== Data Keuangan Gym ===")
        if self.data:
            df = main.pd.DataFrame(self.data)
            print(df)
        else:
            print("Data masih kosong.")

    def tambah_data(self):
        print("\n=== Tambah Data Baru ===")
        tanggal = input("Tanggal (format: Januari-01-2025): ")
        tipe = input("Tipe (pemasukan/pengeluaran): ").lower()
        kategori = input("Kategori (misalnya: membership, gaji, listrik): ").lower()

        try:
            nominal = int(input("Nominal (angka): "))
        except ValueError:
            print("Nominal harus berupa angka.")
            return

        deskripsi = input("Deskripsi: ").lower()

        data_baru = {
            'tanggal': tanggal,
            'tipe': tipe,
            'kategori': kategori,
            'nominal': nominal,
            'deskripsi': deskripsi
        }

        self.data.append(data_baru)
        print("✅ Data berhasil ditambahkan.")

    def ubah_data(self):
        print("\n=== Ubah Data ===")
        tanggal = input("Masukkan tanggal transaksi yang ingin diubah(contoh: januari-01-2025): ")

        for item in self.data:
            if item['tanggal'] == tanggal:
                print(f"Data ditemukan: {item}")  
                tipe = input("Tipe baru (kosongkan jika tidak diubah): ").lower()
                kategori = input("Kategori baru: ").lower()
                nominal_input = input("Nominal baru: ")
                deskripsi = input("Deskripsi baru: ").lower()

                if tipe:
                    item['tipe'] = tipe
                if kategori:
                    item['kategori'] = kategori
                if nominal_input:
                    try:
                        item['nominal'] = int(nominal_input)
                    except ValueError:
                        print("Nominal harus angka. Tidak diubah.")
                if deskripsi:
                    item['deskripsi'] = deskripsi

                print("✅ Data berhasil diubah.")
                return

        print("⚠️ Tanggal tidak ditemukan.")

    def hapus_data(self):
        print("\n=== Hapus Data ===")
        tanggal = input("Masukkan tanggal transaksi yang ingin dihapus(contoh: januari-01-2025): ")

        awal = len(self.data)
        self.data = [item for item in self.data if item['tanggal'] != tanggal]

        if len(self.data) < awal:
            print("✅ Data berhasil dihapus.")
        else:
            print("⚠️ Tanggal tidak ditemukan.")

    def simpan_ke_csv(self):
        df = main.pd.DataFrame(self.data)
        df.to_csv(self.nama_file, index=False)
        print("✅ Data berhasil disimpan ke CSV.")

    def laporan_bulanan(self):
        print("\n=== Rekap Total Pemasukan dan Pengeluaran per Bulan ===")
        laporan = {}

        for item in self.data:
            try:
                bulan, _, tahun = item['tanggal'].split('-')
                key = f"{bulan}-{tahun}"
                if key not in laporan:
                    laporan[key] = {
                        'pemasukan': 0,
                        'pengeluaran': 0
                    }

                if item['tipe'] == 'pemasukan':
                    laporan[key]['pemasukan'] += int(item['nominal'])
                elif item['tipe'] == 'pengeluaran':
                    laporan[key]['pengeluaran'] += int(item['nominal'])

            except Exception as e:
                print(f"Error saat membaca tanggal: {item['tanggal']} - {e}")

        for bulan_tahun in sorted(laporan.keys()):
            print(f"{bulan_tahun} → Pemasukan: Rp{laporan[bulan_tahun]['pemasukan']:,} | Pengeluaran: Rp{laporan[bulan_tahun]['pengeluaran']:,}")

    def laporan_tahunan(self):
        print("\n=== Rekap Total Pemasukan dan Pengeluaran per Tahun ===")
        laporan = {}

        for item in self.data:
            try:
                _, _, tahun = item['tanggal'].split('-')
                if tahun not in laporan:
                    laporan[tahun] = {
                        'pemasukan': 0,
                        'pengeluaran': 0
                    }

                if item['tipe'] == 'pemasukan':
                    laporan[tahun]['pemasukan'] += int(item['nominal'])
                elif item['tipe'] == 'pengeluaran':
                    laporan[tahun]['pengeluaran'] += int(item['nominal'])

            except Exception as e:
                print(f"Error saat membaca tanggal: {item['tanggal']} - {e}")

        for tahun in sorted(laporan.keys()):
            print(f"{tahun} → Pemasukan: Rp{laporan[tahun]['pemasukan']:,} | Pengeluaran: Rp{laporan[tahun]['pengeluaran']:,}")
