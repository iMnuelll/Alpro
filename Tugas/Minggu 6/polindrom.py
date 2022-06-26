def polindrome(num):
  return int(str(num)[::-1])
  
bil = (input("Silahkan masukkan bilangan yang anda inginkan : "))
temp = ""
print("Result : ", end="")

for i in range(len(bil)-1, -1, -1): 
    temp+=bil[i]
if(bil == temp): 
    print("Palindrom")
else:
    print("Bukan Palindrom")
print(polindrome(bil))