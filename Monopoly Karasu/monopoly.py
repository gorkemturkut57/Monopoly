def kurallar():
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    print("""Oyun Kuralları:
--> "Zar at:" Seçeneği çıktıktan sonra Enter'a basıldığında oyun otomatik olarak 2 tane zar atacaktır.
--> Aloğlu Köyüne giden kişi mito ona balya çektirdiği için 2 tur orda kalacak,diğer oyuncular onun dükkanına geldiğinde kira alamayacak ve diğer oyuncularla pazarlık yapamayacaktır.
--> Çelene veya Mücoya gidersen mitoya benzin parası vereceğin için gerekli miktar bakiyenden düşecek.
--> Dükkanların maaliyeti yanında yazdığı değer kadardır.Eğer sayının başında eksi varsa bu kasaya ödeme yapılacağı anlamına gelir.
--> Eğer sayının başında artı varsa bu kasadan para alacağın anlamına gelir.
--> Satın alınmış bölgelerin altı sahibinin rengi ile boyalıdır.
--> Oyuncunun olduğu yerin ismi oyuncunun rengiyle yazılıdır.
--> Bir oyuncu başkası tarafından satın alınmış yere gelirse oranın kirasını ödemek zorundadır.
--> Bul garayı al parayı olan yerlere geldiğinde sistem otomatik olarak oyuncu için bir şans kartı çeker.
--> A31 ve Bim'in ikisine de sahip olan kişi,buraya gelen kişilerden kiranın 2 katı kadar ücret alır.
--> Her oyuncunun başlangıçta 20000TL parası var
-->Parası eksiye düşen oyuncunun aldığı arsalar son aldığından ilk aldığına doğru sıfıra eşit veya sıfırdan büyük olana kadar kendi ücretinin yarı fiyatına satılır.
 """)
    print("Oyuncuların Renkleri:")
    print(Fore.RED+"1.Oyuncu KIRMIZI")
    print(Fore.GREEN+"2.Oyuncu YEŞİL")
    print(Fore.BLUE+"3.Oyuncu MAVİ")
    print(Fore.YELLOW+"4.Oyuncu SARI")
    print("Dükkanların Kiraları:")
    print("""-Demircan Tekel:1000
-Yüksel Berber:1200
-Yovuz Arıcı:900
-A31:2000
-Galeri Mito:2100
-Motor Kazım:1300
-Karasu Köfte Dünyası:1500
-Nesrin Havlu:31
-Gürcü'nün Kahve:1600
-Resul'ün Kahve:1400
-Öztürk Gebelit:3500
-KafeCİ:5000
-Bim:1500
-ClupŞahane:4000
-Ayakkap Dünyası mito:1000
-Akoğlu Kasap:3000
---------------------------------------------------------------------------------------""")
kurallar()
def tablo_olustur(tablo=[["|Başlangıç(+10000)|","|Demircan Tekel(2000)|","|Yüksel Berber(2500)|","|Bul garayı al parayı|","|Çelen(-3000)|","|Yovuz Arıcı(1000)|","|A31(4000)|"," |Serbest Bölge|"],["|Galeri Mito(5000)|","  |Ayakkap Dünyası mito(2000)|"],["|Motor Kazım(2500)|","  |Karasu Köfte Dünyası(3000)|"],["|Nesrin Havlu(500)|","  |Gürcü'nün  Kahvesi  (3000)|"],["|Alaoğlu Köyü Mito|","|Resul'ün Kahve(3000)|","|ÖztürkGebelit(6000)|","|Bul garayı al parayı|","|KafeCİ(8000)|","|MücoBenzin(-6000)|","|Bim(3000)|","|ClupŞahane6000|"]]):
    say=0
    for i in tablo:
        say+=1
        sayac=0
        for j in i:
            sayac+=1
            if (say==1 and sayac==8) or (2<=say<=4 and sayac==2):
                print(j)
            elif (2 <= say <= 4 and sayac == 1):
                if say==3 and sayac==1 :
                    print(j,"                                        MONOPOLY KARASU",
                          end="                                              ")
                else:
                    print(j,
                          end="                                                                                                      ")
            else:
                print(j,end=" ")
def zar_at():
    import random
    zar=random.randint(2,12)
    return zar
def main():
    import colorama
    from colorama import Fore, Back
    colorama.init(autoreset=True)
    oyuncuların_zarları={"oyuncu1":0,"oyuncu2":0,"oyuncu3":0,"oyuncu4":0}
    oyuncuların_paraları={"oyuncu1":20000,"oyuncu2":20000,"oyuncu3":20000,"oyuncu4":20000}
    oyuncu1_arsalar=[]
    oyuncu2_arsalar=[]
    oyuncu3_arsalar = []
    oyuncu4_arsalar = []
    tablo=[["|Başlangıç(+10000)|","|Demircan Tekel(2000)|","|Yüksel Berber(2500)|","|Bul garayı al parayı|","|Çelen(-3000)|","|Yovuz Arıcı(1000)|","|A31(4000)|"," |Serbest Bölge|"],["|Galeri Mito(5000)|","  |Ayakkap Dünyası mito(2000)|"],["|Nesrin Havlu(500)|","  |Karasu Köfte Dünyası(3000)|"],["|KasapAkoğlu(4500)|","  |Gürcü'nün  Kahvesi  (3000)|"],["|Alaoğlu Köyü Mito|","|Resul'ün Kahve(3000)|","|ÖztürkGebelit(6000)|","|Bul garayı al parayı|","|KafeCİ(8000)|","|MücoBenzin(-6000)|","|Bim(3000)|","|ClupŞahane6000|"]]
    tablo1=[["|Başlangıç(+10000)|","|Demircan Tekel(2000)|","|Yüksel Berber(2500)|","|Bul garayı al parayı|","|Çelen(-3000)|","|Yovuz Arıcı(1000)|","|A31(4000)|"," |Serbest Bölge|"],["|Galeri Mito(5000)|","  |Ayakkap Dünyası mito(2000)|"],["|Nesrin Havlu(500)|","  |Karasu Köfte Dünyası(3000)|"],["|KasapAkoğlu(4500)|","  |Gürcü'nün  Kahvesi  (3000)|"],["|Alaoğlu Köyü Mito|","|Resul'ün Kahve(3000)|","|ÖztürkGebelit(6000)|","|Bul garayı al parayı|","|KafeCİ(8000)|","|MücoBenzin(-6000)|","|Bim(3000)|","|ClupŞahane6000|"]]
    dükkanların_ücretleri={"|Demircan Tekel(2000)|":2000,"|Yüksel Berber(2500)|":2500,"|Yovuz Arıcı(1000)|":1000,"|A31(4000)|":4000,"|Galeri Mito(5000)|":5000,"  |Ayakkap Dünyası mito(2000)|":2000,"  |Karasu Köfte Dünyası(3000)|":3000,"|NesrinHavlu500|":500,"  |Gürcü'nün  Kahvesi  (3000)|":3000,"|Resul'ün Kahve(3000)|":3000,"|ÖztürkGebelit(6000)|":6000,"|KafeCİ(8000)|":8000,"|Bim(3000)|":3000,"|ClupŞahane6000|":6000,"|KasapAkoğlu(4500)|":4500}
    dükkanların_kiraları={"|Demircan Tekel(2000)|":1000,"|Yüksel Berber(2500)|":1200,"|Yovuz Arıcı(1000)|":900,"|A31(4000)|":2000,"|Galeri Mito(5000)|":2100,"  |Ayakkap Dünyası mito(2000)|":1000,"  |Karasu Köfte Dünyası(3000)|":1500,"|NesrinHavlu500|":31,"  |Gürcü'nün  Kahvesi  (3000)|":1600,"|Resul'ün Kahve(3000)|":1400,"|ÖztürkGebelit(6000)|":3500,"|KafeCİ(8000)|":5000,"|Bim(3000)|":1500,"|ClupŞahane6000|":4000,"|KasapAkoğlu(4500)|":3000}
    sayaç=0
    alaoğlundaki_oyuncu=0
    alaoğlundan_çıkabilecek_oyuncular = []
    devam_edenler=["oyuncu1","oyuncu2","oyuncu3","oyuncu4"]
    serbest_bölgeye_girdi=0
    while True:
        çıkarılan_yerler = []
        sayaç = sayaç + 1
        if alaoğlundaki_oyuncu=="oyuncu1" and sayaç==1:
            sayaç=2
        elif alaoğlundaki_oyuncu == "oyuncu4" and sayaç==4:
            sayaç=1
        elif alaoğlundaki_oyuncu == "oyuncu3" and sayaç==3:
            sayaç=4
        elif alaoğlundaki_oyuncu == "oyuncu2" and sayaç==2:
            sayaç=3
        if sayaç==4 and "oyuncu4" not in devam_edenler:
            sayaç=1
        if sayaç==1:
            oyuncu_no = "oyuncu1"
            arka_renk = Back.RED
            yazı_rengi = Fore.RED
            if "oyuncu1" not in devam_edenler:
                sayaç=2
        if sayaç==2:
            arka_renk = Back.GREEN
            yazı_rengi = Fore.GREEN
            oyuncu_no="oyuncu2"
            if "oyuncu2" not in devam_edenler:
                sayaç=3
        if sayaç==3:
            arka_renk = Back.BLUE
            yazı_rengi = Fore.BLUE
            oyuncu_no="oyuncu3"
            if "oyuncu3" not in devam_edenler:
                sayaç=4
        if sayaç==4:
            arka_renk = Back.YELLOW
            yazı_rengi = Fore.YELLOW
            oyuncu_no="oyuncu4"
            sayaç=0
        devam="e"
        while devam=="e" and serbest_bölgeye_girdi!=1:
            zar_salla = input(yazı_rengi+"""
Zar atmak için Enter'a,Para miktarlarını görmek için Space'a basınız:""")
            if zar_salla=="" or zar_salla==" ":
                devam = "h"
            else:
                print("Lütfen geçerli bir değer giriniz!")
        while zar_salla==" " and serbest_bölgeye_girdi!=1:
            print("Güncel para miktarları:")
            print(Fore.RED+"1.Oyuncu:{}".format(oyuncuların_paraları.get("oyuncu1")))
            print(Fore.GREEN + "2.Oyuncu:{}".format(oyuncuların_paraları.get("oyuncu2")))
            print(Fore.BLUE + "3.Oyuncu:{}".format(oyuncuların_paraları.get("oyuncu3")))
            print(Fore.YELLOW + "4.Oyuncu:{}".format(oyuncuların_paraları.get("oyuncu4")))
            devam = "e"
            while devam == "e":
                zar_salla = input(yazı_rengi+"""
Zar atmak için Enter'a,Para miktarlarını görmek için Space'a basınız:""")
                if zar_salla == "" or zar_salla == " ":
                    devam = "h"
                else:
                    print("Lütfen geçerli bir değer giriniz!")
        if zar_salla=="" and serbest_bölgeye_girdi!=1:
            zar=zar_at()
        if serbest_bölgeye_girdi==1:
            zar=istediği_zar
            print(oyuncuların_zarları.get(oyuncu_no),"wqewqewqewee")
            serbest_bölgeye_girdi=0
        önceki_zar_sayısı=oyuncuların_zarları.get(oyuncu_no)
        toplam_zar_sayısı=önceki_zar_sayısı+zar
        oyuncuların_zarları.update({oyuncu_no:toplam_zar_sayısı})
        if toplam_zar_sayısı>21:
            oyuncunun_ilk_parası=oyuncuların_paraları.get(oyuncu_no)
            oyuncunun_son_parası=oyuncunun_ilk_parası+10000
            oyuncuların_paraları.update({oyuncu_no:oyuncunun_son_parası})
            toplam_zar_sayısı=toplam_zar_sayısı-22
            oyuncuların_zarları.update({oyuncu_no:toplam_zar_sayısı})
        while oyuncuların_zarları["oyuncu1"]==oyuncuların_zarları["oyuncu2"]!=0 or oyuncuların_zarları["oyuncu3"]==oyuncuların_zarları["oyuncu2"]!=0 or oyuncuların_zarları["oyuncu1"]==oyuncuların_zarları["oyuncu3"]!=0 or oyuncuların_zarları["oyuncu1"]==oyuncuların_zarları["oyuncu4"]!=0 or oyuncuların_zarları["oyuncu2"]==oyuncuların_zarları["oyuncu4"]!=0 or oyuncuların_zarları["oyuncu3"]==oyuncuların_zarları["oyuncu4"]!=0:
            önceki_zar_sayısı = oyuncuların_zarları.get(oyuncu_no)
            toplam_zar_sayısı = önceki_zar_sayısı - zar
            zar=zar_at()
            toplam_zar_sayısı=toplam_zar_sayısı+zar
            oyuncuların_zarları.update({oyuncu_no: toplam_zar_sayısı})
        say1 = -1
        for i in tablo:
            say1 += 1
            say2 = -1
            for j in i:
                say2 += 1
                if j == yazı_rengi + tablo1[say1][say2]:
                    tablo[say1][say2] = tablo1[say1][say2]

        if toplam_zar_sayısı>21:
            toplam_zar_sayısı=toplam_zar_sayısı-22
        oyuncuların_zarları.update({oyuncu_no:toplam_zar_sayısı})
        oyuncunun_son_zarı=oyuncuların_zarları[oyuncu_no]
        if oyuncunun_son_zarı<=7:
            oyuncunun_gittiği_yer = tablo[0][oyuncunun_son_zarı]
            tablo[0][oyuncunun_son_zarı]=yazı_rengi+tablo[0][oyuncunun_son_zarı]
        elif 8<=oyuncunun_son_zarı<=10:
            oyuncunun_son_zarı=oyuncunun_son_zarı-7
            oyuncunun_gittiği_yer=tablo[oyuncunun_son_zarı][1]
            tablo[oyuncunun_son_zarı][1]=yazı_rengi+tablo[oyuncunun_son_zarı][1]
        elif 11<=oyuncunun_son_zarı<=18:
            say=10
            for i in range(4,20,2):
                say+=1
                if say==oyuncunun_son_zarı:
                    oyuncunun_son_zarı = oyuncunun_son_zarı - i
                    break
            oyuncunun_gittiği_yer=tablo[4][oyuncunun_son_zarı]
            tablo[4][oyuncunun_son_zarı]=yazı_rengi+tablo[4][oyuncunun_son_zarı]
        elif 19<=oyuncunun_son_zarı<=21:
            say = 18
            for i in range(16, 22, 2):
                say += 1
                if say == oyuncunun_son_zarı:
                    oyuncunun_son_zarı = oyuncunun_son_zarı - i
                    break
            oyuncunun_gittiği_yer=tablo[oyuncunun_son_zarı][0]
            tablo[oyuncunun_son_zarı][0]=yazı_rengi+tablo[oyuncunun_son_zarı][0]
        print(yazı_rengi+f"""
{oyuncu_no} için gelen zar:{zar}
 """)
        tablo_olustur(tablo)
        if (oyuncunun_gittiği_yer not in oyuncu1_arsalar and oyuncunun_gittiği_yer not in oyuncu2_arsalar and oyuncunun_gittiği_yer not in oyuncu3_arsalar and oyuncunun_gittiği_yer not in oyuncu4_arsalar) and (oyuncunun_gittiği_yer!="|Başlangıç(+10000)|" and oyuncunun_gittiği_yer!="|Bul garayı al parayı|" and oyuncunun_gittiği_yer!="|Çelen(-3000)|" and oyuncunun_gittiği_yer!=" |Serbest Bölge|" and oyuncunun_gittiği_yer!="|Alaoğlu Köyü Mito|" and oyuncunun_gittiği_yer!="|MücoBenzin(-6000)|"):
            try:
                if oyuncuların_paraları.get(oyuncu_no) >= dükkanların_ücretleri.get(oyuncunun_gittiği_yer):
                    satın_almak_istiyor_mu = input(yazı_rengi+"\n\n{} isimli yeri satın almak istiyorsanız e'ye basınız:".format(oyuncunun_gittiği_yer))
                    if satın_almak_istiyor_mu == "e":
                        if oyuncu_no == "oyuncu1":
                            oyuncu1_arsalar.append(oyuncunun_gittiği_yer)
                        elif oyuncu_no == "oyuncu2":
                            oyuncu2_arsalar.append(oyuncunun_gittiği_yer)
                        elif oyuncu_no == "oyuncu3":
                            oyuncu3_arsalar.append(oyuncunun_gittiği_yer)
                        else:
                            oyuncu4_arsalar.append(oyuncunun_gittiği_yer)
                        dükkanın_ücreti = dükkanların_ücretleri.get(oyuncunun_gittiği_yer)
                        oyuncunun_parası = oyuncuların_paraları.get(oyuncu_no)
                        oyuncunun_güncel_parası = oyuncunun_parası - dükkanın_ücreti
                        oyuncuların_paraları.update({oyuncu_no: oyuncunun_güncel_parası})
                    else:
                        print("", end="")
            except:
                print("",end="")
        elif oyuncu_no == "oyuncu1" and (oyuncunun_gittiği_yer in oyuncu2_arsalar or oyuncunun_gittiği_yer in oyuncu3_arsalar or oyuncunun_gittiği_yer in oyuncu4_arsalar):
            A=1
            alacak_oyuncu=1
            if oyuncunun_gittiği_yer in oyuncu2_arsalar:
                oyuncu1_parası = oyuncuların_paraları.get("oyuncu1")
                oyuncu2_parası = oyuncuların_paraları.get("oyuncu2")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu1_güncel_parası = oyuncu1_parası - gidilen_yerin_kirası
                oyuncu2_güncel_parası = oyuncu2_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu1": oyuncu1_güncel_parası})
                oyuncuların_paraları.update({"oyuncu2": oyuncu2_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu2'ye {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu2"
                diger_yazı_rengi=Fore.GREEN
                verecek_oyuncu=2
            elif oyuncunun_gittiği_yer in oyuncu3_arsalar:
                oyuncu1_parası = oyuncuların_paraları.get("oyuncu1")
                oyuncu3_parası = oyuncuların_paraları.get("oyuncu3")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu1_güncel_parası = oyuncu1_parası - gidilen_yerin_kirası
                oyuncu3_güncel_parası = oyuncu3_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu1": oyuncu1_güncel_parası})
                oyuncuların_paraları.update({"oyuncu3": oyuncu3_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu3'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu3"
                diger_yazı_rengi=Fore.BLUE
                verecek_oyuncu=3
            elif oyuncunun_gittiği_yer in oyuncu4_arsalar:
                oyuncu1_parası = oyuncuların_paraları.get("oyuncu1")
                oyuncu4_parası = oyuncuların_paraları.get("oyuncu4")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu1_güncel_parası = oyuncu1_parası - gidilen_yerin_kirası
                oyuncu4_güncel_parası = oyuncu4_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu1": oyuncu1_güncel_parası})
                oyuncuların_paraları.update({"oyuncu4": oyuncu4_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu4'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu4"
                diger_yazı_rengi=Fore.YELLOW
                verecek_oyuncu=4
        elif oyuncu_no == "oyuncu2" and (
                oyuncunun_gittiği_yer in oyuncu1_arsalar or oyuncunun_gittiği_yer in oyuncu3_arsalar or oyuncunun_gittiği_yer in oyuncu4_arsalar):
            A=1
            alacak_oyuncu=2
            if oyuncunun_gittiği_yer in oyuncu1_arsalar:
                oyuncu2_parası = oyuncuların_paraları.get("oyuncu2")
                oyuncu1_parası = oyuncuların_paraları.get("oyuncu1")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu2_güncel_parası = oyuncu2_parası - gidilen_yerin_kirası
                oyuncu1_güncel_parası = oyuncu1_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu2": oyuncu2_güncel_parası})
                oyuncuların_paraları.update({"oyuncu1": oyuncu1_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu1'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu1"
                diger_yazı_rengi=Fore.RED
                verecek_oyuncu=1
            elif oyuncunun_gittiği_yer in oyuncu3_arsalar:
                oyuncu2_parası = oyuncuların_paraları.get("oyuncu2")
                oyuncu3_parası = oyuncuların_paraları.get("oyuncu3")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu2_güncel_parası = oyuncu2_parası - gidilen_yerin_kirası
                oyuncu3_güncel_parası = oyuncu3_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu2": oyuncu2_güncel_parası})
                oyuncuların_paraları.update({"oyuncu3": oyuncu3_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu3'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu3"
                diger_yazı_rengi=Fore.BLUE
                verecek_oyuncu=3
            elif oyuncunun_gittiği_yer in oyuncu4_arsalar:
                oyuncu2_parası = oyuncuların_paraları.get("oyuncu2")
                oyuncu4_parası = oyuncuların_paraları.get("oyuncu4")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu2_güncel_parası = oyuncu2_parası - gidilen_yerin_kirası
                oyuncu4_güncel_parası = oyuncu4_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu2": oyuncu2_güncel_parası})
                oyuncuların_paraları.update({"oyuncu4": oyuncu4_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu4'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu4"
                diger_yazı_rengi=Fore.YELLOW
                verecek_oyuncu=4
        elif oyuncu_no == "oyuncu3" and (
                oyuncunun_gittiği_yer in oyuncu2_arsalar or oyuncunun_gittiği_yer in oyuncu1_arsalar or oyuncunun_gittiği_yer in oyuncu4_arsalar):
            A=1
            alacak_oyuncu=3
            if oyuncunun_gittiği_yer in oyuncu2_arsalar:
                oyuncu3_parası = oyuncuların_paraları.get("oyuncu3")
                oyuncu2_parası = oyuncuların_paraları.get("oyuncu2")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu3_güncel_parası = oyuncu3_parası - gidilen_yerin_kirası
                oyuncu2_güncel_parası = oyuncu2_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu3": oyuncu3_güncel_parası})
                oyuncuların_paraları.update({"oyuncu2": oyuncu2_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu2'ye {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu2"
                diger_yazı_rengi=Fore.GREEN
                verecek_oyuncu=2
            elif oyuncunun_gittiği_yer in oyuncu1_arsalar:
                oyuncu3_parası = oyuncuların_paraları.get("oyuncu3")
                oyuncu1_parası = oyuncuların_paraları.get("oyuncu1")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu3_güncel_parası = oyuncu3_parası - gidilen_yerin_kirası
                oyuncu1_güncel_parası = oyuncu1_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu3": oyuncu3_güncel_parası})
                oyuncuların_paraları.update({"oyuncu1": oyuncu1_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu1'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu1"
                diger_yazı_rengi=Fore.RED
                verecek_oyuncu=1
            elif oyuncunun_gittiği_yer in oyuncu4_arsalar:
                oyuncu3_parası = oyuncuların_paraları.get("oyuncu3")
                oyuncu4_parası = oyuncuların_paraları.get("oyuncu4")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu3_güncel_parası = oyuncu3_parası - gidilen_yerin_kirası
                oyuncu4_güncel_parası = oyuncu4_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu3": oyuncu3_güncel_parası})
                oyuncuların_paraları.update({"oyuncu4": oyuncu4_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu4'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu4"
                diger_yazı_rengi=Fore.YELLOW
                verecek_oyuncu=4
        elif oyuncu_no == "oyuncu4" and (oyuncunun_gittiği_yer in oyuncu2_arsalar or oyuncunun_gittiği_yer in oyuncu3_arsalar or oyuncunun_gittiği_yer in oyuncu1_arsalar):
            A=1
            alacak_oyuncu=4
            if oyuncunun_gittiği_yer in oyuncu2_arsalar:
                oyuncu4_parası = oyuncuların_paraları.get("oyuncu4")
                oyuncu2_parası = oyuncuların_paraları.get("oyuncu2")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu4_güncel_parası = oyuncu4_parası - gidilen_yerin_kirası
                oyuncu2_güncel_parası = oyuncu2_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu4": oyuncu4_güncel_parası})
                oyuncuların_paraları.update({"oyuncu2": oyuncu2_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu2'ye {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu2"
                diger_yazı_rengi=Fore.GREEN
                verecek_oyuncu=2
            elif oyuncunun_gittiği_yer in oyuncu3_arsalar:
                oyuncu4_parası = oyuncuların_paraları.get("oyuncu4")
                oyuncu3_parası = oyuncuların_paraları.get("oyuncu3")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu4_güncel_parası = oyuncu4_parası - gidilen_yerin_kirası
                oyuncu3_güncel_parası = oyuncu3_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu4": oyuncu4_güncel_parası})
                oyuncuların_paraları.update({"oyuncu3": oyuncu3_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu3'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu3"
                diger_yazı_rengi=Fore.BLUE
                verecek_oyuncu=3
            elif oyuncunun_gittiği_yer in oyuncu1_arsalar:
                oyuncu4_parası = oyuncuların_paraları.get("oyuncu4")
                oyuncu1_parası = oyuncuların_paraları.get("oyuncu1")
                gidilen_yerin_kirası = dükkanların_kiraları.get(oyuncunun_gittiği_yer)
                oyuncu4_güncel_parası = oyuncu4_parası - gidilen_yerin_kirası
                oyuncu1_güncel_parası = oyuncu1_parası + gidilen_yerin_kirası
                oyuncuların_paraları.update({"oyuncu4": oyuncu4_güncel_parası})
                oyuncuların_paraları.update({"oyuncu1": oyuncu1_güncel_parası})
                print(f"\n\n{oyuncu_no},oyuncu1'e {gidilen_yerin_kirası}TL verdi.")
                diger_oyuncu_no="oyuncu1"
                diger_yazı_rengi=Fore.RED
                verecek_oyuncu=1
        try:
            if A==1 and oyuncuların_paraları.get(oyuncu_no)>0:
                oyuncu_pazarlık_yapmak_istiyor_mu = input(yazı_rengi + f"{oyuncunun_gittiği_yer} isimli yer için {diger_oyuncu_no} ile pazarlık yapmak istiyorsanız e'ye basınız:")
                if oyuncu_pazarlık_yapmak_istiyor_mu == "e":
                    diger_oyuncu_pazarlık_yapmak_istiyor_mu = input(
                        diger_yazı_rengi + f"{oyuncu_no} ile pazarlık yapmak istiyorsanız e'ye basınız:")
                    if diger_oyuncu_pazarlık_yapmak_istiyor_mu == "e":
                        devam1 = "e"
                        say1 = 0
                        while devam1 == "e":
                            say1 += 1
                            if say1 == 1:
                                devam2="e"
                                while devam2=="e":
                                    try:
                                        oyuncu_fiyat = int(input(yazı_rengi + f"Fiyat giriniz:"))
                                        devam2="h"
                                    except:
                                        print("Lütfen ilk önce bir fiyat sununuz!")
                                        devam2="e"
                            else:
                                if diger_oyuncu_fiyat != "h" and diger_oyuncu_fiyat != "e":
                                    oyuncu_fiyat = input(
                                        yazı_rengi + f"{diger_oyuncu_no}'nin teklifini kabul ediyorsanız e'yi,yeni bir fiyat sunmak istiyorsanız istediğiniz fiyatı,pazarlığı sonlandırmak istiyorsanız h'yi tuşlayınız:")
                            if oyuncu_fiyat != "h" and oyuncu_fiyat != "e":
                                diger_oyuncu_fiyat = input(
                                    diger_yazı_rengi + f"{oyuncu_no}'nin teklifini kabul ediyorsanız e'yi,yeni bir fiyat sunmak istiyorsanız istediğiniz fiyatı,pazarlığı sonlandırmak istiyorsanız h'yi tuşlayınız:")
                            if oyuncu_fiyat == "h" or diger_oyuncu_fiyat == "h":
                                break
                            elif oyuncu_fiyat == "e":
                                if int(diger_oyuncu_fiyat) <= int(oyuncuların_paraları.get(oyuncu_no)):
                                    if diger_oyuncu_fiyat>=0:
                                        fiyat = int(diger_oyuncu_fiyat)
                                        devam1 = "h"
                                        break
                                    else:
                                        print("Lütfen sıfırdan büyük bir değer giriniz!")
                                else:
                                    print(f"{oyuncu_no}'nin parası yeterli değil!")
                            elif diger_oyuncu_fiyat == "e":
                                if int(oyuncu_fiyat) <= oyuncuların_paraları.get(oyuncu_no):
                                    if oyuncu_fiyat>=0:
                                        fiyat = int(oyuncu_fiyat)
                                        devam1 = "h"
                                        break
                                    else:
                                        print("Lütfen sıfırdan büyük bir değer giriniz!")
                                else:
                                    print(f"{oyuncu_no}'nin parası yeterli değil!")
                        if devam1 == "h":
                            oyuncunun_parası1 = oyuncuların_paraları.get(oyuncu_no)
                            oyuncunun_parası1 = oyuncunun_parası1 - fiyat
                            oyuncuların_paraları.update({oyuncu_no: oyuncunun_parası1})
                            oyuncunun_parası2 = oyuncuların_paraları.get(diger_oyuncu_no)
                            oyuncunun_parası2 = oyuncunun_parası2 + fiyat
                            oyuncuların_paraları.update({diger_oyuncu_no: oyuncunun_parası2})
                            if alacak_oyuncu == 1:
                                oyuncu1_arsalar.append(oyuncunun_gittiği_yer)
                            elif alacak_oyuncu == 2:
                                oyuncu2_arsalar.append(oyuncunun_gittiği_yer)
                            elif alacak_oyuncu == 3:
                                oyuncu3_arsalar.append(oyuncunun_gittiği_yer)
                            elif alacak_oyuncu == 4:
                                oyuncu4_arsalar.append(oyuncunun_gittiği_yer)
                            if verecek_oyuncu == 1:
                                oyuncu1_arsalar.remove(oyuncunun_gittiği_yer)
                            elif verecek_oyuncu == 2:
                                oyuncu2_arsalar.remove(oyuncunun_gittiği_yer)
                            elif verecek_oyuncu == 3:
                                oyuncu3_arsalar.remove(oyuncunun_gittiği_yer)
                            elif verecek_oyuncu == 4:
                                oyuncu4_arsalar.remove(oyuncunun_gittiği_yer)
        except:
            print("", end="")
        if oyuncunun_gittiği_yer=="|Alaoğlu Köyü Mito|" and oyuncu_no not in alaoğlundan_çıkabilecek_oyuncular:
            tur_sayısı=0
            alaoğlundaki_oyuncu=oyuncu_no
        try:
            tur_sayısı+=1
            if tur_sayısı == 9:
                tur_sayısı = 0
                alaoğlundaki_oyuncu = 0
        except:
            print("",end="")
        if oyuncunun_gittiği_yer=="|MücoBenzin(-6000)|" or oyuncunun_gittiği_yer=="|Çelen(-3000)|":
            para1=oyuncuların_paraları.get(oyuncu_no)
            if oyuncunun_gittiği_yer == "|MücoBenzin(-6000)|":
                para1=para1-6000
                print(yazı_rengi+f"\n\n{oyuncu_no} 6000TL ödedi")
            else:
                para1=para1-3000
                print(yazı_rengi+f"\n\n{oyuncu_no} 3000TL ödedi")
            oyuncuların_paraları.update({oyuncu_no: para1})
        if oyuncunun_gittiği_yer==" |Serbest Bölge|":
            try:
                devam3 = "e"
                while devam3 == "e":
                    try:
                        istediği_zar = int(input("\n\nKaç adım gitmek istediğinizi giriniz(1-21):"))
                        eski_zar = oyuncuların_zarları.get(oyuncu_no)
                        eski_zar = eski_zar + istediği_zar
                        if 1 <= istediği_zar <= 21:
                            devam3 = "h"
                            sayaç = sayaç - 1
                            serbest_bölgeye_girdi = 1
                            print(sayaç, "SAYAÇ")
                            print("serbest girdi mi",serbest_bölgeye_girdi)
                            for i in oyuncuların_zarları.values():
                                if i == eski_zar:
                                    devam3 = "e"
                                    print("Gitmek istediğiniz yerde başka bir oyuncu var!")
                        else:
                            print("Lütfen 1-21 arasında bir değer giriniz!")
                    except:
                        print("Lütfen tam sayı giriniz!")
            except:
                print("",end="")








        if oyuncunun_gittiği_yer=="|Bul garayı al parayı|":
            import random
            şans_çarkı_index=random.randint(0,5)
            şans_çarkı=["Ci'nin kafede 5TL olan şeye 10TL ödedin.(-10TL)","Emre abi benzine para vermedi benzin parası senden (-5000TL)","Alaoğluna gitmemek için uyduduğun bahaneyi Mito yedi.Bir dahaki sefere bu kartı kullanılarak Alaoğlundan çıkabilirsin.","Tayyip bey asgari ücrete zam yaptı (+2000)","Dolar düştü(+1000TL)","Volkan kitapların parasını vermedi(-300TL)"]
            say1=-1
            for i in şans_çarkı:
                say1+=1
                if say1==şans_çarkı_index:
                    print()
                    print()
                    print(yazı_rengi+i)
                    break
            oyuncu_para1=oyuncuların_paraları.get(oyuncu_no)
            if i=="Ci'nin kafede 5TL olan şeye 10TL ödedin.(-10TL)":
                oyuncu_para1=oyuncu_para1-10
            elif i=="Emre abi benzine para vermedi benzin parası senden (-5000TL)":
                oyuncu_para1=oyuncu_para1-5000
            elif i=="Alaoğluna gitmemek için uyduduğun bahaneyi Mito yedi.Bir dahaki sefere bu kartı kullanılarak Alaoğlundan çıkabilirsin.":
                alaoğlundan_çıkabilecek_oyuncular.append(oyuncu_no)
            elif i=="Tayyip bey asgari ücrete zam yaptı (+2000)":
                oyuncu_para1=oyuncu_para1+2000
            elif i=="Volkan kitapların parasını vermedi(-300TL)":
                oyuncu_para1=oyuncu_para1-300
            else:
                oyuncu_para1=oyuncu_para1+1000
            oyuncuların_paraları.update({oyuncu_no:oyuncu_para1})
        for oyuncunun_numarası,oyuncunun_mevcut_parası in oyuncuların_paraları.items():
            try:
                while oyuncunun_mevcut_parası < 0:
                    if oyuncunun_numarası == "oyuncu1":
                        çıkarılan_yer = oyuncu1_arsalar.pop()
                    elif oyuncunun_numarası == "oyuncu2":
                        çıkarılan_yer = oyuncu2_arsalar.pop()
                    elif oyuncunun_numarası == "oyuncu3":
                        çıkarılan_yer = oyuncu3_arsalar.pop()
                    elif oyuncunun_numarası == "oyuncu4":
                        çıkarılan_yer = oyuncu4_arsalar.pop()
                    çıkarılan_yer_fiyatı = dükkanların_ücretleri.get(çıkarılan_yer) // 2
                    oyuncunun_mevcut_parası = oyuncunun_mevcut_parası + çıkarılan_yer_fiyatı
                    oyuncuların_paraları.update({oyuncu_no:oyuncunun_mevcut_parası})
                    çıkarılan_yerler.append(çıkarılan_yer)
            except:
                print(yazı_rengi+f"{oyuncu_no}'nin godomanlık hayatı bitti!")
                devam_edenler.remove(oyuncu_no)
                say1 = -1
                for i in tablo:
                    say1 += 1
                    say2 = -1
                    for j in i:
                        say2 += 1
                        if j == yazı_rengi + tablo1[say1][say2]:
                            tablo[say1][say2] = tablo1[say1][say2]
                oyuncuların_zarları.update({oyuncu_no:-1000})
                oyuncuların_paraları.update({oyuncu_no:0})
        if çıkarılan_yerler!=[]:
            for i in çıkarılan_yerler:
                print(i,end=",")
            print(yazı_rengi+f"isimli yerler {oyuncu_no}'nin parası bittiği için bankaya yarı fiyatına satıldı!")
        if len(devam_edenler)==1:
            for i in devam_edenler:
                print(i,"KAZANDI!")

main()


