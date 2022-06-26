print("=== Toko Koomputer Davidcomp ===\n")
merk_laptop = input("Masukkan Merk Laptop : ")
match merk_laptop :
    case'asus':
        print("\t\t--Katalog Laptop ASUS--\n \t\tModel : Asus Vivobook\n \t\tHarga : 5.500.000\n\n \t\tModel: Asus TUF\n \t\tHarga : 12.000.000")
    case'lenovo':
        print("\t\t--Katalog Laptop Lenovo--\n \t\tModel : Lenovo Thinkpad\n \t\tHarga : 7.500.000\n\n \t\tModel: Lenovo Ideapad\n \t\tHarga : 10.000.000") 
    case'acer' :
        print("\t\t--Katalog Laptop Acer--\n \t\tModel : Acer Aspire\n \t\tHarga : 4.500.000\n\n \t\tModel: Acer Swift\n \t\tHarga : 13.000.000") 
    case _:
        print('Laptop merk',merk_laptop,'tidak ada')