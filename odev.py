
class Kütüphane:
    def __init__(self, dosya_adı="books.txt"):
        self.dosya_adı = dosya_adı

    def kitaplar_listele(self):
        with open(self.dosya_adı, "r") as dosya:
            kitap_satırları = dosya.read().splitlines()
            for satır in kitap_satırları:
                kitap_bilgisi = satır.split(',')
                print(f"Kitap: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}")

    def kitap_ekle(self):
        başlık = input("Kitap başlığını girin: ")
        yazar = input("Kitap yazarını girin: ")
        çıkış_yılı = input("İlk çıkış yılını girin: ")
        sayfa_sayısı = input("Sayfa sayısını girin: ")

        kitap_bilgisi = f"{başlık},{yazar},{çıkış_yılı},{sayfa_sayısı}\n"

        with open(self.dosya_adı, "a") as dosya:
            dosya.write(kitap_bilgisi)
        print("Kitap başarıyla eklendi!")

    def kitap_sil(self):
        silinecek_başlık = input("Silmek istediğiniz kitabın başlığını girin: ")

        with open(self.dosya_adı, "r") as dosya:
            kitap_satırları = dosya.read().splitlines()

        yeni_kitap_listesi = [satır for satır in kitap_satırları if silinecek_başlık not in satır]

        with open(self.dosya_adı, "w") as dosya:
            dosya.writelines('\n'.join(yeni_kitap_listesi))
        print(f"'{silinecek_başlık}' başlıklı kitap başarıyla silindi!")


kütüphane_nesnesi = Kütüphane()


while True:
    print("\n*** MENÜ***")
    print("1) Kitapları Listele:")
    print("2) Kitap Ekle:")
    print("3) Kitap Sil:")
    print("4) Çıkış:")

    kullanıcı_girişi = input("Lütfen seçiminizi yapın (1-4): ")

    if kullanıcı_girişi == "1":
        kütüphane_nesnesi.kitaplar_listele()
    elif kullanıcı_girişi == "2":
        kütüphane_nesnesi.kitap_ekle()
    elif kullanıcı_girişi == "3":
        kütüphane_nesnesi.kitap_sil()
    elif kullanıcı_girişi == "4":
        break
    else:
        print("Geçersiz giriş. Lütfen geçerli bir seçenek girin.")


        
