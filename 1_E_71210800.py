awal = int(input("Masukkan awal deret : "))
akhir = int(input("Masukkan akhir deret : "))

for i in range(awal,akhir):
    if i %2 == 0 and i%5 !=0 and i%9 != 0:
        print(i, end=" ")