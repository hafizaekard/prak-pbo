from abc import ABC, abstractmethod

#parent class - kelas abstrak
class AkunBank(ABC):
  def _init_(self,nama,tahun_daftar,saldo): #inisiasi variabel dari akunbank
    self.nama=nama
    self.tahun_daftar=tahun_daftar
    self.saldo=saldo

#fungsi konkrit 
  def lihat_saldo(self):
    print(f"Saldo : {self.saldo}")

#abstrak
  @abstractmethod
  def transfer_saldo(self,trx):
    self.trx = trx
    return self.trx

  @abstractmethod
  def lihat_suku_bunga(self):
    pass

#child class
class AkunGold(AkunBank):
    def _init_(self,nama,tahun_daftar,saldo):
        super()._init_(nama,tahun_daftar,saldo)
    #transfer saldo
    def transfer_saldo (self,trx):
        super().transfer_saldo(trx)
        usia_akun = 2023-self.tahun_daftar
        print(f"Usia akun = {usia_akun}")
        print(f"Total Transfer = {self.trx}")
        #kondisi dari transfer saldo
        if usia_akun >= 3 and self.trx >= 100000:
            print ("Biaya administrasi gratis.")
            print (f"Total saldo anda adalah : {self.saldo-self.trx} ")
            self.saldo-=self.trx #update saldo 
        elif usia_akun < 3 and self.trx >= 100000:
            print ("Biaya administrasi Rp.2000")
            self.trx = self.trx + 2000
            print (f"Total Transfer adalah : {self.trx}")
            print (f"Total saldo anda adalah : {self.saldo-self.trx} ")
            self.saldo-=self.trx
        elif self.trx < 100000:
            print ("Biaya administrasi gratis.")
            print (f"Total saldo anda adalah : {self.saldo-self.trx} ")
            self.saldo-=self.trx
        else :
            print ("Tidak memenuhi syarat")
            print (f"Total saldo anda adalah :{self.saldo-self.trx} ")
            self.saldo-=self.trx

    def lihat_suku_bunga(self):
        super().lihat_suku_bunga()
        usia_akun = 2023-self.tahun_daftar
        print(f"Usia akun = {usia_akun}")
        #kondisi dari suku bunga
        if usia_akun >=3 and self.saldo>=10000000000:
            print ("Bunga bulanan adalah 1%.")
            print (f"Total tabungan sekarang : Rp.{self.saldo}")
        elif usia_akun <3 and self.saldo>=1000000000:
            print ("Bunga bulanan adalah 2%.")
            print (f"Total tabungan sekarang : Rp.{self.saldo}")
        elif self.saldo<10000000000:
            print ("Bunga bulanan adalah 2%.")
            print (f"Total tabungan sekarang : Rp.{self.saldo}") 

#child class
class AkunSilver(AkunBank):
    def _init_(self,nama,tahun_daftar,saldo):
        super()._init_(nama,tahun_daftar,saldo)
    #fungsi turunan 
    def transfer_saldo (self,trx):
        super().transfer_saldo(trx)
        usia_akun = 2023-self.tahun_daftar
        print(f"Usia akun = {usia_akun}")
        #kondisi dari transfer saldo
        if usia_akun >= 3 and self.trx >= 100000:
            print ("Biaya administrasi Rp.2000.")
            self.trx = self.trx + 2000
            print (f"Total Transfer adalah : Rp. {self.trx}")
            print (f"Total saldo anda adalah : {self.saldo-self.trx}  ")
            self.saldo-=self.trx
        elif usia_akun < 3 and self.trx >= 100000:
            print ("Biaya administrasi Rp.5000")
            self.trx = self.trx + 5000
            print (f"Total Transfer adalah : Rp. {self.trx}")
            print (f"Total saldo anda adalah : {self.saldo-self.trx}")
            self.saldo-=self.trx
        elif self.trx < 100000:
            print ("Biaya administrasi gratis.")
            print (f"Total saldo anda adalah : {self.saldo-self.trx} ")
            self.saldo-=self.trx
        else :
            print ("Tidak memenuhi syarat")
            print (f"Total saldo anda adalah : {self.saldo-self.trx} ")
            self.saldo-=self.trx
            
    #fungsi turunan 
    def lihat_suku_bunga(self):
        super().lihat_suku_bunga()
        usia_akun = 2023-self.tahun_daftar
        print(f"Usia akun = {usia_akun}")
        #kondisi dari suku bunga
        if usia_akun >=3 and self.saldo>=10000000:
            print ("Bunga bulanan adalah 1%.")
            print (f"Total tabungan sekarang : Rp.{self.saldo}")
        elif usia_akun <3 and self.saldo>=10000000:
            print ("Bunga bulanan adalah 2%.")
            print (f"Total tabungan sekarang : Rp.{self.saldo}")
        elif self.saldo <10000000:
            print ("Bunga bulanan adalah 3%.")
            print (f"Total tabungan sekarang : Rp.{self.saldo}")




Akun1 = AkunGold("gaplek", 2003, 13000)
Akun1.transfer_saldo(5500000)
