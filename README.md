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
