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
image dedektif_e_resim = "images/karakterler/erkek_dedektif.png"
image dedektif_k_resim = "images/karakterler/kadin_dedektif.png"
image hizmetci_resim = "images/karakterler/hizmetci.png"
image eski_sevgili_resim = "images/karakterler/eski_sevgili.png"
image eski_sevgili_abisi_resim = "images/karakterler/eski_sevgili_abisi.png"
image kurbanin_annesi_resim = "images/karakterler/kurbanin_annesi.png"
image kurbanin_babasi_resim = "images/karakterler/kurbanin_babasi.png"
image sef_resim = "images/karakterler/sef.png"


# Transform tanımlamaları
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

    "Zengin ve küstah genç adam Lukas Steiner, odasında cansız halde bulundu. Parmaklarının ucunda bir kahve fincanı, göğsünde ise soğuk bir bıçağın izini taşıyan derin bir yara..."

    "Steiner, kadınlara karşı küçümseyici tavırlarıyla tanınır; ardında incinmiş kalpler, bastırılmış öfkeler ve sessizce yutulmuş nefretler bırakırdı."

    "O sabah, kahve fincanındaki parmak izleri ve tek bir yudum dahi alınmamış kahve, olayın yalnızca başlangıcıydı."

    "Hizmetçi gözaltına alındı. Fakat o evde herkesin bir bahanesi, herkesin karanlıkta kalan bir yüzü vardı."
    "Zira bazı sırlar, kahveden bile daha acıydı."
    
    jump dedektif_secimi

label dedektif_secimi:
    scene sorgu_odasi at bg_fullscreen with fade
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

    sef "Kasabamıza hoş geldiniz, Dedektif. Sizlerle tanışmak büyük bir onurdur."

    menu:
        "Kasaba şefiyle tanış":
            if secilen_dedektif_tipi == "erkek":
                show dedektif_e_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Memnun oldum, nasılsınız? Dosyayı inceledim, ancak bana olayı kısaca anlatır mısınız?"
            elif secilen_dedektif_tipi == "kadin":
                show dedektif_k_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Memnun oldum, nasılsınız? Dosyayı inceledim, ancak bana olayı kısaca anlatır mısınız?"
            $ tanisma_secildi = True

        "Direkt vakaya geç":
            if secilen_dedektif_tipi == "erkek":
                show dedektif_e_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Merhaba Şef, hemen vakaya geçebilir miyiz?"
            elif secilen_dedektif_tipi == "kadin":
                show dedektif_k_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Merhaba Şef, hemen vakaya geçebilir miyiz?"
            $ tanisma_secildi = False

    if tanisma_secildi:
        jump tanis
    else:
        jump gec

label tanis:
    show sef_resim at karakter_buyuk_sol with dissolve
    sef "İyiyim, umarım siz de iyisinizdir... Dedektif, sabah saatlerinde bağırışlar üzerine yukarı çıktık. Lukas Steiner odasında ölü bulundu."
    sef "Göğsünde derin bir bıçak yarası vardı. Yanında da dokunulmamış bir kahve fincanı..."
    sef "Parmak izleri hizmetçiye aitmiş ama kız kahveyi içmeden bırakmış. Hizmetçi zehir koyduğunu kabul ediyor ama 'öldürmedim' diyor."
    sef "O evde herkesin bir bahanesi var ama hiçbiri temiz değil, bilesiniz."
    
    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag
    else:
        show dedektif_k_resim at karakter_buyuk_sag

    secilen_dedektif_karakteri "Şüpheliler belliyse hemen sorgulamak istiyorum."

    jump supheliler_sorgulaniyor

label gec:
    show sef_resim at karakter_buyuk_sol with dissolve
    sef "Anladım Dedektif. O zaman hemen vakaya geçelim..."
    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
        secilen_dedektif_karakteri "Şüpheliler belli ise hemen sorgulamak istiyorum"
    elif secilen_dedektif_tipi == "kadin":
        show dedektif_k_resim at karakter_buyuk_sag with moveinright
        secilen_dedektif_karakteri "Şüpheliler belli ise hemen sorgulamak istiyorum"

    jump supheliler_sorgulaniyor


# Oyun değişkenleri
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
        "Suçluyu Belirle" if sorgu_hizmetci_dinlendi and sorgu_eski_sevgili_dinlendi and sorgu_eski_sevgili_abisi_dinlendi and sorgu_kurbanin_annesi_dinlendi and sorgu_kurbanin_babasi_dinlendi:
            jump sucluyu_sec

label sorgu_hizmetci:
    scene sorgu_odasi at bg_fullscreen
    show hizmetci_resim at karakter_buyuk_sol with moveinleft

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright

    secilen_dedektif_karakteri "Direkt konuya gireceğim, boş vaktimiz yok. Lukas Steiner vefat ettiği zaman elinde fincan vardı. Kahveyi sen hazırlamışsın Elena Hanım. Fincanda sadece senin parmak izlerin var. Bunu nasıl açıklarsın?"
    hizmetci "…"
    hizmetci "Kahveyi hazırladım evet ama sadece içine biraz bitki özü kattım. Uykusuzdu son günlerde. Ona zarar vermek istemedim."
    menu: 
        "Kahve içilmemiş. Bu durum için üzgün olmalısınız, sonuçta yardımcı olamadınız.":
            hizmetci "Evet gerçekten çok üzgünüm… Bir yudum bile içse uykusuzluğuna çok iyi geleceğine emindim."
            secilen_dedektif_karakteri "Anladım. Mutfakta olduğunuz için bıçakların hepsini biliyor olmalısın sonuçta mutfakta çalışıyorsun. Steiner’ın ölüm sebebi bıçak yarası, buna ne diyeceksiniz?"
            hizmetci "Evet, bıçakları tanırım. Ama o bıçaklıkta değildi. Yani... biri almıştı zaten."
            secilen_dedektif_karakteri "Bunu nereden çıkardınız? Bu sizin sorumluluğunuzdaydı. Bıçağı birine siz vermiş olabilir misiniz?"
            "Elena keskin bir şekilde cevap verdi"
            hizmetci "Hayır."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Elena Hanım."
        "Bitki özü katmanla zarar vermenin ne alakası olabilir ki? Bir ihtimal fincanın içinde bitki özünden başka bir şeyde olabilir mi Elena hanım?":
            hizmetci "Bitki özü ve biraz şeker koydum, kahvenin içinde başka bir şey yoktu "
            "Elena gözlerini kaçırır, parmakları ile oynar"
            secilen_dedektif_karakteri "Anladım, zaten olay olduğu sırada bodruma indiğini söylüyorsun. Neden bodruma inmiştin?"
            hizmetci "Akşam yemeği için malzeme almam gerekiyordu."
            secilen_dedektif_karakteri "Sizi gören biri oldu mu?"
            hizmetci "Gitmeden önce Matilda hanıma haber vermiştim."
            secilen_dedektif_karakteri "Anladım. Mutfakta olduğunuz için bıçakların hepsini biliyor olmalısın sonuçta mutfakta çalışıyorsun. Steiner’ın ölüm sebebi bıçak yarası, buna ne diyeceksiniz?"
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

    secilen_dedektif_karakteri "Merhaba Clara hanım, Lukas’la ilişkiniz çalkantılıydı. Ne sıklıkla görüşüyordunuz?"
    eski_sevgili "Çok... Sık sık ayrılıp barışırdık. Ama hep o terk ederdi. Beni oyuncak gibi görürdü."
    menu:
        "O gün konuştunuz mu?":
            secilen_dedektif_karakteri "O gün konuştunuz mu?"
            eski_sevgili "Hayır. Görüşmedik. Zaten konuşacak pek bir şeyimiz kalmamıştı."
            secilen_dedektif_karakteri "Peki onu öldürmeyi hiç düşündünüz mü?"
            eski_sevgili "Bir an... sadece bir an aklımdan geçti. Ama yapmadım. Yapamazdım."
            secilen_dedektif_karakteri "Kardeşiniz Arthur çok korumacı. Onun bir şey yapmış olmasından şüpheleniyor musunuz?"
            eski_sevgili "Arthur beni korur evet. Ama bazen fazla ileri gidebilir… Umarım bir çılgınlık yapmamıştır."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Clara hanım."
        "Bana biraz Lukas Steiner’ı anlatır mısınız?":
            secilen_dedektif_karakteri "Bana biraz Lukas Steiner’ı anlatır mısınız?"
            eski_sevgili "O bencildi. Bencilden çok narsist demek yanlış olmaz. Kendisinden başka kimsenin üstün olmadığını düşünürdü."
            "Clara’nın gözleri dolar."
            eski_sevgili "Ama onu çok seviyorum... hala çok seviyorum, benim biricik Lukas’ım… Sonumuz böyle olamazdı."
            "Dedektif, Clara’ya mendil uzattı. Clara mendili alıp göz yaşlarını silerken dedektif konuştu."
            secilen_dedektif_karakteri "Onu öldürmeyi hiç düşündünüz mü?"
            eski_sevgili "Ne?! Saçmalamayın ne dediğimi görmüyor musunuz? Biricik Lukas’ımı nasıl öldürebilirim?!"
            secilen_dedektif_karakteri "Kişiliği çok da iyi değilmiş sizin de dediğiniz gibi ayrıca birçok kişi Lukas Steiner’ın size kötü davrandığını söylüyor bu durumda içten içe ona kinlenmiş olabilirsiniz."
            "Clara öfke dolu bakışlarını dedektife kilitledi."
            eski_sevgili "Evet, belki bana kötü davrandı… belki kalbimi paramparça etti ama onu öldürecek kadar nefret etmedim! Ben sadece… sadece onun değişmesini istedim… Sevdiği bir adam gibi olmasını… Ama her defasında beni daha fazla kırdı. Bu, onu öldürmek istediğim anlamına gelmez!"
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Clara hanım."

    jump supheliler_sorgulaniyor

label sorgu_eski_sevgili_abisi:
    scene sorgu_odasi at bg_fullscreen
    show eski_sevgili_abisi_resim at karakter_buyuk_sol with dissolve

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    secilen_dedektif_karakteri "Merhaba Arthur, kız kardeşin için endişelendiğini biliyorum. Ama Lukas’a zarar verdin mi?"
    eski_sevgili_abisi "Onu tehdit ettim evet... ama ben öldürmedim."
    secilen_dedektif_karakteri "Üniformanda Lukas’a ait kan lekesi var. Bunu nasıl açıklarsın?"
    eski_sevgili_abisi "Onu engellemeye çalıştım. O gece Clara’ya gitmeye kalktı. Aramızda boğuşma oldu... ama o sırada canlıydı."
    menu:
        "Gerçekleri anlatmazsan, işini kaybedebilirsin":
            secilen_dedektif_karakteri "Gerçekleri anlatmazsan, işini kaybedebilirsin"
            eski_sevgili_abisi "İşimi mi? Bu benim onurum. Ama... belki haklısın. Belki bir hata yaptım. Onu durdurmalıydım..."
            secilen_dedektif_karakteri "Neyden bahsettiğinizi bilmiyorum ancak gerçekten şüpheli davranıyorsunuz Arthur bey."
            eski_sevgili_abisi "Bakın… o gece Clara ağlıyordu o adi yine onu aşağılamış, küçük düşürmüştü. Dayanamadım! Lukas’a hesap sormaya gittim. Tartıştık, üstüme yürüdü ve boğuşma yaşadık ama onu orada, yerde bıraktım. Hâlâ yaşıyordu, yemin ederim!"
            secilen_dedektif_karakteri "Bana o gece orada olduğunuzu kanıtlayacak birini söyler misiniz?"
            eski_sevgili_abisi "Köşkteki hizmetçi Elena o gün beni içeri almıştı."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Arthur Bey."
        "Neden aranızda bir boğuşma oldu? Ayrıca bir gün öncesinde buluştuğunuza dair bir bilgilendirme almadım. Köşk hizmetçileri cinayetin işlendiği sabah geldiğinizi ve Lukas Steiner’la sohbet etmek için odasına gittiğinizi söylüyor.":
            secilen_dedektif_karakteri "Neden aranızda bir boğuşma oldu? Ayrıca bir gün öncesinde buluştuğunuza dair bir bilgilendirme almadım. Köşk hizmetçileri cinayetin işlendiği sabah geldiğinizi ve Lukas Steiner’la sohbet etmek için odasına gittiğinizi söylüyor"
            eski_sevgili_abisi "Ne ima etmeye çalışıyorsunuz, ha?!"
            eski_sevgili_abisi "Kardeşim o adamın elinde oyuncak oldu yıllarca! Onun ne yaptığını, nasıl aşağıladığını bilmiyorsunuz!"
            eski_sevgili_abisi "Evet, Lukas’la o sabah görüştüm! Evet, onunla boğuştum ama öldürmedim! Eğer onu bıçaklayan biri varsa, belki de yıllardır içlerinde biriken nefreti artık taşıyamayan biridir!" 
            eski_sevgili_abisi "Ama ben değilim! Ben sadece... Clara’yı korumaya çalıştım! Suç mu bu?!"
            secilen_dedektif_karakteri "Sakin olun Arthur. Ben burada sizinle kavga etmeye gelmedim. Ama siz şu an bana, kontrolünü kaybedebilen bir adamın resmini çiziyorsunuz. Bu kontrolsüzlük… bir bıçağı göğse saplamaya ne kadar uzak olabilir ki?"
            eski_sevgili_abisi "Ben bir askerim, dedektif! Kraliyet muhafızıyım! Duygularımla hareket edecek kadar acemi değilim. Onun gibi pisliklere karşı bile!"
            secilen_dedektif_karakteri "Ve askerlik onuru bazen aile onurunun gerisinde kalmaz mı? Mesela bir adam, kız kardeşinin onurunu kurtarmak için kan dökmeyi göze almaz mı?"
            eski_sevgili_abisi "Siz ne bilirsiniz aileyi, onuru, çaresizliği?! O herife kaç kez söyledim kardeşimden uzak dur diye ama dinlemedi."
            eski_sevgili_abisi "O gece Clara odasında ağlıyordu. Gittim Lukas’ın yüzüne tükürdüm… bir de sadece yumruk attım. Bıçak falan yoktu! Ona zarar vermek isteseydim... çok daha fazlasını yapardım."
            secilen_dedektif_karakteri "Demek yumruk attınız. Bu ilk kez duyduğum bir detay. Neden şimdi söylüyorsunuz?"
            eski_sevgili_abisi "Çünkü biliyorum! Şimdi söyledim diye ‘katil’ damgası vuracaksınız! Ama ben öldürmedim! O kahrolası herif ölümü belki hak etti ama o bıçağı ben saplamadım!"
            secilen_dedektif_karakteri "Eğer doğruyu söylüyorsanız, o zaman sizin çıkışınızdan sonra bir başkasının odaya girdiğini kanıtlamamız gerek ama eğer yalan söylüyorsanız… o zaman bu çıkışınız sadece son çırpınışınız olur."
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
    kurbanin_annesi "Üzgünüm elbette. Ama size bir sır vereyim dedektif… Oğlumun karakteri bozuktu. Kadınlara saygısı yoktu. Belki bu onun sonuydu."
    secilen_dedektif_karakteri "Oğlunuza karşı öfke duyduğunuz oldu mu?"
    kurbanin_annesi "Evet. Ama bir anne öfkeyle cinayet işlemez. Sessizce utançla bekler sadece..."
    secilen_dedektif_karakteri "Bu mektup... Lukas’a yazılmış tehditlerle dolu. Yazı stilinizle eşleşiyor."
    kurbanin_annesi "Ben yazmadım. Ama kimin yazdığını tahmin edebiliyorum."
    menu:
        "Eğer kimin yazdığını biliyorsanız, söylemek zorundasınız Matilda Hanım. Aksi halde sizi gizli tanık değil, şüpheli olarak ele alırım.":
            secilen_dedektif_karakteri "Eğer kimin yazdığını biliyorsanız, söylemek zorundasınız Matilda Hanım. Aksi halde sizi gizli tanık değil, şüpheli olarak ele alırım."
            kurbanin_annesi "Beni tehdit mi ediyorsunuz, dedektif?"
            secilen_dedektif_karakteri "Hayır, sadece gerçeği arıyorum. Ve siz o gerçeği saklıyorsunuz gibi görünüyor."
            "Matilda Steiner’ın gözleri dolar ve kısık sesle konuşur"
            kurbanin_annesi "Tamam… Tamam… O mektubu ben yazmadım… ama kimin yazdığını biliyorum. Kocam… Gregory"
            secilen_dedektif_karakteri "Gregory mi? Lukas’ın babası?"
            kurbanin_annesi "Evet. Gregory, Lukas’ın kadınlara olan tavırlarına eskiden göz yumar, hatta desteklerdi. Ama yaşlandıkça... değişti." 
            kurbanin_annesi "Bir gece Lukas bana bağırırken Gregory odaya girdi ve ‘bir daha annene sesini yükselttiğini duyarsam, bu ev senin için mezar olur’ dedi."
            secilen_dedektif_karakteri "Yani diyorsunuz ki Gregory oğlunu tehdit etti. Bu soruşturma için oldukça önemli bir detay, Matilda Hanım."
            kurbanin_annesi "Gregory bazen susar ama öfkesini biriktirir. Bunu yapabileceğini düşünmüyorum ama... ihtimal dışı da değil."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Matilda Hanım."
        "Belki bu mektup bir annenin çaresizliğiydi. Oğlunuzu uyarmak istemiş olabilirsiniz. Size saldırmak için değil, anlamak için buradayım.":
            secilen_dedektif_karakteri "Belki bu mektup bir annenin çaresizliğiydi. Oğlunuzu uyarmak istemiş olabilirsiniz. Size saldırmak için değil, anlamak için buradayım."
            kurbanin_annesi "Dedektif… Lukas benim oğlumdu. Ama o... beni defalarca küçük düşürdü. İnsanlara, özellikle kadınlara kötü davranıyordu. Onun annesi olmaktan bazen utanıyordum."
            secilen_dedektif_karakteri "Bunu anlamak kolay değil ama lütfen söyleyin. Bu mektup sizi değilse kimi işaret ediyor?"
            kurbanin_annesi "Gregory. Kocam. Bir süredir çok öfkeliydi Lukas’a. ‘Biz böyle bir evlat yetiştirmedik’ diyordu. Mektubu o yazmış olabilir. El yazımız benzerdir… belki de dikkatli bakarsanız farkı görebilirsiniz."
            secilen_dedektif_karakteri "Anlıyorum. Teşekkür ederim. Bunu doğrulamak için Gregory ile de konuşmam gerekecek"
    jump supheliler_sorgulaniyor

label sorgu_kurbanin_babasi:
    scene sorgu_odasi at bg_fullscreen
    show kurbanin_babasi_resim at karakter_buyuk_sol with dissolve

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
    else:
        show dedektif_k_resim at karakter_buyuk_sag with moveinright

    secilen_dedektif_karakteri "Bay Steiner, Lukas’la son zamanlarda pek görüşmediğiniz doğru mu?"
    kurbanin_babasi "İşim başımdan aşkındı. Oğlum benim ilgimi hak etmiyordu zaten."
    secilen_dedektif_karakteri "Cinayet gecesi bodruma inmişsiniz. Neden?"
    kurbanin_babasi "Havadar bir yer. Sakinleşmek için inmiştim."
    secilen_dedektif_karakteri "Ayakkabı iziniz bulunmuş. Bu da mı tesadüf?"
    kurbanin_babasi "Tesadüf değil, doğruluk. Bir şey sakladığım yok, o gün bodruma indiğimi zaten söylüyorum."
    secilen_dedektif_karakteri "Peki kadınlara karşı tutumunuz oğlunuzunkine benziyor mu?"
    kurbanin_babasi "Eskiden ben de öyleydim. Ama yaşlandım... Onlara muhtacım artık. Lukas bunu kabul edemedi."
    menu:
        "Bana dürüst olun, Lukas’ı durdurmaya çalıştınız mı? Ona karşı ölümcül bir öfke duydunuz mu?":
            secilen_dedektif_karakteri "Bana dürüst olun, Lukas’ı durdurmaya çalıştınız mı? Ona karşı ölümcül bir öfke duydunuz mu?"
            kurbanin_babasi "Evet, öfkelendim. Bir babanın oğluna duyduğu hayal kırıklığı, sandığınızdan daha ağırdır."
            secilen_dedektif_karakteri "Sessizliğiniz ve geçmişiniz sizi daha da şüpheli yapıyor. Ayrıca mektubun sizin el yazınıza benzediği iddiası var."
            kurbanin_babasi "Ne?! Ben mi yazmışım? Güzel numara. Ama o mektubu ben değil... Matilda yazdı. Oğluna ne kadar hayal kırıklığı duyduğunu biliyordum. Belki de o beni korumaya çalışıyor, kim bilir?"
            secilen_dedektif_karakteri "Yani eşinizin sizi suçlamak üzere olduğunu söylüyorsunuz?"
            kurbanin_babasi "Hayır... Ama onu da göz önünde bulundurmanızı öneririm, dedektif. Herkesin bir sınırı vardır."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Gregory bey."
    
        "Eşinizin el yazısına benzeyen bir tehdit mektubu bulduk. Ama Matilda, yazının size ait olduğunu düşünüyor.":
            secilen_dedektif_karakteri "Eşinizin el yazısına benzeyen bir tehdit mektubu bulduk. Ama Matilda, yazının size ait olduğunu düşünüyor."
            kurbanin_babasi "Evet, yazı benim. Mektubu ben yazdım. Ama okumamışsınız galiba. Oğluma öldürmekten değil, değişmekten bahsediyordum. Kadınlara olan tavırlarını bırakmasını, annesine saygı duymasını istiyordum."
            secilen_dedektif_karakteri "Ama mektuptaki ton sert. ‘Bu ev senin mezarın olabilir’ demişsiniz."
            kurbanin_babasi "Sözlerin ardındaki niyeti bilmeden suçlama yapmayın. Ben Lukas’a babası olarak son kez gözdağı verdim. Ama onu öldürmek mi? Hayır, dedektif. Ben öyle biri değilim."
            secilen_dedektif_karakteri "Bodruma inmeniz, ayakkabı izleriniz, öfkeniz… Hepsi üst üste binince..."
            kurbanin_babasi "Oğluma öfkeliydim, evet. Ama öylece odasında canice bıçaklayacak kadar değil. Gerçek katili bulmak istiyorsanız, kahveye odaklanın ve bıçağa odaklanın."
            secilen_dedektif_karakteri "Anladım. Sorgu için teşekkürler Gregory bey."
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

# --- SONLAR ---

label son1:
    scene sorgu_odasi at bg_fullscreen
    show eski_sevgili_abisi_resim at karakter_buyuk with dissolve
    "Dedektifin zihninde, parçalar nihayet birleşti. Yudumlanmamış kahve, hizmetçinin paniklemiş bakışları, Arthur’un korumacı öfkesi ve Clara’nın suskunluğu..."
    "Dedektif hizmetçiyi tekrar sorgular. Elena zehri koyduğunu kabul eder ancak o anda cinayetin bıçakla işlendiği hatırlatılır. Bu detayla birlikte, gerçek niyetin zehirle öldürmek olduğu ortaya çıkar."
    "Ancak kahve içilmediği için plan boşa çıkmıştır."
    "Bu noktada Arthur’un baskıya dayanamayıp yaptığı itiraf devreye girer:"
    "Arthur: 'O… Clara’yı üzüyordu. Onu her gördüğümde dişlerimi sıkıyordum. O gece… gözüm döndü. Sadece durdurmak istedim. Ama elimdeki bıçak...'"

    "Kasaba Şefi: 'Tebrik ederim dedektif, sayende Steiner vakasını çözebildik. Soruşturmaya göre sana gerçeği açıklayacağım.'"
    "Kasaba Şefi: 'Zehir planını hizmetçi Elena kurmuş ama ölümcül darbe Arthur von Eltz’den geldi.'"
    "Kasaba Şefi: 'Clara’nın hareketlerinden de anlaşılacağı üzere planı biliyor ama susturulmuş. Bu da onu işbirlikçi yapar.'"
    "Kasaba Şefi: 'Lukas Steiner, nefretle çevrili bir adamdı. Öldürülmesi bireysel bir öfkenin değil, bir zincirin sonucudur.'"
    secilen_dedektif_karakteri "Bir kahve fincanı. İçilmeyen bir kahve. Ve bir adam… çok fazla düşmana sahip bir adam."
    "Katil bulundu, Arthur tutuklanır."
    "Clara ve hizmetçi ise 'delil yetersizliğinden' serbest bırakılır ama şehirden ayrılmak zorunda kalırlar."
    "Dedektif raporuna şöyle yazar:"
    "Bu dava kapandı. Ama Steiner’ın gölgesi... başka hayatları da karartmış olabilir."
    "Bu sona değil, bir başlangıca benziyor."
    return

label son2:
    scene sorgu_odasi at bg_fullscreen
    show hizmetci_resim at karakter_buyuk with dissolve
    "Deliller hizmetçiyi gösteriyordu. Zehirli kahve, mutfak bilgisi, parmak izi. Başka ne gerekiyordu ki?"
    "Dedektif, Elena’yı cinayetle suçlar. Hizmetçi gözyaşlarıyla bağırır:"
    "Elena: 'Hayır! Yemin ederim ben öldürmedim. Ben sadece... onu biraz korkutmak istedim!'"
    "Clara ağlar, Arthur dişlerini sıkar ama hiçbir şey söylemez. Dedektif, 'iş tamam' diye düşünür."
    "Aylar sonra, bir mektup gelir dedektife. Anonim:"
    "'Hizmetçi suçlu değildi. Cinayet, bir koruyucunun öfkesiydi. Sen yanlış kişiyi mahkum ettin. Şimdi onun kanı da senin vicdanında.'"
    "Hizmetçi hapse girer, Clara ve Arthur sessizce yaşamlarına devam eder."
    "Dedektifin itibarı sorgulanır."
    "Yerel gazete: 'Dedektif, yanlış kadını içeri tıktı mı? Kahve fincanı mı yoksa bir bıçak mı gerçek delildi?'"
    return

label son3:
    scene sorgu_odasi at bg_fullscreen
    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk with dissolve
    else:
        show dedektif_k_resim at karakter_buyuk with dissolve
    "Hiçbir şey tam olarak uyuşmuyor. Parmak izi, ama içilmemiş kahve. İtiraf, ama yanlış silah. Öfke, ama suskunluk…"
    "Dedektif hiçbir şüpheliyi suçlayamaz. Elindeki kanıtlar her birini işaret eder ama aynı anda hiç kimseyi de net olarak göstermez."
    "Savcılık, dosyanın kapatılmasını ister."
    "'Deliller yetersiz. Bu cinayet faili meçhul kalacak.'"
    "Dedektif dosyayı kapatır, odasına döner. Günlüğüne şöyle yazar:"
    "'Lukas Steiner’ın ruhu hâlâ bu evde dolaşıyor. Ne Elena’nın korkusu ne Clara’nın hüznü ne de Arthur’un suskunluğu… gerçeği açığa çıkarmaya yetmedi.'"
    "Cinayet çözülmedi ve kurbanın ailesi tatmin olmadı."
    "Dedektif başka bir davaya verildi."
    "'Bu dava burada bitti. Ama cevaplar hâlâ bu duvarlarda yankılanıyor.'"
    return

label son4:
    scene sorgu_odasi at bg_fullscreen
    show kurbanin_annesi_resim at karakter_buyuk with dissolve
    "Dedektif, mektubu, Matilda’nın gözyaşlarını ve bastırılmış öfkesini birleştirdi. El yazısı eşleşiyor, Lukas’a tehditler savrulmuş. Geriye sadece bir imza eksik kalmıştı."
    "Matilda tutuklandığında sessiz kaldı. Ne yalanladı, ne de itiraf etti."
    "Olay kasabada büyük yankı uyandırdı. Bir anne, öz oğlunu öldürmüş müydü? Herkes ikiye bölündü."
    "Ancak birkaç gün sonra, gerçek suç aleti bodrum katındaki eski sandığın altında bulundu. Üzerindeki parmak izleri Matilda’ya ait değildi."
    "Yerel gazete: 'Dedektif vakayı kapattı ama arkasında kırık bir onur ve yarım kalan bir adalet bıraktı.'"
    "Matilda Steiner serbest bırakıldı. Ancak herkesin gözünde hala bir şüpheli…"
    "Lukas’ın gerçek katili hâlâ bulunamadı. Ve siz başka bir kasabada, yeni bir vakayla görevlendirildiniz."
    return

label son5:
    scene sorgu_odasi at bg_fullscreen
    show kurbanin_babasi_resim at karakter_buyuk with dissolve
    "Dedektif, Gregory’nin bodruma inişini, mektubu ve geçmişteki şiddet eğilimini kafasında tarttı. Bir baba, öfkesiyle oğlunu öldürebilir miydi? Cevap, ayakkabı izlerinin yönü ve bıçaktaki tutarsız parmak izlerinde gizliydi."
    "Gregory tutuklandığında ilk kez gözleri doldu."
    "Gregory: 'Ben oğlumu sevmedim belki ama… onu öldürmedim,' dedi."
    "Basın ve halk memnundu. Zengin bir adam düşmüştü. Adalet yerini bulmuş gibi görünüyordu."
    "Ama aylar sonra dedektif bir haber aldı."
    "Elena adlı eski hizmetçi intihar etmişti. Ardında kısa bir not bırakmıştı:"
    "'O gece kahveyi ben hazırladım. Ama asıl planı ben yapmadım. Gerçek suçlular... hâlâ serbest.'"
    "Yerel gazete: 'Dedektif, birilerini suçladı ama belki de sadece en kolay hedefi seçti.'"
    "Gregory Steiner mahkum edildi. Ama bu dava… hiçbir zaman tam olarak kapanmadı."
    return