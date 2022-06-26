nama = str(input("Masukkan nama : "))
jumlah_barang = int(input('Masukkan jumlah barang : '))
keranjang = []
listharga = []
for i in range (jumlah_barang) :
    print('Barang ke - ', i + 1)
    nama_barang = str(input('Masukkan nama barang : '))
    keranjang.append(nama_barang)
    
    print('Item : ', nama_barang)
    harga_barang = int(input('Masukkan harga barang : '))
    listharga.append(harga_barang)
    print('Harga', nama_barang, 'adalah', harga_barang)
    print('Item yang dibeli : ', keranjang,'Dengan harga',listharga)
    print('Harga item yang dibeli : ', listharga)
    total_harga = harga_barang
    if total_harga >= 200000 :
            total_hargadiskon = total_harga - (total_harga * 0.1)
    elif nama_barang == 'Minyak' or nama_barang == "minyak" :
            total_hargaminyak = total_harga - (total_harga *0.1)
            print('Nama item : ', nama_barang)
            print('Mendapatkan diskon sebesar 10%')
    else : 
        total_harga = harga_barang * jumlah_barang