print("===Toko Skincare===")
print("Harga Skincare Whitening = Rp.670.000")
print("Harga Skincare Ulimate Series = Rp.880.000")
print("Harga Skincare Acne Series = Rp.450.000")
whitening = int(input("Jumlah Skincare Whitening : "))
ultimate = int(input("Jumlah Skincare Ultimate Series : "))
acne = int(input("Jumlah Skincare Acne Series : "))
harga_whitening = 670000
harga_ultimate_series = 880000
harga_acne_series = 450000
diskon_whitening = (harga_whitening-(harga_whitening*50/100))*whitening 
diskon_ultimate_series = (harga_ultimate_series-(harga_ultimate_series*30/100))*ultimate  
total = diskon_whitening + diskon_ultimate_series + harga_acne_series
print ("Total Harga = ",total)