def masukkan_data():
    individu = {}
    n = int(input("Tentukan jumlah N : "))

    for i in range(n):
        nama = str(input(f"Masukkan nama ke {i+1}: "))
        nilai = int(input(f"Masukkan nilai {i+1}: "))
        individu[nama] = nilai

    return individu

print(masukkan_data())