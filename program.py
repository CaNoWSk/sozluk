meme_dict = {
    "char" : "karakter",
    "skin" : "kaplama",
    "skill" : "yetenek",
    "gg" : "iyi oyun",
    "nt" : "iyi deneme",
    "rank" : "derece",
    "drop" : "almak",
    "LOL" : "komik bir şeye verilen cevap",
    "CRINGE" : "garip ya da utandırıcı bir şey",
    "ROFL" : "bir şakaya karşılık cevap",
   "SHEESH" : "onaylamamak",
    "CREEPY" : "korkunç",
    "AGGRO" : "agresifleşmek/sinirlenmek",
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
}

kelimemiz = input("Öğrenmek istediğiniz kelimeyi yazın ")

if  kelimemiz in meme_dict.keys():
     print(meme_dict[kelimemiz])

else :
      print("böyle bir kelime yok ama bana yaz eklerimms")
