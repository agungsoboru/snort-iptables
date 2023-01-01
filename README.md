# snort-iptables
integrasi snort ids untuk mendeteksi anomali pada jaringan lalu memblokir ip yang membuat masalah menggunakan firewall iptables atau iptables port bloking dengan kode program python


anda harus punya snort

2 log snort harus ada alert di /var/log/snort/ 

alert harus ada klasifikasi nama folder menggunakan ip seperti contoh folder snort di repo saya yang ini

jangan lupa program berada di fodler yang ada ip folder itu 

lalu setelah semua log ada seperti sampel file snort di repo saya itu jalankan program dan uncomment line iptables nya untuk menjalankan command

# note 
jika hanya mencoba anda tidk harus melakukan instalasi snort cukup masukan kode program main ke folder snort lalu tambahkan folder dengan nama alamat ip contohnya 192.168.43.2

lalu jalankan program

lalu tambahkan folder lagi alamat ip contoh 202.245.2.100 lalu jalankan lagi program

# note install snort



Siapkan Pendukung
Cek repository

apt update

Cek Jaringan
ifconfig
catat nama interface yang nanti akan di monitor

enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.169  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::a00:27ff:fe2c:cc3c  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:2c:cc:3c  txqueuelen 1000  (Ethernet)
        RX packets 34056  bytes 43367030 (43.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4141  bytes 337064 (337.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

maka interface yang dimonitor adalah

enp0s3

Siapkan Aplikasi Pendukung
sudo locale-gen id_ID.UTF-8
apt update
apt -y install oinkmaster snort snort-common snort-rules-default snort-doc
Akan di tanya

interface yang akan di monitor, misalnya enp0s3
range IP yang di monitor, misalnya 192.168.0.0/24
Cek Snort
snort -C
Jalankan Snort mode NIDS
snort -dev -l /var/log/snort/ -h 192.168.0.0/24 -c /etc/snort/snort.conf &
kalau ingin supaya bisa di baca di kemudian hari oleh wireshark harus di simpan dalam bentuk binary, dengan perintah

/usr/sbin/snort -m 027 -b -l /var/log/snort/ -u agung -c /etc/snort/snort.conf -S HOME_NET=[192.168.0.0/24] -i enp0s3 &
Supaya tidak rewel, sebaiknya permission /var/log/snort di jadikan

chmod 770 /var/log/snort
ini sebetulnya cara yang tidak baik.

Menjalankan Snort mode NIDS, log text
Agar log /var/log/snort bisa di baca oleh manusia, kita bisa menjalankan snort dengan perintah,

snort -c /etc/snort/snort.conf -l /var/log/snort/ -K ascii -D


# referensi

https://lms.onnocenter.or.id/wiki/index.php/SNORT:_Install_SNORT_saja_Ubuntu_20.04

kalau gasalah command ini   snort -c /etc/snort/snort.conf -l /var/log/snort/ -K ascii -D 

untuk menjalankan snort di command itu tambahkan -i ens160 misalnya nama interface 

coba cari saya lupa 
