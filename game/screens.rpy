################################################################################
## Başlatma
################################################################################

init offset = -1


################################################################################
## Stiller
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Oyun içi ekranlar
################################################################################


## Söyleme ekranı ##############################################################
##
## Söyleme ekranı oyuncuya diyalogu göstermek için kullanılır. İki parametre
## alır; kim ve ne. Bunlar sırasıyla konuşan karaktere ve gösterliecek metne
## karşılık gelir. (Eğer isim verilmezse 'kim' parametresi Hiçbiri (None)
## olabilir.)
##
## Ren'Py, bu ekranı gösterilen metni düzenlemek için kullandığından "what"
## id'si ile gösterilebilir bir metin yaratmalıdır. Aynı zamanda gösterilebilir
## yaratmak için "who" ve stil özelliklerini uygulamak için "window" id'lerini
## alabilir.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Bir yan resim varsa, metnin üzerinde göster. Telefon versiyonunda
    ## gösterme - yeterince yer yok.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Karakter nesnesi aracılığıyla isim kutusunun stillendirilmesine izin ver.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Giriş ekranı ################################################################
##
## Bu ekran renpy.input'u göstermek için kullanılır. Komut istemi parametresi
## bir metin komutu aktarmak için kullanılır.
##
## Bu ekran çeşitli giriş parametrelerini kabul etmek için "input" id'si ile bir
## giriş göstermeli.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Seçim ekranı ################################################################
##
## Bu ekran menü ifadesiyle sunulan oyun içi seçimleri göstermek için
## kullanılır. Tek parametre olan maddeler, nesne listeleridir; her birinin
## başlığı ve eylem alanı vardır.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Hızlı Menü ekranı ###########################################################
##
## Hızlı menü, oyun-dışı menülere kolay erişim için oyunda gösterilir.

screen quick_menu():

    ## Bunun diğer ekranlar üzerinde göründüğünden emin olun.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Geri") action Rollback()
            textbutton _("Geçmiş") action ShowMenu('history')
            textbutton _("Atla") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Oto") action Preference("auto-forward", "toggle")
            textbutton _("Kayıt") action ShowMenu('save')
            textbutton _("H.Kayıt") action QuickSave()
            textbutton _("H.Yükle") action QuickLoad()
            textbutton _("Tercih") action ShowMenu('preferences')


## Bu kod, oyuncu kasten arayüzü gizlemediği sürece hızlı menünün oyunda
## gösterildiğinden emin olmak içindir.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Ana Menü ve Oyun Menüsü Ekranları
################################################################################

## Gezinti ekranı ##############################################################
##
## Bu ekran ana menü ve oyun menülerindedir, diğer menülere gezintiyi sağlar
## veya oyunu başlatabilir.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Başla") action Start()

        else:

            textbutton _("Geçmiş") action ShowMenu("history")

            textbutton _("Kayıt") action ShowMenu("save")

        textbutton _("Yükle") action ShowMenu("load")

        textbutton _("Tercihler") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Yeniden Oynatmayı Durdur") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Ana Menü") action MainMenu()

        textbutton _("Hakkında") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Yardım mobil cihazlarla alakalı ya da gerekli değildir.
            textbutton _("Yardım") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Çıkış düğmesi iOS'ta yasaklanmıştır ve Android ve Web'de
            ## gereksizdir.
            textbutton _("Çıkış") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Ana Menü ekranı #############################################################
##
## Ren'Py başlatıldığında ana menüyü göstermek için kullanılır.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Bu diğer herhangi bir menünün aktif olmadığından emin olur.
    tag menu

    add gui.main_menu_background

    ## Bu boş çerçeve ana menüyü karartır.
    frame:
        style "main_menu_frame"

    ## Kullan ifadesi bunun içine başka bir ekranı dahil eder. Ana menünün asıl
    ## içeriği gezinti ekranındadır.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Oyun Menüsü ekranı ##########################################################
##
## Bu, bir oyun menüsünün temel yapısını ortaya koyar. Ekran başlığı ile
## çağrılır; arka planı, başlığı ve gezinmeyi gösterir.
##
## Kaydırma parametresi Hiçbiri (None), "viewport" veya "vpgrid" olabilir. Bu
## ekran, içine yerleştirilen bir veya birden çok alt nesne (children) ile
## kullanılmak içindir.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Gezinti bölmesi için yer ayır.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Dön"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Hakkında ekranı #############################################################
##
## Bu ekran oyun ve Ren'Py ile ilgili telif hakkı ve atıf bilgisi içerir.
##
## Bu ekranla ilgili özel bir şey yoktur. Özelleştirilmiş bir ekran yaratmak
## için örnek olarak kullanılabilir.

screen about():

    tag menu

    ## Bu kullan ifadesi bu ekrana oyun menüsünü dahil eder. Vbox alt nesnesi
    ## (child) daha sonra oyun menüsü ekranındaki gözlemci (viewport) içine
    ## yerleştirilir.
    use game_menu(_("Hakkında"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versiyon [config.version!t]\n")

            ## gui.about genelde options.rpy'de ayarlanır.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t] ile yapılmıştır.")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Yükleme ve Kayıt ekranları ##################################################
##
## Bu ekranlar oyuncunun oyunu kaydetmesi ve yeniden yüklemesi içindir. İkisi
## de neredeyse aynı olduğundan üçüncü bir ekran olan file_slots olarak
## eklenmiştir.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Kayıt"))


screen load():

    tag menu

    use file_slots(_("Yükle"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Sayfa {}"), auto=_("Otomatik kayıtlar"), quick=_("Hızlı kayıtlar"))

    use game_menu(title):

        fixed:

            ## Bu, girişin diğer bütün düğmelerden önce önce giriş olayını
            ## almasını sağlar.
            order_reverse True

            ## Bir düğmeye basılarak düzenlenebilen sayfa adı.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Dosya slotları ızgarası.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("boş slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Diğer sayfalara ulaşmak için düğmeler.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) ifadesi 1'den 9'a kadar sayıları verir.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Yükleme Senkronizasyonu"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Sync'i İndirin"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Tercihler ekranı ############################################################
##
## Tercihler ekranı oyuncunun oyunu kendisine uygun şekilde yapılandırmasını
## sağlar.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Tercihler"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Görüntü")
                        textbutton _("Pencere") action Preference("display", "window")
                        textbutton _("Tam ekran") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Atla")
                    textbutton _("Görülmemiş Metin") action Preference("skip", "toggle")
                    textbutton _("Seçim Sonrası") action Preference("after choices", "toggle")
                    textbutton _("Geçişler") action InvertSelected(Preference("transitions", "toggle"))

                ## "radio_pref" veya "check_pref" türündeki ek vbox'lar,
                ## yaratıcı tarafından belirlenmiş tercihlere burada
                ## eklenebilir.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Metin Hızı")

                    bar value Preference("text speed")

                    label _("Zamanı Oto İleri Sar")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Müzik Düzeyi")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Ses Düzeyi")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Konuşma Düzeyi")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Hepsini Sustur"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Geçmiş ekranı ###############################################################
##
## Bu ekran oyuncuya diyalog geçmişini gösterir. Bu ekranla ilgili özel bir
## şey olmasa da _history_list'te depolanmış diyalog geçmişine erişmesi
## gerekmektedir.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Bu ekranı öngörmekten uzak dur, çünkü çok büyük olabilir.
    predict False

    use game_menu(_("Geçmiş"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Geçmiş yüksekliği (history_height) yok ise her şeyi düzgünce
                ## yerleştirir.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Eğer seçili ise, Karakter'den metin rengini al.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Diyalog geçmişi boş.")


## Geçmiş ekranında ne tür etiketlerin gösterilmesine izin verileceğini
## belirler.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Yardım ekranı ###############################################################
##
## Tuş ve fare girdileriyle ilgili bilgi veren bir ekran. Asıl yardımı
## görüntülemek için diğer ekranları kullanır. (keyboard_help, mouse_help, ve
## gamepad_help)

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Yardım"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Klavye") action SetScreenVariable("device", "keyboard")
                textbutton _("Fare") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Oyun Kumandası") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Girin")
        text _("Diyalogu ilerletir ve arayüzü aktifleştirir.")

    hbox:
        label _("Boşluk")
        text _("Seçim yapmadan diyalogu ilerletir.")

    hbox:
        label _("Ok Tuşları")
        text _("Arayüzde gezinmeyi sağlar.")

    hbox:
        label _("Kaçış")
        text _("Oyun menüsüne erişir.")

    hbox:
        label _("Ctrl")
        text _("Basılı iken diyalogu atlar.")

    hbox:
        label _("Tab")
        text _("Diyalog atlamayı etkinleştirir ya da devre dışı bırakır.")

    hbox:
        label _("Sayfa Yukarı")
        text _("Önceki diyaloga geri sarar.")

    hbox:
        label _("Sayfa Aşağı")
        text _("Daha yeni diyaloga ileri sarar.")

    hbox:
        label "H"
        text _("Kullanıcı arayüzünü gizler.")

    hbox:
        label "S"
        text _("Ekran görüntüsü kaydeder.")

    hbox:
        label "V"
        text _("Yardımcı {a=https://www.renpy.org/l/voicing}kendiliğniden-seslendirme{/a}yi açar veya kapatır.")

    hbox:
        label "Shift+A"
        text _("Erişilebilirlik menüsünü açar.")


screen mouse_help():

    hbox:
        label _("Sol Tıklama")
        text _("Diyalogu ilerletir ve arayüzü aktifleştirir.")

    hbox:
        label _("Orta Tıklama")
        text _("Kullanıcı arayüzünü gizler.")

    hbox:
        label _("Sağ Tıklama")
        text _("Oyun menüsüne erişir.")

    hbox:
        label _("Fare Tekerleği Yukarı")
        text _("Önceki diyaloga geri sarar.")

    hbox:
        label _("Fare Tekerleği Aşağı")
        text _("Daha yeni diyaloga ileri sarar.")


screen gamepad_help():

    hbox:
        label _("Sağ Trigger\nA/Alt Tuş")
        text _("Diyalogu ilerletir ve arayüzü aktifleştirir.")

    hbox:
        label _("Sol Trigger\nSol Omuz")
        text _("Önceki diyaloga geri sarar.")

    hbox:
        label _("Sağ Omuz")
        text _("Daha yeni diyaloga ileri sarar.")

    hbox:
        label _("D-Pad, Çubuklar")
        text _("Arayüzde gezinmeyi sağlar.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Oyun menüsüne erişir.")

    hbox:
        label _("Y/Üst Tuş")
        text _("Kullanıcı arayüzünü gizler.")

    textbutton _("Kalibre Et") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Ek ekranlar
################################################################################


## Doğrulama ekranı ############################################################
##
## Doğrulama ekranı, Ren'Py oyuncuya bir evet-hayır sorusu sorduğunda
## kullanılır.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Bu ekran gösterilirken diğer ekranların girdi almamasını sağla.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Evet") action yes_action
                textbutton _("Hayır") action no_action

    ## Sağ tık ve Escape "no" anlamına gelir.
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Atlama gösterge ekranı ######################################################
##
## Atlama gösterge ekranı, atlama işleminin devam ettiğini gösterir.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Atlama")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Bu transform, okları arka arkaya yakıp söndürmek için kullanılır.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## İçinde SİYAH, SAĞI GÖSTEREN KÜÇÜK ÜÇGEN olan bir font kullanmalıyız.
    font "DejaVuSans.ttf"


## Bildirim ekranı #############################################################
##
## Bildirim ekranı oyuncuya bir mesaj göstermek için kullanılır. (Mesela hızlı
## kayıt yapıldığında veya ekran görüntüsü alındığında.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL ekranı ##################################################################
##
## Bu ekran NVL-modu diyalogları ve menüleri için kullanılır.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Diyalogu vpgrid ya da vbox'ta gösterir.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Verilmişse menüyü görüntüler. config.narrator_menu True olarak
        ## ayarlanırsa menü yanlış görüntülenebilir.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Bu, bir seferde gösterilen NVL-modu girdilerinin maksimum sayısını kontrol
## eder.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Kabarcık ekranı #############################################################
##
## Baloncuk ekranı, konuşma balonları kullanıldığında oyuncuya diyalog
## görüntülemek için kullanılır. Kabarcık ekranı say ekranı ile aynı
## parametreleri alır, "what" id'si ile bir görüntülenebilir oluşturmalıdır ve
## "namebox", "who" ve "window" id'leri ile görüntülenebilir oluşturabilir.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobil Varyasyonlar
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Fare olmayabileceği için, hızlı menüyü dokunması daha kolay olan daha büyük
## ve daha az düğmeli bir versiyonu ile değiştiririz.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Geri") action Rollback()
            textbutton _("Atla") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Oto") action Preference("auto-forward", "toggle")
            textbutton _("Menü") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
