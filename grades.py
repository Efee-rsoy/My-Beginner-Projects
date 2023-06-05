Ogrenciler = {"Efe": {"Not":15, "No":365},
               "Zeynep": {"Not":80, "No": 55}, 
               "Ali": {"Not":56, "No": 985}, 
               "Atakan":{"Not":74, "No": 91}}
isim = input("Bir İsim Giriniz: ").lower()
if isim == "efe":
    print(Ogrenciler["Efe"])
elif isim == "zeynep":
    print(Ogrenciler["Zeynep"])
elif isim == "ali":
    print(Ogrenciler["Ali"])
elif isim == "atakan": 
    print(Ogrenciler["Atakan"])