nim = 1202213188
password = "PestaRahasiaNihBos"
while True :
    inputNim = int(input("Masukkan Kode NIM mu : "))
    inputPass = input("Masukkan password untuk masuk : ")
    try :
        hitung = len(inputPass)
        if hitung < 8 :
            raise NameError
        elif inputPass != password or inputNim != nim :
            print("NIM atau Password salah!")
        elif inputPass == password :
            print("Silahkan Masuk!")
            break
    except NameError :
        print("Password masuk adalah minimal 8 karekter!")