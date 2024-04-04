import random

def bentuk_papan():
    return [['?' for _ in range(3)] for _ in range(3)]

def tempatkan_bom(papan):
    baris_bom, kolom_bom = random.randint(0, 2), random.randint(0, 2)
    return baris_bom, kolom_bom

def tampilkan_papan(papan):
    for baris in papan:
        print(' '.join(baris))
    print()

def cek_kemenangan(papan, baris_bom, kolom_bom):
    return all(papan[i][j] != '?' or (i, j) == (baris_bom, kolom_bom) for i in range(3) for j in range(3))

def main():
    print("BEWARE OF MINES!!")
    print("Win without getting hit by a bomb by filling in the numbers 0-2 and containing the 'Row, Column, space'.")
   
    papan = bentuk_papan()
    baris_bom, kolom_bom = tempatkan_bom(papan)
    while True:
        tampilkan_papan(papan)
        try:
            baris, kolom = map(int, input("Enter coordinates (Baris Kolom): ").split())
            if papan[baris][kolom] == '?':
                if (baris, kolom) == (baris_bom, kolom_bom):
                    print("Yikes, you found a bomb, The end :(")
                    papan[baris_bom][kolom_bom] = 'X'
                    tampilkan_papan(papan)
                    break
                print("No bombs here, move on.")
                papan[baris][kolom] = 'O'
                if cek_kemenangan(papan, baris_bom, kolom_bom):
                    print("Congrats! You Win!")
                    break
            else:
                print("The koordinat has been opened")
        except (ValueError, IndexError):
            print("Error! Enter numbers 0-2 for rows and columns, for example 0 1.")

if __name__ == "__main__":
    main()
