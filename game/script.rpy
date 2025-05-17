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
            dedektif_e "Erkek dedektifi seçtiniz."
            jump dedektif_isim_girisi
        "Kadın Dedektif":
            $ secilen_dedektif_tipi = "kadin"
            $ secilen_dedektif_karakteri = dedektif_k
            show dedektif_k_resim at karakter_buyuk
            hide dedektif_e_resim
            dedektif_k "Kadın dedektifi seçtiniz."
            jump dedektif_isim_girisi

label dedektif_isim_girisi:
    scene sorgu_odasi at bg_fullscreen with fade

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk
        $ dedektif_isim = renpy.input("Lütfen erkek dedektifin ismini girin:")
        if dedektif_isim == "":
            $ dedektif_isim = "Erkek Dedektif"
        $ secilen_dedektif_karakteri = Character(dedektif_isim, color="#c8c8ff")
        secilen_dedektif_karakteri "Merhaba, ben [dedektif_isim]."

    elif secilen_dedektif_tipi == "kadin":
        show dedektif_k_resim at karakter_buyuk
        $ dedektif_isim = renpy.input("Lütfen kadın dedektifin ismini girin:")
        if dedektif_isim == "":
            $ dedektif_isim = "Kadın Dedektif"
        $ secilen_dedektif_karakteri = Character(dedektif_isim, color="#c8c8ff")
        secilen_dedektif_karakteri "Merhaba, ben [dedektif_isim]."

    jump olaylar_baslangici

label olaylar_baslangici:
    scene kasaba at bg_fullscreen
   
    show sef_resim at karakter_buyuk
    "Kasabamıza hoş geldiniz Dedektif [dedektif_isim] sizlerle tanışmak büyük bir onurdur. "

    menu:
        "Kasaba şefiyle tanış":
            if secilen_dedektif_tipi == "erkek":
                show dedektif_e_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Memnun oldum ,nasılsınız? Dosyayı inceledim ancak bana olayı kısaca anlatır mısınız ?"
            elif secilen_dedektif_tipi == "kadin":
                show dedektif_k_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Memnun oldum ,nasılsınız ? Dosyayı inceledim ancak bana olayı kısaca anlatır mısınız ?"
        "Direkt vakaya geç":
            if secilen_dedektif_tipi == "erkek":
                show dedektif_e_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Merhaba Şef hemen vakaya geçebilir miyiz?"
            elif secilen_dedektif_tipi == "kadin":
                show dedektif_k_resim at karakter_buyuk_sag with moveinright
                secilen_dedektif_karakteri "Merhaba Şef hemen vakaya geçebilir miyiz?"

    jump supheliler_sorgulaniyor

label supheliler_sorgulaniyor: 
    scene sorgu_odasi at bg_fullscreen
    sef "Önce kimi sorgulamak istersiniz?"

    menu:
        "Hizmetçi":
            jump sorgu_hizmetci
        "Eski Sevgili (Clara)":
            jump sorgu_eski_sevgili
        "Eski Sevgilinin Abisi (Arthur)":
            jump sorgu_eski_sevgili_abisi
        "Kurbanın Annesi (Matilda)":
            jump sorgu_kurbanin_annesi
        "Kurbanın Babası (Gregory)":
            jump sorgu_kurbanin_babasi

label sorgu_hizmetci:
    scene sorgu_odasi at bg_fullscreen
    show hizmetci_resim at karakter_buyuk
    hizmetci "O sabah kahveyi hazırladım ama Lukas'ın odasına kimseyi almadım."
    jump supheliler_sorgulaniyor

label sorgu_eski_sevgili:
    scene sorgu_odasi at bg_fullscreen
    show eski_sevgili_resim at karakter_buyuk
    eski_sevgili "Lukas'la uzun zamandır konuşmuyorduk. O gece evde değildim."
    jump supheliler_sorgulaniyor

label sorgu_eski_sevgili_abisi:
    scene sorgu_odasi at bg_fullscreen
    show eski_sevgili_abisi_resim at karakter_buyuk
    eski_sevgili_abisi "Kız kardeşimi üzmeseydi, belki hâlâ hayatta olurdu. Ama ben ona zarar vermedim."
    jump supheliler_sorgulaniyor

label sorgu_kurbanin_annesi:
    scene sorgu_odasi at bg_fullscreen
    show kurbanin_annesi_resim at karakter_buyuk
    kurbanin_annesi "Oğlumun başına gelenler için çok üzgünüm. O sabah ben mutfaktaydım."
    jump supheliler_sorgulaniyor

label sorgu_kurbanin_babasi:
    scene sorgu_odasi at bg_fullscreen
    show kurbanin_babasi_resim at karakter_buyuk
    kurbanin_babasi "Lukas ile aramızda bazı sorunlar vardı ama onu öldürecek kadar ileri gitmem."
    jump supheliler_sorgulaniyor

return