# 🔐 Türkçe Alfabe Kaydırmalı Şifreleme Sistemi

Bu Python projesi, Türkçe alfabeye özel olarak hazırlanmış bir **harf kaydırmalı (shift-based) şifreleme ve çözme** sistemidir. Kullanıcı, bir metni şifreleyebilir veya şifrelenmiş bir metni çözebilir.

---

## 📌 Özellikler

- Türkçe karakterler desteklenir (ç, ğ, ı, ö, ş, ü).
- Özel karakterler ve boşluklar bozulmadan korunur.
- Alfabe kaydırması mantığına dayanır (a → ç, b → d, ... z → c).

---

## 🧠 Nasıl Çalışır?

İki farklı liste kullanılır:

- `aHarf`: Türkçe alfabenin normal sıralaması.
- `bHarf`: `aHarf`'in her harfi 3 karakter ileri kaydırılmış halidir (mod 29).

### 🔄 Şifreleme

Her harf, `aHarf` listesindeki konumuna göre `bHarf` listesinden karşılık gelen harfe dönüştürülür.

### 🔓 Şifre Çözme

`bHarf` listesindeki her harf, `aHarf`'teki orijinal karşılığına dönüştürülür.

---

## 🚀 Kullanım

1. Python yüklü olmalıdır (3.x).
2. Terminalden çalıştır:

```bash
python cesar.py
