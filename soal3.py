def hapus_spasi_berlebih(teks):
    kata = teks.strip().split()
    hasil = ' '.join(kata)
    return hasil
teks_input = input("Masukkan teks: ")

output = hapus_spasi_berlebih(teks_input)

print("Output setelah dihapus spasi berlebih:")
print(output)
