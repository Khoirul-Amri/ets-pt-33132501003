from lampu import Lampu

lp1 = Lampu("L1")
lp2 = Lampu("L2")

lp1.nyalakan()
lp1.atur(60)

print(lp1)
print(lp2)
print(Lampu.jumlah_lampu)