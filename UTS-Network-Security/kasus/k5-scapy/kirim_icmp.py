import sys
from scapy.all import ICMP, IP, sr1

if len(sys.argv) != 2:
    print("Penggunaan: python3 kirim_icmp.py <ip-target>")
    sys.exit(1)

target = sys.argv[1]

paket = IP(dst=target) / ICMP()

print("Mengirim:", paket.summary())

balasan = sr1(paket, timeout=3, verbose=False)

if balasan is None:
    print("Tidak ada balasan.")
else:
    print("TTL balasan:", balasan[IP].ttl)
    print("Tipe ICMP balasan:", balasan[ICMP].type)