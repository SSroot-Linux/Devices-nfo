import platform
import psutil
import cpuinfo
import sys
import socket
import time
import pyfiglet
import requests

isim = pyfiglet.figlet_format("***MR GESTALT***")
print(isim)

print("Devices Infos")
print("---------------------------------------------")
print("1-)Bilgileri Göster")
print("2-)Koddan cık")


def sistem_bilgileri():
    print("===== İşletim Sistemi Bilgileri =====")
    os_bilgileri = platform.uname()
    print(f"Sistem: {os_bilgileri.system}")
    print(f"Node Adı: {os_bilgileri.node}")
    print(f"Sürüm: {os_bilgileri.release}")
    print(f"Sürüm: {os_bilgileri.version}")
    print(f"Makine: {os_bilgileri.machine}")
    print(f"İşlemci: {os_bilgileri.processor}")
    print(f"Api Versiyon: {sys.api_version}")

    print("\n===== CPU Bilgileri =====")
    cpu_bilgileri = cpuinfo.get_cpu_info()
    print(f"CPU Marka ve Model: {cpu_bilgileri['brand_raw']}")
    print(f"Arch: {cpu_bilgileri['arch']}")
    print(f"Bits: {cpu_bilgileri['bits']}")
    print(f"Yarıklar: {cpu_bilgileri['count']}")

    print("\n===== Ağ Bilgileri =====")
    host_adı = socket.gethostname()
    ip_adresi = socket.gethostbyname(host_adı)
    print(f"Host Adı: {host_adı}")
    api = "https://ipinfo.io/json"
    istek = requests.get(api)
    data = istek.json()
    if istek.status_code == 200:
       print("Internet Baglantisi Basarili")
       print(f"Ip Adresi: {data['ip']}")
       print(f"Local Host IP Adresi: {ip_adresi}")
       

while True:
   try:
      choise = input("Secimin: ")
      if choise == "1":
         time.sleep(1)
         sistem_bilgileri()
         time.sleep(1)
         secim = input("Entere bas ")
         if secim == "":
            break
      elif choise == "2":
         print("Tamam")
         break
   except:
      print("HATA")      
