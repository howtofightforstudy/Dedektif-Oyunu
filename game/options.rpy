## Bu dosya oyununuzu özelleştirmek için değiştirlebilecek ayarları içerir.
##
## İki '#' ile başlayan satırlar yorumdur, öyle kalmalıdırlar. Tek '#' ile
## başlayan satırlar etkin olmayan kodlardır, gerekli olduğunda '#' işareti
## silinerek etkinleştirilebilirler.


## Temeller ####################################################################

## Oyunun insan tarafından okunabilir ismi. Varsayılan pencere başlığını
## ayarlamak için kullanılır, arayüzde ve hata raporlarında görünür.
##
## Stringi çevreleyen _(), stringin çeviriye uygun olduğu anlamına gelir.

define config.name = _("dedektif oyunu")


## Yukarıda yazılan başlığı ana menüde görünüp görünmeyeceğini belirler. Başlığı
## gizlemek için bunu etkinleştirmeyin.

define gui.show_name = True


## Oyunun versiyonu.

define config.version = "1.0"


## Oyunun 'hakkında' ekranına yerleştirilen metin. Metni üçlü-tırnak arasına
## yerleştirin, paragraflar arası boş bir satır bırakın.

define gui.about = _p("""
""")


## Oyunun yayımlanacak derlemenin kısayollarında ve klasörlerinde kullanılacak
## kısa ismi. Bu sadece ASCII karakterleri içermeli; boşluk, iki nokta ya da
## noktalı virgül içermemeli.

define build.name = "dedektifoyunu"


## Sesler ve müzik #############################################################

## Bu üç değişken, diğer şeylerin yanı sıra, hangi mikserlerin varsayılan olarak
## oynatıcıya gösterileceğini kontrol eder. Bunlardan birini False olarak
## ayarlamak ilgili mikseri gizleyecektir.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Kullanıcının ses kanalında bir örnek ses oynatabilmesine izin vermek
## istiyorsanız, aşağıdaki satırı etkinleştirin ve oynatılacak bir örnek ses
## seçin.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Oyuncu ana menüdeyken oynatılacak bir ses dosyasını ayarlamak için aşağıdaki
## satırı etkinleştirin. Bu dosya oyun başladıktan sonra durdurulana ya da başka
## bir dosya oynatılana kadr çalmaya devam edecektir.

# define config.main_menu_music = "main-menu-theme.ogg"


## Geçişler ####################################################################
##
## Bu değişkenler belli olaylardan sonraki geçişleri ayarlamak için kullanılır.
## Her değişken bir geçişe ayarlanmalı, geçiş kullanılmak istenmiyorsa 'Hiçbiri'
## seçilmeli.

## Oyun menüsüne giriş ve menüden çıkış.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Oyun menüleri ekranları arası.

define config.intra_transition = dissolve


## Oyun yüklendikten sonra kullanılan bir geçiş.

define config.after_load_transition = None


## Oyun bittikten sonra ana menüye geçerken kullanılır.

define config.end_game_transition = None


## Oyun başlangı sırasında kullanılan geçiş için bir değişken yok. Onun yerine,
## sahneyi gösterdikten sonra bir 'with' ifadesi kullanın.


## Pencere yönetimi ############################################################
##
## Bu, diyalog ekranının ne zaman gösterildiğini kontrol eder. Eğer "show"
## seçili ise, her zaman gösterilir. Eğer "hide" ise, sadece diyalog olduğu
## zaman gösterilir. Eğer "auto" ise, sahne ifadelerinde pencere gizlenir ve
## diyalog sırasında yeniden gösterilir.
##
## Bu, oyun başladıktan sonra "window show", "window hide", ve "window auto"
## ifadeleriyle değiştirilebilir.

define config.window = "auto"


## Diyalog penceresini gösterip gizlerken kullanılan geçişler

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Tercih varsayılanları #######################################################

## Varsayılan metin hızını kontrol eder. Varsayılan olan 0 sayısı metni anında
## gösterir, eğer başka bir sayı girilirse bu sayı saniye başına yazılan
## karakter hızını belirler.

default preferences.text_cps = 0


## Varsayılan oto-ileri-sarma beklemesi. Uzun sayılar daha uzun beklemeye yol
## açar, 0 ve 30 arası uygundur.

default preferences.afm_time = 15


## Kayıt klasörü ###############################################################
##
## Ren'Py'ın oyun kayıt dosyaları için kullanacağı, platforma özel olan yeri
## knotrol eder. Kayıt dosyaları şuraya yerleştirilecektir:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Bu genelde değiştirilmemelidir, ancak değiştirilecekse mutlaka bir string
## olmalı, bir ifade değil.

define config.save_directory = "dedektifoyunu-1747261818"


## İkon ########################################################################
##
## İşlem çubuğunda ya da kenetlenmiş durumda gösterilecek ikon.

define config.window_icon = "gui/window_icon.png"


## Derleme yapılandırması ######################################################
##
## Bu bölüm Ren'Py'ın projenizi nasıl dağıtım dosyalarına dönüştüreceğini
## kontrol eder.

init python:

    ## Bu fonksiyonlar dosya yolları gerektirir. Dosya yolları büyük-küçük harfe
    ## duyarsızdır ve başında ister / olsun ister olmasın ana klasöre göre
    ## eşleştirilirler. Eğer birden çok eşleşme olursa ilki kullanılır.
    ##
    ## Bir yolda:
    ##
    ## / karakteri klasör ayıracıdır.
    ##
    ## * klasör ayıracı dışında bütün karakterleri eşleştirir.
    ##
    ## ** klasör ayıracı da dahil bütün karakterleri eşleştirir.
    ##
    ## Örneğin, "*.txt" ana klasördeki bütün txt dosyalarını, "game/**.ogg" oyun
    ## klasöründeki ve alt klasörlerdeki bütün ogg'leri,  "**.psd" ise projenin
    ## herhangi bir yerindeki tüm psd dosyalarını eşleştirir.

    ## Dosyaları derlenmiş dağıtımlardan ayırmak için 'Hiçbiri (None)' olarak
    ## sınıflandırın.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Dosyaları arşivlemek için 'arşiv' olarak sınıflandırın.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Doküman yollarıyla eşleşen dosyalar mac uygulaması derlemesinde
    ## kopyalanır, böylece hem uygulamada hem de zip dosyasında görünürler.

    build.documentation('*.html')
    build.documentation('*.txt')


## Uygulama içi satın alımları gerçekleştirmek için bir Google Play lisans
## anahtarı gereklidir. Google Play geliştirici konsolunda, "Para Kazan" > "Para
## Kazanma Kurulumu" > "Lisanslama" altında bulunabilir.

# define build.google_play_key = "..."


## itch.io projesine bağlı, eğik çizgi ile ayrılmış kullanıcı adı ve proje adı.

# define build.itch_project = "renpytom/test-project"
