# LAPORAN UTS NETWORK SECURITY
## Kasus K6

**NIM:** 24552011376  
**Jumlah digit NIM:** 36  
**Nomor Kasus:** K6

---

# Tugas 1 — Docker dan Volume

## Tujuan
Memahami penggunaan Docker container, Docker network, dan volume untuk menyimpan data secara persisten.

## Proses
Praktikum dilakukan menggunakan Docker Compose dengan container target dan attacker pada jaringan laboratorium.

## Hasil
Pengujian dilakukan untuk memastikan container berjalan, jaringan Docker terbentuk, dan data tetap tersimpan menggunakan volume.

## Analisis
Docker memungkinkan beberapa sistem berjalan dalam lingkungan terisolasi. Volume digunakan agar data tetap tersedia meskipun container dihentikan atau dibuat ulang.

---

# Tugas 2 — Kriptografi

## Tujuan
Memahami proses enkripsi, dekripsi, hashing, dan penggunaan pasangan kunci RSA.

## Proses
- Enkripsi dan dekripsi menggunakan AES-256-CBC dengan PBKDF2.
- Integritas data diperiksa menggunakan SHA-256.
- Membuat pasangan kunci RSA 2048-bit dan sertifikat self-signed.

## Hasil
Hash SHA-256 sebelum dan sesudah proses dekripsi:

`ba00dcca033b5d1bcd46a143d134172554ea37b3a4849e4e98297e9846aaef54`

Hasil hash cocok, sehingga isi file hasil dekripsi sesuai dengan file aslinya.

## Analisis
AES digunakan untuk menjaga kerahasiaan data, SHA-256 untuk memeriksa integritas, dan RSA untuk kriptografi kunci publik.

Private key tidak disertakan dalam repository.

---

# Tugas 3 — Simulasi ARP

## Tujuan
Memahami cara kerja ARP dan risiko manipulasi ARP cache.

## Proses
Dilakukan simulasi perubahan entri ARP pada lingkungan Docker lokal. Selanjutnya, entri ARP diperbaiki menggunakan permanent neighbor entry.

## Hasil
Alamat IP dan MAC address dari container korban, gateway, dan penyerang diamati selama simulasi.

## Analisis
ARP digunakan untuk memetakan alamat IP ke alamat MAC dalam jaringan lokal. Manipulasi ARP cache dapat menyebabkan komunikasi diarahkan ke perangkat yang salah. Entri ARP permanen dapat membantu mencegah perubahan dinamis yang tidak diinginkan.

---

# Tugas 4 — Analisis WPA2 Handshake

## Tujuan
Memahami analisis file capture WPA2 menggunakan Aircrack-ng.

## Proses
Menjalankan perintah:

`aircrack-ng -w wordlist-k6.txt handshake-k6.cap`

## Hasil
Pengujian menghasilkan pesan:

`This file is not a regular 802.11 (wireless) capture.`

Dilanjutkan dengan:

`Read 0 packets. No networks found, exiting.`

Pemeriksaan metadata menunjukkan file menggunakan format PCAP dengan link-layer type Ethernet, bukan IEEE 802.11.

## Analisis
Aircrack-ng membutuhkan paket wireless 802.11 untuk menganalisis handshake WPA2. Karena file yang diberikan berisi format Ethernet, proses analisis tidak dapat dilanjutkan.

Dengan demikian, password tidak berhasil ditemukan maupun dinyatakan `KEY NOT FOUND`. Diperlukan file capture wireless yang benar dari penguji.

### Empat tahap WPA2 Four-Way Handshake
1. AP mengirim ANonce kepada client.
2. Client membuat PTK dan mengirim SNonce serta MIC.
3. AP memverifikasi MIC dan mengirim pesan instalasi kunci serta GTK.
4. Client mengirim konfirmasi bahwa kunci telah terpasang.

---

# Tugas 5 — ICMP dengan Scapy

## Tujuan
Memahami pengiriman dan analisis paket ICMP menggunakan Python Scapy.

## Proses
Script `kirim_icmp.py` digunakan untuk mengirim ICMP Echo Request ke target dalam jaringan Docker.

## Hasil
Output pengujian:
- TTL balasan: `64`
- Tipe ICMP balasan: `0`

## Analisis
ICMP Type 8 merupakan Echo Request, sedangkan Type 0 merupakan Echo Reply. Balasan Type 0 menunjukkan bahwa target merespons permintaan ICMP.

Pengujian ini merupakan pengiriman ICMP biasa, bukan pelaksanaan Smurf Attack.

---

# Tugas 6 — TCP SYN dan Three-Way Handshake

## Tujuan
Memahami proses pembentukan koneksi TCP dan mengamati paket SYN.

## Proses
Koneksi HTTP diuji dari container attacker menuju target. Selanjutnya dilakukan pengiriman lima paket SYN secara terbatas menggunakan hping3 dan pengamatan menggunakan tcpdump.

## Hasil
Pengujian HTTP menghasilkan:

`HTTP/1.1 200 OK`

Pengujian hping3 mengirim lima paket SYN dan menerima lima balasan SYN-ACK dengan packet loss 0%.

Pengamatan tcpdump menunjukkan tiga tahap:
1. SYN
2. SYN-ACK
3. ACK

Jumlah koneksi SYN_RECV yang diamati setelah pengujian adalah 0.

## Analisis
Three-Way Handshake merupakan proses pembentukan koneksi TCP. Pengujian ini hanya mengirim lima paket SYN secara terbatas untuk pembelajaran, bukan serangan SYN Flood berskala besar.

---

# Tugas 7 — DNS Exfiltration Detection

## Tujuan
Memahami simulasi penyisipan data dalam query DNS dan mendeteksi label hexadecimal.

## Proses
BIND9 dikonfigurasi untuk domain:

`k6.exfil.lab`

Data NIM dikonversi menjadi hexadecimal dan digunakan sebagai subdomain dalam query DNS.

## Hasil
Query DNS:

`3234353532303131333736.k6.exfil.lab`

Alamat IP hasil resolusi:

`172.21.0.2`

Hasil analisis script Python:

```text
Label HEX terdeteksi: 3234353532303131333736
Hasil decode: 24552011376
```

## Analisis
Data hexadecimal dapat disisipkan ke dalam label subdomain DNS. Script Python mendeteksi label tersebut, kemudian mengubahnya kembali menjadi teks. Pola seperti ini dapat digunakan untuk membantu mengidentifikasi indikasi DNS tunneling atau DNS exfiltration.

---

# Kesimpulan

Praktikum ini memberikan pemahaman mengenai containerisasi, kriptografi, ARP, analisis paket jaringan, protokol ICMP dan TCP, serta pemantauan query DNS.

Sebagian besar pengujian berhasil dilakukan dalam lingkungan Docker terisolasi. Pada tugas WPA2, analisis tidak dapat dilakukan karena file capture yang tersedia menggunakan format Ethernet, bukan IEEE 802.11. Keterbatasan tersebut dicatat sesuai hasil pengujian.

Seluruh hasil dan bukti praktikum disimpan pada folder `ss/`.