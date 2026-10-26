data_debit = [12.5, 14.0, 13.5, 15.0, 11.0]


def hitung_rata_rata(data):
    """
    Menghitung nilai rata-rata dari sekumpulan data numerik pembacaan debit air.
    Input : data (list dari float atau int)
    Output: nilai rata-rata (float)
    """
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)


def cari_terendah(data):
    """
    Mencari nilai pembacaan debit terendah dari sekumpulan data.
    Input : data (list dari float atau int)
    Output: nilai terkecil dari data (float atau int)
    """
    terendah = data[0]
    for nilai in data:
        if nilai < terendah:
            terendah = nilai
    return terendah


def cek_status(debit):
    """
    Memeriksa status kategori debit air berdasarkan nilai pembacaan sensor.
    Batas kategori:
      - RENDAH : debit < 10 L/menit
      - NORMAL : 10 <= debit <= 20 L/menit
      - TINGGI : debit > 20 L/menit
    Input : debit (float atau int)
    Output: status kategori debit (str)
    """
    if debit < 10:
        return "RENDAH"
    elif debit <= 20:
        return "NORMAL"
    else:
        return "TINGGI"


if __name__ == "__main__":
    rata = hitung_rata_rata(data_debit)
    print("Rata-rata :", rata)
    print("Terendah  :", cari_terendah(data_debit))
    print("Status    :", cek_status(rata))