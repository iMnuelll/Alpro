print("===>>> Program Wishlist Anime <<<===")
print('1. Tambah Judul Anime')
print('2. Mengurutkan daftar Anime')
print('3. Menampilkan Seluruh Judul Anime')
print('0. Exit')

anime = []
def tambah_anime() :
    tambah_Anime = input('Masukkan Judul Anime : ')
    print(f'{tambah_Anime}, berhasil ditambahkan')
    anime.append(tambah_Anime)
def tampil () :
    print('Daftar judul Anime :')
    for i in range (0, len(anime)) : 
           print(f'{i+1}.{anime[i]}')
def urut () :
    anime.sort()
    print('Daftar anime telah dirutukan')

while True :
    menu = int(input('Masukkan menu yang Anda inginkan : '))
    if menu == 1 :
        tambah_anime()
    elif menu == 2 :
        urut()
    elif menu == 3 :
        tampil()
    elif menu == 0 :
        print('Terimakasih telah menggunakan program kami.')
        break
    else :
        print('Menu yang Anda masukkan tidak tersedia, seilahkan pilih menu lain')
