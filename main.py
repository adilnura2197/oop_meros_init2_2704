class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

    def info(self):
        print(f"Nomi: {self.nomi}")
        print(f"Tezlik: {self.tezlik}")


class Mashina(Transport):
    def __init__(self, nomi, tezlik, yoqilgi):
        super().__init__(nomi, tezlik)
        self.yoqilgi = yoqilgi

    def info(self):
        super().info()
        print(f"Yoqilg'i: {self.yoqilgi}")


m = Mashina("Cobalt", 180, "benzin")
m.info()


class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def info(self):
        print(f"Ism: {self.ism}")
        print(f"Maosh: {self.maosh}")


class Dasturchi(Xodim):
    def __init__(self, ism, maosh, til):
        super().__init__(ism, maosh)
        self.til = til

    def info(self):
        super().info()
        print(f"Til: {self.til}")


d = Dasturchi("Aziz", 500, "Python")
d.info()
