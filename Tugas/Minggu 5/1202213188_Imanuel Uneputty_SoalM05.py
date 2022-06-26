nama = str(input("Masukkan nama : "))
jumlah_barang = int(input('Masukkan jumlah barang : '))
total = 0
keranjang = []
listharga = []
for i in range (jumlah_barang) :
    print('Barang ke - ', i + 1)
    nama_barang = str(input('Masukkan nama barang : '))
    keranjang.append(nama_barang)
    harga_barang = int(input('Masukkan harga barang : '))
    listharga.append(harga_barang)
    print('Item yang dibeli : ', keranjang,'Dengan harga',listharga)

    if nama_barang == 'minyak' or nama_barang == 'Minyak':
        harga_barang -= (harga_barang*0.1)
        total += harga_barang
    else :
        total += harga_barang
if total >= 200000  :
    diskon = total*0.1
    total -= diskon
    print('Total diskon anda :', diskon)
    print('Harga yang harus anda bayar : ', total)
else : 
     print('Harga yang harus anda bayar : ', total)