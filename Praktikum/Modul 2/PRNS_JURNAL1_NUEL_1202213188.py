input1 = input("Peserta 1, Masukkan sinyal tanganmu : ")
input2 = input("Peserta 2, Masukkan sinyal tanganmu : ")
if input1 == input2 :
    print("Hasil seri")
elif input1 == ("gunting") :
    if input2 == ("batu") :
        print("Peserta 1 kalah sehingga Peserta 2 menang")
    elif input2 == ("kertas") :
        print("Peserta 2 kalah sehingga Paserta 1 menang")
elif input1 == ("kertas") :
    if input2 == ("batu") :
        print("Peserta 2 kalah sehingga Peserta 1 menang")
    elif input2 == ("gunting") :
        print("Peserta 1 kalah sehingga Peserta 2 menang")
elif input1 == ("batu") :
    if input2 == ("gunting") :
        print("Peserta 2 kalah sehingga Peserta 1 menang")
    elif input2 == ("kertas") :
        print("Peserta 1 kalah sehingga Peserta 2 menang")