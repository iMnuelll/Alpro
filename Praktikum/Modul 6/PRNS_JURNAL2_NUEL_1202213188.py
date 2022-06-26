print("Silahkan tulis pesan dan kesan kamu untuk Praktikum Alpro 2022!")
print()
print("Mungkin kalian punya masukan, atau  mungkin ada pesan untuk para asisten boleh banget ditulis ya! (Minimal 50 Karekter) \n")
print("=========")
kesan = "Kesan saya selama mengikuti Praktikum Alpro adalah, saya semakin menyukai coding."
pesan = "Pesan yang bisa saya sampaikan untuk abang dan kakak Asisten Terimakasih sudah mengajar dan menumbuhkan minat saya terhadap coding."

data = open("KesanPesan.txt", "a")

data.write(f"{kesan}\n")
data.write(f"{pesan}")
data.close()

print(kesan)
print(pesan)