import re
from datetime import datetime
def cari_tanggal(teks):
    pola = r'\d{4}-\d{2}-\d{2}'
    tanggal_ditemukan = re.findall(pola, teks)
    tanggal_sekarang = datetime.now()
    for tgl_str in tanggal_ditemukan:
        tanggal_objek = datetime.strptime(tgl_str, "%Y-%m-%d")
        selisih_hari = (tanggal_sekarang - tanggal_objek).days
        print(f"{tanggal_objek} selisih {selisih_hari} hari")

teks_input = input("Masukkan teks: ")
cari_tanggal(teks_input)
