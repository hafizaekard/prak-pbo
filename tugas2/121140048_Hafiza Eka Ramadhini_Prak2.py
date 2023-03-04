class Profile:
    def __init__(self, nama, NIM, Asal_kelas_siakad, Jumlah_SKS):
        self.nama = nama
        self.NIM = NIM
        self.Asal_kelas_siakad = Asal_kelas_siakad
        self.Jumlah_SKS = Jumlah_SKS 
        
Profile = Profile("Hafiza", "121140048", "RB", "22")

print(Profile.nama)
print(Profile.NIM)
print(Profile.Asal_kelas_siakad)
print(Profile.Jumlah_SKS)
