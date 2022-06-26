a = int(input("Masukkan Bilangan 1 : "))
b = input("Masukkan Operasinya (+ -) : ")
c = int(input("Masukkan Bilangan 2 : "))

match b:
    case'+':
        print ("Hasil Operasi",a,'+',c,"=",a+c)
    case'-':
        print("Hasil Operasi",a,'-',c,"=",a-c)
