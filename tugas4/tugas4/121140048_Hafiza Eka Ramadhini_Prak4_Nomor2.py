"""
Hafiza Eka Ramadhini 121140048 RB
Tugas 4 No 2
"""

class Robot:
    jumlah_turn = 0
    result = 0

    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage
        self.tangan_robot = 0
        self.power = False
        self.myrobot = False

    def set_tangan_robot(self, tangan_robot):
        self.tangan_robot = tangan_robot

    def lakukan_aksi(self, target):
        target.health -= self.damage

    def power_up(self) :
        pass

    def power_down(self) :
        pass

    def jumlah_turn() :
        Robot.jumlah_turn += 1
    
    def set_myrobot(objek):
        objek.myrobot = True
        pass

    def result(objek_1, objek_2):
        hands1 = objek_1.hands
        hands2 = objek_2.hands

        if hands1 == hands2 :
            print ("the players achieved equal result") 
        else :
            if hands1 == 1 :
                if hands2 == 2 :
                  
                  Robot.result = 2
                elif hands2 == 3 :
                    Robot.result = 1
            elif hands1 == 2 :
                if hands2 == 3 :
                    Robot.result = 2
                elif hands2 == 1 :
                    Robot.result = 1
            elif hands1== 3 :
                if hands2 == 1 :
                    Robot.result = 2
                elif hands2 == 2 :
                    Robot.result = 1

        if Robot.result == 1 :
            objek_1.power_up()
            objek_1.lakukan_aksi(objek_2)
            objek_1.power_down()
        elif Robot.result == 2 :
            objek_2.power_up()
            objek_2.lakukan_aksi(objek_1)
            objek_2.power_down()
        
        objek_1.tangan_robot = 0
        objek_2.tangan_robot = 0

        Robot.result = 0

class Antares(Robot) :
    def __init__(self, nama  = "Antares", health = 50000, damage = 5000):
        super().__init__(nama, health, damage)

    def power_up(self):
        if Robot.jumlah_turn % 3 == 0 and Robot.jumlah_turn > 1 :
            self.damage *= 1.5
            self.power = True

        if self.myrobot ==  True :
            print(f"Robotmu ({self.nama}) menyerang sebanyak {self.damage} DMG")
        else :
            print(f"Robot lawan ({self.nama}) menyerang sebanyak {self.damage} DMG")
        
    def power_down(self) :
        if self.power_upgrade == True :
            self.damage *= 0.2
        self.power = False

class Alphasetia(Robot) :
    def __init__(self, nama = "Alphasetia", health = 40000, damage = 6000):
        super().__init__(nama, health, damage)

    def power_up(self):
        if Robot.jumlah_turn % 2 == 0 and Robot.jumlah_turn > 1 :
            self.health += 4000
            if self.myrobot ==  True :
                print(f"Robotmu ({self.nama}) menambah darah sebanyak 4000 HP")
            else :
                print(f"Robot lawan ({self.nama}) menambah darah sebanyak 4000 HP")

        if self.myrobot ==  True :
            print(f"Robotmu ({self.nama}) menyerang sebanyak {self.damage} DMG")
        else :
            print(f"Robot lawan ({self.nama}) menyerang sebanyak {self.damage} DMG")
                
class Lecalicus(Robot) :
    def __init__(self, nama = "Lecalicus", health = 450000, damage = 5500):
        super().__init__(nama, health, damage)

    def power_up(self):
        if Robot.jumlah_turn % 4 == 0 and Robot.jumlah_turn > 1 :
            self.damage *= 2
            self.health += 7000
            self.power = True
            if self.myrobot ==  True :
                print(f"Robotmu ({self.nama}) menambah darah sebanyak 7000 HP")
            else :
                print(f"Robot lawan ({self.nama}) menambah darah sebanyak 7000 HP")

        if self.myrobot ==  True :
            print(f"Robotmu ({self.nama}) menyerang sebanyak {self.damage} DMG")
        else :
            print(f"Robot lawan ({self.nama}) menyerang sebanyak {self.damage} DMG")

    def power_down(self) :
        if self.power == True :
            self.damage /= 2
        self.power = False

print("Selamat datang di pertandingan robot Yamako")
chooseyours = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
chooseenemy= int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))

if chooseyours == 1 :
    myrobot = Antares()
elif chooseyours == 2 :
    myrobot = Alphasetia()
elif chooseyours == 3 :
    myrobot = Lecalicus()

Robot.set_myrobot(myrobot)

if chooseenemy == 1 :
    enemy = Antares()
elif chooseenemy == 2 :
    enemy = Alphasetia()
elif chooseenemy == 3 :
    enemy = Lecalicus()

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting", "\n")

while myrobot.health > 0 and enemy.health > 0 :
    Robot.jumlah_turn_bertambah()
    print(f"Turn saat ini : {Robot.jumlah_turn}")
    print(f"Robotmu ({myrobot.nama} - {myrobot.health}), robot lawan ({enemy.nama} - {enemy.health}")

    myHands = int(input(f"Pilih tangan robotmu ({myrobot.nama}): "))
    enemyHands = int(input(f"Pilih tangan robotmu ({enemy.nama}): "))

    myrobot.set_tangan_robot(myHands)
    enemy.set_tangan_robot(enemyHands)

    Robot.Suit(myrobot, enemy)

print()
