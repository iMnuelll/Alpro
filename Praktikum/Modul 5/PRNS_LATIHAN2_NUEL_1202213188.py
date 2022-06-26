input_kata = input('Masukkan kata : ').strip()
print('===== Menu Tuple =====')
print('1. Tampilkan kata dalam bentuk tuple')
print('2. Jumlah Huruf')
print('3. Membalik Urutan')
print('0. Exit')

def tampilan_tuple () :
    print('Kata dalam bentuk tuple :', tuple(input_kata))
def jumlah_huruf () :
    print('Jumlah huruf :',len(input_kata))
def membalik_urutan () :
    print('Membalik urutan :',tuple(input_kata[::-1]))

while True :
    pilihan = int(input('Pilih opsi : '))
    if pilihan == 1 :
        tampilan_tuple ()
    elif pilihan == 2 :
        jumlah_huruf ()
    elif pilihan == 3 :
        membalik_urutan ()
    elif pilihan == 0 :
        break
    else :
        print('Masukkan pilihan lain')