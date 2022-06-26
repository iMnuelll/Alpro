print('===>>> PROGRAM MANAJEMEN DATA PENDAPATAN PENJUALAN CILOK <<<===')
print('1. Tambah Data Pendapatan')
print('2. Mengurutkan Data (dari yang terbesar)')
print('3. Menghitung Total Data Pendapatan')
print('4. Menghapus Data Pendapatan')
print('5. Menampilkan Seluruh Data Pendapatan')
print('0. Exit')

data_pendapatan = []

def tambah_data_pendapatan() :
        data_Pendapatan = int(input('Masukkan data pendapatan penjualan cilok : '))
        print(f'Data pendapatan penjualan cilok sebesar {data_Pendapatan} berhasil ditambahkan')
        data_pendapatan.append(data_Pendapatan)
def tampilkan_seluruh_data () :
        for i in range (0, len(data_pendapatan)) : 
            print(f'{i+1}. Rp{data_pendapatan[i]}')
def urutan_data_terbesar () :
    data_pendapatan.reverse()
    print('Data penjualan cilok telah diurutkan')
def menghitung_total () :
    jumlah = sum(data_pendapatan)
    print(f'Jumlah pendapatan penjualan cilok adalah {jumlah}')
def menghapus_data () :
    hapus = int(input('Masukkan data yang akan dihapus : '))
    data_pendapatan.remove(hapus)
    print(f'Data pendapatan penjualan cilok sebesar {hapus} berhasil dihapus')

while True :
    pilihan = int(input('Masukkan menu yang Anda Inginkan : '))
    if pilihan == 0 :
        print('Terimakasih sudah menggunakan program kami.')
        break
    elif pilihan == 1 :
        tambah_data_pendapatan()
    elif pilihan == 2 :
        urutan_data_terbesar()
    elif pilihan == 3 :
        menghitung_total ()
    elif pilihan == 4 :
        menghapus_data()
    elif pilihan == 5 :
        tampilkan_seluruh_data()
    else :
        print('Menu yang anda masukkan tidak tersedia, silahkan pilih menu lain')