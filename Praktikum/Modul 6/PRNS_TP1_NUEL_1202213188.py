try :
    print("[]=== Kalkulator Pintar ===[]")
    angka_1 = int(input('Masukkan Angka Pertama : '))
    angka_2 = int(input('Masukkan Angka Kedua : '))
    print('Pilih Operasi Bilangan : ')
    print('''1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian ''')

    opsi = int(input('Masukkan Operasi : '))
    if opsi == 1 :
        print(f'Hasil penjumlahan : {angka_1+angka_2}')
        print('Terimakasih sudah menggunakan kalkulator pintar!')
    elif opsi == 2 :
        print(f'Hasil penguranan : {angka_1-angka_2}')
        print('Terimakasih sudah menggunakan kalkulator pintar!')
    elif opsi == 3 :
        print(f'Hasil perkalian : {angka_1*angka_2}')
        print('Terimakasih sudah menggunakan kalkulator pintar!')
    elif opsi == 4 :
        print(f'Hasil pembagian : {angka_1/angka_2}')
        print('Terimakasih sudah menggunakan kalkulator pintar!') 

except ValueError :
    print('Program ini hanya menerima jenis nilai integer!')
    print('Terimakasih sudah menggunakan kalkulator pintar!')        
except ZeroDivisionError :
    print('Tidak dapat melakukan pembagian dengan bilangan 0!')
    print('Terimakasih sudah menggunakan kalkulator pintar!')
except TypeError :
    print('Inputan string tidak bisa melakukan operasi aritmatika!')
except NameError :
    print('Variabel tidak tersedia')