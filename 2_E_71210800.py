senin = ["ke-1 Algoritma Graf","ke-3 Sistem Operasi","ke-4 PAK","ke-5 Praktikum INLAN"]
selasa = ["ke-2 Matematika Teknik","ke-4 Bhs Indonesia","ke-6 PKN"]
kamis = ["ke-1 IMK","ke-3 LogMat","ke-4 Prktekkom"]
jumat = ["ke-2 Sistem Basis Data","ke-4 Praktikum Sistem Basis Data","ke-6 INLAN"]

hari = str(input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri : "))

if hari == "senin":
    for i in senin :
        print("Kelas",i)

elif hari == "selasa":
    for i in selasa:
        print("Kelas",i)

elif hari == "rabu":
    print("Hari rabu Anda tidak ada kelas")

elif hari == "kamis":
    for i in kamis:
        print("Kelas",i)

elif hari == "jumat":
    for i in jumat:
        print("Kelas",i)