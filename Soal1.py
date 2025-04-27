def cek_anagram(kata1, kata2):
    kata1_urut = sorted(kata1.lower())
    kata2_urut = sorted(kata2.lower())
    
    return kata1_urut == kata2_urut

kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

if cek_anagram(kata_pertama, kata_kedua):
    print(f"{kata_pertama} dan {kata_kedua} adalah anagram.")
else:
    print(f"{kata_pertama} dan {kata_kedua} bukan anagram.")
