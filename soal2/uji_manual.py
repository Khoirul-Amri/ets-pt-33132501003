from debit import cari_terendah, cek_status, hitung_rata_rata

print(hitung_rata_rata([10, 20, 30]))
print(cari_terendah([12.5, 14.0, 11.0]))

nilai_input = float(input("Masukkan nilai debit: "))
print(cek_status(nilai_input))