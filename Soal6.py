import re
import random
import string
def cari_email_dan_buat_password(teks):
    pola_email = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    email_ditemukan = re.findall(pola_email, teks)
    karakter_password = string.ascii_letters + string.digits
    for email in email_ditemukan:
        username = email.split('@')[0]
        password = ''.join(random.choice(karakter_password) for _ in range(8))
        print(f"{email} username: {username} , password: {password}")

teks_input = input("Masukkan teks: ")
cari_email_dan_buat_password(teks_input)
