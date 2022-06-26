print("-----Silahkan Login-----")
percobaan = 3
while True :
    username = input("Masukkan username :")
    password = input("Masukkan password :")
    if username == "qwerty" and password == "kijolp" :
        print("Anda berhasil login")
        break
    else :
        percobaan -=1
        print('Gagal login,',percobaan,'percobaan tersisa')
        if percobaan == 0 :
            print('Anda dikeluarkan dari sistem')
            break
