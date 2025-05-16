

# Karakter tanımlamaları
define dedektif_e = Character("Dedektif", color="#c8c8ff")
define dedektif_k = Character("Dedektif", color="#c8c8ff")
define hizmetci = Character("Hizmetçi", color="#c8ffc8")

# Resim tanımlamaları
image ev = "images/ev.jpg"
image sorgu_odasi = "images/sorgu_odasi.png"
image dedektif_e_resim = "images/karakterler/erkek_dedektif.png"
image dedektif_k_resim = "images/karakterler/kadin_dedektif.png"
image hizmetci_resim = "images/karakterler/hizmetci.png"

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
    show hizmetci_resim at karakter_buyuk_sol with dissolve

    hizmetci "Ben kimseye zara vermedim efendim. Sadece işimi yaptım. Kahve hazırladım, odasını temizledim ve kapıyı kapattım. Yemin ederim ben yapmadım!"
    show dedektif_e_resim at karakter_buyuk_sag with moveinright
    dedektif_e "Gerçekler her ne ise eninde sonunda ortaya çıkacaktır."
    hide hizmetci_resim with dissolve

    show dedektif_e_resim at karakter_buyuk with moveinright
    dedektif_e "Bu cinayet sıradan bir cinayet değil!"
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
            $ dedektif_isim = "Erkek Dedektif" # Varsayılan isim
        $ secilen_dedektif_karakteri = Character(dedektif_isim, color="#c8c8ff")
        show dedektif_e_resim at karakter_buyuk
        secilen_dedektif_karakteri "Merhaba, ben [dedektif_isim]."
    elif secilen_dedektif_tipi == "kadin":
        show dedektif_k_resim at karakter_buyuk
        $ dedektif_isim = renpy.input("Lütfen kadın dedektifin ismini girin:")
        if dedektif_isim == "":
            $ dedektif_isim = "Kadın Dedektif" # Varsayılan isim
        $ secilen_dedektif_karakteri = Character(dedektif_isim, color="#c8c8ff")
        show dedektif_k_resim at karakter_buyuk
        secilen_dedektif_karakteri "Merhaba, ben [dedektif_isim]."

    jump olaylar_baslangici

label olaylar_baslangici:
    scene sorgu_odasi at bg_fullscreen

    show hizmetci_resim at karakter_buyuk_sol with dissolve
    hizmetci "Neden beni buraya getirdiniz? Ne istiyorsunuz benden?"

    if secilen_dedektif_tipi == "erkek":
        show dedektif_e_resim at karakter_buyuk_sag with moveinright
        secilen_dedektif_karakteri "Sakin olun, neler olduğunu anlatın."
    elif secilen_dedektif_tipi == "kadin":
        show dedektif_k_resim at karakter_buyuk_sag with moveinright
        secilen_dedektif_karakteri "Sakin olun, neler olduğunu anlatın."

    # Oyunun geri kalan olay örgüsü burada devam edecek...
    return
