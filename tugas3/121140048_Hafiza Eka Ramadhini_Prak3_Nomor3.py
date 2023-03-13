class Person:
    # class attribute (static)
    count = 0

    # constructor
    def __init__(self, name: str, age: int, phone: str, address: str):
        # public attribute
        self.name = name

        # protected attribute
        self._age = age

        # private attribute
        self.__phone = phone
        self.__address = address

        # set id dan tambahkan nilai count
        self.id = Person.count

        # Nilai count akan bertambah setiap kali objek Person dibuat
        Person.count += 1

    # Accessor dan Mutator untuk mengakses dan mengubah nilai atribut private
    def get_phone(self):
        return self.__phone

    def set_phone(self, phone: str):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address: str):
        self.__address = address

    # decorator to access protected attribute
    @property
    def age(self):
        return self._age

    # decorator to change protected attribute
    @age.setter
    def age(self, age: int):
        self._age = age


class Student(Person):
    # constructor
    def __init__(self, name: str, age: int, phone: str, address: str, nim: str):
        # memanggil constructor parent class
        super().__init__(name, age, phone, address)

        # public attribute
        self.nim = nim

    @property
    def phone(self):
        return self.get_phone()

    @phone.setter
    def phone(self, phone: str):
        self.set_phone(phone)


def main():
    # Buat objek Person dan Student
    person = Person("Jerry", 20, "081212121212", "Jl. Teratai No. 5")
    student = Student("Jessica", 19, "081212121213", "Jl. Teratai No. 10", "141456780")

    # print seluruh atribut person
    print("dictionary atribut person")
    for key, value in person.__dict__.items():
        print('%-20s %s' % (key, value))

    # newline
    print()

    # print seluruh atribut student
    print("dictionary atribut student")
    for key, value in student.__dict__.items():
        print('%-20s %s' % (key, value))

    # newline
    print()

    # percobaan mengakses atribut public
    print("Akses atribut public")
    print("Person Name: %s" % person.name)
    print("Student Name: %s" % student.name)

    '''
    Attribut name adalah atribut public, sehingga dapat diakses dari luar kelas.
    Attribut public juga akan diturunkan ke subclass dari kelas tersebut.
    '''

    # newline
    print()

    # percobaan mengakses atribut protected
    print("Akses atribut protected")
    print("Umur: %d" % person._age)
    print("Umur: %d" % student._age)

    '''
    Attribut _age adalah atribut protected, atribut protected adalah atribut yang hanya dapat diakses dari kelas tersebut dan kelas turunannya.
    Pemberian nama variable yang diawali dengan underscore _ adalah konvensi yang digunakan untuk menandakan bahwa variable tersebut adalah atribut protected. Akan tetapi, Python tidak akan membatasi akses ke atribut protected. hal ini dikarenakan Python didesain sebagai bahasa pemrograman yang mudah digunakan dan tidak terlalu ketat, beberapa orang menyebut access modifier atau information hiding sebagai hal yang unpythonic.

    As is true for modules, classes in Python do not put an absolute barrier between definition and user, but rather rely on the politeness of the user not to "break into the definition".
    — 9. Classes, The Python 2.6 Tutorial (2013)

    Python bergantung pada kebijaksanaan pengguna untuk tidak "mengganggu" definisi kelas, hal ini terlihat pada salah satu slogan pada Python yaitu "we're all responsible users here". jadi konsep access modifier atau information hiding ditetapkan dengan konvensi saja.
    '''

    # newline
    print()

    # percobaan mengakses atribut protected dengan decorator
    print("Akses atribut protected dengan decorator")
    print("Umur: %d" % person.age)
    print("Umur: %d" % student.age)

    '''
    Di python juga terdapat decorator untuk mengakses atribut protected, decorator ini akan memanggil fungsi getter yang telah dibuat pada kelas Person. jadi atribut yang dibatasi aksesnya hanya dapat diakses melalui decorator.
    '''

    # newline
    print()

    # percobaan mengubah atribut private
    print("Akses atribut private")
    try:
        print("Nomor telepon: %s" % person.__phone)
    except AttributeError as e:
        print(e)

    try:
        print("Nomor telepon: %s" % student.__phone)
    except AttributeError as e:
        print(e)

    '''
    Untuk mengakses atribut private, kita harus menggunakan fungsi getter dan setter yang telah dibuat pada kelas Person. Atribut private tidak dapat diakses dari luar kelas. Attribut private pada python ditandai dengan dua underscore (__) di depan nama variable.
    Sama halnya dengan atribut protected, Python sebenarnya tidak akan membatasi akses ke atribut private, akan tetapi sedikit berbeda dengan atribut protected, Python menerapkan konsep name mangling untuk atribut private. Atribut private akan ditambahkan dengan nama kelasnya, sehingga atribut private pada kelas Person akan menjadi _Person__phone, seperti yang terlihat pada output dictionary key pada tiap instance. Hal ini dilakukan untuk menghindari konflik nama variable antar kelas.
    '''

    # newline
    print()

    # percobaan mengakses atribut private dengan getter
    print("Akses atribut private dengan getter")
    print("Nomor telepon: %s" % person.get_phone())
    print("Nomor telepon: %s" % student.get_phone())

    # newline
    print()

    # percobaan mengaksess atribut private dengan name mangling
    print("Akses atribut private dengan name mangling")
    print("Nomor telepon: %s" % person._Person__phone)
    print("Nomor telepon: %s" % student._Person__phone)

    '''
    Untuk melampaui batasan name mangling, kita dapat mengakses atribut private dengan cara mengubah nama variable yang diawali dengan dua underscore (__) menjadi satu underscore (_) dan nama kelasnya, seperti yang terlihat pada percobaan mengakses atribut private pada objek person dan student.
    Namun hal ini sangat tidak disarankan.
    Note pada subclass student, name mangling pada atribut private __phone tetap menjadi _Person__phone karena atribut private pada kelas parent class tidak akan berubah.
    '''


if __name__ == "__main__":
    main()
