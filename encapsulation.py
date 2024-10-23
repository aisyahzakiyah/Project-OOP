class Mobil:
    def __init__(self, Merk, Model, Tahun):
        self.__Merk = Merk
        self.__Model = Model
        self.__Tahun = Tahun

    def get_Merk(self):
        return self.__Merk
    
    def set_Merk(self, Merk):
        self.__Merk = Merk

    def get_Model(self):
        return self.__Model
    
    def set_Model(self, Model):
        self.__Model = Model

    def get_Tahun(self):
        return self.__Tahun
    
    def set_Tahun(self, Tahun):
        if Tahun > 1885:
            self.__Tahun = Tahun
        else:
            print("Tahun tidak valid untuk mobil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


Mobil1 = Mobil("Ferrari", "corolla", 2020)

print(Mobil1.get_Merk())
Mobil1.set_Tahun(2022)
print(Mobil1.get_Tahun())