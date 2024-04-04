def cetak_segitiga():
    tinggi = int(input("Tentukan tinggi segitiga: "))
    for i in range(1, tinggi + 1):
        spasi = " " * (tinggi - i)
        bintang = "*" * (i * 2 - 1)
        print(spasi + bintang)

cetak_segitiga()