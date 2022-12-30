#########################


#DI buat oleh chat GPT 100%

#########################

import os
import re

# regex untuk alamat IP
ip_regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

# nama folder yang berisi folder dengan nama alamat IP
folder_alamat_ip = "C:/Users/agungsurya/Desktop/snort"

# nama file yang berisi daftar alamat IP yang telah di-block
daftar_alamat_ip_terblokir = "daftar_alamat_ip_terblokir.txt"

# baca daftar alamat IP yang telah di-block dari file
with open(daftar_alamat_ip_terblokir, "r") as f:
    alamat_ip_terblokir = set(f.read().splitlines())

# iterate over the folders in the folder_alamat_ip
for folder in os.listdir(folder_alamat_ip):
    # filter folders yang namanya sesuai dengan regex alamat IP
    if re.match(ip_regex, folder):
        # jalankan perintah iptables untuk memblokir alamat IP jika belum ada dalam daftar terblokir
        if folder not in alamat_ip_terblokir:
            #os.system(f"iptables -A INPUT -s {folder} -j DROP") #tidak di pakai saat ini karena percobaan menggunakan windows hanya print tulisan
            print (f"iptables -A INPUT -s {folder} -j DROP")
            alamat_ip_terblokir.add(folder)

# simpan daftar alamat IP yang telah di-block ke file
with open(daftar_alamat_ip_terblokir, "w") as f:
    for ip in alamat_ip_terblokir:
        f.write(ip + "\n")
