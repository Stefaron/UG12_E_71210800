diagonal = int(input("Masukkan Angka : "))

for i in range(diagonal):
    print(" "*(diagonal-i)+" *"*(i+1))

for j in range(diagonal):
    print(" "*(j+2)+" *"*(diagonal-1-j))