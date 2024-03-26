class Personel:
    def __init__(self, ad, departman, calisma_yili, maas):
        self.ad = ad
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

class Firma:
    personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)
        print("-" * 20)
        print(f"\"{personel.ad}\" kişisi listeye eklendi.")
        print("-" * 20)

    def personel_listele(self):
        print("-" * 20)
        for personel in self.personel_listesi:
            print(f"Ad: {personel.ad}")
            print(f"Departman: {personel.departman}")
            print(f"Çalışma Yılı: {personel.calisma_yili}")
            print(f"Maaş: {personel.maas}")
            print("-" * 20)

    def maas_zammi(self, personel, zam_orani):
        personel.maas *= (1 + zam_orani / 100)
        print("-" * 20)
        print("Maaş zammı gerçekleştirildi.")
        print("-" * 20)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)
        print("-" * 20)
        print("Personel listeden çıkartıldı.")
        print("-" * 20)

def menu():
    while True:
        print("Yapmak istediğiniz işlemi seçiniz:")
        print("1. Personel Ekle")
        print("2. Personel Listele")
        print("3. Maaş Zammı Yap")
        print("4. Personel Çıkar")
        print("5. Çıkış")

        secim = int(input("Seçiminiz: "))

        if secim == 1:
            ad = input("Ad: ")
            departman = input("Departman: ")
            calisma_yili = int(input("Çalışma Yılı: "))
            maas = int(input("Maaş: "))

            personel = Personel(ad, departman, calisma_yili, maas)
            firma.personel_ekle(personel)

        elif secim == 2:
            firma.personel_listele()

        elif secim == 3:
            ad = input("Maaş zammı yapmak istediğiniz personelin adını giriniz: ")
            zam_orani = int(input("Zam oranını giriniz: "))

            for personel in firma.personel_listesi:
                if personel.ad == ad:
                    firma.maas_zammi(personel,zam_orani)
                    break

        elif secim == 4:
            ad = input("Çıkarmak istediğiniz personelin adını giriniz: ")

            for personel in firma.personel_listesi:
                if personel.ad == ad:
                    firma.personel_cikart(personel)
                    break

        elif secim == 5:
            break

        else:
            print("Geçersiz seçim!")

firma = Firma()
menu()