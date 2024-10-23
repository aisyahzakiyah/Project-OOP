class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"{self.merk} dibuat pada tahun {self.tahun}."
    
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, model):
        super().__init__(merk, tahun)
        self.model = model
    
    def info_Mobil(self):
        return f"{self.merk} {self.model} dibuat pada tahun {self.tahun}."
    
mobil1 = Mobil("toyota", 2020, "corolla")
print(mobil1.info())
print(mobil1.info_Mobil())