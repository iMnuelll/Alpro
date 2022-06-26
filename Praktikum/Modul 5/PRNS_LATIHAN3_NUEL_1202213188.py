print(">> HIMPUNAN <<")

setA = {0,1,2,3,4,5,6,7,8,9,10}
setB = {6,7,8,9,10,11,12,13,14,15}
setC = {16, 17 ,18, 19, 20}
UPdate = setA.union(setB)

print('1. Menggabungkan 2 set (Union)')
print('2. Irisan 2 Set (Intersection)')
print('3. Selisih 2 Set (Difference)')
print('4. New Set (Update)')

def gabung ():
    print(setA.union(setB))
def irisan () :
    print(setA.intersection(setB))
def selisih () :
    print(setA.difference(setB))
def update () :
    print(UPdate.update(setC))

print('Set A berisikan angka : {0,1,2,3,4,5,6,7,8,9,10} ')
print('Set B berisikan angka : {6,7,8,9,10,11,12,13,14,15} ')
while True :
    pilihan = int(input('Pilih opsi : '))
    if pilihan == 1 :
        gabung()
    elif pilihan == 2 :
        irisan()
    elif pilihan == 3 :
        selisih()
    elif pilihan == 4 :
        update()
    else :
        print('Kamu hanya boleh pilih menu sampai 4')
