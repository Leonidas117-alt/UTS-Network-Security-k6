# UTS Network Security — Kasus K6

Dokumentasi pengerjaan Ujian Tengah Semester (UTS) mata kuliah Network Security.

## Identitas

| Keterangan | Informasi |
|---|---|
| NIM | 24552011376 |
| Jumlah digit NIM | 36 |
| Nomor kasus | K6 |
| Lingkungan | Windows, Docker Desktop, Kali Linux |

## Daftar Tugas

1. Docker dan Volume
2. Kriptografi AES, SHA-256, dan RSA
3. Simulasi ARP dan mitigasi
4. Analisis WPA2 Handshake
5. ICMP dengan Scapy
6. TCP SYN dan Three-Way Handshake
7. DNS Exfiltration Detection

## Struktur Repository

- `01-sumber-lab/` — konfigurasi Docker dan sumber praktikum.
- `02-dokumen/` — hasil praktikum.
- `kasus/` — script Python.
- `ss/` — bukti screenshot setiap tugas.
- `jawaban.md` — laporan jawaban dan analisis.

## Teknologi

- Docker dan Docker Compose
- Kali Linux
- Python dan Scapy
- OpenSSL
- Aircrack-ng
- hping3
- BIND9
- tcpdump

## Catatan Pengujian

Seluruh pengujian dilakukan dalam lingkungan laboratorium Docker yang terisolasi.

Pada tugas WPA2, file capture yang diberikan terdeteksi menggunakan format Ethernet, bukan IEEE 802.11. Aircrack-ng tidak dapat menemukan jaringan wireless dari file tersebut. Hasil ini dilaporkan sesuai keluaran pengujian.

Private key dan file rahasia tidak disertakan dalam repository.
