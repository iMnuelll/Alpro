banyakbil = int(input("Input banyak bilangan :"))
for i in range (banyakbil + 1) :
    bil = int(input('Input bilangan :'))
    if bil > 0 :
        print(bil, 'adalah bilangan positif')
    elif bil == 0 :
        print(bil, 'adalah bilangan nol')
    else :
        print(bil, 'adalah bilangan negatif')