from perangkat import SensorDebit, SensorSuhu

suhu = SensorSuhu("Suhu")
for val in [30.1, 30.6, 30.3]:
    suhu.baca(val)

debit = SensorDebit("Debit", "L/menit")
for val in [12.0, 15.0, 15.0]:
    debit.baca(val)

daftar_sensor = [suhu, debit]

for p in daftar_sensor:
    print(f"{p.nama} -> {p.proses()}")
    