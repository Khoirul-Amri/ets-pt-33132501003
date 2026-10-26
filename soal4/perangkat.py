class Perangkat:
    def __init__(self, nama):
        self.nama = nama
        self.data = []

    def baca(self, nilai):
        self.data.append(nilai)

    def proses(self):
        raise NotImplementedError("Metode proses() harus diimplementasikan pada kelas turunan.")


class SensorSuhu(Perangkat):
    # Mewarisi constructor Perangkat tanpa constructor sendiri
    def proses(self):
        # Mengembalikan nilai tertinggi pada data
        return max(self.data)


class SensorDebit(Perangkat):
    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan

    def proses(self):
        # Mengembalikan nilai rata-rata data
        return sum(self.data) / len(self.data)