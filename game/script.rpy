# Oyundaki karakterleri tanimla. Renk argumani karakterin
# isminin rengini belirler.
define e = Character("Eileen")
define hizmetci = Character("hizmetçi", color="#00ff00")
image ev = "images/ev.jpg"
image hizmetci = "images/karakterler/hizmetci.png"
define hizmetci = Character("Hizmetçi", color="#c8ffc8")
define dedektif = Character("Dedektif", color="#c8c8ff")
image dedektif = "images/karakterler/erkek_dedektif.png"
transform karakter_buyuk:
    zoom 1.5 # Oranı ihtiyacına göre artırabilirsin 
    anchor (0.5, 1.0)
    xalign 0.5
    yalign 0.65
transform karakter_buyuk_sag:
    zoom 1.5
    anchor (0.5, 1.0)
    xalign 0.8   # Sağda hizalama
    yalign 0.65

transform karakter_buyuk_sol:
    zoom 1.5
    anchor (0.5, 1.0)
    xalign 0.2   # Solda hizalama
    yalign 0.65

image hizmetci = Image("images/karakterler/hizmetci.png")

transform bg_fullscreen:
    zoom 2.0
   
    
# Oyun burada baslar.

label start:
    scene ev at bg_fullscreen
    play music "audio/op.mp3" volume 0.5

    "Yıl 1922. Sisli bir sabahın serinliğinde, Steiner malikanesinin gri taş duvarları yankı dolu bir çığlıkla sarsıldı."

    "Zengin ve küstah genç adam Lukas Steiner, odasında cansız halde bulundu. Parmaklarının ucunda bir kahve fincanı, göğsünde ise soğuk bir bıçağın izini taşıyan derin bir yara..."

    "Steiner, kadınlara karşı küçümseyici tavırlarıyla tanınır; ardında incinmiş kalpler, bastırılmış öfkeler ve sessizce yutulmuş nefretler bırakırdı."

    "O sabah, kahve fincanındaki parmak izleri ve tek bir yudum dahi alınmamış kahve, olayın yalnızca başlangıcıydı."

    "Hizmetçi gözaltına alındı. Fakat o evde herkesin bir bahanesi, herkesin karanlıkta kalan bir yüzü vardı."
    "Zira bazı sırlar, kahveden bile daha acıydı."
    show hizmetci at karakter_buyuk_sol 
    with dissolve

    hizmetci "Ben kimseye zara vermedim efendim. 
    Sadece işimi yaptım. Kahve hazırladım, odasını temizledim ve kapıyı kapattım. Yemin ederim ben yapmadım!"
    show dedektif at karakter_buyuk_sag with moveinright
    dedektif "Gerçekler her ne ise eninde sonunda ortaya çıkacaktır."
    hide hizmetci with dissolve

    show dedektif at karakter_buyuk with moveinright
    dedektif "Bu cinayet sıradan bir cinayet değil!"



    # Bir arkaplan goster. Varsayilan olarak bir yer tutucu kullanilir, ancak siz
    # resimler klasorune bir dosya ekleyerek (bg room.png ya da bg room.jpg adinda)
    # eklediginiz resmi gosterebilirsiniz.

    return
