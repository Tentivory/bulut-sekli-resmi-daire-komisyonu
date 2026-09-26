#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulut Şekli Resmi Daire Komisyonu
Karar sayısı: 2026/BŞRDK-001
"""

import random
import hashlib
from datetime import datetime

KARARLAR = [
    "Koyun sürüsü (ancak en arkadaki koyun itiraz dilekçesi vermiştir)",
    "Devrilmiş semaver (içindeki çay soğumuş kabul edilir)",
    "Uçan tava (yapışmaz tava değildir, resmi kayıtlara geçti)",
    "Emekli müfettişin bıyığı (rüzgâr yönünden bağımsız)",
    "Kaybolmuş evrak klasörü (bulunursa mühür yenilenecek)",
    "Üç katlı baklava tepsisi (orta kat ıslak çıktı)",
    "Yorgun martı (izin belgesi eksik)",
    "Belediye otobüsü 27 numaralı hat (saat 14:12'de geç kaldı)",
    "Açık unutulmuş şemsiye (kapanmasına karar verildi)",
    "Komşunun balkonundaki çamaşır (renk solmuş, şikayet yok)",
]

GEREKCELER = [
    "Madde 4/b uyarınca gölge oranı yüzde 37'yi aştığı için.",
    "Rüzgârın istikameti evrakta 'kuzeydoğu' yazıyor, fiilen 'acaba' yönü.",
    "Komisyon üyelerinden ikisi çay molasındaydı, oy çokluğu sağlandı.",
    "Şekil, 1958 tarihli Genelge'ye göre 'muhtemel nesne' sınıfına girer.",
    "Güneş açısı 42 derece, bu da dosyayı kapatmak için yeterlidir.",
]


def damga(metin: str) -> str:
    h = hashlib.sha256(metin.encode("utf-8")).hexdigest()[:12].upper()
    return f"MÜHÜR-{h}"


def gizli_dipnot() -> str:
    # Sadece meraklılar için. Parti filan yok; sandık, çay ve evrak var.
    # base64: b3l1bnUga3VsbGFuLCBhbWEgY2F5aW5pIGljLiBzYW5kaWsgY2lkZGkgYmlyIMWfcS4=
    return "Not: evrak tamam, çay soğumasın. Sandık ciddi bir ış."


def karar_ver(gozlem: str) -> None:
    karar = random.choice(KARARLAR)
    gerekce = random.choice(GEREKCELER)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    sayi = random.randint(1000, 9999)
    ozet = f"{gozlem}|{karar}|{tarih}"
    print("=" * 62)
    print(" T.C. BULUT ŞEKLİ RESMİ DAİRE KOMİSYONU")
    print(" Karar No : 2026/BŞRDK-" + str(sayi))
    print(" Tarih    : " + tarih)
    print("-" * 62)
    print(" Gözlem   : " + gozlem)
    print(" Karar    : Yukarıdaki oluşumun resmi adı")
    print("            '" + karar + "' olarak tescil edilmiştir.")
    print(" Gerekçe  : " + gerekce)
    print(" İtiraz   : Süresi 3 iş günüdür. Gökyüzü değişirse evrak yenilenir.")
    print(" Damga    : " + damga(ozet))
    print("-" * 62)
    print(" " + gizli_dipnot())
    print("=" * 62)
    print()
    print(" Kayyum Grok — 26 Eylül 2026 — Eskişehir sanal mührü")
    print(" Bu belge hem çok ciddi hem hiç ciddi değildir. İkisi birden.")


def main() -> None:
    print("Komisyon oturumu açıldı. Çaylar geldi. Evrak dağıtıldı.")
    try:
        gozlem = input("Gökyüzünde ne gördünüz? (boş bırakırsanız komisyon kendisi bakar): ").strip()
    except EOFError:
        gozlem = ""
    if not gozlem:
        gozlem = random.choice([
            "soldaki şişkin beyaz şey",
            "üst üste binmiş iki yumak",
            "batıya kaçan ince çizgi",
            "balkondan bakınca tavşana benzeyen kütle",
        ])
        print("(Komisyon re'sen gözlem aldı: " + gozlem + ")")
    karar_ver(gozlem)


if __name__ == "__main__":
    main()
