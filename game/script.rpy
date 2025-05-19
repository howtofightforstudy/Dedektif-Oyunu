# Karakter tanımlamaları
define dedektif_e = Character("Dedektif", color="#c8c8ff")
define dedektif_k = Character("Dedektif", color="#c8c8ff")
define hizmetci = Character("Hizmetçi", color="#c8ffc8")
define eski_sevgili = Character("Clara", color="#c8c8ff")
define eski_sevgili_abisi = Character("Arthur", color="#c8c8ff")
define kurbanin_annesi = Character("Matilda", color="#c8ffc8")
define kurbanin_babasi = Character("Gregory", color="#c8ffc8")
define sef = Character("Kasaba Şefi", color="#c8ffc8")

# Resim tanımlamaları
image ev = "images/ev.jpg"
image sorgu_odasi = "images/sorgu_odasi.png"
image kasaba = "images/kasaba.png"
image gazete = "images/gazete.png"
image dedektif_e_resim = "images/karakterler/erkek_dedektif.png"
image dedektif_k_resim = "images/karakterler/kadin_dedektif.png"
image hizmetci_resim = "images/karakterler/hizmetci.png"
image eski_sevgili_resim = "images/karakterler/eski_sevgili.png"
image eski_sevgili_abisi_resim = "images/karakterler/eski_sevgili_abisi.png"
image kurbanin_annesi_resim = "images/karakterler/kurbanin_annesi.png"
image kurbanin_babasi_resim = "images/karakterler/kurbanin_babasi.png"
image sef_resim = "images/karakterler/sef.png"

transform karakter_buyuk:
    zoom 1.5
    anchor (0.5, 1.0)
    xalign 0.5
    yalign 0.65

transform karakter_buyuk_sag:
    zoom 1.5
    anchor (0.5, 1.0)
    xalign 0.8
    yalign 0.65

transform karakter_buyuk_sol:
    zoom 1.5
    anchor (0.5, 1.0)
    xalign 0.2
    yalign 0.65

transform bg_fullscreen:
    zoom 2.0

# Oyun değişkenleri
default dedektif_isim = ""
default secilen_dedektif_tipi = ""
default secilen_dedektif_karakteri = None

# Oyun başlangıcı
label start:
    scene ev at bg_fullscreen
    play music "audio/op.mp3" volume 0.5

    "Yıl 1922. Sisli bir sabahın serinliğinde, Steiner malikanesinin gri taş duvarları yankı dolu bir çığlıkla sarsıldı."
    "Zengin ve küstah genç adam Lukas Steiner, odasında cansız halde bulundu. Parmaklarının ucunda bir çay fincanı, göğsünde ise soğuk bir bıçağın izini taşıyan derin bir yara..."
    "Steiner, kadınlara karşı küçümseyici tavırlarıyla tanınır; ardında incinmiş kalpler, bastırılmış öfkeler ve sessizce yutulmuş nefretler bırakırdı."
    "O sabah, çay fincanındaki parmak izleri ve tek bir yudum dahi alınmamış çay, olayın yalnızca başlangıcıydı."
    "Hizmetçi gözaltına alındı. Fakat o evde herkesin bir bahanesi, herkesin karanlıkta kalan bir yüzü vardı."
    "Zira bazı sırlar, kahveden bile daha acıydı."
    jump dedektif_secimi

label dedektif_secimi:
    scene kasaba at bg_fullscreen with fade
    show dedektif_e_resim at karakter_buyuk_sol with moveinleft
    show dedektif_k_resim at karakter_buyuk_sag with moveinright
    menu:
        "Erkek Dedektif":
            $ secilen_dedektif_tipi = "erkek"
            $ secilen_dedektif_karakteri = dedektif_e
            show dedektif_e_resim at karakter_buyuk
            hide dedektif_k_resim 
            "Erkek dedektifi seçtiniz."
            jump dedektif_isim_girisi
        "Kadın Dedektif":
            $ secilen_dedektif_tipi = "kadin"
            $ secilen_dedektif_karakteri = dedektif_k
            show dedektif_k_resim at karakter_buyuk
            hide dedektif_e_resim
            "Kadın dedektifi seçtiniz."
            jump dedektif_isim_girisi

label dedektif_isim_girisi:
    scene sorgu_odasi at bg_fullscreen with fade

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk
        $ dedektif_isim = renpy.input("Lütfen erkek dedektifin ismini girin:")
        if dedektif_isim == "":
            $ dedektif_isim = "Erkek Dedektif"
        $ dedektif_isim = "Dedektif " + dedektif_isim
        $ secilen_dedektif_karakteri = Character(dedektif_isim, color="#c8c8ff")
        secilen_dedektif_karakteri "Merhaba, ben [dedektif_isim]."

    elif secilen_dedektif_tipi == "kadin":
        show dedektif_k_resim at karakter_buyuk
        $ dedektif_isim = renpy.input("Lütfen kadın dedektifin ismini girin:")
        if dedektif_isim == "":
            $ dedektif_isim = "Kadın Dedektif"
        $ dedektif_isim = "Dedektif " + dedektif_isim
        $ secilen_dedektif_karakteri = Character(dedektif_isim, color="#c8c8ff")
        secilen_dedektif_karakteri "Merhaba, ben [dedektif_isim]."

    jump olaylar_baslangici

label olaylar_baslangici:
    scene kasaba at bg_fullscreen
    show sef_resim at karakter_buyuk_sol with dissolve

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright

    sef "Kasabamıza hoş geldiniz [dedektif_isim] sizlerle tanışmak büyük bir onurdur."
    secilen_dedektif_karakteri "Memnun oldum Şef. Dosyayı inceledim ancak bana kısaca olayı anlatır mısınız?"
    sef "Lukas steiner’ın ölüm sebebi göğsündeki bıçak yarası ancak elindeki çay fincanı da şüpheleri çekti."
    sef "Bu durumda fincandaki çayı incelemeye gönderdik."
    sef "Adli tıp incelemesine göre çayın içinde sakinleştirici, yatıştırıcı maddeler bulunuyor."
    sef "Çayı hazırlayan ise Steiner malikanesinde çalışan Hizmetçi Elena."
    sef "Şüphelilerimiz Lukas Steiner'ın eski sevgilisi Clara, eski sevgilisinin abisi Arthur, çayı hazırlayan hizmetçi Elena ve ebeveynleri."
    secilen_dedektif_karakteri "Bilgiler için teşekkür ederim Şef. Şüphelileri sorgulamak istiyorum."
    jump supheliler_sorgulaniyor

default sorgu_hizmetci_dinlendi = False
default sorgu_eski_sevgili_dinlendi = False
default sorgu_eski_sevgili_abisi_dinlendi = False
default sorgu_kurbanin_annesi_dinlendi = False
default sorgu_kurbanin_babasi_dinlendi = False


label supheliler_sorgulaniyor: 
    scene sorgu_odasi at bg_fullscreen

    show sef at karakter_buyuk
    sef "Kimi sorgulamak istersiniz?"
    menu:
        "Hizmetçi (Elena)":
            $ sorgu_hizmetci_dinlendi = True
            jump sorgu_hizmetci
        "Eski Sevgili (Clara)":
            $ sorgu_eski_sevgili_dinlendi = True
            jump sorgu_eski_sevgili
        "Eski Sevgilinin Abisi (Arthur)":
            $ sorgu_eski_sevgili_abisi_dinlendi = True
            jump sorgu_eski_sevgili_abisi
        "Kurbanın Annesi (Matilda)":
            $ sorgu_kurbanin_annesi_dinlendi = True
            jump sorgu_kurbanin_annesi
        "Kurbanın Babası (Gregory)":
            $ sorgu_kurbanin_babasi_dinlendi = True
            jump sorgu_kurbanin_babasi
        #suclular dinlendiyse acilacak
        "Suçluyu Belirle" if sorgu_hizmetci_dinlendi and sorgu_eski_sevgili_dinlendi and sorgu_eski_sevgili_abisi_dinlendi and sorgu_kurbanin_annesi_dinlendi and sorgu_kurbanin_babasi_dinlendi:
            jump sucluyu_sec

label sorgu_hizmetci:
    scene sorgu_odasi at bg_fullscreen
    show hizmetci_resim at karakter_buyuk_sol with moveinleft

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright

    secilen_dedektif_karakteri "Merhaba Elena hanım. Direkt konuya gireceğim, boş vaktimiz yok."
    secilen_dedektif_karakteri "Lukas Steiner’ın ölüm sebebinin göğsündeki bıçak yarası olduğunu düşünüyoruz."
    secilen_dedektif_karakteri "Ancak olay yerinde elinde fincan vardı ve içindeki çayda bazı zararlı maddeler bulundu."
    secilen_dedektif_karakteri "Çayı siz hazırlamışsınız Elena hanım. Fincanda sadece sizin parmak izleriniz var. Bunu nasıl açıklarsınız?"
    hizmetci "…"
    hizmetci "Çayı hazırladım evet ama sadece içine biraz bitki özü kattım. Uykusuzdu son günlerde. Ona zarar vermek istemedim."
    secilen_dedektif_karakteri "Bitki özü dediğiniz madde tam olarak nedir?"
    "Elena bakışlarını masaya sabitlerken konuştu."
    hizmetci "Melisa ve papatya karışımıydı. Doğal, aktardan almıştım."
    hizmetci "Lukas Bey son zamanlarda çok gergindi, geceleri uyuyamıyordu."
    hizmetci "Konuşmalarımızda hep yorgun olduğunu söylerdi."
    hizmetci "Eğer böyle bir şey olacağını bilseydim asla dokunmazdım kahvesine."
    hizmetci "Yemin ederim, onu zehirlemek gibi bir niyetim yoktu!"

    menu: 
        "Anladım. Mutfakta olduğunuz için bıçakların hepsini biliyor olmalısın sonuçta mutfakta çalışıyorsunuz.":
            secilen_dedektif_karakteri "Anladım. Mutfakta olduğunuz için bıçakların hepsini biliyor olmalısın sonuçta mutfakta çalışıyorsun."
            secilen_dedektif_karakteri "Steiner’ın ölüm sebebi bıçak yarası, biraz da bunun hakkında konuşalım."
            hizmetci "Evet, bıçakları tanırım ama o bıçaklıkta değildi. Yani... biri almıştı zaten."
            secilen_dedektif_karakteri "Bunu nereden çıkardınız? Bu sizin sorumluluğunuzdaydı. Bıçağı birine siz vermiş olabilir misiniz?"
            "Elena keskin bir şekilde cevap verdi"
            hizmetci "Hayır."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Elena Hanım."
        "Bitki özü katmanızla zarar vermenizin ne alakası olabilir ki?":
            secilen_dedektif_karakteri "Bitki özü katmanızla zarar vermenizin ne alakası olabilir ki?"
            secilen_dedektif_karakteri "Bir ihtimal fincanın içinde bitki özünden başka bir şeyde olabilir mi Elena hanım?"
            hizmetci "Bitki özü ve biraz şeker koydum, çayın içinde başka bir şey yoktu "
            "Elena gözlerini kaçırır, parmakları ile oynar"
            secilen_dedektif_karakteri "Anladım, zaten olay olduğu sırada bodruma indiğinizi söylüyorsunuz. Neden bodruma inmiştiniz?"
            hizmetci "Akşam yemeği için malzeme almam gerekiyordu."
            secilen_dedektif_karakteri "Sizi gören biri oldu mu?"
            hizmetci "Gitmeden önce Matilda hanıma haber vermiştim."
            secilen_dedektif_karakteri "Anladım. Mutfakta olduğunuz için bıçakların hepsini biliyor olmalısın sonuçta mutfakta çalışıyorsun."
            secilen_dedektif_karakteri " Steiner’ın ölüm sebebi bıçak yarası, buna ne diyeceksiniz?"
            hizmetci "Evet, bıçakları tanırım. Ama o bıçaklıkta değildi. Yani... biri almıştı zaten."
            secilen_dedektif_karakteri "Bunu nereden çıkardınız? Bu sizin sorumluluğunuzdaydı. Bıçağı birine siz vermiş olabilir misiniz?"
            "Elena titrek bir sesle cevap verir"
            hizmetci "Hayır..."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Elena Hanım."
    jump supheliler_sorgulaniyor

label sorgu_eski_sevgili:
    scene sorgu_odasi at bg_fullscreen
    show eski_sevgili_resim at karakter_buyuk_sol with moveinleft

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright

    secilen_dedektif_karakteri "Merhaba Clara hanım, Lukas Steiner'la ilişkiniz çalkantılıydı. Ne sıklıkla görüşüyordunuz?"
    eski_sevgili "Çok... Sık sık ayrılıp barışırdık. Ama hep o terk ederdi. Beni oyuncak gibi görürdü."
    menu:
        "O gün konuştunuz mu?":
            secilen_dedektif_karakteri "O gün konuştunuz mu?"
            eski_sevgili "Hayır. Görüşmedik. Zaten konuşacak pek bir şeyimiz kalmamıştı."
            secilen_dedektif_karakteri "Peki onu öldürmeyi hiç düşündünüz mü?"
            eski_sevgili "Bir an... sadece bir an aklımdan geçti. Ama yapmadım. Yapamazdım."
            secilen_dedektif_karakteri "Peki kardeşiniz hakkında konuşalım. Kardeşiniz Arthur çok korumacı."
            secilen_dedektif_karakteri "Onun bir şey yapmış olmasından şüpheleniyor musunuz?"
            eski_sevgili "Arthur beni korur evet ama bazen fazla ileri gidebilir… Umarım bir çılgınlık yapmamıştır."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Clara hanım."
        "Bana biraz Lukas Steiner’ı anlatır mısınız?":
            secilen_dedektif_karakteri "Bana biraz Lukas Steiner’ı anlatır mısınız?"
            eski_sevgili "O bencildi. Bencilden çok narsist demek yanlış olmaz. Kendisinden başka kimsenin üstün olmadığını düşünürdü."
            "Clara’nın gözleri dolar."
            eski_sevgili "Ama onu çok seviyorum... hala çok seviyorum, benim biricik Lukas’ım… Sonumuz böyle olamazdı."
            "Dedektif, Clara’ya mendil uzattı. Clara mendili alıp göz yaşlarını silerken dedektif konuştu."
            secilen_dedektif_karakteri "Onu öldürmeyi hiç düşündünüz mü?"
            eski_sevgili "Ne?! Saçmalamayın ne dediğimi görmüyor musunuz? Biricik Lukas’ımı nasıl öldürebilirim?!"
            secilen_dedektif_karakteri "Kişiliği çok da iyi değilmiş sizin de dediğiniz gibi ayrıca birçok kişi Lukas Steiner’ın size kötü davrandığını söylüyor."
            secilen_dedektif_karakteri "Bu durumda içten içe ona kinlenmiş olabilirsiniz."
            "Clara öfke dolu bakışlarını dedektife kilitledi."
            eski_sevgili "Evet, belki bana kötü davrandı… belki kalbimi paramparça etti ama onu öldürecek kadar nefret etmedim!"
            eski_sevgili "Ben sadece… sadece onun değişmesini istedim… Sevdiği bir adam gibi olmasını…"
            eski_sevgili "Ama her defasında beni daha fazla kırdı. Bu, onu öldürmek istediğim anlamına gelmez!"
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Clara hanım."
    jump supheliler_sorgulaniyor

label sorgu_eski_sevgili_abisi:
    scene sorgu_odasi at bg_fullscreen
    show eski_sevgili_abisi_resim at karakter_buyuk_sol with dissolve
   
    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
   
        show dedektif_k_resim at karakter_buyuk_sag with moveinright
    
    secilen_dedektif_karakteri "Merhaba Arthur Bey, bildiğiniz gibi Lukas Steiner göğsünde bıçak yarasıyla ölü bulundu."
    secilen_dedektif_karakteri "Siz de bu cinayette şüphelilerden birisiniz. Şüpheli olma nedeniniz de kız kardeşiniz ile kurbanın ilişkisi."
    secilen_dedektif_karakteri "Kız kardeşin için endişelendiğini biliyorum ama Lukas Steiner’a zarar verdiniz mi?"
    eski_sevgili_abisi "Evet onu tehdit ettim ama ben öldürmedim."
    secilen_dedektif_karakteri "Üniformanızda Lukas Steiner'a ait kan lekesi var. Bunu nasıl açıklarsınız?"
    eski_sevgili_abisi "Onu engellemeye çalıştım. O gece Clara’ya gitmeye kalktı. Aramızda boğuşma oldu... ama o sırada canlıydı."
    menu:
        "Gerçekleri anlatmazsanız, işini kaybedebilirsiniz":
            secilen_dedektif_karakteri "Gerçekleri anlatmazsanız, işini kaybedebilirsiniz"
            "Arthur başını öne eğdi, elleri dizlerinde kenetlendi. Mırıldandı."
            eski_sevgili_abisi "İşimi mi? Bu benim onurum. Ama... belki haklısın. Belki bir hata yaptım. Onu durdurmalıydım..."
            secilen_dedektif_karakteri "Neyden bahsettiğinizi bilmiyorum ancak gerçekten şüpheli davranıyorsunuz Arthur bey."
            eski_sevgili_abisi "Bakın… o gece Clara ağlıyordu o adi yine onu aşağılamış, küçük düşürmüştü. Dayanamadım! Lukas’a hesap sormaya gittim."
            eski_sevgili_abisi "Tartıştık, üstüme yürüdü ve boğuşma yaşadık ama onu orada yerde bıraktım. Hâlâ yaşıyordu, yemin ederim!"
            secilen_dedektif_karakteri "Bana o gece orada olduğunuzu kanıtlayacak birini söyler misiniz?"
            eski_sevgili_abisi "Köşkteki hizmetçi Elena o gün beni içeri almıştı."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Arthur Bey."
        "Neden aranızda bir boğuşma oldu? Ayrıca bir gün öncesinde buluştuğunuza dair bir bilgilendirme almadım.":
            secilen_dedektif_karakteri "Neden aranızda bir boğuşma oldu? Ayrıca bir gün öncesinde buluştuğunuza dair bir bilgilendirme almadım."
            secilen_dedektif_karakteri "Köşk hizmetçileri cinayetin işlendiği sabah geldiğinizi ve Lukas Steiner’la sohbet etmek için odasına gittiğinizi söylüyor."
            eski_sevgili_abisi "Ne ima etmeye çalışıyorsunuz, ha?!"
            eski_sevgili_abisi "Kardeşim o adamın elinde oyuncak oldu yıllarca! Onun ne yaptığını, nasıl aşağıladığını bilmiyorsunuz!"
            eski_sevgili_abisi "Evet, Lukas’la o sabah görüştüm! Evet, onunla boğuştum ama öldürmedim!"
            eski_sevgili_abisi "Eğer onu bıçaklayan biri varsa, belki de yıllardır içlerinde biriken nefreti artık taşıyamayan biridir!" 
            eski_sevgili_abisi "Ama ben değilim! Ben sadece... Clara’yı korumaya çalıştım! Suç mu bu?!"
            secilen_dedektif_karakteri "Sakin olun Arthur Bey. Ben burada sizinle kavga etmeye gelmedim."
            secilen_dedektif_karakteri "Ama siz şu an bana, kontrolünü kaybedebilen bir adamın resmini çiziyorsunuz. Bu kontrolsüzlük… bir bıçağı göğse saplamaya ne kadar uzak olabilir ki?"
            "Arthur dişlerini sıktı, yumrukları istemsizce sıkıldı. Gözleri bir an için parladı ama sonra başını iki yana salladı."
            eski_sevgili_abisi "Ben bir askerim, dedektif! Kraliyet muhafızıyım! Duygularımla hareket edecek kadar acemi değilim. Onun gibi pisliklere karşı bile!"
            secilen_dedektif_karakteri "Ve askerlik onuru bazen aile onurunun gerisinde kalmaz mı? Mesela bir adam, kız kardeşinin onurunu kurtarmak için kan dökmeyi göze almaz mı?"
            eski_sevgili_abisi "Siz ne bilirsiniz aileyi, onuru, çaresizliği?! O herife kaç kez söyledim kardeşimden uzak dur diye ama dinlemedi."
            eski_sevgili_abisi "O gece Clara odasında ağlıyordu. Gittim Lukas’ın yüzüne tükürdüm… bir de sadece yumruk attım. Bıçak falan yoktu! Ona zarar vermek isteseydim... çok daha fazlasını yapardım."
            secilen_dedektif_karakteri "Demek yumruk attınız. Bu ilk kez duyduğum bir detay. Neden şimdi söylüyorsunuz?"
            "Arthur gözlerini bir an yere indirdi, sonra kararlı bir bakışla dedektife döndü."
            eski_sevgili_abisi "Çünkü biliyorum! Şimdi söyledim diye ‘katil’ damgası vuracaksınız! Ama ben öldürmedim! O kahrolası herif ölümü belki hak etti ama o bıçağı ben saplamadım!"
            secilen_dedektif_karakteri "Eğer doğruyu söylüyorsanız, o zaman sizin çıkışınızdan sonra bir başkasının odaya girdiğini kanıtlamamız gerek."
            secilen_dedektif_karakteri "Ama eğer yalan söylüyorsanız… o zaman bu çıkışınız sadece son çırpınışınız olur."
            secilen_dedektif_karakteri "Sorgu için teşekkürler Arthur Bey."
    jump supheliler_sorgulaniyor

label sorgu_kurbanin_annesi:
    scene sorgu_odasi at bg_fullscreen
    show kurbanin_annesi_resim at karakter_buyuk_sol with dissolve

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright

    secilen_dedektif_karakteri "Bayan Steiner, oğlunuzun ölümüne üzülüyor musunuz?"
    kurbanin_annesi "Üzgünüm elbette. Ama size bir sır vereyim dedektif… Oğlumun karakteri bozuktu. Kadınlara saygısı yoktu belki bu onun sonuydu."
    secilen_dedektif_karakteri "Oğlunuza karşı öfke duyduğunuz oldu mu?"
    kurbanin_annesi "Evet. Ama bir anne öfkeyle cinayet işlemez. Sessizce utançla bekler sadece..."
    secilen_dedektif_karakteri "Odanızda bir mektup bulundu."
    secilen_dedektif_karakteri "Bu mektup... Lukas’a yazılmış tehditlerle dolu. Yazı stilinizle eşleşiyor."
    kurbanin_annesi "Ben yazmadım ama kimin yazdığını tahmin ediyorum."
    menu:
        "Eğer kimin yazdığını biliyorsanız, söylemek zorundasınız Matilda Hanım. Aksi halde sizi gizli tanık değil, şüpheli olarak ele alırım.":
            secilen_dedektif_karakteri "Eğer kimin yazdığını biliyorsanız, söylemek zorundasınız Matilda Hanım. Aksi halde sizi gizli tanık değil, şüpheli olarak ele alırım."
            kurbanin_annesi "Beni tehdit mi ediyorsunuz, dedektif?"
            secilen_dedektif_karakteri "Hayır, sadece gerçeği arıyorum ve siz o gerçeği saklıyorsunuz gibi görünüyor."
            "Matilda Steiner’ın gözleri dolar ve kısık sesle konuşur"
            kurbanin_annesi "Mektubu yazan kişi hizmetçimiz Elena..."
            secilen_dedektif_karakteri "Elena mı? Neden?"
            kurbanin_annesi "O, Lukas’ın davranışlarına en çok maruz kalanlardan biriydi. Bir keresinde mutfağa ağlayarak geldiğini gördüm."
            kurbanin_annesi "Elinde ezilmiş bir not vardı, parmakları titriyordu. Belki sabrı tükenmişti..."
            secilen_dedektif_karakteri "Yani diyorsunuz ki Elena oğlunuza tehdit mektubu yazmış olabilir?"
            kurbanin_annesi "Evet ama bunu ona sormadan bilemezsiniz. O çok şey gördü ama çok az konuşur."
            secilen_dedektif_karakteri "Peki neden Elena'yı kovmadınız? Sonuçta oğlunuzu tehdit etti."
            "Matilda Steiner'ın yeniden gözleri doldu, bu sefer göz yaşlarını tutamadı."
            kurbanin_annesi "Elena'nın ailesi eski hizmetçilerimiz..."
            kurbanin_annesi "Onları depoda çıkan yangın nedeniyle kaybettik. Bizi kurtardılar... onlara borçluyduk."
            kurbanin_annesi "O yangın gecesi Elena henüz yedi yaşındaydı... bizi dışarı çıkarttıktan sonra annesi onu alevlerin arasından dışarı itmiş, kendisi ise çıkamamıştı."
            kurbanin_annesi "Kucağımda titreyerek ağlıyordu. O günden sonra onun annesi gibi olmaya çalıştım. Kovmak mı? O benim kızım gibiydi. Bazen öz kızım gibi bile..."
            kurbanin_annesi "Ancak Elena büyüdükçe bize borçlu hissetti ve malikanede çalışmak istediğini söyledi. Çok ısrar ettiği için kabul etmek zoruda kaldık..."
            kurbanin_annesi "Lukas’la aralarındaki gerilimi biliyordum ama Elena asla zarar vermez diye düşündüm. Onda hâlâ o gece gözlerime bakan o küçük kız vardı."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Matilda Hanım."
        "Belki bu mektup bir annenin çaresizliğiydi. Oğlunuzu uyarmak istemiş olabilirsiniz. Size saldırmak için değil, anlamak için buradayım.":
            secilen_dedektif_karakteri "Belki bu mektup bir annenin çaresizliğiydi. Oğlunuzu uyarmak istemiş olabilirsiniz. Size saldırmak için değil, anlamak için buradayım."
            kurbanin_annesi "Dedektif… Lukas benim oğlumdu ama o... beni defalarca küçük düşürdü. İnsanlara, özellikle kadınlara kötü davranıyordu. Onun annesi olmaktan bazen utanıyordum."
            secilen_dedektif_karakteri "Bunu anlamak kolay değil ama lütfen söyleyin. Bu mektup sizi değilse kimi işaret ediyor?"
            "Matilda derin bir nefes aldı."
            kurbanin_annesi "El yazısı benzese de ben değilim ama mektubun tarzı... Elena’nın yazılarına benziyor."
            kurbanin_annesi "Hizmetçi olarak köşkte çok şey yaşadı. Belki bir uyarıydı bu mektup belki de haykırış..."
            secilen_dedektif_karakteri "Anlıyorum. Yardımcı olduğunuz için teşekkür ederim."
    jump supheliler_sorgulaniyor

label sorgu_kurbanin_babasi:
    scene sorgu_odasi at bg_fullscreen
    show kurbanin_babasi_resim at karakter_buyuk_sol with dissolve

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright

    secilen_dedektif_karakteri "Bay Steiner, Lukas’la son zamanlarda pek görüşmediğiniz doğru mu?"
    kurbanin_babasi "Doğru. İşlerim yoğundu. Bazı şeyler... önceliği kaybediyor bazen."
    secilen_dedektif_karakteri "Babanız olarak onunla neden bu kadar mesafe koydunuz?"
    kurbanin_babasi "Belki başarısızlığı görmek istemedim. Belki kendimde onun hatalarını gördüm. Bilmiyorum. Kaçtım sadece."
    secilen_dedektif_karakteri "Kadınlara karşı tutumunuz oğlunuzunkine benziyor muydu?"
    kurbanin_babasi "Eskiden ben de hatalar yaptım ama zaman insanı değiştiriyor. Ben değiştim. Oğlumsa aynı kaldı."
    menu:
        "Bana dürüst olun, Lukas’ı durdurmaya çalıştınız mı? Ona karşı ölümcül bir öfke duydunuz mu?":
            secilen_dedektif_karakteri "Bana dürüst olun, Lukas’ı durdurmaya çalıştınız mı? Ona karşı ölümcül bir öfke duydunuz mu?"
            kurbanin_babasi "Ona karşı öfkem vardı, evet ama ölümcül mü? Hayır. Oğlumdu o. Ne kadar hayal kırıklığı yaşatsam da... onu gömmek istemezdim."
            secilen_dedektif_karakteri "Sessizliğiniz ve geçmişiniz sizi daha da şüpheli yapıyor. Üstelik odanızda bir mektup bulundu."
            secilen_dedektif_karakteri "Yazı stili eşinizin yazı stili ile uyuşuyor, utanç kaynağınızı belki de ortadan kaldırmak istediniz."
            kurbanin_babasi "Saçmalamayın. O mektup eşimin olamaz. Evet, Lukas’la aramız iyi değildi ama bu kadar ileri gidecek biri değiliz."
            secilen_dedektif_karakteri "Kusura bakmayın Bay Steiner. Bu sadece bir olasılık. Elimizdeki her ihtimali değerlendirmek zorundayım."
            "Gregory ellerini masaya koydu."
            kurbanin_babasi "Anlıyorum. İşiniz kolay değil. Ama size şunu söyleyeyim; ben Lukas’ın ölümünü isteyecek kadar nefret dolu biri olmadım. Sadece ondan yoruldum..."
            secilen_dedektif_karakteri "Yoruldum derken?"
            kurbanin_babasi "Onunla ne zaman konuşmaya çalışsam ya bir duvara çarptım ya da kendimi suçlu hissettim. Matilda arada kaldı."
            kurbanin_babasi "Elena'ya bağırdı, çalışanları aşağıladı. Hiç kimseye karşı gerçek bir sevgi göstermedi ve ben onu değiştiremedim."
            secilen_dedektif_karakteri "Peki ya eşiniz? Matilda Lukas'a karşı bir tehdit unsuru olabilir mi sizce?"
            kurbanin_babasi "Matilda mı? Hayır. O hâlâ Lukas'ı savunurdu. İçten içe üzülse de tam anlamıyla bir anne gibi davranırdı."
            kurbanin_babasi "Onun ölmesini asla istemezdi ama korkuyordu. Bunu fark etmem zaman aldı."
            secilen_dedektif_karakteri "Korkuyor muydu? Neden?"
            kurbanin_babasi "Lukas kontrolden çıkmıştı. Ona bir şey söylendiğinde öfkeleniyor, bağırıyor, etrafa zarar veriyordu."
            kurbanin_babasi "Bir gün cam bir vazoyu yere fırlattı... Matilda'nın yüzüne parça sıçradı. O olaydan sonra odasına bile yaklaşamaz olduk."
            secilen_dedektif_karakteri "Bu olayı neden daha önce anlatmadınız?"
            kurbanin_babasi "Çünkü oğlumun adını daha fazla kirletmek istemedim. Onu kaybettik... ama her şeyine rağmen benim oğlumdu."
            secilen_dedektif_karakteri "Anlıyorum... Bu söyledikleriniz soruşturmada önemli olabilir. Son bir sorum olacak. Cinayet gecesi, gerçekten bodruma yalnız başınıza mı indiniz?"
            kurbanin_babasi "Evet. Kimseyle karşılaşmadım. Sessizlik iyi gelir sanmıştım. Ne ironi… o sessizlik o gece çok şeyin üzerini örtmüş."
            secilen_dedektif_karakteri "Peki. İş birliğiniz için teşekkür ederim Bay Steiner. Gerekirse tekrar konuşmak isteyebilirim."
            kurbanin_babasi "Elbette. Umarım adalet yerini bulur. Ve umarım Lukas’ın adı sadece hatalarıyla anılmaz."
    jump supheliler_sorgulaniyor

label sucluyu_sec:
    scene sorgu_odasi at bg_fullscreen
    show sef_resim at karakter_buyuk_sol with dissolve
    sef "[dedektif_isim] gösterdiğiniz yoğun çaba için teşekkürler şimdi yaptığınız sorgulamalara göre kesin olarak suçluyu bulduk diyebilir misiniz?"
    menu:
        "Evet":
            sef "[dedektif_isim] suçlu kim?"
            menu:
                "Hizmetçiyi (Elena) suçla":
                    jump suclu_hizmetci
                "Eski sevgilinin abisini (Arthur) suçla":
                    jump suclu_eski_sevgilinin_abisi
                "Delil yetersiz, suçlu ilan etme":
                    jump suclu_yok
                "Kurbanın annesini (Matilda) suçla":
                    jump suclu_kurbanin_annesi
                "Kurbanın babasını (Gregory) suçla":
                    jump suclu_kurbanin_babasi
        "Emin Değilim...":
            sef "Sorguları yeniden dinlemek ister misin?"
            menu:
                "Evet":
                    jump supheliler_sorgulaniyor
                "Hayır":
                    jump sucluyu_sec

label suclu_eski_sevgilinin_abisi:
    scene sorgu_odasi at bg_fullscreen
    jump son1

label suclu_hizmetci:
    scene sorgu_odasi at bg_fullscreen
    jump son2

label suclu_yok:
    scene sorgu_odasi at bg_fullscreen
    jump son3

label suclu_kurbanin_annesi:
    scene sorgu_odasi at bg_fullscreen
    jump son4

label suclu_kurbanin_babasi:
    scene sorgu_odasi at bg_fullscreen
    jump son5

label son1:
    scene sorgu_odasi at bg_fullscreen
    show eski_sevgili_abisi_resim at karakter_buyuk with dissolve
    "Dedektifin zihninde, parçalar nihayet birleşti. Yudumlanmamış çay, hizmetçinin paniklemiş bakışları, Arthur’un korumacı öfkesi ve Clara’nın suskunluğu..."
    "Dedektif hizmetçiyi tekrar sorgular. Elena bitki özünü fazlaca koyduğunu kabul eder ancak o anda cinayetin bıçakla işlendiği hatırlatılır."
    "Bu detayla birlikte, gerçek niyetin zehirlemeye çalışmak olduğu ortaya çıkar ancak çay içilmediği için plan boşa çıkmıştır."
    "Bu noktada Arthur’un baskıya dayanamayıp yaptığı itiraf devreye girer:"
    eski_sevgili_abisi "O… Clara’yı üzüyordu. Onu her gördüğümde dişlerimi sıkıyordum. O gece… gözüm döndü. Sadece durdurmak istedim. Ama elimdeki bıçak...'"

    hide eski_sevgili_abisi_resim
    scene kasaba at bg_fullscreen
    show sef_resim at karakter_buyuk_sol with dissolve
   
    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright
    sef "Tebrik ederim dedektif, sayende Steiner vakasını çözebildik. Soruşturmaya göre sana gerçeği açıklayacağım."
    sef "Zehir planını hizmetçi Elena kurmuş ama ölümcül darbe Arthur von Eltz’den geldi."
    sef "Clara’nın hareketlerinden de anlaşılacağı üzere planı biliyor ama susturulmuş. Bu da onu işbirlikçi yapar."
    sef "Lukas Steiner, nefretle çevrili bir adamdı. Öldürülmesi bireysel bir öfkenin değil, bir zincirin sonucudur."
    secilen_dedektif_karakteri "Bir çay fincanı. İçilmeyen bir çay ve bir adam… çok fazla düşmana sahip bir adam."
    
    scene kasaba at bg_fullscreen
    "Yerel Gazete yazar..."
    "Katil bulundu, Arthur tutuklanır."
    "Clara ve hizmetçi ise 'delil yetersizliğinden' serbest bırakılır ama şehirden ayrılmak zorunda kalırlar."
    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright
    "Dedektif raporuna şöyle yazar:"
    secilen_dedektif_karakteri "Bu dava kapandı. Ama Steiner’ın gölgesi... başka hayatları da karartmış olabilir."
    secilen_dedektif_karakteri "Bu sona değil, bir başlangıca benziyor."
    return

label son2:
    scene sorgu_odasi at bg_fullscreen
    show hizmetci_resim at karakter_buyuk with dissolve
    "Deliller hizmetçiyi gösteriyordu. Zehirli çay, mutfak bilgisi, parmak izi. Başka ne gerekiyordu ki?"
    "Dedektif, Elena’yı cinayetle suçlar. Hizmetçi gözyaşlarıyla bağırır:"
    hizmetci "Hayır! Yemin ederim ben öldürmedim. Ben sadece... onu biraz korkutmak istedim!"
    "Clara ağlar, Arthur dişlerini sıkar ama hiçbir şey söylemez. Dedektif, 'iş tamam' diye düşünür."
    "Aylar sonra anonim bir mektup gelir dedektife."
    "'Hizmetçi suçlu değildi. Cinayet, bir koruyucunun öfkesiydi. Sen yanlış kişiyi mahkum ettin. Şimdi onun kanı da senin vicdanında.'"
    "Hizmetçi hapse girer, Clara ve Arthur sessizce yaşamlarına devam eder."
    "Dedektifin itibarı sorgulanır."
    "Yerel Gazete yazar..."
    "Dedektif, yanlış kadını içeri tıktı mı? Çay fincanı mı yoksa bir bıçak mı gerçek delildi?'"
    return

label son3:
    scene sorgu_odasi at bg_fullscreen
    "Hiçbir şey tam olarak uyuşmuyor. Parmak izi, ama içilmemiş çay. İtiraf ama yanlış silah. Öfke ama suskunluk…"
    "Dedektif hiçbir şüpheliyi suçlayamaz. Elindeki kanıtlar her birini işaret eder ama aynı anda hiç kimseyi de net olarak göstermez."
    "Savcılık, dosyanın kapatılmasını ister."
    "Yerel Gazete yazar..."
    "Deliller yetersiz. Bu cinayet faili meçhul kalacak."
    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk with dissolve
    else:
        show dedektif_k_resim at karakter_buyuk with dissolve
    "Dedektif dosyayı kapatır, odasına döner. Günlüğüne şöyle yazar:"
    "'Lukas Steiner’ın ruhu hâlâ bu evde dolaşıyor. Ne Elena’nın korkusu ne Clara’nın hüznü ne de Arthur’un suskunluğu… gerçeği açığa çıkarmaya yetmedi.'"
    if secilen_dedektif_tipi == "erkek":
        hide dedektif_e_resim at karakter_buyuk with dissolve
    else:
        hide dedektif_k_resim at karakter_buyuk with dissolve
    "Cinayet çözülmedi ve kurbanın ailesi tatmin olmadı."
    "Dedektif başka bir davaya verildi."
    "'Bu dava burada bitti ama cevaplar hâlâ bu duvarlarda yankılanıyor.'"
    return

label son4:
    scene kasaba at bg_fullscreen
    show kurbanin_annesi_resim at karakter_buyuk with dissolve
    "Dedektif, mektubu, Matilda’nın gözyaşlarını ve bastırılmış öfkesini birleştirdi. El yazısı eşleşiyor, Lukas’a tehditler savrulmuş. Geriye sadece bir imza eksik kalmıştı."
    "Matilda tutuklandığında sessiz kaldı. Ne yalanladı, ne de itiraf etti."
    "Olay kasabada büyük yankı uyandırdı. Bir anne, öz oğlunu öldürmüş müydü? Herkes ikiye bölündü."
    "Ancak birkaç gün sonra, gerçek suç aleti bodrum katındaki eski sandığın altında bulundu. Üzerindeki parmak izleri Matilda’ya ait değildi."
    "Yerel gazete yazıyor..."
    "Dedektif vakayı kapattı ama arkasında kırık bir onur ve yarım kalan bir adalet bıraktı."
    hide kurbanin_annesi_resim with dissolve
    "Matilda Steiner serbest bırakıldı. Ancak herkesin gözünde hala bir şüpheli…"
    "Lukas’ın gerçek katili hâlâ bulunamadı. Ve siz başka bir kasabada, yeni bir vakayla görevlendirildiniz."
    return

label son5:
    scene kasaba at bg_fullscreen
    show kurbanin_babasi_resim at karakter_buyuk with dissolve
    "Dedektif, Gregory’nin bodruma inişini, mektubu ve geçmişteki şiddet eğilimini kafasında tarttı. Bir baba, öfkesiyle oğlunu öldürebilir miydi?"
    "Cevap, ayakkabı izlerinin yönü ve bıçaktaki tutarsız parmak izlerinde gizliydi."
    "Gregory tutuklandığında ilk kez gözleri doldu."
    kurbanin_babasi "Ben oğlumu sevmedim belki ama… onu öldürmedim"
    "Basın ve halk memnundu. Zengin bir adam düşmüştü. Adalet yerini bulmuş gibi görünüyordu."
    "Ama aylar sonra dedektif bir haber aldı."
    "Elena adlı eski hizmetçi intihar etmişti. Ardında kısa bir not bırakmıştı:"
    "'O gece kahveyi ben hazırladım. Ama asıl planı ben yapmadım. Gerçek suçlular... hâlâ serbest.'"
    "Yerel Gazete yazıyor..."
    "Dedektif, birilerini suçladı ama belki de sadece en kolay hedefi seçti."
    "Gregory Steiner mahkum edildi ama bu dava… hiçbir zaman tam olarak kapanmadı."
    return