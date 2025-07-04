import os
import requests
from bs4 import BeautifulSoup

# Hedef URL
url = "https://cvbenim.com/is-ilanlari-sayfa"

# HTML içeriği çek
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# İlan başlıklarını çek
basliklar = soup.find_all("a", class_="ilnBslk")
ilanlar = [b.text.strip() for b in basliklar]
ilanlar = sorted(ilanlar)

# __file__ → çalışan dosyanın yolunu verir
script_adi = os.path.splitext(os.path.basename(__file__))[0]
txt_adi = f"{script_adi}_data.txt"

# Kayıt klasörü ve dosya yolu
klasor = r"C:\Users\ensko\vscodeProjects\scraping_lab\data_record"
os.makedirs(klasor, exist_ok=True)
dosya_yolu = os.path.join(klasor, txt_adi)

# Yazma işlemi
with open(dosya_yolu, "w", encoding="utf-8") as f:
    for ilan in ilanlar:
        f.write(ilan + "\n")

print(f"{len(ilanlar)} ilan 'data_record' dosyasına '{txt_adi}' adıyla yazıldı.")
