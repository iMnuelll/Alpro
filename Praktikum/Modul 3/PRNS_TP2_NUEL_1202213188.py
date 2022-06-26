print("===Mini Market Daspro===")
angka = 0
print("1. Sayur\n2. Buah\n3. Daging\n0. Cek Keranjang")
pesan = int(input("Mau beli menu nomor berapa ?:"))
jumlahpesan = int(input("Berapa banyak ?"))
while pesan == 1 or pesan == 2 or pesan == 3 or pesan == 4 :
    angka += 1
    if pesan == 1 : 
        print(jumlahpesan,("Sayur telah ditambahkan ke dalam keranjang"))
        pesan = int(input("Mau beli menu nomor berapa ? :"))
        jumlahpesansayur = int(input("Berapa banyak ?"))
    elif pesan == 2 :
        print(jumlahpesan,("Buah telah ditambahkan ke dalam keranjang"))
        pesan = int(input("Mau beli menu nomor berapa ? :"))
        jumlahpesanbuah = int(input("Berapa banyak ?"))
    elif pesan == 3 :
        print(jumlahpesan,("Daging telah ditambahkan ke dalam keranjang"))
        pesan = int(input("Mau beli menu nomor berapa ? :"))
        jumlahpesandaging = int(input("Berapa banyak ?"))
    elif pesan == 0 :
        break 
print("Isi Keranjangmu :")
print("-",jumlahpesansayur)
print("-",jumlahpesandaging)
print("-",jumlahpesanbuah)