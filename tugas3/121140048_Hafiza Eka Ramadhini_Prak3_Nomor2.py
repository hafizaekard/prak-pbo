class AkunBank:

    # static variable to store all pelanggan
    list_pelanggan = []

    def __init__(self, no_pelanggan: int, nama_pelanggan: str, saldo: int) -> None:
        '''
        Constructor untuk kelas AkunBank

        Parameters
        ----------
        no_pelanggan : int
            Nomor pelanggan
        nama_pelanggan : str
            Nama pelanggan
        saldo : int
            Saldo yang dimiliki
        '''
        self.no_pelanggan = no_pelanggan
        self.nama_pelanggan = nama_pelanggan
        self.__saldo = saldo

        # append each instance to list_pelanggan
        AkunBank.list_pelanggan.append(self)

    def lihat_menu(self):
        '''
        Fungsi ini digunakan untuk menampilkan menu utama
        '''
        print('Selamat datang di Bank Jago')
        print('Halo %s, ingin nelakukan apa?' % self.nama_pelanggan)
        print('1. Lihat saldo')
        print('2. Tarik tunai')
        print('3. Transfer saldo')
        print('4. Keluar')
        print('Masukkan nomor input: ', end='')

    def lihat_saldo(self):
        '''
        Fungsi ini digunakan untuk menampilkan saldo
        '''
        print('%s memiliki saldo Rp %d' % (self.nama_pelanggan, self.__saldo))

    def tarik_tunai(self, jumlah: int) -> None:
        '''
        Fungsi ini digunakan untuk menarik tunai dari saldo

        Parameters
        ----------
        jumlah : int
            Jumlah uang yang ingin ditarik
        '''
        if jumlah > self.__saldo:
            print('Nominal saldo yang Anda punya tidak cukup!')
        else:
            self.__saldo -= jumlah
            print('Saldo berhasil ditarik!')

    def transfer(self, jumlah: int, tujuan: int) -> None:
        '''
        Fungsi ini digunakan untuk mentransfer saldo ke rekening lain

        Parameters
        ----------
        jumlah : int
            Jumlah uang yang ingin ditransfer
        no_rek_tujuan : int
            Nomor rekening tujuan
        '''
        if jumlah > self.__saldo:
            print('Nominal saldo yang Anda punya tidak cukup!')
        else:
            for pelanggan in AkunBank.list_pelanggan:
                if pelanggan.no_pelanggan == tujuan:
                    pelanggan.__saldo += jumlah
                    self.__saldo -= jumlah
                    print('Transfer Rp %d ke %s sukses!' % (jumlah, pelanggan.nama_pelanggan))
                    return
            print('No rekening tujuan tidak dikenal! Kembali ke menu utama...')


def main() -> None:
    # populate data
    akun1 = AkunBank(1234, "isi-nama-kalian", 5_000_000_000)
    akun2 = AkunBank(2345, "Ukraine", 6_666_666_666)
    akun3 = AkunBank(3456, "Elon Musk", 9_999_999_999)

    # loop menu
    while True:
        akun1.lihat_menu()
        pilihan = int(input())

        # newline
        print()

        # lihat saldo
        if pilihan == 1:
            akun1.lihat_saldo()

        # tarik tunai
        elif pilihan == 2:
            jumlah = int(input('Masukkan jumlah Nominal yang ingin ditarik: '))
            akun1.tarik_tunai(jumlah)

        # transfer
        elif pilihan == 3:
            jumlah = int(input('Nasukkan nominal yang ingin ditransfer: '))
            tujuan = int(input('Masukkan no rekeninq tujuan: '))
            akun1.transfer(jumlah, tujuan)

        # keluar
        elif pilihan == 4:
            break

        # input tidak valid
        else:
            print('Input tidak valid!')

        # newline if not exit
        if pilihan != 4:
            print()


if __name__ == '__main__':
    main()
