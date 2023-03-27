"""
Hafiza Eka Ramadhini 121140048 RB
Tugas 4 No 1
"""

class Komputer:
    def __init__(self, merk, jenis, harga):
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

    def __str__(self):
        return f"{self.nama} {self.jenis} produksi {self.merk}"

class Processor(Komputer):
    def __init__(self, merk, jenis, harga, jumlah_core, kecepatan_processor) -> None:
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "Processor"
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

class RAM(Komputer):
    def __init__(self, merk, jenis, harga, kapasitas):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "RAM"
        self.kapasitas = kapasitas

class HDD(Komputer):
    def __init__(self, merk, jenis, harga, kapasitas, rpm):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "SATA"
        self.kapasitas = kapasitas
        self.rpm = rpm

class VGA(Komputer):
    def __init__(self, merk, jenis, harga, kapasitas):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "VGA"
        self.kapasitas = kapasitas

class PSU(Komputer):
    def __init__(self, merk, jenis, harga, daya):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "PSU"
        self.daya = daya

p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
p2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
ram1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
ram2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
hdd1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
hdd2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
vga1 = VGA('Asus', 'VGA GTX 1050',250000, '2GB')
vga2 = VGA('Asus', '1060Ti', 250000, '8GB')
psu1 = PSU('Corsair', 'Corsair V550', 250000, '500W')
psu2 = PSU('Corsair', 'Corsair V550', 250000, '500W')

rakit = [[p1, ram1, hdd1, vga1, psu1], [p2, ram2, hdd2, vga2, psu2]]

for pc in rakit : 
    print("Komputer ")
    for komponen in pc :
        print(komponen)

print()
