#pylint:disable=E0001
#pylint:disable=E0001
import platform
import psutil
import cpuinfo
import sys
import socket
import time
import pyfiglet
import requests
import webbrowser
from bs4 import BeautifulSoup

isim = pyfiglet.figlet_format("***MR GESTALT***")
time.sleep(1)
print(isim)
time.sleep(1)
print("Devices Infos")
time.sleep(1)
print("---------------------------------------------")
time.sleep(1)
print("1-)Bilgileri Göster")
time.sleep(1)
print("-" * 45)
time.sleep(1)
print("2-)Site Ip Sorgu")
print("-" * 45)
time.sleep(1)
print("3-)Koddan cık")
time.sleep(1)
print("-" * 45)


def sistem_bilgileri():
    time.sleep(1)
    print("===== İşletim Sistemi Bilgileri =====")
    os_bilgileri = platform.uname()
    time.sleep(1)
    print(f"Sistem: {os_bilgileri.system}")
    print(f"Node Adı: {os_bilgileri.node}")
    print(f"Sürüm: {os_bilgileri.release}")
    print(f"Sürüm: {os_bilgileri.version}")
    print(f"Makine: {os_bilgileri.machine}")
    print(f"İşlemci: {os_bilgileri.processor}")
    print(f"Api Versiyon: {sys.api_version}")

    print("\n===== CPU Bilgileri =====")
    cpu_bilgileri = cpuinfo.get_cpu_info()
    time.sleep(1)
    print(f"CPU Marka ve Model: {cpu_bilgileri['brand_raw']}")
    print(f"Arch: {cpu_bilgileri['arch']}")
    print(f"Bits: {cpu_bilgileri['bits']}")
    print(f"Yarıklar: {cpu_bilgileri['count']}")

    print("\n===== Ağ Bilgileri =====")
    host_adı = socket.gethostname()
    ip_adresi = socket.gethostbyname(host_adı)
    time.sleep(1)
    print(f"Host Adı: {host_adı}")
    try:
        api = "https://ipinfo.io/json"
        istek = requests.get(api)
        data = istek.json()
        print("Internet Bağlantısı Başarılı")
        print(f"IP Adresi: {data['ip']}")
        print(f"Local Host IP Adresi: {ip_adresi}")
    except requests.exceptions.RequestException:
        print("Internet bağlantısı başarısız. Lütfen internete bağlanın.")
        
def site():
   site = input("Site Isim: ") 
   url = f"https://www.ipsorgu.com/site_ip_adresi_sorgulama.php?site={site}#sorgu_sonuc"
   istek2 = requests.get(url)
   if istek2.status_code == 200:
      cekme = BeautifulSoup(istek2.text, "html.parser")    
      baslik = cekme.title.string
      print(baslik)
   else:
      print("Istek basarisiz oldu")                             
while True:
   try:
      choise = input("Seçimin: ")
      time.sleep(1)
      print("-" * 45)
      time.sleep(1)
      print("\n")
      if choise == "1":
         time.sleep(1)
         sistem_bilgileri()
         time.sleep(3)
         print("-" * 45)
         time.sleep(1)
         print("\n")
      elif choise == "2":
         time.sleep(1)
         site()
         time.sleep(1)
      elif choise == "3":
         print("Tamam")
         break
   except Exception as e:
      print(f"Hata:{e}")
