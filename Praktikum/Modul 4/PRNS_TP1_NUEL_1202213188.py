print("========== Daspro Market ==========")
data = []
def toko() :
    
    while True:
        
        print("Ketik Stop Untuk Berhenti")
        item = input("Masukkan nama barang kedalam keranjang : ")
        if item == "Stop" :
            break
        else :
            data.append(item)
    print(f"Barang yang ada didalam keranjang : {data}")
toko()