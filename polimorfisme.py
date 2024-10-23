class Hewan:
    def Suara(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode isi")
    
class Kucing(Hewan):
    def Suara(self):
        return "Meooooooooooooung!"
    
class Sapi(Hewan):
    def Suara(self):
        return "Moooooooooooo!"
    
def cetak_Suara(Hewan):
    print(Hewan.Suara())

Hewan1 = Kucing()
Hewan2 = Sapi()

cetak_Suara(Hewan1)
cetak_Suara(Hewan2)