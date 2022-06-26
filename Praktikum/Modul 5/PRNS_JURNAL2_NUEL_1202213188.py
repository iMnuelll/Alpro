akunDaspro = {
    "Nama" : "Daspro Lab",
    "password" : "D45P120"
}
print("=== MENU ===")
print("1. Ganti nama")
print("2. Ganti password")
print("3. Tampilkan hasil")
print("0. Exit")

while True :
    input_menu = int(input("Pilih Opsi : "))
    if input_menu == 1 :
        nama_akun = input('Masukkan Nama Baru : ')
        akunDaspro["Nama"] = nama_akun
    elif input_menu == 2 :
        password_akun = input("Masukkan Password Baru : ")
        akunDaspro["password"] = password_akun
    elif input_menu == 3 :
        print(akunDaspro)
    elif input_menu == 0 :
        print("Terimakasih sudah menggunakan program kami.")
        break
    else :
        print("Menu yang tersedia hanya 4")