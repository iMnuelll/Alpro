print('=== Program perhitungan tinggi badan infinity ===')
print("Ketik 'stop' untuk mengehentikan perulangan")
att = 0
data = []
while True :
    att+=1
    inputtinggi = input(f'Masukkan tinggi orang ke - {att} :')
    if inputtinggi == 'stop':
        break
    else:
        data.append(int(inputtinggi))

rataRata = (sum(data) / len(data) )
print('rata - rata tinggi badan adalah ',rataRata)