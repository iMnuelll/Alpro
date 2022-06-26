angka = []
jum = 0
try :
    print('PROGRAM MENGHITUNG RATA - RATA')
    awal = int(input('Ingin menghitung berapa nilai : '))
    for i in range(0, awal) :
        i+=1
        nilai = int(input(f'Nilai Ke {i}: '))
        angka.append(nilai)
    rata2 = sum(angka) / awal
    print('Hasil rata-rata yang di dapat adalah',rata2)
except ValueError :
    print('Program ini hanya menerima inputan angka!')
finally :
    print("Program Selesai...")