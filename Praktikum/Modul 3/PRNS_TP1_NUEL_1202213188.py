jumlah_murid = int(input("Masukkan jumlah muridnya : "))
jumlah = 0
for i in range (1, jumlah_murid+1) :
    temp = int(input("Masukkan nilai murid ke - %i:"%i))
    jumlah+=temp
    rata_rata = jumlah / jumlah_murid
print("Nilai rata - rata",jumlah_murid,"murid tersebut adalah",rata_rata)