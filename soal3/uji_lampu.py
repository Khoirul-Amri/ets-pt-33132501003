from lampu import Lampu

# Buat objek Lampu L1
l1 = Lampu("L1")
print(f"Awal           -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}")

# Nyalakan lampu
l1.nyalakan()
print(f"Setelah nyalakan -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}")

# Input tiga nilai kecerahan berurutan (60, 150, -5)
for _ in range(3):
    nilai = int(input("Masukkan nilai kecerahan: "))
    l1.atur(nilai)
    print(f"Setelah atur({nilai}) -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}")

# Matikan lampu
l1.matikan()
print(f"Setelah matikan  -> aktif: {l1.aktif}, kecerahan: {l1.kecerahan}")