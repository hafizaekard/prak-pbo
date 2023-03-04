username = "informatika"
password = "12345678"

for i in range(3):
    usn = str(input("Username anda : "))
    psw = str(input("Password anda : "))
    if usn == username and psw == password:
        print("Berhasil login!")
        exit()
    elif i == 2 and (usn != username or psw != password):
        print("Akun anda diblokir!")
    else:
        print("Username atau password salah, coba lagi!")
    print()
