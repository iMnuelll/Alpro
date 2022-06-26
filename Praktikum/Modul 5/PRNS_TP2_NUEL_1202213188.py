angka1 = set([])
angka2 = set([])
inputan = int(input('Masukkan Banyak Angka : '))
for i in range(inputan) :
    input_angka = int(input('Masukkan angka : '))
    angka1.add(input_angka)
    angka2.add(input_angka)
    i+=1
    
print(angka1 | angka2)