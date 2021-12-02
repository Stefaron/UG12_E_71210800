def nilai_maksimal(bilangan):
    terbesar = bilangan[0]

    for i in bilangan:
        if i > terbesar:
            terbesar = i

    return terbesar

def nilai_minimal(bilangan):
    terkecil = bilangan[0]

    for i in bilangan:
        if i < terkecil:
            terkecil = i

    return terkecil


angka1 = [3,20,100,-35,50]
print(angka1)
print("Angka terbesar adalah :", nilai_maksimal(angka1))
print("Angka terkecil adalah :", nilai_minimal(angka1))
    
print("")

angka2 = [3,20,90,35,75]
print(angka2)
print("Angka terbesar adalah :", nilai_maksimal(angka2))
print("Angka terkecil adalah :", nilai_minimal(angka2))