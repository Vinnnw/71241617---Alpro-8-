def kata_terpendek_terpanjang(kalimat):
    kata_list = kalimat.strip().split()
    kata_terpendek = min(kata_list, key=len)
    kata_terpanjang = max(kata_list, key=len)
    return kata_terpendek, kata_terpanjang

kalimat_input = input("Masukkan kalimat: ")
terpendek, terpanjang = kata_terpendek_terpanjang(kalimat_input)

print(f"Kata terpendek: {terpendek}")
print(f"Kata terpanjang: {terpanjang}")
