print("===MENU===\n 1. Pintu dan jendela\n 2. CCTV \n 3. Alarm")
pilihan1 = int(input("Masukkan Pilihan anda : "))
case1= "Pintu dan jendela"
case2= "CCTV"
case3= ("Alarm")
match pilihan1 :
    case 1 :
        print("\t\t1.Mengunci\n\t\t2.Membuka")
        pilihan2 = int(input("Masukkan Pilihan anda : "))
        match pilihan2 :
            case 1 :
                print(case1,"telah terkunci")
            case 2 :
                print(case1, "telah terbuka")
    case 2 :
        print("\t\t1.Nyalakan\n\t\t2.Matikan")
        pilihan2 = int(input("Masukkan Pilihan anda : "))
        match pilihan2 :
            case 1 :
                print(case2, "telah dinyalakan")
            case 2 :
                print(case2, "telah dimatikan")
    case 3 :
        print("\t\t1.Nyalakan\n\t\t2.Matikan")
        pilihan2 = int(input("Masukkan Pilihan anda : "))
        match pilihan2 :
            case 1 :
                print(case3, "telah dinyalakan")
            case 2 :
                print(case3, "telah dimatikan")
    case _:
        print("Input salah")