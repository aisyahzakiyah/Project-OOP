# Praktek 3
# Membuat sebuah sistem restoran sederhana menggunakan OOP
# Interaksi antar objek

class Menuitem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama} - ${self.harga:.2f}"
    
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = []

    def pesan(self, menu_item):
        self.pesanan.append(menu_item)
        print(f"{self.nama} memesan {menu_item}")

    def bayar(self):
        total = sum(item.harga for item in self.pesanan)
        return total
    
class Pelayan:
    def __init__(self, nama):
        self.nama = nama

    def ambil_pesanan(self, Pelanggan):
        print(f"{self.nama} mengambil pesanan dari {Pelanggan.nama}")

    def antar_pesanan(self, Pelanggan):
        total = Pelanggan.bayar()
        print(f"{self.nama} mengantarkan pesanan kepada {Pelanggan.nama}")
        print(f"total tagihan: ${total:.2f}")

class Dapur:
    def __init__(self):
        self.menu = {
            "Mie ayam": Menuitem("Mie ayam", 30000),
            "Es Teller": Menuitem("Es Teller", 15000),
            "Bakpao": Menuitem("Bakpao", 5000)
        }

    def siapkan_pesanan(self, pesanan):
        for item in pesanan:
            if item.nama in self.menu:
                print(f"menyediakan {item} dengan harga ${item.harga:.2f}")
            else:
                print(f"{item.menu} tidak ada dalam menu")

Pelanggan = Pelanggan("Chaewon")
Pelayan = Pelayan("Winter")
Dapur = Dapur()

Mie_ayam = Menuitem("Mie ayam", 30000)
Es_Teller = Menuitem("Es Teller", 15000)

Pelanggan.pesan(Mie_ayam)
Pelanggan.pesan(Es_Teller)

Pelayan.ambil_pesanan(Pelanggan)
Dapur.siapkan_pesanan(Pelanggan.pesanan)

Pelayan.antar_pesanan(Pelanggan)