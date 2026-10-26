import os


def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("Nilai acuan tidak boleh 0")
    return (galat_absolut(hasil, acuan) / abs(acuan)) * 100


def baca_log(nama_file):
    data_valid = []
    data_ditolak = []

    with open(nama_file, "r", encoding="utf-8") as f:
        baris_list = f.readlines()

    # Baris 1 adalah header, data dimulai dari baris 2 (indeks 1)
    for no_baris, line in enumerate(baris_list[1:], start=2):
        teks = line.strip()
        if not teks:
            continue

        parts = [p.strip() for p in teks.split(",")]

        # Pemeriksaan 1: Jumlah kolom harus tepat dua
        if len(parts) != 2:
            data_ditolak.append((no_baris, teks, "Jumlah kolom bukan 2"))
            continue

        waktu, str_debit = parts

        # Pemeriksaan 2: Nilai debit harus berupa angka numerik
        try:
            val_debit = float(str_debit)
        except ValueError:
            data_ditolak.append((no_baris, teks, "Nilai debit bukan angka"))
            continue

        # Pemeriksaan 3: Nilai debit harus berada pada rentang 5 sampai 25 L/menit
        if not (5.0 <= val_debit <= 25.0):
            data_ditolak.append(
                (no_baris, teks, "Nilai di luar rentang 5 - 25 L/menit")
            )
            continue

        data_valid.append(val_debit)

    return data_valid, data_ditolak


if __name__ == "__main__":
    jalur_file = os.path.join(os.path.dirname(__file__), "log_debit.csv")
    valid, ditolak = baca_log(jalur_file)

    rata_valid = sum(valid) / len(valid)

    # Cetak hasil untuk Soal 5b
    print("=== HASIL SOAL 5B ===")
    print(f"Jumlah data valid  : {len(valid)}")
    print(f"Jumlah data ditolak: {len(ditolak)}")
    print("Alasan penolakan:")
    for no, isi, alasan in ditolak:
        print(f"  - Baris {no}: '{isi}' -> Alasan: {alasan}")
    print(f"Rata-rata data valid: {rata_valid:.2f}")

    # Cetak hasil untuk Soal 5c
    print("\n=== HASIL SOAL 5C ===")
    acuan = 13.5714
    rata_terformat = round(rata_valid, 2)
    ga = galat_absolut(rata_terformat, acuan)
    gr = galat_relatif(rata_terformat, acuan)
    status = "LULUS" if gr <= 0.5 else "TIDAK LULUS"

    print(f"Galat absolut      : {ga:.4f}")
    print(f"Galat relatif (%)  : {gr:.4f}%")
    print(f"Status             : {status}")