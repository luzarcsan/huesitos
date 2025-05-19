# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Huesitos")
define d = Character("David")
define e = Character("Eugenia")
define m = Character("Michi")

#Color de incendio
image alarma_roja = Solid("#FF000088")

#BAILE MAPACHE
transform saltar_mapache:
    linear 0.2 yoffset -40
    linear 0.2 yoffset 0
    repeat

#Reescalado de imagenes
image bano = im.Scale("bano.png", 1920, 1080)
image michi_interior = im.Scale("michi_interior.png", 1920, 1080)
image michi_durmiendo = im.Scale("MICHI/michi_durmiendo.png", 700, 900)
image michi_bostezando = im.Scale("MICHI/michi_bostezando.png", 1700, 900)
image michi_normal = im.Scale("MICHI/michi_normal.png", 1700, 900)
image casa_michi = im.Scale("casa_michi.png", 1920, 1080)
image exterior = im.Scale("exterior.png", 1920, 1080)
image ventana = im.Scale("ventana.png", 1920, 1080)
image puerta = im.Scale("puerta.png", 1920, 1080)
image salon = im.Scale("salon.png", 1920, 1080)
image cocina = im.Scale("cocina.png", 1920, 1080)

# The game starts here.

label start:
    
    scene salon
    with fade

    # Falta la musica
    # TAMAnO DE DAVID= 0.85
    show david_movil at Transform(zoom=0.85), center

    d "¡Mira, Huesitos! Este meme está siendo un éxito."

    hide david_movil

    show phone

    "Texto en pantalla: 'Cuando ves a tu crush y te da un calambre en la pata.'"

    play sound "ladrido2.mp3" fadein 1.0
    pause(3.0)

    # Ubicación de huesitos: Transform(align=(0.0, -0.5))
    show huesitos_dientes at Transform(align=(0.0, -0.5)) 
    with dissolve

    "Huesitos gruñe, se da media vuelta."

    hide phone
    
    pause(0.5)

    h "(No me gusta lo que estás haciendo...)"
    hide huesitos_dientes

    show david_serio at Transform(zoom=0.85), center
    d "¿A dónde vas?"
    hide david_serio

    # UBICACIÓN CENTRO HUESITOS: Transform(align=(0.5, -0.5))
    show huesitos_dientes at Transform(align=(0.5, -0.5))
    h "(A por la última salchicha. Este es el meme que colmó el plato.)"

label kitchen:

    play music "misionimposible.mp3" fadein 1.0 volume 0.25

    pause(2.5)

    scene cocina
    with fade

    pause(1.5)

    show huesitos_molesto at Transform(align=(0.5, -0.5))
    with dissolve

    pause(1.5)
    "Huesitos mueve una silla con esfuerzo, abre el frigorífico y saca una salchicha envuelta en papel de aluminio."

    "Finalmente, Huesitos la mete en el microondas."
    stop music fadeout 1.0
    play sound "explosion.mp3" volume 2.0
    hide huesitos_molesto
    with dissolve

    pause(5.0)

    play sound "alarma.mp3" volume 0.6
    
    # Alarma roja
    python:
        for i in range(3):
            renpy.show("alarma_roja")
            renpy.pause(0.5)
            renpy.hide("alarma_roja")
            renpy.pause(0.5)

    show alarma_roja
    with dissolve
    pause(0.7)

    show huesitos_sorprendido at Transform(align=(0.0, -0.5))
    with dissolve

    pause(0.5)
    h "(Oh! No!)"

    show david_asustado at Transform(zoom=0.85), right
    with dissolve
    d "¿Qué está pasando aquí? ¡Fuego, fuego!"

    # PRIMERA DECISION
    menu:
        "¿Por dónde escapará Huesitos?"
        "Puerta perruna":
            jump puerta
        "Ventana":
            jump ventana

label puerta:
    scene puerta
    with fade
    pause(1.0)
    "Huesitos corre hacia la puerta y desaparece por un pasadizo secreto."
    jump exterior_michi

label ventana:
    scene ventana
    with fade
    pause(1.0)
    
    "Huesitos salta por la ventana y se encuentra con un mapache marchoso!"
    play music "pedro.mp3" volume 0.6
    show mapache at center, saltar_mapache
    with dissolve

    "*baila*"
    pause(2.5)

    stop music fadeout 1.0
    jump exterior_michi

# Sección de MICHI
label exterior_michi:
    scene exterior
    with fade

    pause (1.0)
    "Huesitos, tras huir de su dueño, se encuentra cerca de la casa de Michi."
    show huesitos_triste at Transform(align=(0.5, -0.5))
    with dissolve
    h "(Voy a ver a mi mejor amigo a ver que me dice.)"

label michi:
    scene casa_michi
    with fade
    
    pause(1.0)

    "Michi se encuentra durmiendo."

    play music "panterarosa.mp3" volume 0.3

    show michi_durmiendo at Transform(align=(0.0, 1.2))
    with dissolve

    show huesitos_habla at Transform(align=(1.0, -0.5))
    with dissolve
    h "(Michi, ¿podemos hablar?)"

    hide michi_durmiendo
    with dissolve
    show michi_bostezando at Transform(align=(-2.2, 1.0))
    with dissolve

    m "(Si es sobre el incendio… ya lo vi en las noticias.)"

    hide huesitos_habla
    show huesitos_sorprendido at Transform(align=(1.0, -0.5))

    h "(¿¡Ya salió en las noticias!?)"

    hide michi_bostezando
    show michi_normal at Transform(align=(-2.2, 1.0))

    m "(Tienes talento para el drama. ¿Qué hiciste ahora?)"

    hide huesitos_sorprendido
    show huesitos_habla at Transform(align=(1.0, -0.5))

    h "(No fue a propósito… Bueno, no del todo. Pero he tenido suficiente.)"

    m "(No me gusta meterme en problemas… Pero si vas a lanzarte a una locura, no voy a dejar que lo hagas solo.)"

    h "(¿Eso es un sí?)"

    m "(Eso es un 'me estás arrastrando a algo que va a terminar mal, pero te conozco y sé que no vas a parar hasta hacerlo.')"

    stop music fadeout 1.0
    pause(1.0)

    m "(Dame cinco minutos. Le tengo que dejar una nota de despedida a doña Eugenia.)"

    hide huesitos_habla
    with dissolve
    "Michi, justo cuando iba a entrar, encuentra un trozo de tarta sobrante que había hecho doña Eugenia con todo su cariño."

    # SEGUNDA DECISION
    menu:
        "¿Catará la tarta?"
        "Anda que no!":
            jump come_tarta
        "Por ahora no.":
            jump no_come_tarta

label come_tarta:
    scene michi_interior
    with fade

    pause(1.0)

    "Michi ha probado un pedazo de tarta y se dirige a dejar la nota."

    play music "mario64.mp3" volume 0.5
    show abuelita_feliz at Transform (zoom=0.85), center
    with dissolve

    e "¡Michi! Te manchaste. Ven a bañarte con el nuevo jabón de sandía que compré ayer."

    hide abuelita_feliz
    with dissolve
    stop music fadeout 3.0

    "Huesitos observabdo la situación, suspira..."
    "Y parte solo hacía la aventura."

label bano:
    scene bano
    with fade
    play music "mario64.mp3" volume 0.5 fadein 1.0

    show michi_normal at Transform(align=(2.2, 1.0))
    with dissolve

    m "(Lo siento Huesitos, juro que iré... Espera...)"
    m "(¿Qué hace una cáscara de plátano ahí?)"

    pause(0.5)

    show abuelita_habla at Transform(align=(0.1, 1.0), zoom=0.85)
    with dissolve

    e "Estate quieto Michi, no te muevas tanto por favor. Voy a probar un nuevo experimentillo."

    scene black
    with fade
    stop music fadeout 2.0
    pause(2.0)

    return

label no_come_tarta:
    scene michi_interior
    with fade

    pause(1.0)

    "Michi deja la nota."

    "Doña Eugenia aparece con una bufanda tejida y les desea suerte."
    play music "mario64.mp3" volume 0.5
    show abuelita_habla at Transform (zoom=0.85), center
    with dissolve

    e "Ánimo Michi, no te preocupes por mí. Solo cuida de Huesitos."

    hide abuelita_habla
    with dissolve

    "Huesitos y Michi se alejan juntos hacia el horizonte."
    with dissolve

    stop music fadeout 2.0
    scene black
    with fade
    pause(2.0)

    return