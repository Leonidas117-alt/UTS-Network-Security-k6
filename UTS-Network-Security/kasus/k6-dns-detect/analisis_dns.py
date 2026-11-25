
import re
import sys

DOMAIN = "k6.exfil.lab"

if len(sys.argv) != 2:
    print("Penggunaan: python analisis_dns.py <file-log>")
    sys.exit(1)

log_file = sys.argv[1]

with open(log_file, "r", encoding="utf-8", errors="ignore") as file:
    logs = file.read()

# Mencari label hexadecimal sebelum domain lab
pattern = r"\b([0-9a-fA-F]+)\." + re.escape(DOMAIN) + r"\b"

matches = re.findall(pattern, logs, re.IGNORECASE)

if not matches:
    print("Tidak ditemukan label hexadecimal untuk", DOMAIN)
    sys.exit(0)

for hex_data in sorted(set(matches)):
    try:
        decoded = bytes.fromhex(hex_data).decode("utf-8")
        print("Label HEX terdeteksi:", hex_data)
        print("Hasil decode:", decoded)
    except (ValueError, UnicodeDecodeError):
        print("Label ditemukan tetapi gagal di-decode:", hex_data)
