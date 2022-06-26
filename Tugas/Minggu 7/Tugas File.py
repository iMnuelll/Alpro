print('=== Program Biodata ===')
jumlah = 5

print('Pencobaan hanya boleh dilakukan dua kali, jika lebih program akan berhenti')
def nama() :
    with open('Nama.txt','r+') as f :
        for i in range(jumlah) :
            i +=1
            nama = input(f'Masukkan nama ke - {i}: ')
            f.write(f'{nama}\n')

def umur() :
    with open('Umur.txt','r+') as f :
        for i in range(jumlah) :
            i +=1
            umur = int(input(f'Masukkan umur orang ke - {i} : '))
            f.write(f'{umur}\n')

def namaUmur () :
    with open('Nama.txt','r') as pertama :
        with open('Umur.txt','r') as kedua :
            with open('namaUmur.txt','r+') as ketiga :
                for baris1, baris2 in zip(pertama, kedua):
                    ketiga.write('{} {}\n'.format(baris1.rstrip(), baris2.rstrip()))
                for line in ketiga :
                    print(line, end='')

while True:
    coba = 1
    coba <= 2
    filepertama = 'Nama.txt'
    ask1 = input("Masukkan Nama file pertama : ")
    if ask1 == filepertama :
        try:
            f = open(ask1,'r')
        except FileNotFoundError:
            print(f'File {ask1} tidak ditemukan') 
        except :
            print('Ada yang salah ketika menuliskan nama file')
        else :
            print('File bisa terbuka')
        finally :
            print('try,except, dan finally telah selesai dikerjakan')
        nama()
        break
    elif ask1 != filepertama :  
        try:
            f = open(ask1,'r')
        except FileNotFoundError:
            print(f'File {ask1} tidak ditemukan') 
        except :
            print('Ada yang salah ketika menuliskan nama file')
        else :
            print('File bisa terbuka')
        finally :
            print('try,except, dan finally telah selesai dikerjakan')
        coba +=1
        print(f'Percobaan ke {coba}')
        ask1 = input("Masukkan Nama file pertama : ")
        if ask1 == filepertama:
            try:
                f = open(ask1,'r')
            except FileNotFoundError:
                print(f'File {ask1} tidak ditemukan')
            except :
                print('Ada yang salah ketika menuliskan nama file')
                break
            else :
                print('File bisa terbuka')
            finally :
                print('try,except, dan finally telah selesai dikerjakan')
            nama()
            break
        elif ask1 != filepertama or coba == 2:
            try:
                f = open(ask1,'r')
            except FileNotFoundError:
                print(f'File {ask1} tidak ditemukan')
            except :
                print('Ada yang salah ketika menuliskan nama file')
                break
            else :
                print('File bisa terbuka')
            finally :
                print('try,except, dan finally telah selesai dikerjakan')
            break
print('--------------------')

while True:
    coba = 1
    coba <= 2
    filekedua = 'Umur.txt'
    ask1 = input("Masukkan Nama file kedua : ")
    if ask1 == filekedua :
        try:
            f = open(ask1,'r')
        except FileNotFoundError:
            print(f'File' +ask1+ 'tidak ditemukan') 
        except :
            print('Ada yang salah ketika menuliskan nama file')
        else :
            print('File bisa terbuka')
        finally :
            print('try,except, dan finally telah selesai dikerjakan')
        umur()
        namaUmur()
        break
    elif ask1 != filekedua :
        try:
            f = open(ask1,'r')
        except FileNotFoundError:
            print('File' +ask1+ 'tidak ditemukan')
        except :
            print('Ada yang salah ketika menuliskan nama file')
                
        else :
            print('File bisa terbuka')
        finally :
            print('try,except, dan finally telah selesai dikerjakan')  
        coba +=1
        print(f'Percobaan ke {coba}')
        ask1 = input("Masukkan Nama file kedua : ")
        if ask1 == filekedua:
            try:
                f = open(ask1,'r')
            except FileNotFoundError:
                print('File' +ask1+ 'tidak ditemukan')
            except :
                print('Ada yang salah ketika menuliskan nama file')
                
            else :
                print('File bisa terbuka')
            finally :
                print('try,except, dan finally telah selesai dikerjakan')
        umur()
        namaUmur()
        break
    elif ask1 != filekedua or coba == 2:
        try:
            f = open(ask1,'r')
        except FileNotFoundError:
            print(f'File {ask1} tidak ditemukan')
        except :
            print('Ada yang salah ketika menuliskan nama file')
        
        else :
            print('File bisa terbuka')
        finally :
            print('try,except, dan finally telah selesai dikerjakan')
        break
print('--------------------')
print('Penggabungan Dua File')
f = open('namaUmur.txt','r')
print (f.read())