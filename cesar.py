aHarf = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ",
         "h", "ı", "i", "j", "k", "l", "m", "n", "o",
         "ö", "p", "r", "s", "ş", "t", "u", "ü", "v",
         "y", "z"]

bHarf = ["ç", "d", "e", "f", "g", "ğ", "h", "ı", "i",
         "j", "k", "l", "m", "n", "o", "ö", "p", "r",
         "s", "ş", "t", "u", "ü", "v", "y", "z", "a",
         "b", "c"]

sifre = input("Şifre Kırmak İçin 1. Şifre Oluşturmak İçin 2: ")

if(sifre == "1"):
    metin = input("Çözmek istediğiniz şifreli metni girin: ")
    cozum = ""

    for harf in metin:
        if harf in bHarf:
            index = bHarf.index(harf)
            cozum += aHarf[index]
        else:
            cozum += harf  # boşluk, nokta vs. aynen eklenir

    print("Çözülen Metin:", cozum)

elif(sifre == "2"):
    metin = input("Şifrelemek istediğiniz metni girin: ")
    sifreli = ""

    for harf in metin:
        if harf in aHarf:
            index = aHarf.index(harf)
            sifreli += bHarf[index]
        else:
            sifreli += harf  # boşluk, nokta vs. aynen eklenir

    print("Şifreli Metin:", sifreli)

else:
    print("Hatalı Giriş Tekrar Deneyiniz.")