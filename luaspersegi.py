fileread = open("inputpersegi.txt", "r")
splitted = fileread.read().split(' ')
sisi = list(map(float, splitted))
luas = sisi[0] * sisi[1]
keliling = sisi[0] * 4
print("\nLuas Persegi: ",luas)
print("Keliling Persegi: ",keliling)