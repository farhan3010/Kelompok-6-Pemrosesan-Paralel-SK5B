fileread = open("inputsegitiga.txt", "r")
splitted = fileread.read().split(' ')
angka = list(map(float, splitted))
luas = angka[0] * angka[1]/2
keliling = angka[0] * 3
print("\nLuas Segitiga: ",luas)
print("Keliling Segitiga: ",keliling)