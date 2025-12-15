class Hewan:
    def makan(self):
        print("Hewan sedang makan")

    def ayam(self):
        print("Ini Ayam")
        
class Kucing(Hewan):
    def suara(self):
        print("Meong")
    
class Singa(Hewan):
    def makan(self):
        print("Singa makan daging")
        
h = Hewan()        
k = Kucing()
s = Singa()
k.makan()
k.suara()
h.ayam()
s.makan()

print("="*25)
# ==================================
class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print("Merk kendaraan:", self.merk)

class Motor(Kendaraan):
    def __init__(self, merk, tipe):
        super().__init__(merk)
        self.tipe = tipe
        
    def info(self):
        print("Motor matic", self.tipe)

m = Kendaraan("Honda")
t = Motor("Honda", "Injeksi") 
m.info()
t.info()
