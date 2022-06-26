nilai = []
print('Nilai Tertinggi ?')
while True :
    input_nilai = input("Masukkan nilai-nilai yang kamu dapatkan ('stop') untuk berhenti : ")
    if input_nilai == 'stop' :
        break
    nilai.append(int(input_nilai))
print('Nilai tertinggi yang Suneo dapatkan pada UTS kali ini : ',max(nilai))