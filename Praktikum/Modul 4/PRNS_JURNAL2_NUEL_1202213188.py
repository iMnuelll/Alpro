class studio : 
    def __init__(self, namaBand, jumlahAnggota, genre) :
        self.namaBand = namaBand
        self.jumlahAnggota = jumlahAnggota
        self.genre = genre
    def genreIndie(self) :
        if(self.genre == "Indie") :
            print('Cari Stuio lain bro!')
        else :
            print('Band lu asik banget sih!!!')
namaBand = input('Nama band : ')
jumlahAnggota = int(input('Jumlah anggota : '))
genre = input('Genre musik : ')

band = studio(namaBand, jumlahAnggota, genre)
band.genreIndie()