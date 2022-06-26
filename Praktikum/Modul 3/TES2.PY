print('=== Program perhitungan tinggi badan infinity ===')
print("Ketik 'stop' untuk mengehentikan perulangan")
att = 0
data = []
while True :
    att+=1
    inputtinggi = float(input(f'Masukkan tinggi orang ke - {att} :'))
    data.append(inputtinggi)
    if inputtinggi == 'stop':
        break
        
rataRata = (sum(data) / att )
print('rata - rata tinggi badan adalah ',rataRata)