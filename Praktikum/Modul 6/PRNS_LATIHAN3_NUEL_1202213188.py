nama = ("Imanuel Uneputty")
kelas = ("SI-45-03")
nim = (1202213188)
motto = ("Jaya Jaya Jaya")

buka = open("Tambahin.txt","a")

buka.write(f"Nama : {nama}\n")
buka.write(f"Kelas : {kelas}\n")
buka.write(f"NIM : {nim}\n")
buka.write(f"Motto : {motto}\n")

buka.close()