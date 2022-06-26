def Tanah(panjang, lebar):
    panjang = float(panjang)
    lebar = float(lebar)

    def luasTanah(panjang, lebar) :
        return panjang * lebar
    def kelilingTanah(panjang, lebar) :
        return 2 *(panjang+lebar)
    print(f'Luas tanah = {luasTanah(panjang, lebar)} m^2')
    print(f'Keliling tanah = {kelilingTanah(panjang,lebar)} m')
panjang = float(input('Masukkan Panjang Tanah : '))
lebar = float(input('Masukkan Lebar Tanah : '))

Tanah(panjang, lebar)