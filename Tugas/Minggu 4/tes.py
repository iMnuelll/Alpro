print("=== Selamat Datang === ")
nama =(input("Silahkan masukkan nama anda = "))
a = str(input("Silahkan masukkan barang pertama : "))
b = int(input("Masukkan harga : "))
c = int(input("Masukkan jumlah yang ingin dibeli : "))
d = str(input("Silahkan masukkan barang kedua : "))
e = int(input("Masukkan harga : "))
f = int(input("Masukkan jumlah yang ingin dibeli : "))
barang_pertama = b*c
barang_kedua = e*f
total = barang_pertama+barang_kedua
if a ==("Minyak"):
    diskon = int(barang_pertama*0.1)
    total_harga1 = int(barang_pertama - diskon)
elif a ==("minyak"):
    diskon = int(barang_pertama*0.1)
    total_harga1 = int(barang_pertama - diskon)
else :
    total_harga1 = int(barang_pertama)
if d ==("Minyak"):
    diskon = int(barang_kedua*0.1)
    total_harga2 = int(barang_kedua - diskon)
elif d ==("minyak"):
    diskon = int(barang_kedua*0.1)
    total_harga2 = int(barang_kedua - diskon)    
else :
    diskon = (0)
    total_harga2 =int(barang_kedua)
totalharga = total_harga1+total_harga2
if totalharga >= 200000 :
    diskon = int(totalharga * 0.05)
    totalkeseluruhan = (totalharga - diskon)
else :
    totalkeseluruhan = totalharga
print("Total harga : ",totalkeseluruhan)
