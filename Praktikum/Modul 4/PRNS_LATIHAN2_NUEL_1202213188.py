class Wisata :
    def __init__(self) :
        self.nama = ["Toraja", "Makassar", "Bulukumba"]
        self.Julukan = ['Tator', "Kota Daeng", "Bumi Panrita Lopi"]
        self.Wisata = ["Burake", "Pantai Losari", "Pantai Bira"]
    def daspro(self) :
        print('===== Rekomendasi Tempat Wisata di Sulawesi Selatan =====')
        for w,i in enumerate(self.nama):
            print(f"Nama daerah \t: {i}")
            print(f"Julukan \t: {self.Julukan[w]}\Tempat Wisata\t:{self.Wisata[w]}\n")
Wisata().daspro()
