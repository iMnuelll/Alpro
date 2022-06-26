januariPemasukan = []
februariPemasukan = []
maretPemasukan = []
aprilPemasukan = []
meiPemasukan = []
juniPemasukan = []
juliPemasukan = []
agustusPemasukan = []
septemberPemasukan = []
oktoberPemasukan = []
novemberPemasukan = []
desemberPemasukan = []

def mainMenu() :
    print("=== Menu Utama =====")
    print("""
    1. Input Pemasukan
    2. Exit
    """)
def keuntungan() :
    inputBulan = input("Silahkan masukkan bulan : ")
    if inputBulan == "Januari" :
        pemasukan = int(input("Masukkan keuntungan : "))
        januariPemasukan.append(pemasukan)
    elif inputBulan == "Februari" :
        pemasukan = int(input("Masukkan keuntungan : "))
        februariPemasukan.append(pemasukan)
    elif inputBulan == "Maret" :
        pemasukan = int(input("Masukkan keuntungan : "))
        maretPemasukan.append(pemasukan)
    elif inputBulan == "April" :
        pemasukan = int(input("Masukkan keuntungan : "))
        aprilPemasukan.append(pemasukan)
    elif inputBulan == "Mei" :
        pemasukan = int(input("Masukkan keuntungan : "))
        meiPemasukan.append(pemasukan)
    elif inputBulan == "Juni" :
        pemasukan = int(input("Masukkan keuntungan : "))
        juniPemasukan.append(pemasukan)
    elif inputBulan == "Juli" :
        pemasukan = int(input("Masukkan keuntungan : "))
        juliPemasukan.append(pemasukan)
    elif inputBulan == "Agustus" :
        pemasukan = int(input("Masukkan keuntungan : "))
        agustusPemasukan.append(pemasukan)
    elif inputBulan == "September" :
        pemasukan = int(input("Masukkan keuntungan : "))
        septemberPemasukan.append(pemasukan)
    elif inputBulan == "Oktober" :
        pemasukan = int(input("Masukkan keuntungan : "))
        oktoberPemasukan.append(pemasukan)
    elif inputBulan == "November" :
        pemasukan = int(input("Masukkan keuntungan : "))
        novemberPemasukan.append(pemasukan)
    elif inputBulan == "Desember" :
        pemasukan = int(input("Masukkan keuntungan : "))
        desemberPemasukan.append(pemasukan)

print("--- Program Pencatatan Laporan Keuangan Bulanan ---")
print()

count = 0
while count < 1000 :
    mainMenu()
    pilihMenu = int(input("Pilih Menu : "))
    if pilihMenu == 1 :
        print()
        keuntungan()
    elif pilihMenu == 2 :
        print("Terima Kasih")
        break
    elif pilihMenu == 3 :
        laba = januariPemasukan[0],februariPemasukan,maretPemasukan,aprilPemasukan,meiPemasukan,juniPemasukan,juliPemasukan,agustusPemasukan,septemberPemasukan,oktoberPemasukan,novemberPemasukan,desemberPemasukan
        print(laba)

    count +=1