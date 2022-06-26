input = int(input("Masukkan Umur : "))
if input >= 0 and input <= 5 :
    print("Balita")
elif input >= 6 and input <= 13 :
    print("Anak - anak")
elif input >= 14 and input <= 17 :
    print("Remaja")
elif input >= 18 and input <= 59 :
    print("Dewasa")
elif input >= 60 :
    print("Lansia")