import random
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GG" : "iyi oyundu",
            "wydm" :"ne demek istiyorsun",
            "Ez" : "kolaydı",
            }
print(meme_dict["LOL"]) 
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("böyle bir sözcük yok")
