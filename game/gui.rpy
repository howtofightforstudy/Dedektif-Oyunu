################################################################################
## Başlatma
################################################################################

## Başlatma uzaklık ifadesi bu dosyadaki başlatma ifadelerinin başka bir
## dosyadaki başlatma ifadelerinden önce çalışmasını sağlar.
init offset = -2

## gui.init çağrısı duyarlı varsayılan stilleri sıfırlar, oyunun en ve boyunu
## ayarlar.
init python:
    gui.init(1920, 1080)

## Ekranlarda veya dönüşümlerde geçersiz veya kararsız özellikler için
## kontrolleri etkinleştirin
define config.check_conflicting_properties = True


################################################################################
## GUI Yapılandırma Değişkenleri
################################################################################


## Renkler #####################################################################
##
## Arayüzdeki metin renkleri

## Arayüzde başlık ve vurgulu metinlerde kullanılan bir renk
define gui.accent_color = '#99ccff'

## Bir metin düğmesi seçili ya da fare üstünde değilken kullanılan renk.
define gui.idle_color = '#888888'

## Küçük renk, aynı etkiyi yaratmak için daha parlak/koyu olması gereken küçük
## metin için kullanılır.
define gui.idle_small_color = '#aaaaaa'

## Üstüne fare imleci tutulan düğme ve çubuklar için kullanılan renk.
define gui.hover_color = '#c1e0ff'

## Odaklanmamış ancak seçilmiş bir metin düğmesi için kullanılan renk. Bir buton
## ancak ekranda ise ya da tercih değeri ise seçilir.
define gui.selected_color = '#ffffff'

## Seçilemeyen bir metin düğmesinde kullanılan renk.
define gui.insensitive_color = '#8888887f'

## Çubukların dolmamış parçaları için kullanılan renk. Direkt olarak
## kullanılmazlar, ancak resimleri yeniden yaratırken kullanılırlar.
define gui.muted_color = '#3d5166'
define gui.hover_muted_color = '#5b7a99'

## Diyalog ve menü seçimleri için kullanılan renkler.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fontlar ve Font Boyutları ###################################################

## Oyun-içi metin için kullanılan font.
define gui.text_font = "DejaVuSans.ttf"

## Karakter adları için kullanılan font.
define gui.name_text_font = "DejaVuSans.ttf"

## Oyun-dışı metin için kullanılan font.
define gui.interface_text_font = "DejaVuSans.ttf"

## Normal diyalog metni için kullanılan boyut.
define gui.text_size = 33

## Karakter adı boyutu.
define gui.name_text_size = 45

## Oyun arayüzü için kullanılan metin boyutu.
define gui.interface_text_size = 33

## Oyun arayüzünde kullanılan başlık boyutu.
define gui.label_text_size = 36

## Bildirim ekranındaki metin boyutu.
define gui.notify_text_size = 24

## Oyun başlığı boyutu.
define gui.title_text_size = 75


## Ana ve Oyun Menüleri ########################################################

## Ana menü ve oyun menüsü için kullanılan resimler.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diyalog #####################################################################
##
## Bu değişkenler diyaloğun ekranda satır satır nasıl görüneceğini belirler.

## Diyalog metni kutusunun boyu.
define gui.textbox_height = 278

## Metin kutusunun dikey olarak ekrandaki yeri. 0.0 en üst, 0.5 merkez, 1.0 ise
## en alt.
define gui.textbox_yalign = 1.0


## Konuşan karakterin adının metin kutusuna göre yerleştirilmesi. Soldan ya da
## üstten herhangi sayıda piksel olabilir, ya da 0.5 ile ortalanabilir.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Karakter adının yatay hizalanması. 0.0 ile sola yapıştırılabilir, 0.5 ile
## ortalanabilir ve 1.0 ile sağa yapıştırılabilir.
define gui.name_xalign = 0.0

## Karakter adını taşıyan kutunun eni, boyu ve sınırları. Otomatik boyutlandırma
## için seçim yapmayın.
define gui.namebox_width = None
define gui.namebox_height = None

## Karakter adını taşıyan kutunun sınırları, sırasıyla sol, üst, sağ ve alt.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Etkin ise isim kutusunun arkaplanı eğilecek, etkin değil ise arkaplan
## boyutlandırılacak.
define gui.namebox_tile = False


## Metin kutusuna göre diyaloğun yerleştirilmesi. Soldan ya da üstten herhangi
## sayıda piksel olabilir, ya da 0.5 ile ortalanabilir.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Diyalog metninin piksel olarak maksimum genişliği.
define gui.dialogue_width = 1116

## Diyalog metninin yatay hizalandırılması. 0.0 ile sola yapıştırılabilir, 0.5
## ile ortalanabilir ve 1.0 ile sağa yapıştırılabilir.
define gui.dialogue_text_xalign = 0.0


## Düğmeler ####################################################################
##
## Bu değişkenler, gui/button'daki resim dosyaları ile birlikte hangi düğmelerin
## gösterileceğini kontrol eder.

## Bir düğmenin piksel olarak eni ve boyu. Eğer seçilmezse, Ren'Py bir boyut
## hesaplar.
define gui.button_width = None
define gui.button_height = None

## Bir düğmenin sınırları, sırasıyla sol, üst, sağ ve alt.
define gui.button_borders = Borders(6, 6, 6, 6)

## Etkin ise arkaplan resmi eğilecek. Etkin değil ise arkaplan resmi doğrusal
## boyutlandırılacak.
define gui.button_tile = False

## Düğme tarafından kullanılan font.
define gui.button_text_font = gui.interface_text_font

## Düğme tarafından kullanılan metin boyutu.
define gui.button_text_size = gui.interface_text_size

## Düğme metninin değişik durumlardaki rengi.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Düğme metninin yatay hizalandırılması. (0.0 sol, 0.5 merkez, 1.0 sağ).
define gui.button_text_xalign = 0.0


## Bu değişkenler değişik butonlarda kullanılan ayarların üstüne yazılır. Lütfen
## hangi düğmelerin mevcut olduğu ve ne için kullanıldıklarını öğrenmek için gui
## blgelerine bakınız.
##
## Bu yapılandırmalar varsayılan arayüz tarafından kullanılır:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Düzgün isimlendirilmiş değişkenler ekleyerek kendi düzenlemelerinizi de
## yapabilirsiniz. Örneğin bir sonraki yorum satırını aktifleştirerek bit
## navigasyon düğmesinin genişliğini ayarlayabilirsiniz.

# define gui.navigation_button_width = 250


## Seçim Düğmeleri #############################################################
##
## Seçim düğmeleri oyun içi menülerde kullanılır.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Dosya Solut Düğmeleri #######################################################
##
## Bir dosya slotu düğmesi özel bir tür düğmedir. Bir önizleme resmi ve kayıdın
## içeriğine dair bir metin içerir. Diğer düğmeler gibi bir kayıt slotu düğmesi
## de gui/button'daki resimleri kullanır.

## Kayıt slotu düğmesi.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Kayıt slotlarında kullanılan önizleme resminin boy ve eni.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Kayıt slotlarının gösterildiği satır ve sütun sayısı.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Konumlandırma ve Boşluklar ##################################################
##
## Bu değişkenler değişik kullanıcı arayüzü elemanlarının yerlerini ve
## aralarındaki boşlukları kontrol eder.

## Navigasyon düğmelerinin sol taraflarının ekranın soluna göre konumları.
define gui.navigation_xpos = 60

## Atlama göstergesinin dikey konumu.
define gui.skip_ypos = 15

## Bildirim ekranının dikey konumu.
define gui.notify_ypos = 68

## Menü seçimleri arası boşluk.
define gui.choice_spacing = 33

## Ana menü ve oyun menülerindeki navigasyon bölümündeki düğmeler.
define gui.navigation_spacing = 6

## Tercihler arası boşluk miktarını kontrol eder.
define gui.pref_spacing = 15

## Terchi düğmeleri arası boşluk miktarını kontrol eder.
define gui.pref_button_spacing = 0

## Dosya sayfası düğmeleri arası boşluk.
define gui.page_spacing = 0

## Dosya slotları arası boşluk.
define gui.slot_spacing = 15

## Ana menü metni konumu.
define gui.main_menu_text_xalign = 1.0


## Çerçeveler ##################################################################
##
## Bu değişkenler bir pencere veya üst sayfa olmadığı zaman kullanıcı arayüzü
## elemanlarının görünümünü kontrol eder.

## Genel çerçeveler.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Onay ekranının bir parçası olarak kullanılan çerçeve.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Atlama ekranının bir parçası olarak kullanılan çerçeve.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Bildirim ekranının bir parçası olarak kullanılan çerçeve.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Çerçeve arkaplanları eğimli olmalı mı ?
define gui.frame_tile = False


## Çubuklar, Kaydırma Çububkları ve Kaydırıcılar ###############################
##
## Bunlar çubuklar, kaydırma çububkları ve kaydırıcıların boyutunu kontrol eder.
##
## Varsayılan GUI yalnızca kaydırıcıları ve dikey kaydırma çubuklarını kullanır.
## Diğer bütün çubuklar sadece yaratıcı tarafından yazılmış ekranlarda
## kullanılır.

## Yatay çubuklar, kaydırma çububkları ve kaydırıcıların boyu. Dikey çubuklar,
## kaydırma çububkları ve kaydırıcıların eni.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## Eğer çubuk resimleri eğilmeliyse etkin. Eğer doğrusal boyutlandırılmalılar
## ise etkin değil.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Yatay sınırlar.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Dikey sınırlar.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## Geçmiş ######################################################################
##
## Geçmiş ekranı oyuncunun halihazırda gördüğü diyaloğu gösterir.

## Ren'Py tarafından tutulacak diyalog bloklarının sayısı.
define config.history_length = 250

## Geçmiş ekranı girişinin boyu. Performans bedeliyle boyu değişken yapmak için
## seçim yapmayın.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## Konuşan karakterin isminin konumu, genişliği ve hizalanması.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Diyalog metninin konumu, genişliği ve hizalanması.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Modu ####################################################################
##
## NVL-mod ekran, NVL-mod karakterler tarafından konuşulan diyalogu gösterir.

## NVL-mod arkaplan penceresinin sınırları.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Ren'Py tarafındad gösterilecek maksimum NVL-modu girişi sayısı. Bundan daha
## çok giriş gösterilmesi gerektiğinde, en eski giriş kaldırılacak.
define gui.nvl_list_length = 6

## NVL-modu girişinin boyu. Boyun dinamik olarak değiştirilmesi için seçim
## yapmayın.
define gui.nvl_height = 173

## gui.nvl_height seçili değilken NVL-modu girişleri arası, aynı zamanda NVL-
## modu menüsü ve NVL-modu girişleri arası boşluk.
define gui.nvl_spacing = 15

## Konuşan karakterin isminin konumu, genişliği ve hizalanması.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Diyalog metninin konumu, genişliği ve hizalanması.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## nvl_thought metninin konumu, genişliği ve hizalanması (nvl_narrator karakteri
## tarafından konuşulan metin.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## nvl menu_button'ları konumu.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Yerelleştirme ###############################################################

## Satırları kırma iznini kontrol eder. Varsayılan ayar pek çok dile
## uygundur. Mevctu bütün değerler https://www.renpy.org/doc/html/
## style_properties.html#style-property-language adresinde bulunabilir.

define gui.language = "unicode"


################################################################################
## Mobil cihazlar
################################################################################

init python:

    ## Hızlı düğmelerin boyutlarını değiştirerek tablet ve telefonlarda
    ## dokunmayı kolaylaştırır.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Telefonlarda kolayca görünebildiklerinden emin olmak için çeşitli GUI
    ## elemanlarının boy ve aralığını değiştirir.
    @gui.variant
    def small():

        ## Font boyutları.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Metin kutusunun konumunu ayarla.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Çeiştli şeylerin boy ve aralığını ayarla.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Dosya düğmesi düzeni.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-modu.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
