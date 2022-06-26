print("""Daftar barang yang tersedia di toko fashion melomarc :\n
1.Kemeja => Rp.50000
2.celana => Rp.60000
3.sepatu => Rp.30000
""")
kemeja = 50000
celana = 60000
sepatu = 30000
total_harga = 0

totalBarang = int(input("Berapa barang yang ingin dibeli :"))

for i in range (totalBarang) :
    kodeBarang = int(input("Masukkan kode barang yang ingin dibeli (1/2/3/selesai) : "))
    if kodeBarang == 1 :
        print('Kemeja ditambahkan')
        total_harga += 50000
    elif kodeBarang == 2 :
        print('Celana ditambahkan')
        total_harga += 60000
    elif kodeBarang == 3 :
        print('Sepatu ditambahkan')
        total_harga += 30000
    

print("Total yang harus dibayar sebesar Rp.", total_harga)