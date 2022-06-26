print('|| Program Tantangan Mr.X ||')
nama = input('Masukkan Nama : ')
id = input('Masukkan ID : ')
divisi = input('Masukkan Divisi : ')
status = input('Masukkan Status : ')

opens = open('tantangan.txt','w')

opens.write(f'Halo, perkenalkan namaku {nama} dengan NIM {id} dan berada di kelas {divisi}. Status hubunganku saat ini {status}. hehehe <3')