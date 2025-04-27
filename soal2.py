def hitung_kemunculan_kata(teks, kata_cari):
    teks_bersih = teks.replace('.', '').replace(',', '').lower()
    kata_cari = kata_cari.lower()
    daftar_kata = teks_bersih.split()
    jumlah = daftar_kata.count(kata_cari)
    return jumlah

kalimat = input("Masukkan kalimat: ")
kata_dicari = input("Masukkan kata yang ingin dicari: ")
jumlah_kemunculan = hitung_kemunculan_kata(kalimat, kata_dicari)

print(f"Kata '{kata_dicari}' ada {jumlah_kemunculan}buah.")
