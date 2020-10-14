# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.a

define pl = Character("Player", color="#c8c8ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return


# Construction Pieces:

label start:


    $ Init()

    $ show_buttons = 0
    $ center_choices = True

    centered "Please select if you would like to add any content packs."

    menu:
        "1.4 Content Pack - Adds 1.4 Update Content":
            $ contentpacks.append("1.4")
        "Base Game - No Changes":
            pass

    centered "Please select a difficulty. This can be changed anytime in game on the player menu."

    menu:
        "{color=#33FF6E}Story Only{/color} - Skip All Battles":
            $ difficulty = -1
        "{color=#ECFF33}Easy{/color} - Enemy health & damage are reduced":
            $ difficulty = 0
        "{color=#33FFFC}Normal{/color} - No differences to Gameplay":
            $ difficulty = 1
        "{color=#FF3333}Hardcore{/color} - Enemies will not despawn after combat":
            $ difficulty = 2

    $ center_choices = False
    $ show_buttons = 1


#label splash screen
label splashscreen:

    scene black
    with Pause(0.3)
    scene splashscreen_bg
    with Dissolve(0.7)

    show logo_splash #at splash_logo_notext

    pause 2.0

    show logo_splash step_2
    with Dissolve(0.8)

    pause 0.7

    hide logo_splash
    with Dissolve(0.7)
    scene black
    with Dissolve(0.7)

    pause 1.0

    $ renpy.movie_cutscene("superhippo.ogv")

    pause 1.0


    return

    play music "bgm/Abstract.ogg" fadein 0.8
    "My body aches with a pain strangely foreign to my flesh, yet all too familiar to my mind. A light feeling of euphoria rushes over me as I stare further into the void that lies before by my closed eyes."
    "I feel myself jolt a bit at first, but I find myself still unable to restore my vision; this blanket of darkness before me seems to extend into the distant horizon, reflecting a faint presence in my midst."
    #<foliage sounds>
    play sound "sfx/leavesrustle.ogg"
    "My sudden bodily spasms come to a halt as I hear the sound of foliage lightly crackling in front of me."
    stop music fadeout 1.0
    "Before my mind has time to react to the imminent aura that stands before me, a soft voice breaks the ambient silence."
    unk "Hmm? Now now, what could this be?"


    "As her body presses heavily against my own, I in turn feel what I can only assume to be her breasts pressured up against my chest."
    #<Sound of physical contact - slap/punch?>
    play sound "sfx/battle/swing.ogg"
    scene white
    with Dissolve(0.2)
    scene black
    with Dissolve(0.1)
    scene white
    with Dissolve(0.2)
    "I feel my entire body spasm after a modest slap, and then feel the blood returning to all my limbs, a sense of urgency replacing the former numbness."
    "My eyes suddenly thrust open as well, the sharp contrast from the absolute darkness prior to the light shining down from the thick canopy above momentarily blinding me."
    #<Darkness fades out into Hidden Grove Background; Kamala centered in middle>
    scene Vatika
    with fade
    show Kamala Clothed Neutral at sp1_1
    with charFadeInOut
    play music "bgm/Romance.ogg" fadein 0.8
    "When I finally come to my senses, I am greeted by the sight of a thickly built woman with tan skin and eyes that glistened hazy green."
        hide Kamala
    with charFadeInOut
    scene black
    with dissolve
    $ show_buttons = 0
    centered "You are about to enter the map view."
    centered "Click adjacent tiles to move. These are denoted by slow blinking."
    centered "Use the top left menu to access the player menu, skip a turn, or re-explore a tile. The player menu can also be accessed with a right click."
    centered "Some tiles will autotrigger events upon landing on them, and others will require clicking the Explore button."
    centered "Not all areas will show all icons upon arriving - some will only show tiles you've already landed on."
    $ show_buttons = 1
    $ mapShow(mpVatika_intro)


        show Kamala Clothed Neutral at sp1_1
    unk "Now now, I am sure there is much for you to ask, but first use your newfound words to tell me your name."
    hide Kamala
    with charFadeInOut

    scene black
    with fade

    $ playername = renpy.input("My name is _____________________.", default="Siddhartha",length=15)

    if not playername:
        $ playername = "Siddhartha"
    else:
        $ playername = playername.strip()

    scene Vatika
    with fade
    show Kamala Clothed Happy at sp1_1
    with charFadeInOut

    unk "Such a lovely name for a wanderer, is it not?"
    unk "Ah ah, and yet how could I possibly omit such an important facet? You may call me Kamala."
    show Kamala Clothed Neutral at jumpEffect
    play music "bgm/Neutral.ogg" fadein 0.8
    "Kamala retracts her hand from my shoulder as we both rise in unison."
    show Kamala Clothed Happy
    with charDissolve
    ka "Now my dear [playername], I am sure you have many questions to ask of me. I will do only my finest to assure your complacency."


#money stuff
label moneystuff:
    nvl clear
    " You open the drawer of the bedside cabinet that you have designated as your piggy bank. \n \n Currently you have £[cash] on you, and £[cashstash] in the drawer. {nw}"
    menu:
        "Stick £100 in the drawer" if cash >99:
            $cash = cash - 100
            $cashstash = cashstash + 100
            jump moneystuff
        "Stick £250 in the drawer" if cash >249:
            $cash = cash - 250
            $cashstash = cashstash + 250
            jump moneystuff
        "Stick £500 in the drawer" if cash >499:
            $cash = cash - 500
            $cashstash = cashstash + 500
            jump moneystuff
        "Stick £1000 in the drawer" if cash >999:
            $cash = cash - 1000
            $cashstash = cashstash + 1000
            jump moneystuff
        "Stick everything in the drawer" if cash > 0:
            $cashstash = cashstash + cash
            $cash = 0
            jump moneystuff
        "Take £100 from the drawer" if cashstash >99:
            $cash = cash + 100
            $cashstash = cashstash - 100
            jump moneystuff
        "Take £250 from the drawer" if cashstash >249:
            $cash = cash + 250
            $cashstash = cashstash - 250
            jump moneystuff
        "Take £500 from the drawer" if cashstash >499:
            $cash = cash + 500
            $cashstash = cashstash - 500
            jump moneystuff
        "Take £1000 from the drawer" if cashstash >999:
            $cash = cash + 1000
            $cashstash = cashstash - 1000
            jump moneystuff
        "Take everything in the drawer" if cashstash > 0:
            $cash = cash + cashstash
            $cashstash = 0
            jump moneystuff
        "Okay, done with this":
            if moneydropoff == True:
                $moneydropoff = False
                jump backhometwo
            else:
                jump statschecked

# Declare characters used by this game.
#characters
define narrator = Character(None, color="#CDA559", size=48, italic=True)
define pa = Character('[playername]', color="#CDA559", size=48)
define th = Character('Thief', color="#CDA559", size=48)
define da  = Character('Dancer', color="#CDA559", size=48)
define dm = Character("Kara'mate Mage", color="#CDA559", size=48)
define be = Character('Berserker', color="#CDA559", size=48)
define sh = Character('Shadow', color="#CDA559", size=48)
define ge = Character('Gel', color="#CDA559", size=48)
define su = Character('Succubus', color="#CDA559", size=48)
define asu = Character('Asuri', color="#CDA559", size=48)
define de = Character('Devil', color="#CDA559", size=48)
define fo = Character('Fox', color="#CDA559", size=48)
define ph = Character('Phantom', color="#CDA559", size=48)
define ma = Character('Mayuri', color="#CDA559", size=48)
define dr = Character('Dragon', color="#CDA559", size=48)
define og = Character('Ogre', color="#CDA559", size=48)
define ne = Character('Necromancer', color="#CDA559", size=48)
define un = Character('Rotting Lost One', color="#CDA559", size=48)
define gh = Character('Ghost', color="#CDA559", size=48)
define ca = Character('Cat', color="#CDA559", size=48)
define ja = Character('Jarita', color="#CDA559", size=48)
define me = Character('Mermaid', color="#CDA559", size=48)
define unk = Character('???', color="#CDA559", size=48)


init -6 python:
    import math

    #achievements

    achievement.register("KS_ADITI_GOOD")
    achievement.register("KS_ADITI_BAD")
    achievement.register("KS_ANNAVERE_GOOD")
    achievement.register("KS_ANNAVERE_BAD")
    achievement.register("KS_HANSA_GOOD")
    achievement.register("KS_HANSA_BAD")
    achievement.register("KS_KAMALA_GOOD")
    achievement.register("KS_KAMALA_BAD")
    achievement.register("KS_LYDRIA_GOOD")
    achievement.register("KS_LYDRIA_BAD")
    achievement.register("KS_MYSA_END")
    achievement.register("KS_NIIJA_END")
    achievement.register("KS_NISHA_END")
    achievement.register("KS_PRISHA_END")
    achievement.register("KS_SAANVI_GOOD")
    achievement.register("KS_SAANVI_BAD")
    achievement.register("KS_SYLL_GOOD")
    achievement.register("KS_SYLL_BAD")
    achievement.register("KS_TAKAL_END")
    achievement.register("KS_END_BAD")
    achievement.register("KS_END_GOOD")
    achievement.register("KS_EINYA_SECRET")
    achievement.register("KS_KAMALA_SECRET")
    achievement.register("KS_PILLAR_ONE")
    achievement.register("KS_PILLAR_TWO")
    achievement.register("KS_PILLAR_THREE")
    achievement.register("KS_PILLAR_FOURTH")
    achievement.register("KS_PILLAR_FIVE")
    achievement.register("KS_PILLAR_SIX")
    achievement.register("KS_PILLAR_SEVEN")
    achievement.Sync()

init python:

    global itemIncense

    itemIncense = incense()


    from time import sleep

    _game_menu_screen = "playerMenu"

    def genText(price):
        return "Destroy this item and recieve " + str(price) + " jivas?"

    #initialize all important variables for the game
    def Init():

        #items
        global rawMeat, annaverebag,clothDress ,itemTorch,AuxTome,ZodiacTome,obsidianDagger ,kamalaDesire ,kamalaHope ,annanvereAmbitionMerit ,annanvereAmbitionSin ,einyaAmbitionMerit ,einyaAmbitionSin ,einyaReflection ,aditiReflection ,hansaWeapons ,hansaWeakness ,hansaAmbition,mysaDesire ,syllNecklace,roseGoldCrown ,annavereCrown ,asuraChain,brownRibbon ,ironClamp,songbirdCage ,engraveAmulet ,leatherJournal ,grayLocket ,devilShackle ,shadeHeart ,coralWard,vritraWill ,mysaScroll1 ,mysaScroll2,mysaScroll3,mysaScroll4,mysaScroll5,saanviAmbition,lotusBloom,pondwaterFruit,jaritaPlume,devilLuster,phantomMemory,voiceOfGods,voidCall,voidFire,shadowHeart,mermaidSong,callofSea,riteDead, saanviRibbon, itemIncense

        saanviRibbon = saanviRibbon_()
        itemIncense = incense()
        rawMeat = rawMeat_()
        annaverebag = annaverebag_()
        clothDress = clothDress_()
        itemTorch = itemTorch_()
        AuxTome = AuxTome_()
        ZodiacTome = ZodiacTome_()
        obsidianDagger = obsidianDagger_()
        kamalaDesire = kamalaDesire_()
        kamalaHope = kamalaHope_()
        annanvereAmbitionMerit = annanvereAmbitionMerit_()
        annanvereAmbitionSin = annanvereAmbitionSin_()
        einyaAmbitionMerit = einyaAmbitionMerit_()
        einyaAmbitionSin = einyaAmbitionSin_()
        einyaReflection = einyaReflection_()
        aditiReflection = aditiReflection_()
        hansaWeapons = hansaWeapons_()
        hansaWeakness = hansaWeakness_()
        hansaAmbition = hansaAmbition_()
        mysaDesire = mysaDesire_()
        syllNecklace = syllNecklace_()
        roseGoldCrown = prishaCrown_()
        annavereCrown = annavereCrown_()
        asuraChain = asuraChain_()
        brownRibbon = brownRibbon_()
        ironClamp = ironClap_()
        songbirdCage = songbirdCage_()
        engraveAmulet = engraveAmulet_()
        leatherJournal = leatherJournal_()
        grayLocket = grayLocket_()
        devilShackle = devilShackle_()
        shadeHeart = shadeHeart_()
        coralWard = coralWard_()
        vritraWill = vritraWill_()
        mysaScroll1 = mysaScroll1_()
        mysaScroll2 = mysaScroll2_()
        mysaScroll3 = mysaScroll3_()
        mysaScroll4 = mysaScroll4_()
        mysaScroll5 = mysaScroll5_()
        saanviAmbition = saanviAmbition_()
        lotusBloom = lotusBloom_()
        pondwaterFruit = pondwaterFruit_()
        jaritaPlume = jaritaPlume_()
        devilLuster = devilLuster_()
        phantomMemory = phantomMemory_()
        voiceOfGods = voiceOfGods_()
        voidCall = voidCall_()
        voidFire = voidFire_()
        shadowHeart = shadowHeart_()
        mermaidSong = mermaidSong_()
        callofSea = callofSea_()
        riteDead = riteDead_()

        global eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12,eq13, eq14,eq15, eq16, eq17,eq18,eq19,eq20,eq21,eq22,eq23,eq24,eq25
        eq1 = eq_1()
        eq2 = eq_2()
        eq3 = eq_3()
        eq4 = eq_4()
        eq5 = eq_5()
        eq6 = eq_6()
        eq7 = eq_7()
        eq8 = eq_8()
        eq9 = eq_9()
        eq10 = eq_10()
        eq11 = eq_11()
        eq12 = eq_12()
        eq13 = eq_13()
        eq14 = eq_14()
        eq15 = eq_15()
        eq16 = eq_16()
        eq17 = eq_17()
        eq18 = eq_18()
        eq19 = eq_19()
        eq20 = eq_20()
        eq21 = eq_21()
        eq22 = eq_22()
        eq23 = eq_23()
        eq24 = eq_24()
        eq25 = eq_25()


        global can_save
        global karma, sin, merit
        global scale_level
        global show_buttons
        global has_right
        global shop
        shop = 0
        show_buttons = 1
        can_save = 0
        karma = 0
        sin = 0
        merit = 0

        global show_box
        show_box = 1

        isnewgame = 0
        global samaPareScale1
        global samaPareScale2
        samaPareScale = 7
        samaPareScale = 3
        #this is the scale_level
        scale_level = 1
        has_right = False

        global o_At5,o_At8,o_At20,o_Acr5,o_Acr28,o_Acr11,o_Acr20,o_Acr32,o_Ad7,o_Ad13,o_As25,o_As3,o_As11 ,o_As15,o_As19 ,o_Ca1,o_Ca10,o_Ca18,o_Ca28,o_Ca23,o_Ca36,o_Ci1,o_Ci6,o_Ci21 ,o_Ci20,o_Ci14,o_Cit7,o_Cit22,o_Cit26,o_Cit17,o_Cit29,o_Cro2,o_Cro26,o_Cro8,o_Cro41,o_Cro22,o_Cro36,o_Cro49,o_Fa4,o_Fa10,o_Fa14,o_Fa24,o_Fo3,o_Fo10,o_Fo16,o_Fo21,o_Fo36,o_Isl6,o_Isl12,o_Isl16,o_Jad3,o_Jad7,o_Jad15,o_Jad10,o_Jy4,o_Jy7,o_Jy14,o_Jy17,o_Jy26,o_Jy37,o_Ma4,o_Ma10,o_Ma16,o_Ma33,o_Ma18,o_No2,o_No24,o_No37,o_No15 ,o_No10,o_Oh3,o_Oh27,o_Oh31,o_Ov4,o_Ov54,o_Ov39,o_Ov45,o_Ov30,o_Ri3,o_Ri27,o_Ri20,o_SP2,o_SP8,o_SP22,o_SP28,o_Sa4,o_Sa8,o_Sa9,o_Sa27,o_Sa12,o_Sv1,o_Sv6,o_Sv23,o_Sv12,o_Tr1,o_Tr21,o_Tr5,o_Tr10,o_Uf3,o_Uf5,o_Uf15,o_Uf24,o_Vr3,o_Vr8,o_Vr14,o_Vr17,o_Vr32,o_Wr7,o_Wr13,o_Wr24

        o_At5 = At5()
        o_At8 = At8()
        o_At20 = At20()
        o_Acr5 = Acr5()
        o_Acr28 = Acr28()
        o_Acr11 = Acr11()
        o_Acr20 = Acr20()
        o_Acr32 = Acr32()
        o_Ad7 = Ad7()
        o_Ad13 = Ad13()
        o_As25 = As25()
        o_As3 = As3()
        o_As11 = As11()
        o_As15 = As15()
        o_As19 = As19()
        o_Ca1 = Ca1()
        o_Ca10 = Ca10()
        o_Ca18 = Ca18()
        o_Ca28 = Ca28()
        o_Ca23 = Ca23()
        o_Ca36 = Ca36()
        o_Ci1 = Ci1()
        o_Ci6 = Ci6()
        o_Ci21 = Ci21()
        o_Ci20 = Ci20()
        o_Ci14 = Ci14()
        o_Cit7 = Cit7()
        o_Cit22 = Cit22()
        o_Cit26 = Cit26()
        o_Cit17 = Cit17()
        o_Cit29 = Cit29()
        o_Cro2 = Cro2()
        o_Cro26 = Cro26()
        o_Cro8 = Cro8()
        o_Cro41 = Cro41()
        o_Cro22 = Cro22()
        o_Cro36 = Cro36()
        o_Cro49 = Cro49()
        o_Fa4 = Fa4()
        o_Fa10 = Fa10()
        o_Fa14 = Fa14()
        o_Fa24 = Fa24()
        o_Fo3 = Fo3()
        o_Fo10 = Fo10()
        o_Fo16 = Fo16()
        o_Fo21 = Fo21()
        o_Fo36 = Fo36()
        o_Isl6 = Isl6()
        o_Isl12 = Isl12()
        o_Isl16 = Isl16()
        o_Jad3 = jad3()
        o_Jad7 = jad7()
        o_Jad15 = jad15()
        o_Jad10 = jad10()
        o_Jy4 = jy4()
        o_Jy7 = jy7()
        o_Jy14 = jy14()
        o_Jy17 = jy17()
        o_Jy26 = jy26()
        o_Jy37 = jy37()
        o_Ma4 = Ma4()
        o_Ma10 = Ma10()
        o_Ma16 = Ma16()
        o_Ma33 = Ma33()
        o_Ma18 = Ma18()
        o_No2 = No2()
        o_No24 = No24()
        o_No37 = No37()
        o_No15 = No15()
        o_No10 = No10()
        o_Oh3 = Oh3()
        o_Oh27 = Oh27()
        o_Oh31 = Oh31()
        o_Ov4 = Ov4()
        o_Ov54 = Ov54()
        o_Ov39 = Ov39()
        o_Ov45 = Ov45()
        o_Ov30 = Ov30()
        o_Ri3 = Ri3()
        o_Ri27 = Ri27()
        o_Ri20 = Ri20()
        o_SP2 = SP2()
        o_SP8 = SP8()
        o_SP22 = SP22()
        o_SP28 = SP28()
        o_Sa4 = Sa4()
        o_Sa8 = Sa8()
        o_Sa9 = Sa9()
        o_Sa27 = Sa27()
        o_Sa12 = Sa12()
        o_Sv1 = Sv1()
        o_Sv6 = Sv6()
        o_Sv23 = Sv23()
        o_Sv12 = Sv12()
        o_Tr1 = Tr1()
        o_Tr21 = Tr21()
        o_Tr5 = Tr5()
        o_Tr10 = Tr10()
        o_Uf3 = Uf3()
        o_Uf5 = Uf5()
        o_Uf15 = Uf15()
        o_Uf24 = Uf24()
        o_Vr3 = Vr3()
        o_Vr8 = Vr8()
        o_Vr14 = Vr14()
        o_Vr17 = Vr17()
        o_Vr32 = Vr32()
        o_Wr7 = Wr7()
        o_Wr13 = Wr13()
        o_Wr24 = Wr24()

        global m20, m39, m30
        m20 = madhya20()
        m39 = madhya39()
        m30 = madhya30()

        global amounthealed
        amounthealed = 0

        global n_CrU, n_AsU, n_CitU, n_FalU, n_FalU1, n_FalU2, n_IsleU, n_jadiU, n_riverShop, n_trShop, n_wrU

        n_CrU = CrU()
        n_AsU = AsU()
        n_CitU = CitU()
        n_FalU = FalU()
        n_FalU1 = FalU1()
        n_FalU2 = FalU2()
        n_IsleU = IsleU()
        n_jadiU = jadiU()
        n_riverShop = riverShop()
        n_trShop = trShop()
        n_wrU = wrU()

        global can_save
        global karma, sin, merit
        global scale_level
        global show_buttons
        global has_right
        global battleAction
        global center_choices
        global with_nisha, with_lydria, with_saanvi

        global locationsVisited
        global pillar_1,pillar_2,pillar_3,pillar_4,pillar_5,pillar_6,pillar_7

        battleAction = ""

        #other variables
        global variables
        variables = []

        global contentpacks
        contentpacks = []

        global locationsVisited
        locationsVisited = ["vatika", "crossroads", "overgrowth"]
        pillar_1 = 0
        pillar_2 = 0
        pillar_3 = 0
        pillar_4 = 0
        pillar_5 = 0
        pillar_6 = 0
        pillar_7 = 0

        show_buttons = 1
        can_save = 0
        karma = 0
        sin = 0
        merit = 0
        #this is the scale_level
        scale_level = 1
        has_right = False
        center_choices = False
        with_nisha = 0
        with_lydria = 0
        with_saanvi = 0
        takal_completed = 0

        global skills
        global mind_slot, body_slot, soul_slot, desires_slot
        global player

        global inventory, jivas, skills, equips
        player = Player()
        inventory = []
        equips = []

        jivas = 0

        global njJivas
        njJivas = 0

        global njDiscount
        njDiscount = 0

        mind_slot = mindSlot()
        body_slot = bodySlot()
        soul_slot = soulSlot()
        desires_slot = desiresSlot()
        skills = []

        #characters/interactions
        #declarations
        global objKamala, objKamalaIntro, objKamalaLevelUp, objLeaveVatika, objIntroFountain, objSavePoint, objFountain

        global sex_scenes

        global objVari, objAditi, objAditi2, objAnnavere, objEinya, objEinya2, objHansa, objHansa2, objLydria, objMysa, objNiija, objNisha, objNisha1,objNisha2, objNisha3, objPrisha, objSaanvi, objSaanvi2, objSyll, objTakal, objLydriaEnd, objSaanviEnd, objKamalaEnd, objTakalEnd

        sex_scenes = 0

        global samapare_flood
        samapare_flood = 10

        #kamala
        objKamala = chrKamala()
        objKamalaLevelUp = chrKamalaLevelUp()

        #aditi
        objAditi = chrAditi()
        objAditi2 = chrAditi2()

        #annavere
        objAnnavere = chrAnnavere()

        #einya
        objEinya = chrEinya()
        objEinya2 = chrEinya2()

        #hansa
        objHansa = chrHansa()
        objHansa2 = chrHansa2()

        #lydria
        objLydria = chrLydria()

        #mysa
        objMysa = chrMysa()

        #niija
        objNiija = chrNiija()

        #nisha
        objNisha = chrNisha()
        objNisha1 = chrNisha1()
        objNisha2 = chrNisha2()
        objNisha3 = chrNisha3()

        #prisha
        objPrisha = chrPrisha()

        #saanvi
        objSaanvi = chrSaanvi()
        objSaanvi2 = chrSaanvi2()

        #syll
        objSyll = chrSyll()

        #takal
        objTakal = chrTakal()

        # vari
        objVari = chrVari()


        #endings
        objLydriaEnd = chrLydriaEnd()
        objSaanviEnd = chrSaanviEnd()
        objKamalaEnd = chrKamalaEnd()
        objTakalEnd = chrTakalEnd()

        #environment

        objKamalaIntro = chrKamalaIntro()
        objLeaveVatika = envLeaveVatika()
        objIntroFountain = envIntroFountain()
        objSavePoint = envSavePoint()
        objFountain = envFountain()

        global objStoneBlock
        objStoneBlock = envStoneBlock()






        #worlds
        global mpVatika
        mpVatika = scrVatika()
        mpVatika.addTile(0.495,0.57,5,[1], fountainInteraction, 0)
        mpVatika.addTile(0.495,0.67,0,[0,2,9], nullInteraction, 0)
        mpVatika.addTile(0.44,0.71,lydriaDetermine("icon"),[1,3], lydriaInteraction, lydriaDetermine("auto"))
        mpVatika.addTile(0.385,0.665,saanviDetermine("icon"),[2,4], saanviInteraction, saanviDetermine("auto"))
        mpVatika.addTile(0.325,0.655,0,[3,5,15], nullInteraction, 0)
        mpVatika.addTile(0.27,0.685,0,[4,6], nullInteraction, 0)
        mpVatika.addTile(0.215,0.685,tutInt_(),[5,7], tutInt, 1)
        mpVatika.addTile(0.085,0.645,0,[6,8], nullInteraction, 0)
        mpVatika.addTile(0.025,0.625,3,[7], leavetoWorldmap, 0)
        mpVatika.addTile(0.551,0.71,syllDetermine("icon"),[1,10], syllInteraction, syllDetermine("auto"))
        mpVatika.addTile(0.61,0.665,hansaDetermine("icon"),[9, 11], hansaInteraction, hansaDetermine("auto"))
        mpVatika.addTile(0.672,0.651,einyaDetermine("icon"),[10, 12], einyaInteraction, einyaDetermine("auto"))
        mpVatika.addTile(0.675,0.551,annavereDetermine("icon"),[11, 13, 14], annavereInteraction, annavereDetermine("auto"))
        mpVatika.addTile(0.73,0.551,6,[12], saveInteraction, 0)
        mpVatika.addTile(0.675,0.451,aditiDetermineTile("icon"),[12], aditiInteraction, aditiDetermineTile("auto"))
        mpVatika.addTile(0.33,0.555,kamalaDetermine("icon"),[4], kamalaInteraction, kamalaDetermine("auto"))

        global mpVatika_night
        mpVatika_night = scrVatika_night()
        mpVatika_night.addTile(0.495,0.57,5,[1], fountainInteraction, 0)
        mpVatika_night.addTile(0.495,0.67,kamalaDetermine("icon"),[0,2,9], kamalaInteraction, kamalaDetermine("auto"))
        mpVatika_night.addTile(0.44,0.71,0,[1,3], nullInteraction, 0)
        mpVatika_night.addTile(0.385,0.665,0,[2,4], nullInteraction, 0)
        mpVatika_night.addTile(0.325,0.655,0,[3,5,15], nullInteraction, 0)
        mpVatika_night.addTile(0.27,0.685,0,[4,6], nullInteraction, 0)
        mpVatika_night.addTile(0.215,0.685,tutInt_(),[5,7], tutInt, 1)
        mpVatika_night.addTile(0.085,0.645,0,[6,8], nullInteraction, 0)
        mpVatika_night.addTile(0.025,0.625,3,[7], leavetoWorldmap, 0)
        mpVatika_night.addTile(0.551,0.71,0,[1,10], nullInteraction, 0)
        mpVatika_night.addTile(0.61,0.665,0,[9, 11], nullInteraction, 0)
        mpVatika_night.addTile(0.672,0.651,0,[10, 12], nullInteraction, 0)
        mpVatika_night.addTile(0.675,0.551,0,[11, 13, 14], nullInteraction, 0)
        mpVatika_night.addTile(0.73,0.551,6,[12], saveInteraction, 0)
        mpVatika_night.addTile(0.675,0.451,0,[12], nullInteraction, 0)
        mpVatika_night.addTile(0.33,0.555,0,[4], nullInteraction, 0)

        global mpVatika_end
        mpVatika_end = scrVatikaEnd()
        mpVatika_end.addTile(0.495,0.57,8,[1], Function(mapJump, "ending_scene"), 1)
        mpVatika_end.addTile(0.495,0.67,0,[0,2,9], nullInteraction, 0)
        mpVatika_end.addTile(0.44,0.71,lydriaEndDetermine("icon"),[1,3], lydriaEndInteraction, lydriaEndDetermine("auto"))
        mpVatika_end.addTile(0.385,0.665,saanviEndDetermine("icon"),[2,4], saanviEndInteraction, saanviEndDetermine("auto"))
        mpVatika_end.addTile(0.325,0.655,kamalaEndDetermine("icon"),[3,5,15], kamalaEndInteraction, kamalaEndDetermine("auto"))
        mpVatika_end.addTile(0.27,0.685,0,[4,6], nullInteraction, 0)
        mpVatika_end.addTile(0.215,0.685,0,[5,7], nullInteraction, 0)
        mpVatika_end.addTile(0.085,0.645,0,[6,8], nullInteraction, 0)
        mpVatika_end.addTile(0.025,0.625,3,[7], leavetoWorldmap, 0)
        mpVatika_end.addTile(0.551,0.71,0,[1,10], nullInteraction, 0)
        mpVatika_end.addTile(0.61,0.665,0,[9, 11], nullInteraction, 0) #10
        mpVatika_end.addTile(0.672,0.651,0,[10, 12], nullInteraction, 0)
        mpVatika_end.addTile(0.675,0.551,0,[11, 13, 14], nullInteraction, 0)
        mpVatika_end.addTile(0.73,0.551,0,[12], nullInteraction, 0)
        mpVatika_end.addTile(0.675,0.451,0,[12], nullInteraction, 0)
        mpVatika_end.addTile(0.33,0.555,takalEndDetermine("icon"),[4], takalEndInteraction, takalEndDetermine("auto"))

        #vatika_intro
        global mpVatika_intro
        mpVatika_intro = scrVatikaIntro()
        mpVatika_intro.addTile(0.495,0.57,8,[1], fountainInteraction_intro, 1)
        mpVatika_intro.addTile(0.495,0.67,0,[0,2,9], nullInteraction, 0)
        mpVatika_intro.addTile(0.44,0.71,0,[1,3], nullInteraction, 0)
        mpVatika_intro.addTile(0.385,0.665,0,[2,4],  nullInteraction, 0)
        mpVatika_intro.addTile(0.325,0.655,0,[3,5,15], nullInteraction, 0)
        mpVatika_intro.addTile(0.27,0.685,0,[4,6], nullInteraction, 0)
        mpVatika_intro.addTile(0.215,0.685,0,[5,7], nullInteraction, 0)
        mpVatika_intro.addTile(0.085,0.645,0,[6,8], nullInteraction, 0)
        mpVatika_intro.addTile(0.025,0.625,3,[7], leaveinteraction_intro, 1)
        mpVatika_intro.addTile(0.551,0.71,2,[1,10], kamalaInteraction_intro, 1)
        mpVatika_intro.addTile(0.61,0.665,0,[9, 11], nullInteraction, 0) #10
        mpVatika_intro.addTile(0.672,0.651,0,[10, 12], nullInteraction, 0)
        mpVatika_intro.addTile(0.675,0.551,0,[11, 13, 14], nullInteraction, 0)
        mpVatika_intro.addTile(0.73,0.551,0,[12], nullInteraction, 0)
        mpVatika_intro.addTile(0.675,0.451,0,[12], nullInteraction, 0)
        mpVatika_intro.addTile(0.33,0.555,0,[4], nullInteraction, 0)

        #Worldmap
        global mpWorldMap
        mpWorldMap = scrWorldMap()
        mpWorldMap.addTile(0.145,0.67,0,[1,2], jumpMap, 0, "vatika") #vatika 0
        mpWorldMap.addTile(0.165,0.53,0,[4,0,5,9,2], jumpMap1,0, "crossroads") #crossroad 1
        mpWorldMap.addTile(0.245,0.56,0,[0,3,6,1,8], jumpMap2,0,"overgrowth") #overgrowth  2'
        mpWorldMap.addTile(0.3265,0.61,0,[2], jumpMap3, 0, "heart") #overgrown heart 3
        mpWorldMap.addTile(0.115,0.44,0,[1], jumpMap4, 0, "samapare") #sama pare 4
        mpWorldMap.addTile(0.348,0.46,0,[1], jumpMap5, 0, "jindagee") #jidangee river  5
        mpWorldMap.addTile(0.455,0.5,0,[7,18,2], jumpMap6, 0, "svach") #svach pass  6
        mpWorldMap.addTile(0.43,0.7,0,[6], jumpMap7, 0, "anuraa") #anuraa's folly 7
        mpWorldMap.addTile(0.3065,0.855,0,[2], jumpMap8, 0, "lostsanctuary") #lost sanctuary 8
        mpWorldMap.addTile(0.231,0.355,0,[1,14,12,10], jumpMap9, 0, "northcross") #crossroads north 9
        mpWorldMap.addTile(0.13,0.245,0,[9,11], jumpMap10, 0, "adame") #adame's crossing  10
        mpWorldMap.addTile(0.155,0.137,0,[10], jumpMap11, 0, "cistern") #cistern 11
        mpWorldMap.addTile(0.268,0.2,0,[9,13], jumpMap122, 0, "citadel") #citadel 12
        mpWorldMap.addTile(0.287,0.07,0,[12], jumpMap12, 0, "aatmaon") #aatmaon  13
        mpWorldMap.addTile(0.308,0.285,0,[9,15],jumpMap13, 0, "parivara") #falls 14
        mpWorldMap.addTile(0.378,0.275,0,[14,16], jumpMap14, 0, "underfalls") #underfalls 15
        mpWorldMap.addTile(0.562,0.35,0,[15,17,21], jumpMap15, 0, "caverns") #caverns  16
        mpWorldMap.addTile(0.53,0.505,0,[16], jumpMap16, 0, "court") #madhya court  17
        mpWorldMap.addTile(0.56,0.64,0,[6,19], jumpMap17, 0, "rest") #warrior's rest 18
        mpWorldMap.addTile(0.698,0.4285,0,[18,20], jumpMap18, 0, "gorge") #jala diya gorge 19
        mpWorldMap.addTile(0.695,0.29,0,[19], jumpMap19, 0, "peak") #jyoti peak 20
        mpWorldMap.addTile(0.81,0.415,0,[16,22,23], jumpMap20, 0, "trench") #deep water  21
        mpWorldMap.addTile(0.678,0.785,0,[21], jumpMap21, 0, "acropolis") #acropolis 22
        mpWorldMap.addTile(0.8,0.785,0,[21,24], jumpMap22, 0, "stone") #stone island 23
        mpWorldMap.addTile(0.77,0.875,0,[23,25], jumpMap23, 0, "drop") #Asura's Drop 24
        mpWorldMap.addTile(0.82,0.915,0,[24], jumpMap24, 0, "end") #Vritra's End 25

        global mpOvergrowth
        mpOvergrowth = scrOvergrowth()
        mpOvergrowth.addTile(0.0,0.45,3,[1], leavetoWorldmap, 0)
        mpOvergrowth.addTile(0.06,0.45,0,[0,2,3], nullInteraction, 0)
        mpOvergrowth.addTile(0.1,0.38,0,[1,35], nullInteraction, 0)
        mpOvergrowth.addTile(0.1,0.52,0,[1,4], nullInteraction, 0)
        mpOvergrowth.addTile(0.16,0.54,5,[3,5,53], obv65, 0)
        mpOvergrowth.addTile(0.22,0.52,1,[4,6], Function(callBattle,enemy_thief,"None","None","Overgrowth"), 1)  #5
        mpOvergrowth.addTile(0.28,0.5,0,[5,7], nullInteraction, 0)
        mpOvergrowth.addTile(0.34,0.52,1,[6,8], Function(callBattle,enemy_thief,enemy_thief,"None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.40,0.5,0,[7,9], nullInteraction, 0)
        mpOvergrowth.addTile(0.46,0.52,0,[8,10], nullInteraction, 0)
        mpOvergrowth.addTile(0.52,0.54,1,[9,11,12], Function(callBattle,enemy_berserker,"None","None","Overgrowth"), 1) #19
        mpOvergrowth.addTile(0.58,0.5,0,[10,13], nullInteraction, 0)
        mpOvergrowth.addTile(0.58,0.6,0,[10,24], nullInteraction, 0)
        mpOvergrowth.addTile(0.63,0.44,1,[11,14], Function(callBattle,enemy_berserker,"None","None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.69,0.44,0,[13,15], nullInteraction, 0)
        mpOvergrowth.addTile(0.75,0.44,0,[14,16], nullInteraction, 0) #15
        mpOvergrowth.addTile(0.77,0.34,1,[15,17], Function(callBattle,enemy_thief,enemy_berserker,"None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.76,0.24,0,[16,18], nullInteraction, 0)
        mpOvergrowth.addTile(0.82,0.24,0,[17,19], nullInteraction, 0)
        mpOvergrowth.addTile(0.88,0.24,1,[18,20],  Function(callBattle,enemy_berserker,enemy_berserker,"None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.94,0.24,0,[19,21], nullInteraction, 0)  #2
        mpOvergrowth.addTile(0.95,0.34,0,[20,22], nullInteraction, 0)
        mpOvergrowth.addTile(0.96,0.44,3,[21,23], heartPass, 0)
        mpOvergrowth.addTile(1.0,0.51,0,[22], nullInteraction, 0)
        mpOvergrowth.addTile(0.64,0.6,0,[12,25], nullInteraction, 0)
        mpOvergrowth.addTile(0.7,0.6,5,[24,26,27], obv69, 0) #25
        mpOvergrowth.addTile(0.76,0.6,annavereDetermine("icon"),[25],  annavereInteraction, annavereDetermine("auto"))
        mpOvergrowth.addTile(0.7,0.7,0,[25,28], nullInteraction, 0)
        mpOvergrowth.addTile(0.7,0.8,0,[27,29], nullInteraction, 0)
        mpOvergrowth.addTile(0.76,0.8,0,[28,30],  nullInteraction, 0)
        mpOvergrowth.addTile(0.82,0.8,0,[29,31], nullInteraction, 0) #30
        mpOvergrowth.addTile(0.88,0.8,1,[30,32,62,33],  Function(callBattle,enemy_berserker,enemy_berserker,"None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.94,0.8,an_thief_(),[31], an_thief, 0)
        mpOvergrowth.addTile(0.88,0.92,0,[31,34], nullInteraction, 0)
        mpOvergrowth.addTile(0.92,1.0,3,[33], lostsanctuaryPass, 0)
        mpOvergrowth.addTile(0.16,0.38,0,[2,36], nullInteraction, 0) #35
        mpOvergrowth.addTile(0.22,0.36,1,[35,37],  Function(callBattle,enemy_thief,enemy_thief,"None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.28,0.36,0,[36,38], nullInteraction, 0)
        mpOvergrowth.addTile(0.34,0.34,5,[37,39], obv67, 0)
        mpOvergrowth.addTile(0.40,0.32,0,[38,40,65], nullInteraction, 0)
        mpOvergrowth.addTile(0.41,0.22,0,[39,41], nullInteraction, 0) #40
        mpOvergrowth.addTile(0.40,0.12,0,[40,42], nullInteraction, 0)
        mpOvergrowth.addTile(0.46,0.12,1,[41,43],  Function(callBattle,enemy_thief,enemy_berserker,enemy_thief,"Overgrowth"), 1)
        mpOvergrowth.addTile(0.52,0.11,0,[42,44], nullInteraction, 0)
        mpOvergrowth.addTile(0.58,0.12,0,[43,45], nullInteraction, 0)
        mpOvergrowth.addTile(0.64,0.13,5,[44,46], obv68, 0) #50
        mpOvergrowth.addTile(0.65,0.03,1,[45,47],  Function(callBattle,enemy_thief,"None","None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.71,0.03,0,[46,48], nullInteraction, 0)
        mpOvergrowth.addTile(0.77,0.04,0,[47,49], nullInteraction, 0)
        mpOvergrowth.addTile(0.83,0.03,1,[48,50],  Function(callBattle,enemy_berserker,enemy_berserker,"None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.89,0.02,0,[49,51], nullInteraction, 0) #55
        mpOvergrowth.addTile(0.95,0.03,0,[50,42], nullInteraction, 0)
        mpOvergrowth.addTile(1.0,0.08,3,[51], svachPass, 0)
        mpOvergrowth.addTile(0.16,0.64,0,[4,54], nullInteraction, 0)
        mpOvergrowth.addTile(0.15,0.74,5,[53,55,58], obv66, 0)
        mpOvergrowth.addTile(0.09,0.74,1,[54,56],  Function(callBattle,enemy_asuri,"None","None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.03,0.74,0,[55,57], nullInteraction, 0)
        mpOvergrowth.addTile(0.00,0.84,1,[56],  Function(callBattle,enemy_asuri,"None","None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.21,0.73,0,[54,59], nullInteraction, 0)
        mpOvergrowth.addTile(0.21,0.83,ov_sidequest_(),[58,60], ov_sidequest, 0)
        mpOvergrowth.addTile(0.27,0.83,1,[59,61],  Function(callBattle,enemy_asuri,"None","None","Overgrowth"), 1)
        mpOvergrowth.addTile(0.33,0.8,0,[60], nullInteraction, 0)
        mpOvergrowth.addTile(0.86,0.7,0,[31,63], nullInteraction, 0)
        mpOvergrowth.addTile(0.87,0.6,0,[62,64], nullInteraction, 0)
        mpOvergrowth.addTile(0.85,0.5,1,[63],  Function(callBattle,enemy_thief,enemy_thief,enemy_thief,"Overgrowth"), 1)
        mpOvergrowth.addTile(0.46,0.32,0,[39,66], nullInteraction, 0)
        mpOvergrowth.addTile(0.52,0.34,0,[65,67], nullInteraction, 0)
        mpOvergrowth.addTile(0.58,0.32,1,[66],  Function(callBattle,enemy_succubus,"None","None","Overgrowth"), 1)

        global mpCrossroads
        mpCrossroads = scrCrossroads()
        mpCrossroads.addTile(0.3,1.0,3,[1,14], leavetoWorldmap, 0)
        mpCrossroads.addTile(0.28,0.9,0,[0,2], nullInteraction, 0)
        mpCrossroads.addTile(0.29,0.8,5,[1,3,50], obv102, 0)
        mpCrossroads.addTile(0.28,0.7,1,[2,4], Function(callBattle,enemy_thief,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(0.27,0.6,0,[3,5], nullInteraction, 0)
        mpCrossroads.addTile(0.26,0.5,0,[4,6], nullInteraction, 0)
        mpCrossroads.addTile(0.27,0.4,1,[5,7,26], Function(callBattle,enemy_thief,enemy_thief,"None","Crossroads"), 1)
        mpCrossroads.addTile(0.29,0.3,0,[6,8], nullInteraction, 0)
        mpCrossroads.addTile(0.34,0.25,5,[7,9], obv104, 0)
        mpCrossroads.addTile(0.39,0.2,0,[8,10], nullInteraction, 0)
        mpCrossroads.addTile(0.44,0.15,1,[9,11], Function(callBattle,enemy_thief,enemy_berserker,enemy_thief,"Crossroads"), 1)
        mpCrossroads.addTile(0.49,0.1,0,[10,12], nullInteraction, 0)
        mpCrossroads.addTile(0.54,0.05,0,[11,13], nullInteraction, 0)
        mpCrossroads.addTile(0.59,0.0,3,[12], northPass, 0)
        mpCrossroads.addTile(0.35,0.96,0,[0,15], nullInteraction, 0)
        mpCrossroads.addTile(0.41,0.94,0,[14,16], nullInteraction, 0)
        mpCrossroads.addTile(0.47,0.92,1,[15,17], Function(callBattle,enemy_berserker,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(0.53,0.90,2,[16,18], npc_1, 0)
        mpCrossroads.addTile(0.59,0.88,1,[17,19], Function(callBattle,enemy_thief,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(0.65,0.86,0,[19,20], nullInteraction, 0)
        mpCrossroads.addTile(0.71,0.84,0,[19,21,31], nullInteraction, 0) #20
        mpCrossroads.addTile(0.77,0.82,1,[20,22], Function(callBattle,enemy_fox,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(0.83,0.8,5,[21,23], obv106, 0)
        mpCrossroads.addTile(0.89,0.8,0,[22,24], nullInteraction, 0)
        mpCrossroads.addTile(0.95,0.78,1,[23,25], Function(callBattle,enemy_fox,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(1.0,0.83,3,[24], leavetoWorldmap, 0)
        mpCrossroads.addTile(0.21,0.4,5,[6,27], obv103, 0)
        mpCrossroads.addTile(0.15,0.39,1,[26,28], Function(callBattle,enemy_fox,enemy_fox,"None","Crossroads"), 1)
        mpCrossroads.addTile(0.09,0.4,0,[27,29], nullInteraction, 0)
        mpCrossroads.addTile(0.04,0.44,1,[30,28], Function(callBattle,enemy_berserker,enemy_berserker,enemy_berserker,"Crossroads"), 1)
        mpCrossroads.addTile(0.0,0.36,3,[29], samaparePass, 0)
        mpCrossroads.addTile(0.71,0.74,1,[20,32], Function(callBattle,enemy_thief,enemy_thief,"None","Crossroads"), 1)
        mpCrossroads.addTile(0.73,0.64,0,[31,33], nullInteraction, 0)
        mpCrossroads.addTile(0.75,0.54,1,[32,34,40], Function(callBattle,enemy_fox,enemy_fox,"None","Crossroads"), 1)
        mpCrossroads.addTile(0.81,0.54,0,[33,35], nullInteraction, 0)
        mpCrossroads.addTile(0.87,0.54,0,[34,36], nullInteraction, 0)
        mpCrossroads.addTile(0.89,0.44,4,[35,37], obv107, 0)
        mpCrossroads.addTile(0.91,0.34,1,[36,38], Function(callBattle,enemy_thief,enemy_thief,"None","Crossroads"), 1)
        mpCrossroads.addTile(0.93,0.24,0,[37,39], nullInteraction, 0)
        mpCrossroads.addTile(0.99,0.21,3,[38], jindageePass, 0)
        mpCrossroads.addTile(0.69,0.53,0,[33,41], nullInteraction, 0)
        mpCrossroads.addTile(0.63,0.52,5,[40,42], obv105, 0)
        mpCrossroads.addTile(0.57,0.54,1,[41,43], Function(callBattle,enemy_berserker,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(0.51,0.52,0,[42,44], nullInteraction, 0)
        mpCrossroads.addTile(0.51,0.64,0,[43,45], nullInteraction, 0)
        mpCrossroads.addTile(0.51,0.74,1,[44,46,48], Function(callBattle,enemy_thief,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(0.45,0.77,0,[45,47], nullInteraction, 0)
        mpCrossroads.addTile(0.39,0.74,cro_sidequest_(),[46], cro_sidequest, 0)
        mpCrossroads.addTile(0.57,0.74,0,[45,49], nullInteraction, 0)
        mpCrossroads.addTile(0.63,0.7,5,[48], obv108, 0)
        mpCrossroads.addTile(0.23,0.81,0,[2,51], nullInteraction, 0)
        mpCrossroads.addTile(0.17,0.8,1,[50,52], Function(callBattle,enemy_berserker,"None","None","Crossroads"), 1)
        mpCrossroads.addTile(0.11,0.79,0,[51], nullInteraction, 0)

        global mpOvergrownHeart
        mpOvergrownHeart = scrOvergrownHeart()
        mpOvergrownHeart.addTile(0.5,1.0,3,[1], leavetoWorldmap, 0)
        mpOvergrownHeart.addTile(0.49,0.9,0,[0,2], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.51,0.8,1,[1,3], Function(callBattle,enemy_shadow,"None","None","Heart"), 1)
        mpOvergrownHeart.addTile(0.5,0.7,5,[2,4,5], obv62, 0)
        mpOvergrownHeart.addTile(0.56,0.68,0,[3,13], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.44,0.72,0,[3,6], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.38,0.69,0,[5,7], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.32,0.66,1,[6,8], Function(callBattle,enemy_shadow,enemy_shadow,"None","Heart"), 1)
        mpOvergrownHeart.addTile(0.26,0.64,0,[7,9], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.23,0.54,0,[8,10], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.25,0.44,1,[9,11], Function(callBattle,enemy_shadow,"None","None","Heart"), 1)  #10
        mpOvergrownHeart.addTile(0.26,0.34,0,[10,12], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.28,0.24,0,[11,25], nullInteraction, 0)
        #mpOvergrownHeart.addTile(0.56,0.68,0,[], leavetoWorldmap, 0)
        mpOvergrownHeart.addTile(0.61,0.64,0,[4,14], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.66,0.6,0,[13,15], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.71,0.55,1,[14,16], Function(callBattle,enemy_shadow,enemy_shadow,"None","Heart"), 1)
        mpOvergrownHeart.addTile(0.73,0.45,0,[15,17,30], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.72,0.35,0,[16,18], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.7,0.25,0,[17,19], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.66,0.17,1,[18,20],Function(callBattle,enemy_shadow,"None","None","Heart"), 1)  #20
        mpOvergrownHeart.addTile(0.605,0.15,0,[19,21], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.55,0.13,0,[20,22], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.49,0.14,1,[21,23,26], Function(callBattle,enemy_shadow,"None","None","Heart"), 1)
        mpOvergrownHeart.addTile(0.43,0.16,heartSideQuest_(),[22,24], heartSideQuest, 0)
        mpOvergrownHeart.addTile(0.37,0.17,0,[23,25], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.31,0.15,0,[24,12], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.51,0.24,5,[22,27], obv63, 0)
        mpOvergrownHeart.addTile(0.49,0.34,0,[26,28], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.5,0.44,0,[27,29],nullInteraction, 0)
        mpOvergrownHeart.addTile(0.5,0.54,nishaDetermine("icon"),[28], nishaInteraction, nishaDetermine("auto"))
        mpOvergrownHeart.addTile(0.79,0.44,0,[16,31], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.85,0.46,5,[30,32], obv64, 0)
        mpOvergrownHeart.addTile(0.91,0.48,0,[31,33], nullInteraction, 0)
        mpOvergrownHeart.addTile(0.97,0.47,einyaDetermine("icon"),[32], einyaInteraction, einyaDetermine("auto"))

        global mpSamaPare
        mpSamaPare = scrSamaPare()
        mpSamaPare.addTile(0.465,1.0,3,[1], leavetoWorldmap, 0)
        mpSamaPare.addTile(0.465,0.9,0,[0,2], nullInteraction, 0)
        mpSamaPare.addTile(0.465,0.8,5,[1,3,16,41], obv73, 0)
        mpSamaPare.addTile(0.41,0.8,0,[2,4], nullInteraction, 0)
        mpSamaPare.addTile(0.35,0.8,1,[3,5], Function(callBattle,enemy_jarita,enemy_jarita,enemy_jarita,"SamaPare"), 1)
        mpSamaPare.addTile(0.29,0.8,0,[4,6,7], nullInteraction, 0)
        mpSamaPare.addTile(0.29,0.9,0,[5,8], nullInteraction, 0)
        mpSamaPare.addTile(0.29,0.7,1,[5,14], Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.23,0.9,5,[6,9], obv74, 0)
        mpSamaPare.addTile(0.17,0.9,1,[8,10], Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.11,0.9,0,[9,11,13], nullInteraction, 0)
        mpSamaPare.addTile(0.11,0.8,1,[10,12], Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.11,0.7,samapareFloodGate1_(),[11], samapareFloodGate1, 0)
        mpSamaPare.addTile(0.05,0.9,6,[10], saveInteraction, 0)
        mpSamaPare.addTile(0.29,0.6,0,[7,15], nullInteraction, 0)
        mpSamaPare.addTile(0.35,0.6,1,[14], Function(callBattle,enemy_jarita,enemy_jarita,"None","SamaPare"), 1)
        mpSamaPare.addTile(0.52,0.8,0,[2,17], nullInteraction, 0)
        mpSamaPare.addTile(0.58,0.8,0,[16,18], nullInteraction, 0)
        mpSamaPare.addTile(0.64,0.8,1,[17,19,20],Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.64,0.7,0,[18,39], nullInteraction, 0)
        mpSamaPare.addTile(0.64,0.9,0,[18,21], nullInteraction, 0)
        mpSamaPare.addTile(0.7,0.9,1,[20,22],Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.76,0.9,5,[21,23], obv75, 0)
        mpSamaPare.addTile(0.82,0.9,0,[22,24], nullInteraction, 0)
        mpSamaPare.addTile(0.88,0.9,1,[23,25,26], Function(callBattle,enemy_jarita,enemy_jarita,enemy_jarita,"SamaPare"), 1)
        mpSamaPare.addTile(0.94,0.9,samapareTome_(),[24], samapareTome, 0)
        mpSamaPare.addTile(0.88,0.8,0,[24,27], nullInteraction, 0)
        mpSamaPare.addTile(0.88,0.7,1,[26,28], Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.88,0.6,5,[27,29,31], obv76, 0)
        mpSamaPare.addTile(0.94,0.6,1,[28,30], Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(1.0,0.6,samapareFloodGate2_(),[29], samapareFloodGate2, 0)
        mpSamaPare.addTile(0.82,0.6,0,[28,32], nullInteraction, 0)
        mpSamaPare.addTile(0.82,0.5,1,[31,33], Function(callBattle,enemy_darkmage,enemy_darkmage,"None","SamaPare"), 1)
        mpSamaPare.addTile(0.82,0.4,0,[32,34,37], nullInteraction, 0)
        mpSamaPare.addTile(0.76,0.4,0,[33,35], nullInteraction, 0)
        mpSamaPare.addTile(0.7,0.4,1,[34,36],Function(callBattle,enemy_darkmage,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.64,0.4,samapareMarking_(),[35], samapareMarking, 0)
        mpSamaPare.addTile(0.88,0.4,0,[33,38], nullInteraction, 0)
        mpSamaPare.addTile(0.94,0.4,mysaDetermine("icon"),[37], mysaInteraction, mysaDetermine("auto"))
        mpSamaPare.addTile(0.64,0.6,1,[19,40], Function(callBattle,enemy_jarita,"None","None","SamaPare"), 1)
        mpSamaPare.addTile(0.58,0.6,0,[39], nullInteraction, 0)
        mpSamaPare.addTile(0.465,0.7,samapareTrap_(),[2,42], samapareTrap, 1)
        mpSamaPare.addTile(0.465,0.6,boss_1_(),[41], boss_1, 0)

        global mpJidangeeRiver
        mpJidangeeRiver = scrJidangeeRiver()
        mpJidangeeRiver.addTile(0.0,1.0,3,[1], leavetoWorldmap, 0)
        mpJidangeeRiver.addTile(0.05,0.95,0,[0,2], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.1,0.9,0,[1,3], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.152,0.92,5,[2,4], obv70, 0)
        mpJidangeeRiver.addTile(0.205,0.91,0,[3,5], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.26,0.93,1,[4,6],  Function(callBattle,enemy_slime,"None","None","JindangeRiver"), 1) #5
        mpJidangeeRiver.addTile(0.315,0.91,0,[6,7,25], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.305,0.81,0,[6,8,9], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.315,0.71,0,[7,13], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.255,0.78,1,[7,10], Function(callBattle,enemy_slime,enemy_slime,"None","JindangeRiver"), 1)
        mpJidangeeRiver.addTile(0.2,0.79,0,[9,11], nullInteraction, 0) #10
        mpJidangeeRiver.addTile(0.145,0.76,0,[10,12], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.155,0.66,hansaDetermine("icon"),[11], hansaInteraction, hansaDetermine("auto"))
        mpJidangeeRiver.addTile(0.37,0.7,0,[8,14], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.425,0.71,1,[13,15], Function(callBattle,enemy_slime,"None","None","JindangeRiver"), 1)
        mpJidangeeRiver.addTile(0.48,0.73,0,[14,16], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.54,0.72,1,[15,17,29], Function(callBattle,enemy_slime,enemy_mayuri,"None","JindangeRiver"), 1)
        mpJidangeeRiver.addTile(0.6,0.71,0,[16,18], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.655,0.73,0,[17,19], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.71,0.7,1,[18,20], Function(callBattle,enemy_mayuri,"None","None","JindangeRiver"), 1)
        mpJidangeeRiver.addTile(0.765,0.72,5,[19,21,30], obv71, 0) #
        mpJidangeeRiver.addTile(0.82,0.7,0,[20,22], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.875,0.73,1,[21,23], Function(callBattle,enemy_mayuri,enemy_slime,"None","JindangeRiver"), 1)
        mpJidangeeRiver.addTile(0.93,0.72,0,[22,24], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.98,0.66,ha_weapons_(),[23], ha_weapons, 0)
        mpJidangeeRiver.addTile(0.37,0.91,0,[6,26], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.425,0.91,1,[25,27], Function(callBattle,enemy_slime,"None","None","JindangeRiver"), 1)
        mpJidangeeRiver.addTile(0.48,0.91,5,[26,28], obv72, 0)
        mpJidangeeRiver.addTile(0.535,0.91,1,[27,29], Function(callBattle,enemy_slime,"None","None","JindangeRiver"), 1)
        mpJidangeeRiver.addTile(0.55,0.818,7,[28,16], npc_9, 0)
        mpJidangeeRiver.addTile(0.78,0.82,0,[20,31], nullInteraction, 0)
        mpJidangeeRiver.addTile(0.76,0.92,riverSideQuest_(),[30], riverSideQuest, 0)

        global mpSvachPass
        mpSvachPass = scrSvachPass()
        mpSvachPass.addTile(0.4,1.0,3,[1], leavetoWorldmap, 0)
        mpSvachPass.addTile(0.4,0.9,5,[0,2,15,18], obv82, 0)
        mpSvachPass.addTile(0.4,0.8,0,[1,3], nullInteraction, 0)
        mpSvachPass.addTile(0.45,0.75,1,[2,4], Function(callBattle,enemy_jarita,"None","None","Svach"), 1)
        mpSvachPass.addTile(0.5,0.7,0,[3,5], nullInteraction, 0)
        mpSvachPass.addTile(0.55,0.65,0,[4,6], nullInteraction, 0)
        mpSvachPass.addTile(0.525,0.56,5,[5,7,8], obv83, 0)
        mpSvachPass.addTile(0.47,0.54,0,[6,10], nullInteraction, 0)
        mpSvachPass.addTile(0.575,0.52,0,[6,9], nullInteraction, 0)
        mpSvachPass.addTile(0.585,0.42,3,[8], restPass, 0)
        mpSvachPass.addTile(0.42,0.49,0,[7,11], nullInteraction, 0)
        mpSvachPass.addTile(0.37,0.44,1,[10,12], Function(callBattle,enemy_jarita,enemy_ogre,enemy_jarita,"Svach"), 1)
        mpSvachPass.addTile(0.32,0.39,5,[11,13], obv85, 0)
        mpSvachPass.addTile(0.27,0.34,1,[12,14], Function(callBattle,enemy_thief,enemy_thief,"None","Svach"), 1)
        mpSvachPass.addTile(0.215,0.34,svachSideQuest2_(),[13], svachSideQuest2, 0)
        mpSvachPass.addTile(0.345,0.9,0,[1,16], nullInteraction, 0)
        mpSvachPass.addTile(0.29,0.9,1,[15,17], Function(callBattle,enemy_thief,"None","None","Svach"), 1)
        mpSvachPass.addTile(0.245,0.84,svachSideQuest_(),[16], svachSideQuest, 0)
        mpSvachPass.addTile(0.455,0.9,0,[1,19], nullInteraction, 0)
        mpSvachPass.addTile(0.51,0.9,1,[18,20], Function(callBattle,enemy_ogre,"None","None","Svach"), 1)
        mpSvachPass.addTile(0.56,0.96,0,[19,21], nullInteraction, 0)
        mpSvachPass.addTile(0.61,0.9,1,[20,22], Function(callBattle,enemy_jarita,enemy_thief,"None","Svach"), 1)
        mpSvachPass.addTile(0.66,0.84,0,[21,23], nullInteraction, 0)
        mpSvachPass.addTile(0.715,0.84,5,[22,24], obv84, 0)
        mpSvachPass.addTile(0.77,0.84,0,[23,28,25], nullInteraction, 0)
        mpSvachPass.addTile(0.82,0.9,1,[24,26], Function(callBattle,enemy_jarita,enemy_ogre,"None","Svach"), 1)
        mpSvachPass.addTile(0.87,0.95,0,[25,27], nullInteraction, 0)
        mpSvachPass.addTile(0.92,1.3,0,[26], anuraaPass, 0)
        mpSvachPass.addTile(0.81,0.77,0,[24,29], nullInteraction, 0)
        mpSvachPass.addTile(0.76,0.72,1,[28,30], Function(callBattle,enemy_thief,"None","None","Svach"), 1)
        mpSvachPass.addTile(0.71,0.67,nishaDetermine("icon"),[29], nishaInteraction, nishaDetermine("auto"))

        global mpAnuraaFolly
        mpAnuraaFolly = scrAnuraaFolly()
        mpAnuraaFolly.addTile(0.25,1.0,3,[1], leavetoWorldmap, 0)
        mpAnuraaFolly.addTile(0.3,0.95,0,[0,2], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.32,0.86,1,[1,3], Function(callBattle,enemy_ghost,"None","None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.36,0.8,5,[2,4], obv34, 0)
        mpAnuraaFolly.addTile(0.41,0.766,0,[3,5], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.465,0.73,1,[4,6], Function(callBattle,enemy_ghost,enemy_ghost,"None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.51,0.685,0,[5,7,27],  nullInteraction, 0)
        mpAnuraaFolly.addTile(0.495,0.585,0,[6,8], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.435,0.585,0,[7,9], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.375,0.585,1,[8,10], Function(callBattle,enemy_ghost,enemy_undead,enemy_ghost,"AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.315,0.585,5,[9,11,31], obv35, 0) #10
        mpAnuraaFolly.addTile(0.255,0.555,0,[10,12], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.285,0.465,1,[11,13],  Function(callBattle,enemy_undead,enemy_undead,"None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.335,0.415,0,[12,14], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.39,0.405,1,[13,15], Function(callBattle,enemy_ghost,"None","None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.43,0.335,0,[14,16], nullInteraction, 0) #15
        mpAnuraaFolly.addTile(0.49,0.325,5,[15,17,29], obv36, 0)
        mpAnuraaFolly.addTile(0.55,0.30,1,[16,18], Function(callBattle,enemy_ghost,enemy_undead,"None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.61,0.28,0,[17,19], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.67,0.29,0,[18,20], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.73,0.3,1,[19,21],Function(callBattle,enemy_ghost,enemy_ghost,"None","AnuraaFolly"), 1) #20
        mpAnuraaFolly.addTile(0.79,0.31,5,[20,22], obv37, 0)
        mpAnuraaFolly.addTile(0.77,0.405,1,[21,23], Function(callBattle,enemy_undead,"None","None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.73,0.47,0,[22,24],  nullInteraction, 0)
        mpAnuraaFolly.addTile(0.69,0.54,0,[23,25], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.65,0.61,1,[24,26], Function(callBattle,enemy_undead,enemy_undead,"None","AnuraaFolly"), 1) #25
        mpAnuraaFolly.addTile(0.59,0.6,0,[25,27], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.565,0.685,saanviDetermine("icon"),[6,26,33], saanviInteraction, saanviDetermine("auto"))
        mpAnuraaFolly.addTile(0.5,0.425,1,[16,29], Function(callBattle,enemy_ghost,"None","None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.55,0.48,0,[28,30], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.6,0.425,boss_2_(),[29], boss_2, 0)
        mpAnuraaFolly.addTile(0.3,0.685,1,[10,32], Function(callBattle,enemy_undead,enemy_undead,enemy_undead,"AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.245,0.715,follyKey2_(),[31], follyKey2, 0) #
        mpAnuraaFolly.addTile(0.59,0.785,0,[27,34,41], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.645,0.795,1,[33,35], Function(callBattle,enemy_undead,enemy_undead,"None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.7,0.78,0,[34,36,37], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.755,0.77,5,[35], obv38, 0)
        mpAnuraaFolly.addTile(0.69,0.88,1,[35,38], Function(callBattle,enemy_ghost,"None","None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.67,0.98,follyKey1_(),[37,39], follyKey1, 0) #
        mpAnuraaFolly.addTile(0.615,0.97,0,[38,40], nullInteraction, 0)
        mpAnuraaFolly.addTile(0.56,0.965,1,[41,39], Function(callBattle,enemy_ghost,"None","None","AnuraaFolly"), 1)
        mpAnuraaFolly.addTile(0.56,0.87,0,[33,40], nullInteraction, 0)

        global mpLostSanctuary
        mpLostSanctuary = scrLostSanctuary()
        mpLostSanctuary.addTile(0.1,1.0,3,[1], leavetoWorldmap, 0)
        mpLostSanctuary.addTile(0.15,0.96,0,[0,2], nullInteraction, 0)
        mpLostSanctuary.addTile(0.2,0.91,0,[1,3], nullInteraction, 0)
        mpLostSanctuary.addTile(0.25,0.87,1,[2,4], Function(callBattle,enemy_asuri,"None","None","Sanctuary"), 1)
        mpLostSanctuary.addTile(0.3,0.81,5,[3,5,23], obv77, 0)
        mpLostSanctuary.addTile(0.35,0.77,0,[4,6], nullInteraction, 0)
        mpLostSanctuary.addTile(0.4,0.715,1,[5,7], Function(callBattle,enemy_asuri,enemy_asuri,"None","Sanctuary"), 1)
        mpLostSanctuary.addTile(0.45,0.65,0,[6,8], nullInteraction, 0)
        mpLostSanctuary.addTile(0.505,0.65,5,[7,9,17,18], obv78, 0)
        mpLostSanctuary.addTile(0.57,0.65,5,[8,10,17,18], obv79, 0)
        mpLostSanctuary.addTile(0.625,0.65,1,[9,11], Function(callBattle,enemy_asuri,enemy_devil,"None","Sanctuary"), 1)
        mpLostSanctuary.addTile(0.675,0.7,0,[10,12], nullInteraction, 0)
        mpLostSanctuary.addTile(0.725,0.75,5,[11,13], obv81, 0)
        mpLostSanctuary.addTile(0.775,0.8,1,[12,14], Function(callBattle,enemy_devil,"None","None","Sanctuary"), 1)
        mpLostSanctuary.addTile(0.825,0.85,0,[13,15], nullInteraction, 0)
        mpLostSanctuary.addTile(0.875,0.9,1,[14,16], Function(callBattle,enemy_asuri,enemy_shadow,"None","Sanctuary"), 1)
        mpLostSanctuary.addTile(0.925,0.95,sanctuaryMarking_(),[15], sanctuaryMarking, 0)
        mpLostSanctuary.addTile(0.537,0.57,0,[8,9,21,22], nullInteraction, 0)
        mpLostSanctuary.addTile(0.537,0.73,0,[8,9,19], nullInteraction, 0)
        mpLostSanctuary.addTile(0.537,0.83,1,[18,20], Function(callBattle,enemy_shadow,"None","None","Sanctuary"), 1)
        mpLostSanctuary.addTile(0.537,0.93,sanctuaryScroll_(),[19], sanctuaryScroll, 0)
        mpLostSanctuary.addTile(0.487,0.53,ha_tricksters_(),[17], ha_tricksters, 0)
        mpLostSanctuary.addTile(0.587,0.53,annavereDetermine("icon"),[17], annavereInteraction, annavereDetermine("auto")) #22
        mpLostSanctuary.addTile(0.25,0.75,0,[4,24], nullInteraction, 0)
        mpLostSanctuary.addTile(0.2,0.7,1,[23,25,27], Function(callBattle,enemy_devil,"None","None","Sanctuary"), 1)
        mpLostSanctuary.addTile(0.235,0.61,0,[24,26], nullInteraction, 0)
        mpLostSanctuary.addTile(0.285,0.56,einyaDetermine("icon"),[25], einyaInteraction, einyaDetermine("auto"))
        mpLostSanctuary.addTile(0.15,0.75,5,[24,28], obv80, 0)
        mpLostSanctuary.addTile(0.11,0.82,0,[29,27], nullInteraction, 0)
        mpLostSanctuary.addTile(0.055,0.8,sanctuary_takal_(),[28], sanctuary_takal, 0)

        global mpCrossroadsNorth
        mpCrossroadsNorth = scrCrossroadsNorth()
        mpCrossroadsNorth.addTile(0.25,1.0,3,[1], leavetoWorldmap, 0)
        mpCrossroadsNorth.addTile(0.3,0.95,0,[0,2,13], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.35,0.9,5,[1,3,19], obv57,0)
        mpCrossroadsNorth.addTile(0.36,0.8,1,[2,4], Function(callBattle,enemy_fox,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.365,0.7,0,[3,5,45], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.375,0.6,1,[4,6], Function(callBattle,enemy_fox,enemy_fox,"None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.4,0.505,0,[5,7], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.45,0.45,0,[6,8], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.48,0.355,1,[7,9], Function(callBattle,enemy_fox,enemy_cat,"None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.51,0.265,0,[8,10], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.52,0.17,6,[9,11,39], obv61, 0) #10
        mpCrossroadsNorth.addTile(0.55,0.085,1,[10,12], Function(callBattle,enemy_cat,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.58,0.0,3,[11], citadelPass, 0)
        mpCrossroadsNorth.addTile(0.27,0.86,0,[1,14], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.215,0.82,1,[13,15,46], Function(callBattle,enemy_cat,enemy_fox,"None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.16,0.8,6,[14,16], obv60, 0)
        mpCrossroadsNorth.addTile(0.105,0.77,0,[15,17], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.05,0.75,1,[16,18], Function(callBattle,enemy_fox,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.0,0.78,3,[17], adamePass, 0)
        mpCrossroadsNorth.addTile(0.4,0.865,0,[2,20], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.445,0.82,0,[19,21], nullInteraction, 0) #20
        mpCrossroadsNorth.addTile(0.485,0.74,0,[20,22], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.53,0.69,1,[21,23], Function(callBattle,enemy_cat,enemy_cat,"None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.575,0.64,0,[22,24], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.62,0.59,4,[23,25,31], obv58, 0)
        mpCrossroadsNorth.addTile(0.64,0.5,0,[24,26], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.675,0.42,1,[25,27], Function(callBattle,enemy_fox,enemy_fox,enemy_fox,"Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.71,0.34,0,[26,28], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.745,0.26,1,[27,29], Function(callBattle,enemy_cat,enemy_cat,"None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.76,0.16,0,[29,30], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.795,0.075,1,[29], Function(callBattle,enemy_succubus,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.665,0.65,0,[24,32], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.71,0.71,0,[31,33], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.755,0.77,1,[32,34], Function(callBattle,enemy_mayuri,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.8,0.71,0,[33,35], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.855,0.73,1,[34,36], Function(callBattle,enemy_mayuri,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.9,0.67,0,[35,37], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.945,0.61,5,[36,38], obv59, 0)
        mpCrossroadsNorth.addTile(1.0,0.635,3,[37], parivaraPass, 0)
        mpCrossroadsNorth.addTile(0.465,0.16,0,[10,40], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.41,0.175,1,[39,41], Function(callBattle,enemy_jarita,enemy_jarita,"None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.375,0.1,croN_sidequest_(),[40,42,43], croN_sidequest, 0)
        mpCrossroadsNorth.addTile(0.385,0.0,0,[41], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.32,0.08,1,[41,44], Function(callBattle,enemy_jarita,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.275,0.14,croN_markingJarita_(),[43], croN_markingJarita, 0)
        mpCrossroadsNorth.addTile(0.31,0.71,0,[4,46], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.255,0.745,1,[14,45,47], Function(callBattle,enemy_shadow,"None","None","Crossroads"), 1)
        mpCrossroadsNorth.addTile(0.24,0.65,0,[46,48], nullInteraction, 0)
        mpCrossroadsNorth.addTile(0.185,0.605,croN_sidequest2_(),[47], croN_sidequest2, 0)

        global mpAdameCrossing
        mpAdameCrossing = scrAdameCrossing()
        mpAdameCrossing.addTile(0.5,1.0,3,[1], leavetoWorldmap, 0)
        mpAdameCrossing.addTile(0.45,0.95,0,[0,2], nullInteraction, 0)
        mpAdameCrossing.addTile(0.4,0.9,1,[1,3], Function(callBattle,enemy_phantom,"None","None","AdameCrossing"), 1)
        mpAdameCrossing.addTile(0.355,0.83,0,[2,4], nullInteraction, 0)
        mpAdameCrossing.addTile(0.3,0.813,1,[3,5], Function(callBattle,enemy_phantom,enemy_dancer,enemy_phantom,"AdameCrossing"), 1)
        mpAdameCrossing.addTile(0.245,0.79,0,[4,6,20], nullInteraction, 0)  #5
        mpAdameCrossing.addTile(0.25,0.69,0,[5,7], nullInteraction, 0)
        mpAdameCrossing.addTile(0.3,0.64,5,[6,8], obv8, 0)
        mpAdameCrossing.addTile(0.35,0.61,1,[7,9], Function(callBattle,enemy_phantom,enemy_phantom,"None","AdameCrossing"), 1)
        mpAdameCrossing.addTile(0.4,0.57,0,[8,10], nullInteraction, 0)
        mpAdameCrossing.addTile(0.45,0.53,1,[9,11], Function(callBattle,enemy_dancer,"None","None","AdameCrossing"), 1) #10
        mpAdameCrossing.addTile(0.5,0.49,0,[10,12], nullInteraction, 0)
        mpAdameCrossing.addTile(0.55,0.45,1,[11,13,12], Function(callBattle,enemy_phantom,enemy_phantom,"None","AdameCrossing"), 1)
        mpAdameCrossing.addTile(0.6,0.41,5,[12,14], obv9, 0)
        mpAdameCrossing.addTile(0.725,0.38,aditiDetermineTile("icon"),[13,15], aditiInteraction, aditiDetermineTile("auto"))
        mpAdameCrossing.addTile(0.78,0.365,1,[14,16], Function(callBattle,enemy_dancer,enemy_dancer,"None","AdameCrossing"), 1)
        mpAdameCrossing.addTile(0.835,0.355,0,[15,17], nullInteraction, 0)
        mpAdameCrossing.addTile(0.89,0.365,3,[16], cisternPass, 0)
        mpAdameCrossing.addTile(0.58,0.54,0,[12,19], nullInteraction, 0)
        mpAdameCrossing.addTile(0.63,0.575,annavereDetermine("icon"),[18], annavereInteraction, annavereDetermine("auto"))
        mpAdameCrossing.addTile(0.19,0.77,1,[5,21], Function(callBattle,enemy_phantom,enemy_phantom,"None","AdameCrossing"), 1)#20
        mpAdameCrossing.addTile(0.14,0.72,0,[20,22], nullInteraction, 0)
        mpAdameCrossing.addTile(0.085,0.71,adameSideQuest_(),[21], adameSideQuest, 0)

        global mpCistern
        mpCistern = scrCistern()
        mpCistern.addTile(0.5,1.0, 3,[1], leavetoWorldmap, 0)
        mpCistern.addTile(0.52,0.9, 5, [0,2,5], obv20, 0)
        mpCistern.addTile(0.465,0.89, 1, [1,3], Function(callBattle,enemy_phantom,enemy_phantom,"None","Cistern"), 1)
        mpCistern.addTile(0.41,0.88, 0, [2,4], nullInteraction, 0)
        mpCistern.addTile(0.355,0.9, 0, [3,5], nullInteraction, 0)
        mpCistern.addTile(0.3,0.89, 1, [4,6], Function(callBattle,enemy_shadow,enemy_phantom,enemy_shadow,"Cistern"), 1) #5
        mpCistern.addTile(0.25,0.85, 5, [5,7,9], obv21, 0)
        mpCistern.addTile(0.205,0.905, 1, [6,8], Function(callBattle,enemy_phantom,"None","None","Cistern"), 1)
        mpCistern.addTile(0.24,0.98, cisternSideQuest_(), [7], cisternSideQuest, 0)
        mpCistern.addTile(0.28,0.765, 0, [6,10], nullInteraction, 0)
        mpCistern.addTile(0.3175,0.69, 0, [9,11,12], nullInteraction, 0) #10
        mpCistern.addTile(0.33,0.59, takalDetermine("icon"), [10], takalInteraction, takalDetermine("auto"))
        mpCistern.addTile(0.3725,0.7, 0, [10,13], nullInteraction, 0)
        mpCistern.addTile(0.425,0.72, 1, [12,14], Function(callBattle,enemy_shadow,"None","None","Cistern"), 1)
        mpCistern.addTile(0.48,0.71, 5, [13], obv24, 0)
        mpCistern.addTile(0.575,0.9, 0, [1,16], nullInteraction, 0) #15
        mpCistern.addTile(0.63,0.89, 1, [15,17],Function(callBattle,enemy_phantom,enemy_phantom,"None","Cistern"), 1)
        mpCistern.addTile(0.685,0.88, 0, [16,18], nullInteraction, 0)
        mpCistern.addTile(0.74,0.9, 0, [17,19,21], nullInteraction, 0)
        mpCistern.addTile(0.795,0.88, 1, [18,20], Function(callBattle,enemy_shadow,enemy_phantom,"None","Cistern"), 1)
        mpCistern.addTile(0.844,0.83, 5, [19], obv23, 0)
        mpCistern.addTile(0.75,0.8, 5, [18,22], obv22, 0)
        mpCistern.addTile(0.73,0.71, 1, [21,23,24], Function(callBattle,enemy_phantom,enemy_shadow,enemy_phantom,"Cistern"), 1)
        mpCistern.addTile(0.74,0.61, aditiDetermineTile("icon"), [22], aditiInteraction, aditiDetermineTile("auto"))
        mpCistern.addTile(0.675,0.725, 0, [22,25], nullInteraction, 0)
        mpCistern.addTile(0.62,0.74, 0, [24], nullInteraction, 0) #25

        global mpCitadel
        mpCitadel = scrCitadel()
        mpCitadel.addTile(0.47,1.0,3,[1], leavetoWorldmap, 0)
        mpCitadel.addTile(0.46,0.9,0,[0,2,3,21], nullInteraction, 0)
        mpCitadel.addTile(0.4075,0.89,1,[1,4], Function(callBattle,enemy_shadow,enemy_shadow,"None","Citadel"), 1)
        mpCitadel.addTile(0.5125,0.91,0,[1,14], nullInteraction, 0)
        mpCitadel.addTile(0.355,0.9,0,[2,5,7], nullInteraction, 0)
        mpCitadel.addTile(0.35,0.805,1,[4,6], Function(callBattle,enemy_shadow,enemy_asuri,"None","Citadel"), 1) #5
        mpCitadel.addTile(0.295,0.81,aditiDetermineTile("icon"),[5], aditiInteraction, aditiDetermineTile("auto"))
        mpCitadel.addTile(0.35,0.995,5,[4,8], obv25, 0)
        mpCitadel.addTile(0.2975,0.98,1,[7,9], Function(callBattle,enemy_asuri,enemy_devil,enemy_asuri,"Citadel"), 1)
        mpCitadel.addTile(0.245,1.0,0,[8,10], nullInteraction, 0)
        mpCitadel.addTile(0.195,0.98,0,[9,11], nullInteraction, 0)
        mpCitadel.addTile(0.145,1.0,1,[10,12], Function(callBattle,enemy_shadow,enemy_devil,"None","Citadel"), 1)
        mpCitadel.addTile(0.095,0.98,0,[11,13], nullInteraction, 0)
        mpCitadel.addTile(0.0425,1.0,2,[12], npc_3, 0)
        mpCitadel.addTile(0.5625,0.93,0,[3,15], nullInteraction, 0)
        mpCitadel.addTile(0.6125,0.91,1,[14,16,27], Function(callBattle,enemy_succubus,"None","None","Citadel"), 1) #15
        mpCitadel.addTile(0.665,0.9,0,[15,17], nullInteraction, 0)
        mpCitadel.addTile(0.715,0.89,5,[16,18], obv28, 0)
        mpCitadel.addTile(0.77,0.87,1,[17,19], Function(callBattle,enemy_devil,enemy_shadow,enemy_asuri,"Citadel"), 1)
        mpCitadel.addTile(0.825,0.85,0,[18,20,29], nullInteraction, 0)
        mpCitadel.addTile(0.86,0.77,ka_astrologer_(),[19], ka_astrologer, 0) #20
        mpCitadel.addTile(0.47,0.805,aditiDetermineTile2("icon"),[1,22], aditiInteraction2, aditiDetermineTile2("auto"))
        mpCitadel.addTile(0.475,0.71,5,[21,24,23,25], obv26, 0)
        mpCitadel.addTile(0.47,0.615,3,[22], aatmaonPass, 0)
        mpCitadel.addTile(0.42,0.715,1,[22], Function(callBattle,enemy_shadow,enemy_devil,"None","Citadel"), 1)
        mpCitadel.addTile(0.53,0.71,1,[22,26], Function(callBattle,enemy_asuri,enemy_asuri,"None","Citadel"), 1)
        mpCitadel.addTile(0.55,0.8,5,[25,27], obv27, 0)
        mpCitadel.addTile(0.6025,0.8175,0,[26,28,15], nullInteraction, 0)
        mpCitadel.addTile(0.61,0.715,nishaDetermine("icon"),[27], nishaInteraction, nishaDetermine("auto"))
        mpCitadel.addTile(0.835,0.95,5,[19,30,31], obv109, 0)
        mpCitadel.addTile(0.7875,1.0,1,[29,32], Function(callBattle,enemy_asuri,"None","None","Citadel"), 1)
        mpCitadel.addTile(0.89,0.96,1,[29,33],Function(callBattle,enemy_asuri,"None","None","Citadel"), 1)
        mpCitadel.addTile(0.735,1.0,citadelSideQuest_(),[30], citadelSideQuest, 0) #
        mpCitadel.addTile(0.945,0.97,0,[31,34], nullInteraction, 0)
        mpCitadel.addTile(0.95,0.865,citadelShopkeeper_(),[33], citadelShopkeeper, 0)

        global mpAatmaon
        mpAatmaon = scrAatmaon()
        mpAatmaon.addTile(0.32,1.0,3,[1], leavetoWorldmap, 0)
        mpAatmaon.addTile(0.31,0.9,0,[0,2], nullInteraction, 0)
        mpAatmaon.addTile(0.33,0.8,1,[1,3], Function(callBattle,enemy_necromancer,"None","None","Aatmaon"), 1)
        mpAatmaon.addTile(0.32,0.7,aatmaonAstrologer_(),[2,4,5], aatmaonAstrologer, 0)
        mpAatmaon.addTile(0.28,0.63,0,[3,16], nullInteraction, 0)
        mpAatmaon.addTile(0.36,0.63,5,[3,6], obv1, 0) #5
        mpAatmaon.addTile(0.415,0.68,1,[5,7], Function(callBattle,enemy_necromancer,"None","None","Aatmaon"), 1)
        mpAatmaon.addTile(0.47,0.71,0,[6,8], nullInteraction, 0)
        mpAatmaon.addTile(0.525,0.74,5,[7,9], obv2, 0)
        mpAatmaon.addTile(0.58,0.73,1,[8,10], Function(callBattle,enemy_dancer,enemy_dancer,enemy_dancer,"Aatmaon"), 1)
        mpAatmaon.addTile(0.635,0.72,0,[9,11], nullInteraction, 0) #10
        mpAatmaon.addTile(0.69,0.7,1,[10,12], Function(callBattle,enemy_necromancer,enemy_undead,enemy_undead,"Aatmaon"), 1)
        mpAatmaon.addTile(0.745,0.66,0,[11,13], nullInteraction, 0)
        mpAatmaon.addTile(0.8,0.62,1,[12,14], Function(callBattle,enemy_undead,enemy_undead,enemy_undead,"Aatmaon"), 1)
        mpAatmaon.addTile(0.855,0.58,0,[13,15], nullInteraction, 0)
        mpAatmaon.addTile(0.91,0.54,aatmaonScroll_(),[14], aatmaonScroll, 0) #15
        mpAatmaon.addTile(0.23,0.58,1,[4,17,20], Function(callBattle,enemy_necromancer,enemy_necromancer,"None","Aatmaon"), 1)
        mpAatmaon.addTile(0.175,0.55,6,[16,18], saveInteraction, 0)
        mpAatmaon.addTile(0.12,0.58,0,[17,19], nullInteraction, 0)
        mpAatmaon.addTile(0.065,0.56,aditiDetermineTile("icon"),[18], aditiInteraction, aditiDetermineTile("auto"))
        mpAatmaon.addTile(0.26,0.49,5,[16,21], obv3, 0)
        mpAatmaon.addTile(0.28,0.39,1,[20,22], Function(callBattle,enemy_dancer,enemy_necromancer,enemy_dancer,"Aatmaon"), 1)
        mpAatmaon.addTile(0.335,0.36,0,[21,23], nullInteraction, 0)
        mpAatmaon.addTile(0.36,0.455,1,[22,24], Function(callBattle,enemy_dancer,enemy_dancer,enemy_dancer,"Aatmaon"), 1)
        mpAatmaon.addTile(0.415,0.48,0,[23,25], nullInteraction, 0)
        mpAatmaon.addTile(0.47,0.455,aatmaonMiniboss_(),[24], aatmaonMiniboss, 0)
        mpAatmaon.addTile(0.715,0.2,0,[27], nullInteraction, 0)
        mpAatmaon.addTile(0.77,0.21,kamalaDetermine("icon"),[26,28], kamalaInteraction, kamalaDetermine("auto"))
        mpAatmaon.addTile(0.825,0.22,0,[27,29], nullInteraction, 0)
        mpAatmaon.addTile(0.88,0.2,boss_6_(),[28],boss_6, 0)

        global mpFalls
        mpFalls = scrFalls()
        mpFalls.addTile(0.0,0.95,3,[1], leavetoWorldmap, 0)
        mpFalls.addTile(0.06,0.94,0,[0,2],nullInteraction,0)
        mpFalls.addTile(0.12,0.93,0,[1,3],nullInteraction,0)
        mpFalls.addTile(0.18,0.95,1,[2,4],Function(callBattle,enemy_mayuri,"None","None","Falls"), 1)
        mpFalls.addTile(0.24,0.94,5,[3,5],obv29,0)
        mpFalls.addTile(0.30,0.93,1,[4,6,20],nullInteraction,0)
        mpFalls.addTile(0.36,0.94,0,[5,7],nullInteraction,0)
        mpFalls.addTile(0.42,0.96,1,[6,8,23],Function(callBattle,enemy_mayuri,enemy_mayuri,"None","Falls"), 1)
        mpFalls.addTile(0.48,0.95,0,[7,9],nullInteraction,0)
        mpFalls.addTile(0.54,0.94,hansaDetermine("icon"),[8,10],hansaInteraction,hansaDetermine("auto"))
        mpFalls.addTile(0.60,0.93,5,[9,11,18],obv30,0) #10
        mpFalls.addTile(0.66,0.95,1,[10,12],Function(callBattle,enemy_cat,"None","None","Falls"), 1)
        mpFalls.addTile(0.72,0.94,0,[11,13],nullInteraction,0)
        mpFalls.addTile(0.78,0.96,0,[12,14],nullInteraction,0)
        mpFalls.addTile(0.84,0.95,5,[13,15,27],obv31,0)
        mpFalls.addTile(0.90,0.94,1,[14,16],Function(callBattle,enemy_cat,"None","None","Falls"), 1)
        mpFalls.addTile(0.96,0.93,0,[15,17],nullInteraction,0)
        mpFalls.addTile(1.0,1.0,3,[16],underfallsPass,0)
        mpFalls.addTile(0.63,0.845,1,[10,19],Function(callBattle,enemy_mayuri,enemy_mayuri,enemy_mayuri,"Falls"), 1)
        mpFalls.addTile(0.68,0.795,fallsScroll_(),[18],fallsScroll,0)
        mpFalls.addTile(0.32,0.835,0,[5,21],nullInteraction,0)
        mpFalls.addTile(0.30,0.74,1,[20,22],Function(callBattle,enemy_cat,enemy_cat,"None","Falls"), 1)
        mpFalls.addTile(0.32,0.645,2,[21],npc_4,0)
        mpFalls.addTile(0.425,0.86,0,[7,24],nullInteraction,0)
        mpFalls.addTile(0.445,0.765,5,[23,25],obv33,0)
        mpFalls.addTile(0.43,0.67,1,[24,26],Function(callBattle,enemy_mayuri,enemy_cat,"None","Falls"), 1)
        mpFalls.addTile(0.445,0.575,fallsSideQuest_(),[25],fallsSideQuest,0)
        mpFalls.addTile(0.835,0.85,0,[14,28],nullInteraction,0)
        mpFalls.addTile(0.84,0.75,0,[27,29,30,31],nullInteraction,0)
        mpFalls.addTile(0.84,0.65,prishaDetermine("icon"),[28],prishaInteraction,prishaDetermine("auto"))
        mpFalls.addTile(0.895,0.74,2,[28],npc_5,0)
        mpFalls.addTile(0.785,0.76,2,[28],npc_6,0)

        global mpUnderfalls
        mpUnderfalls = scrUnderfalls()
        mpUnderfalls.addTile(0.52,0.65,3,[1], leavetoWorldmap, 0)
        mpUnderfalls.addTile(0.53,0.76,0,[0,2,19], nullInteraction, 0)
        mpUnderfalls.addTile(0.54,0.87,1,[1,3,13], Function(callBattle,enemy_darkmage,enemy_darkmage,"None","Underfalls"), 1)
        mpUnderfalls.addTile(0.525,0.98,5,[2,4,10], obv90, 0)
        mpUnderfalls.addTile(0.465,0.99,0,[3,5], nullInteraction, 0)
        mpUnderfalls.addTile(0.405,0.98,5,[4,6], obv91, 0)
        mpUnderfalls.addTile(0.345,0.99,1,[5,7], Function(callBattle,enemy_necromancer,enemy_darkmage,"None","Underfalls"), 1)
        mpUnderfalls.addTile(0.285,0.98,0,[6,8], nullInteraction, 0)
        mpUnderfalls.addTile(0.225,0.99,1,[7,9], Function(callBattle,enemy_asuri,enemy_darkmage,"None","Underfalls"), 1)
        mpUnderfalls.addTile(0.165,0.98,determineNiija("icon"),[8], niijaInteraction, determineNiija("auto"))
        mpUnderfalls.addTile(0.585,0.99,0,[3,11], nullInteraction, 0)
        mpUnderfalls.addTile(0.645,0.98,1,[10,12], Function(callBattle,enemy_darkmage,"None","None","Underfalls"), 1)
        mpUnderfalls.addTile(0.705,0.97,underfallsScroll_(),[11], underfallsScroll, 0)
        mpUnderfalls.addTile(0.48,0.87,0,[2,14], nullInteraction, 0)
        mpUnderfalls.addTile(0.42,0.85,1,[13,15], Function(callBattle,enemy_asuri,enemy_asuri,"None","Underfalls"), 1)
        mpUnderfalls.addTile(0.36,0.83,5,[14,16,18], obv92, 0)
        mpUnderfalls.addTile(0.30,0.84,0,[15,17], nullInteraction, 0)
        mpUnderfalls.addTile(0.24,0.83,underfallsMarking_(),[16], underfallsMarking, 0)
        mpUnderfalls.addTile(0.38,0.735,ei_heart_(),[15], ei_heart, 0)
        mpUnderfalls.addTile(0.59,0.76,0,[1,20], nullInteraction, 0)
        mpUnderfalls.addTile(0.65,0.78,0,[19,21], nullInteraction, 0)
        mpUnderfalls.addTile(0.71,0.8,1,[20,22], Function(callBattle,enemy_necromancer,enemy_darkmage,"None","Underfalls"), 1)
        mpUnderfalls.addTile(0.77,0.82,0,[21,23,24], nullInteraction, 0)
        mpUnderfalls.addTile(0.79,0.725,syllDetermine("icon"),[22], syllInteraction, syllDetermine("auto"))
        mpUnderfalls.addTile(0.83,0.84,5,[22,25], obv93, 0)
        mpUnderfalls.addTile(0.89,0.82,1,[24,26], Function(callBattle,enemy_darkmage,"None","None","Underfalls"), 1)
        mpUnderfalls.addTile(0.95,0.8,0,[25,27], nullInteraction, 0)
        mpUnderfalls.addTile(1.0,0.85,3,[26], cavernsPass, 0)

        global mpCaverns
        mpCaverns = scrCaverns()
        mpCaverns.addTile(0.0,0.75,3,[5], leavetoWorldmap, 0)
        mpCaverns.addTile(0.135,0.61,5,[2,14,26], obv14, 0)
        mpCaverns.addTile(0.185,0.64,1,[1,3], Function(callBattle,enemy_slime,"None","None","Caverns"), 1)
        mpCaverns.addTile(0.24,0.62,0,[2,4,27], nullInteraction, 0)
        mpCaverns.addTile(0.295,0.6,1,[3], Function(callBattle,enemy_slime,enemy_slime,"None","Caverns"), 1)
        mpCaverns.addTile(0.06,0.77,0,[0,6], nullInteraction, 0) #5
        mpCaverns.addTile(0.11,0.81,0,[5,7,14], nullInteraction, 0)
        mpCaverns.addTile(0.16,0.85,1,[6,8], Function(callBattle,enemy_ogre,"None","None","Caverns"), 1)
        mpCaverns.addTile(0.21,0.89,0,[7,9], nullInteraction, 0)
        mpCaverns.addTile(0.22,0.99,1,[8,10,11], Function(callBattle,enemy_slime,enemy_ogre,"None","Caverns"), 1)
        mpCaverns.addTile(0.165,0.98,5,[9,12], obv15, 0) #10
        mpCaverns.addTile(0.275,0.97,0,[9,15], nullInteraction, 0)
        mpCaverns.addTile(0.11,0.96,1,[10,13], Function(callBattle,enemy_ogre,enemy_ogre,enemy_ogre,"Caverns"), 1)
        mpCaverns.addTile(0.055,0.94,0,[12], nullInteraction, 0)
        mpCaverns.addTile(0.125,0.71,0,[1,6], nullInteraction, 0)
        mpCaverns.addTile(0.33,0.96,0,[11,16], nullInteraction, 0)
        mpCaverns.addTile(0.385,0.97,1,[15,17], Function(callBattle,enemy_slime,enemy_ogre,"None","Caverns"), 1)
        mpCaverns.addTile(0.44,0.96,0,[16,18], nullInteraction, 0)
        mpCaverns.addTile(0.495,0.95,5,[17,19], obv16, 0)
        mpCaverns.addTile(0.5,0.85,1,[18,20], Function(callBattle,enemy_ogre,enemy_ogre,"None","Caverns"), 1)
        mpCaverns.addTile(0.49,0.75,0,[19,21,28], nullInteraction, 0) #20
        mpCaverns.addTile(0.5,0.65,0,[20,22], nullInteraction, 0)
        mpCaverns.addTile(0.555,0.63,1,[21,23,32], Function(callBattle,enemy_slime,enemy_slime,enemy_slime,"Caverns"), 1)
        mpCaverns.addTile(0.61,0.62,5,[22,24], obv18, 0)
        mpCaverns.addTile(0.66,0.585,1,[23,25], Function(callBattle,enemy_ogre,enemy_ogre,"None","Caverns"), 1)
        mpCaverns.addTile(0.635,0.49,3,[24], trenchPass, 0)
        mpCaverns.addTile(0.115,0.515,0,[1], nullInteraction, 0)
        mpCaverns.addTile(0.225,0.52,cavernSideQuest1_(),[3], cavernSideQuest1, 0) #7
        mpCaverns.addTile(0.435,0.74,5,[20,29], obv17, 0)
        mpCaverns.addTile(0.37,0.76,1,[28,30], Function(callBattle,enemy_ogre,"None","None","Caverns"), 1)
        mpCaverns.addTile(0.315,0.78,0,[29,31], nullInteraction, 0)
        mpCaverns.addTile(0.26,0.76,cavernSideQuest_(),[30], cavernSideQuest, 0)
        mpCaverns.addTile(0.57,0.73,0,[22,33], nullInteraction, 0)
        mpCaverns.addTile(0.59,0.825,0,[32,34], nullInteraction, 0)
        mpCaverns.addTile(0.645,0.83,1,[33,35], Function(callBattle,enemy_slime,enemy_slime,"None","Caverns"), 1)
        mpCaverns.addTile(0.652,0.93,0,[34,36], nullInteraction, 0)
        mpCaverns.addTile(0.71,0.92,5,[35,37], obv19, 0)
        mpCaverns.addTile(0.765,0.93,1,[36,38], Function(callBattle,enemy_ogre,enemy_ogre,"None","Caverns"), 1)
        mpCaverns.addTile(0.82,0.92,0,[37,39], nullInteraction, 0)
        mpCaverns.addTile(0.88,0.9,0,[38,40], nullInteraction, 0)
        mpCaverns.addTile(0.87,0.8,lydriaDetermine("icon"),[39,41], lydriaInteraction, lydriaDetermine("auto"))
        mpCaverns.addTile(0.88,0.7,1,[40,42], Function(callBattle,enemy_slime,enemy_ogre,enemy_slime,"Caverns"), 1)
        mpCaverns.addTile(0.89,0.6,0,[41,43,44], nullInteraction, 0)
        mpCaverns.addTile(0.85,0.525,3,[42], courtPass, 0)
        mpCaverns.addTile(0.945,0.61,0,[42,45], nullInteraction, 0)
        mpCaverns.addTile(1.0,0.585,syllDetermine("icon"),[44], syllInteraction, syllDetermine("auto"))

        global mpMadyaCourt
        mpMadyaCourt = scrMadhyaCourt()
        mpMadyaCourt.addTile(1.0,1.0,3,[1], leavetoWorldmap, 0)
        mpMadyaCourt.addTile(0.945,0.99,0,[0,2], nullInteraction, 0)
        mpMadyaCourt.addTile(0.89,0.98,0,[1,3], nullInteraction, 0)
        mpMadyaCourt.addTile(0.835,0.99,0,[2,4], nullInteraction, 0)
        mpMadyaCourt.addTile(0.78,0.97,5,[3,5], obv52, 0)
        mpMadyaCourt.addTile(0.77,0.875,1,[4,6,17], Function(callBattle,enemy_darkmage,"None","None","MadhyaCourt"), 1)    #5
        mpMadyaCourt.addTile(0.715,0.865,0,[5,7], nullInteraction, 0)
        mpMadyaCourt.addTile(0.655,0.86,0,[6,8,44], nullInteraction, 0)
        mpMadyaCourt.addTile(0.595,0.87,1,[7,9], Function(callBattle,enemy_darkmage,enemy_necromancer,"None","MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.54,0.875,0,[8,10], nullInteraction, 0)
        mpMadyaCourt.addTile(0.485,0.88,5,[9,11,48], obv53, 0) #10
        mpMadyaCourt.addTile(0.43,0.87,1,[10,12],Function(callBattle,enemy_darkmage,enemy_necromancer,enemy_darkmage,"MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.375,0.865,6,[11,13,21], saveInteraction, 0)
        mpMadyaCourt.addTile(0.32,0.87,0,[12,14], nullInteraction, 0)
        mpMadyaCourt.addTile(0.265,0.875,1,[13,15,51], Function(callBattle,enemy_necromancer,"None","None","MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.21,0.88,0,[14,16], nullInteraction, 0) #15
        mpMadyaCourt.addTile(0.155,0.87,5,[15,41,46], obv54, 0)
        mpMadyaCourt.addTile(0.79,0.78,0,[5,18], nullInteraction, 0)
        mpMadyaCourt.addTile(0.775,0.68,6,[17,19], obv56, 0)
        mpMadyaCourt.addTile(0.72,0.69,1,[18,20], Function(callBattle,enemy_darkmage,enemy_darkmage,"None","MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.725,0.59,5,[19], m20_, 0) #20 ################# -> 39
        mpMadyaCourt.addTile(0.385,0.765,lydriaDetermine3("icon"),[12,22,23,28], lydriaInteraction3, lydriaDetermine3("auto"))
        mpMadyaCourt.addTile(0.33,0.745,0,[21,24], nullInteraction, 0)
        mpMadyaCourt.addTile(0.44,0.745,0,[21,26], nullInteraction, 0)
        mpMadyaCourt.addTile(0.275,0.725,0,[22,25], Function(callBattle,enemy_darkmage,enemy_darkmage,enemy_darkmage,"MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.285,0.625,madhyaKey1Hole_(),[24], madhyaKey1Hole, 0)
        mpMadyaCourt.addTile(0.495,0.725,0,[23,27], Function(callBattle,enemy_darkmage,enemy_darkmage,enemy_darkmage,"MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.485,0.625,madhyaKey2Hole_(),[26], madhyaKey2Hole, 0)
        mpMadyaCourt.addTile(0.385,0.665,0,[21,29], nullInteraction, 0)
        mpMadyaCourt.addTile(0.392,0.565,boss_3_(),[28], boss_3, 0)
        mpMadyaCourt.addTile(0.24,0.35,5,[31], m30_, 0) #30 ###################
        mpMadyaCourt.addTile(0.295,0.35,0,[30,32], nullInteraction, 0)
        mpMadyaCourt.addTile(0.35,0.35,1,[31,33], Function(callBattle,enemy_mayuri,"None","None","MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.405,0.35,5,[32,34], obv55, 0)
        mpMadyaCourt.addTile(0.46,0.35,1,[33,35,40], Function(callBattle,enemy_mayuri,"None","None","MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.515,0.35,1,[34,36,40], Function(callBattle,enemy_mayuri,"None","None","MadhyaCourt"), 1)  #35
        mpMadyaCourt.addTile(0.57,0.35,0,[35,37], nullInteraction, 0)
        mpMadyaCourt.addTile(0.625,0.35,1,[36,38], Function(callBattle,enemy_mayuri,"None","None","MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.68,0.35,0,[37,39], nullInteraction, 0)
        mpMadyaCourt.addTile(0.735,0.35,5,[38], m39_, 9) ##################### -> 16
        mpMadyaCourt.addTile(0.487,0.26,lydriaDetermine("icon"),[34,35], lydriaInteraction, lydriaDetermine("auto")) #40
        mpMadyaCourt.addTile(0.1,0.87,0,[16,42], nullInteraction, 0)
        mpMadyaCourt.addTile(0.045,0.89,1,[41,43], Function(callBattle,enemy_necromancer,enemy_necromancer,"None","MadhyaCourt"), 1)
        mpMadyaCourt.addTile(0.0,0.955,madhyaKey1_(),[42], madhyaKey1, 0)
        mpMadyaCourt.addTile(0.64,0.765,0,[7,45], nullInteraction, 0)
        mpMadyaCourt.addTile(0.59,0.73, madhyaTome_(),[44], madhyaTome, 0) #45
        mpMadyaCourt.addTile(0.165,0.77,0,[16,47], nullInteraction, 0)
        mpMadyaCourt.addTile(0.175,0.67,madhyaKey2_(),[46], madhyaKey2, 0)
        mpMadyaCourt.addTile(0.495,0.98,0,[10,49,50], nullInteraction, 0)
        mpMadyaCourt.addTile(0.55,1.0,0,[48], nullInteraction, 0)
        mpMadyaCourt.addTile(0.44,1.0,0,[48], nullInteraction, 0)
        mpMadyaCourt.addTile(0.27,0.975,lydriaDetermine2("icon"),[14], lydriaInteraction2, lydriaDetermine2("auto"))

        global mpWarriorRest
        mpWarriorRest = scrWarriorRest()
        mpWarriorRest.addTile(0.0,1.0,3,[1], leavetoWorldmap, 0)
        mpWarriorRest.addTile(0.04,0.935,0,[0,2], nullInteraction, 0)
        mpWarriorRest.addTile(0.0825,0.88,0,[1,3], nullInteraction, 0)
        mpWarriorRest.addTile(0.125,0.935,1,[2,4], Function(callBattle,enemy_dancer,"None","None","WarriorRest"), 1)
        mpWarriorRest.addTile(0.175,0.945,0,[3,5], nullInteraction, 0)
        mpWarriorRest.addTile(0.225,0.935,0,[4,6], nullInteraction, 0) #5
        mpWarriorRest.addTile(0.275,0.925,1,[5,7], Function(callBattle,enemy_dancer,enemy_berserker,enemy_dancer,"WarriorRest"), 1)
        mpWarriorRest.addTile(0.285,0.83,5,[6,8,9,10], obv99, 0)
        mpWarriorRest.addTile(0.3,0.74,0,[7,11], nullInteraction, 0)
        mpWarriorRest.addTile(0.235,0.82,2,[7], npc_11, 0)
        mpWarriorRest.addTile(0.335,0.83,1,[7,21], Function(callBattle,enemy_berserker,enemy_dancer,"None","WarriorRest"), 1) #10
        mpWarriorRest.addTile(0.315,0.645,0,[8,12,16], nullInteraction, 0)
        mpWarriorRest.addTile(0.365,0.625,0,[11,13], Function(callBattle,enemy_cat,"None","None","WarriorRest"), 1)
        mpWarriorRest.addTile(0.415,0.605,5,[12,14], obv100, 0)
        mpWarriorRest.addTile(0.445,0.53,1,[13,15],Function(callBattle,enemy_cat,"None","None","WarriorRest"), 1)
        mpWarriorRest.addTile(0.4975,0.52,saanviDetermine("icon"),[14], saanviInteraction, saanviDetermine("auto"))
        mpWarriorRest.addTile(0.2625,0.645,0,[11,17], nullInteraction, 0)
        mpWarriorRest.addTile(0.2575,0.55,1,[16,18,19], Function(callBattle,enemy_asuri,enemy_asuri,"None","WarriorRest"), 1)
        mpWarriorRest.addTile(0.29,0.475,annavereDetermine("icon"),[17], annavereInteraction, annavereDetermine("auto"))
        mpWarriorRest.addTile(0.2025,0.55,0,[17,20], nullInteraction, 0)
        mpWarriorRest.addTile(0.16,0.605,restObservation_(),[19], restObservation, 0)  #20
        mpWarriorRest.addTile(0.3875,0.84,0,[10,22], nullInteraction, 0)
        mpWarriorRest.addTile(0.44,0.83,1,[21,23], Function(callBattle,enemy_dancer,enemy_dancer,enemy_dancer,"WarriorRest"), 1)
        mpWarriorRest.addTile(0.49,0.85,0,[22,24], nullInteraction, 0)
        mpWarriorRest.addTile(0.54,0.86,5,[23,25,28], obv101, 0)
        mpWarriorRest.addTile(0.585,0.91,1,[24,26], Function(callBattle,enemy_berserker,enemy_berserker,"None","WarriorRest"), 1) #25
        mpWarriorRest.addTile(0.63,0.96,0,[25,27], nullInteraction, 0)
        mpWarriorRest.addTile(0.68,1.0,3,[26], gorgePass, 0)
        mpWarriorRest.addTile(0.575,0.785,1,[24,29], Function(callBattle,enemy_dancer,"None","None","WarriorRest"), 1)
        mpWarriorRest.addTile(0.54,0.715,hansaDetermine("icon"),[28], hansaInteraction, hansaDetermine("auto"))

        global mpJalaDiya
        mpJalaDiya = scrJaladiya()
        mpJalaDiya.addTile(0.0,1.0,3,[1], leavetoWorldmap, 0)
        mpJalaDiya.addTile(0.055,0.96,0,[0,2], nullInteraction, 0)
        mpJalaDiya.addTile(0.11,0.98,1,[1,3], Function(callBattle,enemy_ogre,"None","None","JalaDiya"), 1)
        mpJalaDiya.addTile(0.1615,0.94,5,[2,4], obv42, 0)
        mpJalaDiya.addTile(0.215,0.95,0,[3,5], nullInteraction, 0)
        mpJalaDiya.addTile(0.2635,0.9,1,[4,6,21],  Function(callBattle,enemy_ogre,enemy_ogre,"None","JalaDiya"), 1)      #5
        mpJalaDiya.addTile(0.31,0.85,0,[5,7], nullInteraction, 0)
        mpJalaDiya.addTile(0.355,0.8,5,[6,8], obv43, 0)
        mpJalaDiya.addTile(0.41,0.75,hansaDetermine("icon"),[7,9,14], hansaInteraction, hansaDetermine("auto"))
        mpJalaDiya.addTile(0.455,0.68,0,[8,10], nullInteraction, 0)
        mpJalaDiya.addTile(0.5,0.61,5,[9,11], obv45, 0)  #10
        mpJalaDiya.addTile(0.51,0.505,1,[10,12],  Function(callBattle,enemy_thief,enemy_cat,enemy_thief,"JalaDiya"), 1)
        mpJalaDiya.addTile(0.55,0.43,0,[11,13], nullInteraction, 0)
        mpJalaDiya.addTile(0.595,0.37,3,[12], peakPass, 0)
        mpJalaDiya.addTile(0.43,0.85,1,[8,15],  Function(callBattle,enemy_cat,enemy_ogre,enemy_cat,"JalaDiya"), 1)     #14
        mpJalaDiya.addTile(0.45,0.95,5,[14,16,19], obv44, 0) #15
        mpJalaDiya.addTile(0.505,0.95,0,[15,17], nullInteraction, 0)
        mpJalaDiya.addTile(0.56,0.96,1,[16,18],  Function(callBattle,enemy_thief,"None","None","JalaDiya"), 1)
        mpJalaDiya.addTile(0.615,0.99,2,[17], npc_8, 0)
        mpJalaDiya.addTile(0.395,0.96,0,[15,20], nullInteraction, 0)
        mpJalaDiya.addTile(0.34,0.98,jaladiyaSideQuest_(),[19], jaladiyaSideQuest, 0) #20
        mpJalaDiya.addTile(0.24,0.805,saanviDetermine("icon"),[5], saanviInteraction, saanviDetermine("auto"))

        global mpJyoti
        mpJyoti = scrJyoti()
        mpJyoti.addTile(0.05,1.0,3,[1], leavetoWorldmap, 0)
        mpJyoti.addTile(0.105,0.99,0,[0,2], nullInteraction, 0)
        mpJyoti.addTile(0.16,0.98,0,[1,3], nullInteraction, 0)
        mpJyoti.addTile(0.215,0.97,0,[2,4], nullInteraction, 0)
        mpJyoti.addTile(0.245,0.885,5,[3,5], obv46, 0)
        mpJyoti.addTile(0.275,0.8,0,[4,6], nullInteraction, 0) #5
        mpJyoti.addTile(0.295,0.705,1,[5,7],  Function(callBattle,enemy_dragon,enemy_dragon,enemy_dragon,"Jyoti"), 1)
        mpJyoti.addTile(0.315,0.61,5,[6,8], obv47, 0)
        mpJyoti.addTile(0.345,0.525,jyotiEvent_(),[7,9], jyotiEvent, 1)
        mpJyoti.addTile(0.34,0.43,0,[8,10], nullInteraction, 0)
        mpJyoti.addTile(0.35,0.335,boss_4_(),[9,41], boss_4, 0) #10
        mpJyoti.addTile(0.525,0.61,0,[12], nullInteraction, 0)
        mpJyoti.addTile(0.565,0.68,0,[11,13], nullInteraction, 0)
        mpJyoti.addTile(0.615,0.715,1,[12,14], Function(callBattle,enemy_dragon,"None","None","Jyoti"), 1)
        mpJyoti.addTile(0.67,0.705,5,[13,15], obv48, 0)
        mpJyoti.addTile(0.71,0.63,0,[14,16], nullInteraction, 0) #15
        mpJyoti.addTile(0.75,0.565,1,[15,17], Function(callBattle,enemy_dragon,enemy_dragon,"None","Jyoti"), 1)
        mpJyoti.addTile(0.79,0.49,5,[16,18], obv49, 0)
        mpJyoti.addTile(0.83,0.415,1,[17,19], Function(callBattle,enemy_dragon,enemy_dragon,enemy_dragon,"Jyoti"), 1)
        mpJyoti.addTile(0.85,0.3225,0,[18,20], nullInteraction, 0)
        mpJyoti.addTile(0.84,0.2225,0,[19,21], nullInteraction, 0) #20
        mpJyoti.addTile(0.86,0.1225,1,[20,22,32], Function(callBattle,enemy_dragon,enemy_dragon,"None","Jyoti"), 1)
        mpJyoti.addTile(0.915,0.1425,0,[21,23], nullInteraction, 0)
        mpJyoti.addTile(0.965,0.1825,1,[22,24], Function(callBattle,enemy_dragon,"None","None","Jyoti"), 1)
        mpJyoti.addTile(0.965,0.2825,jyoti_writing_(),[23,25], jyoti_writing, 0)
        mpJyoti.addTile(0.955,0.3825,0,[24,26], nullInteraction, 0)
        mpJyoti.addTile(0.945,0.4825,5,[25,27], obv50, 0)
        mpJyoti.addTile(0.945,0.5825,1,[26,28], Function(callBattle,enemy_dragon,enemy_dragon,"None","Jyoti"), 1)
        mpJyoti.addTile(0.935,0.6825,0,[27,29], nullInteraction, 0)
        mpJyoti.addTile(0.925,0.7825,1,[28,30], Function(callBattle,enemy_dragon,"None","None","Jyoti"), 1)
        mpJyoti.addTile(0.915,0.8825,0,[29,31], nullInteraction, 0) #30
        mpJyoti.addTile(0.905,0.9825,sa_ribbon_(),[30], sa_ribbon, 0)
        mpJyoti.addTile(0.805,0.1225,0,[21,33], nullInteraction, 0) #32
        mpJyoti.addTile(0.75,0.1225,1,[32,34], Function(callBattle,enemy_dragon,"None","None","Jyoti"), 1)
        mpJyoti.addTile(0.695,0.1225,6,[33,35], saveInteraction, 0)
        mpJyoti.addTile(0.64,0.1225,6,[34,36], saveInteraction, 0)
        mpJyoti.addTile(0.585,0.1225,1,[35,37], Function(callBattle,enemy_dragon,enemy_dragon,"None","Jyoti"), 1)
        mpJyoti.addTile(0.53,0.1225,5,[36,38], obv51, 0)
        mpJyoti.addTile(0.475,0.1225,0,[37,39], nullInteraction, 0)
        mpJyoti.addTile(0.43,0.1725,1,[38,40], Function(callBattle,enemy_dragon,enemy_dragon,"None","Jyoti"), 1)
        mpJyoti.addTile(0.385,0.2225,0,[39,41], nullInteraction, 0)
        mpJyoti.addTile(0.335,0.2425,0,[10,40], nullInteraction, 0)

        global mpDeepWater
        mpDeepWater = scrDeepWater()
        mpDeepWater.addTile(0.55,1.0,3,[1], leavetoWorldmap, 0)
        mpDeepWater.addTile(0.54,0.9,6,[0,2,16], obv86, 0)
        mpDeepWater.addTile(0.49,0.86,0,[1,3], nullInteraction, 0)
        mpDeepWater.addTile(0.435,0.87,1,[2,4], Function(callBattle,enemy_mermaid,"None","None","DeepTrench"), 1)
        mpDeepWater.addTile(0.38,0.86,0,[3,5], nullInteraction, 0)
        mpDeepWater.addTile(0.325,0.85,5,[4,6,29], obv88, 0)
        mpDeepWater.addTile(0.33,0.75,0,[5,7], nullInteraction, 0)
        mpDeepWater.addTile(0.325,0.65,1,[6,8], Function(callBattle,enemy_mermaid,enemy_mayuri,"None","DeepTrench"), 1)
        mpDeepWater.addTile(0.34,0.55,0,[7,9], nullInteraction, 0)
        mpDeepWater.addTile(0.395,0.56,0,[8,10], nullInteraction, 0)
        mpDeepWater.addTile(0.45,0.55,5,[9,11,33], obv89, 0) #10
        mpDeepWater.addTile(0.505,0.54,1,[10,12], Function(callBattle,enemy_mermaid,enemy_mermaid,"None","DeepTrench"), 1)
        mpDeepWater.addTile(0.56,0.53,trenchMermaid_(),[11,13,26], trenchMermaid, 0)
        mpDeepWater.addTile(0.575,0.435,0,[12,14], nullInteraction, 0)
        mpDeepWater.addTile(0.6135,0.3625,0,[13,15,25], nullInteraction, 0)
        mpDeepWater.addTile(0.61,0.265,3,[14], stoneIslandPass, 0) #15
        mpDeepWater.addTile(0.59,0.86,0,[1,17], nullInteraction, 0)
        mpDeepWater.addTile(0.645,0.85,1,[16,18], Function(callBattle,enemy_mermaid,enemy_mermaid,enemy_mermaid,"DeepTrench"), 1)
        mpDeepWater.addTile(0.7,0.845,0,[17,19], nullInteraction, 0)
        mpDeepWater.addTile(0.755,0.83,0,[18,20], nullInteraction, 0)
        mpDeepWater.addTile(0.805,0.78,1,[19,21], Function(callBattle,enemy_mayuri,enemy_mayuri,"None","DeepTrench"), 1) #2-
        mpDeepWater.addTile(0.775,0.69,5,[20,22], obv87, 0)
        mpDeepWater.addTile(0.72,0.67,0,[21,23], nullInteraction, 0)
        mpDeepWater.addTile(0.665,0.65,1,[22,24], Function(callBattle,enemy_mayuri,enemy_mermaid,"None","DeepTrench"), 1)
        mpDeepWater.addTile(0.655,0.55,0,[23,25], nullInteraction, 0)
        mpDeepWater.addTile(0.64,0.45,1,[14,24,36], Function(callBattle,enemy_mayuri,"None","None","DeepTrench"), 1) #25
        mpDeepWater.addTile(0.57,0.63,0,[12,27], Function(callBattle,enemy_mermaid, enemy_mayuri,enemy_mermaid,"DeepTrench"), 1)
        mpDeepWater.addTile(0.565,0.73,0,[26,28], nullInteraction, 0)
        mpDeepWater.addTile(0.51,0.74,0,[27], acropolisPass, 0)
        mpDeepWater.addTile(0.27,0.84,0,[5,30], nullInteraction, 0)
        mpDeepWater.addTile(0.215,0.82,0,[29,31], Function(callBattle,enemy_mayuri,"None","None","DeepTrench"), 1) #30
        mpDeepWater.addTile(0.175,0.75,nishaDetermine("icon"),[30,32], nishaInteraction, nishaDetermine("auto"))
        mpDeepWater.addTile(0.17,0.65,syllDetermine("icon"),[31], syllInteraction, syllDetermine("auto"))
        mpDeepWater.addTile(0.44,0.45,0,[10,34], nullInteraction, 0)
        mpDeepWater.addTile(0.455,0.355,0,[33,35], nullInteraction, 0)
        mpDeepWater.addTile(0.51,0.365,7,[34], npc_10, 0)
        mpDeepWater.addTile(0.695,0.43,0,[25,37], nullInteraction, 0)
        mpDeepWater.addTile(0.75,0.41,0,[36], nullInteraction, 0)

        global mpAcropolis
        mpAcropolis = scrAcropolis()
        mpAcropolis.addTile(0.0,1.0,3,[1], leavetoWorldmap, 0)
        mpAcropolis.addTile(0.05,0.95,0,[0,2], nullInteraction, 0)
        mpAcropolis.addTile(0.095,0.89,1,[1,3], Function(callBattle,enemy_mermaid,enemy_mermaid,enemy_mermaid,"Acropolis"), 1)
        mpAcropolis.addTile(0.14,0.83,0,[2,4,42], nullInteraction, 0)
        mpAcropolis.addTile(0.195,0.84,1,[3,5],Function(callBattle,enemy_mermaid,enemy_devil,enemy_mermaid,"Acropolis"), 1)
        mpAcropolis.addTile(0.25,0.83,5,[4,6,25], obv4, 0) #5
        mpAcropolis.addTile(0.305,0.85,0,[5,7], nullInteraction, 0)
        mpAcropolis.addTile(0.36,0.82,1,[6,8], Function(callBattle,enemy_mermaid,"None","None","Acropolis"), 1)
        mpAcropolis.addTile(0.415,0.81,0,[7,9], nullInteraction, 0)
        mpAcropolis.addTile(0.47,0.82,0,[8,10], nullInteraction, 0)
        mpAcropolis.addTile(0.525,0.81,1,[9,11], Function(callBattle,enemy_devil,enemy_devil,enemy_devil,"Acropolis"), 1)  #10
        mpAcropolis.addTile(0.58,0.79,5,[10,12,16], obv5, 0)
        mpAcropolis.addTile(0.575,0.69,acropolisLeverRight_(),[11,13], acropolisLeverRight, 0)
        mpAcropolis.addTile(0.52,0.68,nishaDetermine("icon"),[12,14,15], nishaInteraction, nishaDetermine("auto"))
        mpAcropolis.addTile(0.515,0.58,boss_5_(),[13], boss_5, 0)
        mpAcropolis.addTile(0.465,0.69,acropolisLeverLeft_(),[13,47], acropolisLeverLeft, 0)  #15
        mpAcropolis.addTile(0.6,0.89,0,[11,17,30], nullInteraction, 0)
        mpAcropolis.addTile(0.655,0.88,1,[16,18], Function(callBattle,enemy_devil,"None","None","Acropolis"), 1)
        mpAcropolis.addTile(0.71,0.87,6,[17,19,38], saveInteraction, 0)
        mpAcropolis.addTile(0.765,0.86,0,[18,20,36], nullInteraction, 0)
        mpAcropolis.addTile(0.82,0.85,5,[19,21], obv6, 0) #20
        mpAcropolis.addTile(0.875,0.86,1,[20,22], Function(callBattle,enemy_mermaid,enemy_mermaid,enemy_mermaid,"Acropolis"), 1)
        mpAcropolis.addTile(0.87,0.76,0,[21,23], nullInteraction, 0)
        mpAcropolis.addTile(0.86,0.66,1,[22,24], Function(callBattle,enemy_devil,enemy_devil,"None","Acropolis"), 1)
        mpAcropolis.addTile(0.865,0.56,acropolisSideQuest_(),[23], acropolisSideQuest, 0)
        mpAcropolis.addTile(0.25,0.73,0,[5,26], nullInteraction, 0)
        mpAcropolis.addTile(0.24,0.63,1,[25,27], Function(callBattle,enemy_mermaid,"None","None","Acropolis"), 1)
        mpAcropolis.addTile(0.295,0.63,0,[26,28], nullInteraction, 0)
        mpAcropolis.addTile(0.31,0.53,1,[27,29], Function(callBattle,enemy_mermaid,enemy_mermaid,"None","Acropolis"), 1)
        mpAcropolis.addTile(0.365,0.53,0,[28,46], nullInteraction, 0)
        mpAcropolis.addTile(0.59,0.985,1,[16,31], Function(callBattle,enemy_devil,enemy_mermaid,"None","Acropolis"), 1) #30
        mpAcropolis.addTile(0.535,0.975,0,[30,32], nullInteraction, 0)
        mpAcropolis.addTile(0.48,0.98,5,[31,33], obv7, 0)
        mpAcropolis.addTile(0.425,0.985,1,[32,34], Function(callBattle,enemy_mermaid,"None","None","Acropolis"), 1)
        mpAcropolis.addTile(0.37,0.975,1,[33,35], Function(callBattle,enemy_devil,"None","None","Acropolis"), 1)
        mpAcropolis.addTile(0.315,0.98,acropolisMermaid_(),[34], acropolisMermaid, 0) #35
        mpAcropolis.addTile(0.755,0.96,1,[19,37], Function(callBattle,enemy_succubus,"None","None","Acropolis"), 1)
        mpAcropolis.addTile(0.805,1.0,acropolisCrown_(),[36], acropolisCrown, 0)
        mpAcropolis.addTile(0.7,0.77,0,[18,39], nullInteraction, 0)
        mpAcropolis.addTile(0.71,0.675,1,[38,40],Function(callBattle,enemy_mermaid,enemy_mermaid,enemy_mermaid,"Acropolis"), 1)
        mpAcropolis.addTile(0.67,0.61,0,[39,41], nullInteraction, 0) #40
        mpAcropolis.addTile(0.63,0.55,einyaDetermine("icon"),[40], einyaInteraction, einyaDetermine("auto"))
        mpAcropolis.addTile(0.14,0.73,1,[3,43], Function(callBattle,enemy_mermaid,enemy_mermaid,enemy_mermaid,"Acropolis"), 1)
        mpAcropolis.addTile(0.14,0.63,0,[42,44], nullInteraction, 0)
        mpAcropolis.addTile(0.085,0.64,0,[43,45], nullInteraction, 0)
        mpAcropolis.addTile(0.095,0.54,1,[44], Function(callBattle,enemy_mermaid,enemy_devil,enemy_mermaid,"Acropolis"), 1)
        mpAcropolis.addTile(0.41,0.59,1,[29,47], Function(callBattle,enemy_mermaid,"None","None","Acropolis"), 1)
        mpAcropolis.addTile(0.41,0.69,0,[46,15], nullInteraction, 0)

        global mpStoneIsland
        mpStoneIsland = scrStoneIsland()
        mpStoneIsland.addTile(0.3,0.865,3,[1], leavetoWorldmap, 0)
        mpStoneIsland.addTile(0.245,0.85,0,[0,2], nullInteraction, 0)
        mpStoneIsland.addTile(0.19,0.835,0,[1,3], nullInteraction, 0)
        mpStoneIsland.addTile(0.135,0.82,10,[2,4], Function(callBattle,enemy_devil,"None","None","IsleStone"), 1)
        mpStoneIsland.addTile(0.08,0.805,0,[3,5], nullInteraction, 0)
        mpStoneIsland.addTile(0.09,0.705,1,[4,6], Function(callBattle,enemy_devil,enemy_shadow,enemy_succubus,"IsleStone"), 1) #5
        mpStoneIsland.addTile(0.1,0.605,5,[5,7], obv39, 0)
        mpStoneIsland.addTile(0.155,0.615,0,[6,8], nullInteraction, 0)
        mpStoneIsland.addTile(0.21,0.625,0,[7,9], nullInteraction, 0)
        mpStoneIsland.addTile(0.265,0.615,1,[8,10,30], Function(callBattle,enemy_shadow,enemy_shadow,"None","IsleStone"), 1)
        mpStoneIsland.addTile(0.32,0.605,0,[9,11], nullInteraction, 0) #10
        mpStoneIsland.addTile(0.375,0.615,1,[10,12,25], Function(callBattle,enemy_succubus,"None","None","IsleStone"), 1)
        mpStoneIsland.addTile(0.43,0.605,5,[11,13,31], obv40, 0)
        mpStoneIsland.addTile(0.485,0.615,1,[12,14,29], Function(callBattle,enemy_devil,"None","None","IsleStone"), 1)
        mpStoneIsland.addTile(0.54,0.625,0,[13,15], nullInteraction, 0)
        mpStoneIsland.addTile(0.595,0.615,1,[14,16], Function(callBattle,enemy_succubus,"None","None","IsleStone"), 1) #15
        mpStoneIsland.addTile(0.65,0.605,5,[15,17], obv41, 0)
        mpStoneIsland.addTile(0.705,0.61,1,[16,18,20], Function(callBattle,enemy_shadow,enemy_shadow,"None","IsleStone"), 1)
        mpStoneIsland.addTile(0.76,0.62,0,[17,19], nullInteraction, 0)
        mpStoneIsland.addTile(0.815,0.63,hansaDetermine("icon"),[18], hansaInteraction, hansaDetermine("auto"))
        mpStoneIsland.addTile(0.695,0.5125,lydriaDetermine("icon"),[17,21,22], lydriaInteraction, lydriaDetermine("auto")) #20
        mpStoneIsland.addTile(0.695,0.41,saanviDetermine("icon"),[20,24], saanviInteraction, saanviDetermine("auto"))
        mpStoneIsland.addTile(0.75,0.485,1,[20,23], Function(callBattle,enemy_devil,enemy_devil,"None","IsleStone"), 1)
        mpStoneIsland.addTile(0.805,0.485,1,[22], Function(callBattle,enemy_succubus,"None","None","IsleStone"), 1)
        mpStoneIsland.addTile(0.6425,0.43,3,[21], dropPass, 0)
        mpStoneIsland.addTile(0.38,0.715,0,[11,26], nullInteraction, 0)
        mpStoneIsland.addTile(0.39,0.815,1,[25,27], Function(callBattle,enemy_succubus,"None","None","IsleStone"), 1)
        mpStoneIsland.addTile(0.445,0.82,isleSideQuest_(),[26,28], isleSideQuest, 0)
        mpStoneIsland.addTile(0.5,0.815,1,[27,29], Function(callBattle,enemy_succubus,"None","None","IsleStone"), 1)
        mpStoneIsland.addTile(0.5,0.715,0,[13,28], nullInteraction, 0)
        mpStoneIsland.addTile(0.27,0.515,2,[9], npc_7, 0)
        mpStoneIsland.addTile(0.435,0.505,ei_devil_(),[12], ei_devil, 0)

        global mpAsuraDrop
        mpAsuraDrop = scrAsuraDrop()
        mpAsuraDrop.addTile(0.95,0.8,3,[1], leavetoWorldmap, 0)
        mpAsuraDrop.addTile(0.895,0.79,0,[0,2], nullInteraction, 0)
        mpAsuraDrop.addTile(0.84,0.78,1,[1,3], Function(callBattle,enemy_undead,"None","None","AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.785,0.77,5,[2,4,34], obv10, 0)
        mpAsuraDrop.addTile(0.73,0.8,0,[3,5], nullInteraction, 0)
        mpAsuraDrop.addTile(0.675,0.81,1,[4,6], Function(callBattle,enemy_undead,enemy_undead,enemy_undead,"AsuraDrop"), 1) #5
        mpAsuraDrop.addTile(0.62,0.82,0,[5,7], nullInteraction, 0)
        mpAsuraDrop.addTile(0.565,0.83,1,[6,8,24,29], Function(callBattle,enemy_undead,enemy_asuri,enemy_undead,"AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.51,0.8,0,[7,9], nullInteraction, 0)
        mpAsuraDrop.addTile(0.455,0.79,0,[8,10], nullInteraction, 0)
        mpAsuraDrop.addTile(0.4,0.78,1,[9,11], Function(callBattle,enemy_asuri,enemy_asuri,enemy_asuri,"AsuraDrop"), 1) #10
        mpAsuraDrop.addTile(0.345,0.77,5,[10,12], obv11, 0)
        mpAsuraDrop.addTile(0.29,0.8,0,[11,13], nullInteraction, 0)
        mpAsuraDrop.addTile(0.235,0.81,1,[12,14,22], Function(callBattle,enemy_undead,enemy_asuri,"None","AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.245,0.71,0,[13,15], nullInteraction, 0)
        mpAsuraDrop.addTile(0.24,0.61,5,[14,16,18], obv12, 0) #15
        mpAsuraDrop.addTile(0.245,0.51,1,[15,17], Function(callBattle,enemy_undead,"None","None","AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.24,0.41,syllDetermine("icon"),[16], syllInteraction, syllDetermine("auto"))
        mpAsuraDrop.addTile(0.185,0.6,1,[15,19], Function(callBattle,enemy_asuri,enemy_asuri,"None","AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.13,0.61,5,[18,20], obv13, 0)
        mpAsuraDrop.addTile(0.075,0.62,0,[19,21], nullInteraction, 0) #20
        mpAsuraDrop.addTile(0.02,0.63,3,[20], endPass, 0)
        mpAsuraDrop.addTile(0.24,0.91,1,[13,23], Function(callBattle,enemy_asuri,enemy_asuri,enemy_asuri,"AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.265,1.0,0,[22], nullInteraction, 0)
        mpAsuraDrop.addTile(0.56,0.73,asuraForbidden_(),[7,25], asuraForbidden, 0)
        mpAsuraDrop.addTile(0.6,0.65,0,[24,26], nullInteraction, 0) #25
        mpAsuraDrop.addTile(0.655,0.66,1,[25,27], Function(callBattle,enemy_undead,enemy_undead,"None","AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.71,0.65,0,[26,28], nullInteraction, 0)
        mpAsuraDrop.addTile(0.765,0.64,einyaDetermine("icon"),[27], einyaInteraction, einyaDetermine("auto"))
        mpAsuraDrop.addTile(0.57,0.93,0,[7,30], nullInteraction, 0)
        mpAsuraDrop.addTile(0.61,1.0,1,[29,31], Function(callBattle,enemy_asuri,"None","None","AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.665,0.99,2,[30,32], npc_2, 0)
        mpAsuraDrop.addTile(0.73,0.98,1,[31,33], Function(callBattle,enemy_undead,"None","None","AsuraDrop"), 1)
        mpAsuraDrop.addTile(0.785,0.97,0,[32,34], nullInteraction, 0)
        mpAsuraDrop.addTile(0.79,0.87,0,[3,33], nullInteraction, 0)

        global mpVritraEnd
        mpVritraEnd = scrVritraEnd()
        mpVritraEnd.addTile(0.235,0.475,3,[1], leavetoWorldmap, 0)
        mpVritraEnd.addTile(0.24,0.575,0,[0,2], nullInteraction, 0)
        mpVritraEnd.addTile(0.235,0.675,1,[1,3], Function(callBattle,enemy_shadow,"None","None","Vritra"), 1)
        mpVritraEnd.addTile(0.24,0.775,5,[2,4,19,22], obv94, 0)
        mpVritraEnd.addTile(0.23,0.875,0,[3,5], nullInteraction, 0)
        mpVritraEnd.addTile(0.235,0.975,0,[4,6], nullInteraction, 0)  #5
        mpVritraEnd.addTile(0.29,0.98,1,[5,7], Function(callBattle,enemy_shadow,enemy_shadow,"None","Vritra"), 1)
        mpVritraEnd.addTile(0.345,0.97,0,[6,8], nullInteraction, 0)
        mpVritraEnd.addTile(0.4,0.965,5,[7,9,25], obv95, 0)
        mpVritraEnd.addTile(0.455,0.97,1,[8,10], Function(callBattle,enemy_shadow,enemy_shadow,enemy_shadow,"Vritra"), 1)
        mpVritraEnd.addTile(0.51,0.975,0,[9,11], nullInteraction, 0)
        mpVritraEnd.addTile(0.565,0.98,0,[10,12], nullInteraction, 0)
        mpVritraEnd.addTile(0.62,0.975,1,[11,13], Function(callBattle,enemy_shadow,enemy_shadow,enemy_shadow,"Vritra"), 1)
        mpVritraEnd.addTile(0.675,0.975,0,[12,14], nullInteraction, 0)
        mpVritraEnd.addTile(0.73,0.965,6,[13,15,28], obv96, 0)
        mpVritraEnd.addTile(0.73,0.865,0,[14,16], nullInteraction, 0) #15
        mpVritraEnd.addTile(0.72,0.77,0,[15,17], nullInteraction, 0)
        mpVritraEnd.addTile(0.71,0.675,5,[16,18,26,35], obv97, 0)
        mpVritraEnd.addTile(0.7075,0.575,boss_7_(),[17], boss_7, 0)
        mpVritraEnd.addTile(0.185,0.78,0,[3,20], nullInteraction, 0)
        mpVritraEnd.addTile(0.13,0.79,1,[19,21], Function(callBattle,enemy_shadow,"None","None","Vritra"), 1) #20
        mpVritraEnd.addTile(0.075,0.78,vritraObservation_(),[20], vritraObservation, 0)
        mpVritraEnd.addTile(0.295,0.775,0,[3,23], nullInteraction, 0)
        mpVritraEnd.addTile(0.35,0.78,0,[22,24], nullInteraction, 0)
        mpVritraEnd.addTile(0.405,0.7725,1,[23,25], Function(callBattle,enemy_shadow,enemy_asuri,"None","Vritra"), 1)
        mpVritraEnd.addTile(0.395,0.869,0,[8,24], nullInteraction, 0)
        mpVritraEnd.addTile(0.655,0.665,0,[17,27], nullInteraction, 0)
        mpVritraEnd.addTile(0.6,0.655, saanviDetermine("icon"),[26], saanviInteraction, saanviDetermine("auto"))
        mpVritraEnd.addTile(0.785,0.965,0,[14,29], nullInteraction, 0)
        mpVritraEnd.addTile(0.84,0.975,1,[28,30], Function(callBattle,enemy_shadow,"None","None","Vritra"), 1)
        mpVritraEnd.addTile(0.892,0.9825,0,[29,31], nullInteraction, 0)
        mpVritraEnd.addTile(0.885,0.885,1,[30,32], Function(callBattle,enemy_shadow,enemy_shadow,"None","Vritra"), 1)
        mpVritraEnd.addTile(0.88,0.785,5,[31,33], obv98, 0)
        mpVritraEnd.addTile(0.875,0.685,1,[32,34], Function(callBattle,enemy_shadow,"None","None","Vritra"), 1)
        mpVritraEnd.addTile(0.82,0.69,0,[33,35], nullInteraction, 0)
        mpVritraEnd.addTile(0.765,0.685,0,[17,34], nullInteraction, 0)

############################################

#spookygirl
label spoogstats:
           $ enum = 60
           $ enemy = "Spooky Doll"
           $ fgheight = " "
           $ edescripts = " The spooky girl is dressed like a Victorian child, despite clearly being in her twenties."
           $ edescriptl = " The spooky girl is dressed like a Victorian child, despite clearly being in her twenties. Her eyes are huge and blank, her skin porcelin pale apart from two perfectly round red circles on her cheeks. She moves stiffly and jerkily, but with an unnerving precision."
           $ ekgreet = " The spooky girl is dressed like a Victorian child, despite clearly being in her twenties. She tips her head to one side, and blinks slowly, her eyes making an unsettling click. \n \"I'm coming to play with you.\" she says, walking slowly towards you."
           $ ehlthmax = 8
           $ ehlth = 8
           $ eskill = 11
           $ espeed = 7
           $ eex = 10
           $ spunkable = False
           $ fooddropper = False
           $ cashdropper = False
           return



label spoogattacks:
         $ enemroll = renpy.random.randint(1, 6)
         if enemroll == 1:
             $ eatdes = "The spooky doll girl moves with shocking speed and pulls down your trousers. Grabbing your dick with her cold hand, she squeezes it firmly, her expresion blank and unchanging. \n \n \"I'm going to play with you forever and ever and ever...\" she says without emotion."
             $ lustdam=  3
         if enemroll == 2:
             $ eatdes = "The spooky girl grabs your crotch and squeezes hard. \n \n \"You're a bad, bad man..\" "
             $ edam = 2
             $ lustdam=  1
         if enemroll == 3:
             $ eatdes = "The spooky girl kicks you in the shin, making you yelp with pain. \n \n \"Let's play,\" she says without intonation."
             $ edam = 2
         if enemroll == 4:
             $ eatdes = "The spooky girl grabs you and presses her cold, firm body against you. \n \"I'm going to milk you.\" she whispers, \"I'm going to milk you dry.\""
             $ lustdam=  3
         if enemroll == 5:
             $ eatdes = "The spooky girl tips her head to one side and stares at you as she rubs her body through her clothes."
             $ lustdam=  1
         if enemroll == 6:
             $ eatdes = "The spooky girl runs her hands over her breasts. \n \"I'm going to play with you.\" "
             $ lustdam=  1

         return

# fingers stats


label fingerstats:
           $ enum = 62
           $ enemy = "impossible fingers"
           $ fgheight = " "
           $ edescripts = " Hundreds of impossibly long, many jointed fingers pour out of the hundreds of holes that cover the floor, walls and ceiling of the room and reach towards you."
           $ edescriptl = " Hundreds of impossibly long, many jointed fingers pour out of the hundreds of holes that cover the floor, walls and ceiling of the room. Each ends in a long, elegantly shaped, black painted fingernail; they reach towards you, prodding and poking, grasping and stroking..."
           $ ekgreet = " You panic as they swarm all around you. You're going to have to fight."
           $ ehlthmax = 13
           $ ehlth = 13
           $ eskill = 14
           $ espeed = 8
           $ eex = 15
           $ spunkable = False
           $ fooddropper = False
           $ cashdropper = False
           return





label fingerattacks:

          if roundcount == 0:
              $eatdes = " Dozens of the fingers crowd in around you, poking and prodding. One wraps around your thigh, squeezing gently. Another strokes a cheek with its long pointed nail, making you shiver..."
              $lustdam=  1
          if roundcount == 1:
              $eatdes = " Dozens of the fingers crowd in around you, poking and prodding, grabbing greedily. One shoves itself down the back of your pants, hunting for your pucker, and you yelp and jump away."
              $lustdam=  1
          if roundcount == 2:
              $eatdes = " Dozens of the fingers crowd in around you, poking and prodding. One wraps around your thigh, squeezing gently. Another strokes a cheek with its long pointed nail, making you shiver, as another three gently but insitantly squirm their way inside your clothes..."
              $lustdam=  1
          if roundcount == 3:
              $eatdes = " Scores of the fingers stroke and tickle you, pulling open your shirt, scratching at your chest, wriggling and probing inside your clothes. Several sneak into your armpits, tickling you, as another forces its way into your mouth..."
              $lustdam=  1
              $ fgheight = " You can hardly see the walls through the hundreds of fingers that squirm and writhe around you."
          if roundcount == 4:
              $eatdes = " Four fingers join forces to tweak at your nipples as another two tickle your armpits and two more try to worm their way into your mouth. As you're distracted with that, two fingers from the floor smoothly yank down your pants. More fingers instantly reach for your groin, and you cover it urgently with one hand."
              $lustdam=  2
          if roundcount == 5:
              $ eatdes = " Scores of fingers snake down from the ceiling, wrap under your arms and lift you into the air. More of them tightly wrap your thighs, pulling them apart as three more home in on your groin -  one coiling around your dick and tugging it, smooth and rhythmic, another wrapping round your balls and squeezing gently, the third probing rudely up your asshole and hunting out your prostate..."
              $lustdam=  3
          if roundcount == 6:
              $eatdes = " Moaning and writhing, you kick and swat at the fingers as best you can, but held helpless in mid air, there's nothing you can do to keep them from stroking and rubbing every inch of you. Three of them are now wrapped around your aching cock, tugging at it furiously as more squeeze your balls and another thrusts remorselessly in and out of your anus..."
              $lustdam=  3
          if roundcount > 6:
              $eatdes = " Every inch of you is being stroked, pinched, scratched and fondled the countless fingers close in on you as you hang helpless in the air. The fingers wrapped tight around your cock jack and squeeze you ever harder as two fingers mercilessly ream your ass hole..."
              $lustdam=  4
          return


         #electric repair store/milker/spunk guns
label electro:
    nvl clear
    scene bg novine
    $elecvis = elecvis + 1
    if elecvis > 1:
        " You enter the cramped and crowded store, and see Emily lounging in her usual place behind the counter. \n \n \"Wotcha,\" she says with a grin, \"What can I do you for?\""
        jump emilybiz

    if elecvis == 1:
        " You step into the cramped and crowded store, a buzzer abov........"

label secondmilked:
    nvl clear
    " Second milking scene to go here. Emily puts spunk into pistol. You get a spunk pistol! Emily acts just slightly creepy."
    $spunkgunloads = 6
    $hour = hour + 3
    $lust = 0
    $milked = True
    jump locats

label emchatter:
    nvl clear
    $emchat = emchat + 1
    $emchattoday = True
    if emchat == 1:
         " Curious, you ask the little electrician why she's not affected by the infection. She just shrugs. \n \n  \"Dunno, I guess I'm immune? Maybe it's cause I had chicken pox when I was a kid, or cause I wasn't baptized, or 'cause I've never ate a blood orange, how should I know?\"\n \n She leans back in her chair, staring at the ceiling, then looks down at you with a grin. \n \n  \"Maybe I'm just too clever for it, ey?\" "
         jump emilybiz
    if emchat == 2:
            " You ask her if she owns the store. \n \n  \"My dad does, but now he's not around, so I'm running the place. Making a better profit than he ever did. Mutant invasions are good for business, who would have thunk it, ey? Maybe I'll be able to buy it off him when this is over... unless I decide to just sell my story to the papers and get rich...\" \n \n  She stares up at the tobacco stained ceiling tiles, dreamily."
            jump emilybiz
    if emchat == 3:
            " You ask her why she didn't leave the island when it was evacuated. She seems to give your question serious consideration, as though she's never really thought about it before. \n \n  \"Hmm, I dunno. Was going to, was on the way down to the boats with my dad, but... it just started seeming like I shouldn't, like it'd be better to stay, somehow. Knew dad wouldn't want me to, so I gave him the slip, made my way back here. Had the idea for the milking machine on my way back, I'd already seen some of what was going down by then. But yeah, I dunno. It just felt.. right.\" \n \n  She falls silent, staring up at the celing with an almost comically serious frown on her face. Could she have some form of the infection that *dosen't* turn you insane, you wonder? You dismiss the thought - really, who knows?"
            jump emilybiz
    if emchat == 4:
             " You ask her what she thinks is going on on the island, and she blows a raspberry and shrugs. \n \n  \"How the flip should I know? Could be like, a goverment experiment, like when they put acid in the drinking water in America.\" \n \n  \"When did they do that?\" you ask, amused. \n \n  \"Oh, you know, they do it all the time, the eff-bee-eye and all. They do it loads, but they cover it up and stuff, so that no-one finds out. Come on, *everyone* knows about *that*.\"
\n \n  You smile, but she's staring up at the ceiling, thoughtfully. \n \n  \"Or maybe it's, you know, magic. The old curse thing.\" \n \n  \"What curse?\" you ask, intrigued. \n \n  \"There was meant to be like, devils and demonds and stuff, on the island like, way back in the middle ages. It's the legend, you know, why all the tourists come here, to look at the old abbey and shit.\" \n \n  \"So you think it could be the same thing?\" \n \n  \"Nah, course not. There's no such thing as demonds.\" "
             jump emilybiz
    if emchat == 5:
            " You ask her if she knows any more about the curse and the \"demonds\". \n \n  \"Nah. I only moved back here with dad about a year back, when I dropped out of college. Lived down in Liverpool with my mam before that, and I'm not really into all that ghosts and goolies stuff. Kids stuff, ennit? You should talk to one of the locals if you wanna know more about that stuff.\" "
            jump emilybiz
    if emchat > 5:
            " You chat for a while, but learn nothing of interest."
            jump emilybiz

label genend:
    " The infection pulsing through your veins, flooding your brain, you can think of nothing but sex and surrender. Any thoughts of escape from the island, of your own survival, of anything other than satisfying your primal carnal urges fade away, drowned in the hot tide of the infection. \n \n You tear off your clothes and stagger through the streets in a daze, following the bobbing tip of your hard cock, searching for the only thing you're capable of caring about any longer. \n \n You spend the rest of your days on the island, stumbling into and out of the clutches of mutant after mutant, being suck and fucked, milked and drained, going at the mutant minxes with as much enthusiasm as they go at you. You forget your past life, and are happy to live in this animal, carnal blur of a reality thinking, and aware of, nothing but sex. "
    jump ending


 # gang of students - Enemy Encounter template

label studgstats:
           $ enum = 110
           $ enemy = "gang of students"
           $ fgheight = " "
           $ edescripts = " You're faced with a gang of giggling girls in school uniforms - grey skirts, white shirts, striped ties and straw boaters."
           $ edescriptl = " You're faced with a gang of giggling girls in school uniforms - grey skirts, white shirts, striped ties and straw boaters. There's a good half dozen of them, all different shapes and sizes, all hot, horny and excited to see you."
           $ ekgreet = " The gang of girls stare at you for a second or so, then one shouts \" Get him!\" and they descend on you in a laughing mob."
           $ ehlthmax = 15
           $ ehlth = 15
           $ eskill = 9
           $ espeed = 8
           $ eex = 15
           $ spunkable = True
           $ fooddropper = False
           $ cashdropper = False
           return


# " A [enemy] approaches!"
nvl clear
b " [edescriptl] [fgheight]\n \n The [enemy]'s health is [ehlth] of [ehlthmax], and their skill rating is [eskill]. \n \n Your health is  [chlth] of [mxhlth], and your skill is [pskill]. Your lust is [lust] out of [maxlust]."

label fighty:

$ boilrando = renpy.random.randint(1, 20)
if boilrando == 1 and susangrowth > 10:
    b " The little head on your neck begins whistling at the top of it's.... lungs? The screeching noise right next to your ear is so painful and distracting, {b}you're unable to concentrate enough to make any action during this round of combat!{/b}"
    jump ehit

$ menu = renpy.display_menu

menu:
     b " [edescripts] [fgheight]\n \n The {b}[enemy]'s{/b} health is [ehlth] of [ehlthmax], and their skill rating is [eskill]. \n \n Your health is  [chlth] of [mxhlth], and your skill is [pskill]. Your lust is [lust] out of [maxlust]."
     "Shove!":
        jump playerattack
     "Special Attacks!" if powshove == True or lightshove == True:
        jump specialattacks
     "Use an attack item!" if stinks >0 or smokes >0 or spunkgunloads >0:
        jump battleitems
     "Recovery!" if meditabil > 0 or edrink > 0:
        jump recoverymenu
     "Wait!" if observo == False:
        jump waitc
     "Observe!" if observo == True:
        jump battobs
     "Surrender!":
        $surrend = True
        $menu = nvl_menu
        jump defeatl
     "Escape!":
        jump escape




label specialattacks:
    menu:
        b " [edescripts] [fgheight]\n \n The [enemy]'s health is [ehlth] of [ehlthmax], and their skill rating is [eskill]. \n \n Your health is  [chlth] of [mxhlth], and your skill is [pskill]. Your lust is [lust] out of [maxlust]."
        "Power Shove!" if powshove == True:
            jump powshov
        "Lightning Shove!!" if lightshove == True:
            jump speedshov
        "No, wait...":
            jump fighty

label battleitems:
    menu:
        b " [edescripts] [fgheight]\n \n The [enemy]'s health is [ehlth] of [ehlthmax], and their skill rating is [eskill]. \n \n Your health is  [chlth] of [mxhlth], and your skill is [pskill]. Your lust is [lust] out of [maxlust]."
        "Throw a stink bomb! ([stinks] bombs) " if stinks >0:
            jump stinkthrow
        "Throw a smokebomb! ([smokes] bombs)" if smokes >0:
            jump smokethrow
        "Fire the Spunk Pistol! ([spunkgunloads] shots)" if spunkgunloads >0:
            jump spunkfire
        "Apply Numbing Cream ([numbs] tubes of cream)" if numbs >0:
            jump numbuse
        "No, wait...":
            jump fighty



label recoverymenu:
    menu:
        b " [edescripts] [fgheight]\n \n The [enemy]'s health is [ehlth] of [ehlthmax], and their skill rating is [eskill]. \n \n Your health is  [chlth] of [mxhlth], and your skill is [pskill]. Your lust is [lust] out of [maxlust]."
        "Meditate!" if meditabil > 0:
            jump meddy
        "Quaff an Energy Drink! ([edrink] carried)" if edrink >0:
            call edrinkbat
            jump eattack
        "No, wait...":
            jump fighty

label gwebdone:

#$ menu = nvl_menu
$damredchk = 0

if edam > 0:          #applying health damage
    $damredchk = 1
$edam = edam - clbon # coat armour bonus deducted
if edam <0:
    $edam = 0
$chlth = chlth - edam


$lustdam = lustdam - numbpower #applying lust damage
if lustdam < 0:
    $lustdam = 0
$lust = lust + lustdam


b " [eatdes]" # enemy attack des
if edam <1:
    $damdes = ""
if edam <1 and damredchk ==1:
    $damdes = " Your armour allows you to shrug off the physical damage!"
if edam == 1:
    $damdes = "One damage point taken!"
if edam == 2:
    $damdes = "Two damage points taken!"
if edam == 3:
    $damdes = "Three damage points taken!"
if edam == 4:
    $damdes = "Four damage points taken!!"
if edam == 5:
    $damdes = "{b}Five{/b} damage points taken!!"
if edam > 5:
    $damdes = "{b}A shitload of damage points taken!!{/b}"
if chlth <1:
    $damdes = "{b}You've been battered too much to fight on!{/b}"

if lustdam <1:
    $ldamdes = ""
if lustdam ==1:
    $ldamdes = "Lust rises by one point!"
if lustdam ==2:
    $ldamdes = "Lust rises by two points!"
if lustdam ==3:
    $ldamdes = "Lust rises by three points!"
if lustdam ==4:
    $ldamdes = "Lust rises by four points!!"
if lustdam ==5:
    $ldamdes = "{b}Lust rises by five{/b} points!!"
if lustdam >5:
    $ldamdes = "{b}Lust rises by a shitload of points!!{/b}"
if lust >= maxlust:
    $ldamdes = "{b}Your lust is unbareable! Oh God...{/b}"

if edam >1 and lustdam >1 or damredchk ==1:
    b " [damdes] [ldamdes]"

$edam = 0
$lustdam = 0
nvl clear #player defeat gets checked here
if pois < 0:
    call scorppoisdef
if lust == maxlust:
    show screen overlay
    $menu = nvl_menu
    call defeatl
if lust > maxlust:
    $menu = nvl_menu
    show screen overlay
    call enhide
    call defeatl
if chlth <1:
    $menu = nvl_menu
    show screen overlay
    call enhide
    call defeath


jump roundtwo

label escape:   # - escaping stuff!
 #---impossible to escape bits
if enum == 450:                      #bossy redhead initial hoseguest fight
  b " You can't escape from this one!"
  jump ehit

# - escape poss calculated
$ plran = renpy.random.randint(2, 14)
$ enran = renpy.random.randint(1, 8)

$ eatt = enran + espeed
$ patt = plran + speed

if eatt > patt:
    jump nogetaway
if patt > eatt:
    jump getaway
if patt == eatt:
    jump nogetaway

label nogetaway:
  b " Couldn't get away!"
  jump ehit

label getaway:

$fooddropper = False
$cashdropper = False
$reward = 0
$foodgot = 0
$numbed = False
$numbpower = 0
$pex = pex + 5
call enhide
$roundcount = 0
if enum == 345:
    $pskill = realskill


if enum == 250:
    b " You turn tail and flee from the lab! You pause outside to gather your breath."
    $labvis = 1
    call locats

if locat == 12:


    b " You push past the [enemy] and run wildy through the sewers. Eventually you collapse, exhausted, leaning against a wall. You have earned five experience points for your successfull escape."
    $menu = nvl_menu
    show screen overlay
    call seweresc


if locat == 4:
    b " You manage to shove past the [enemy] and charge into a door, smashing it open. You have earned five experience points for your successfull escape. \n \n You run on down the endless halls..."
    $menu = nvl_menu
    show screen overlay
    call spookyhalls

if locat == 7:
    b " You push past the [enemy] and run randomly through the library. Once you feel safe, you stop, catch your breath and look around...\n \n You have earned five experience points for your successfull escape."
    $menu = nvl_menu
    show screen overlay
    call libesc

if enum == 160:
    b " You run, shaking the [enemy] out of your clothing as you go. \n \n You lean lean against a wall, catching your breath and wondering what you should do next. You have earned five experience points for your successfull escape."
    nvl clear
    show screen overlay
    jump locats

b " You manage to shove past the [enemy] and run, leaving them far behind you! \n \n You lean against a wall, catching your breath and wondering what you should do next. You have earned five experience points for your successful escape!"
nvl clear
show screen overlay
jump locats

label victory:
if enum == 345:
    $pskill = realskill
$numbed = False
$numbpower = 0
nvl clear
call bgsetter
$roundcount = 0
if enum == 450:
    jump bredoutsidebasewin
if enum == 260:
    jump clevergirlswin
if enum == 9:
    jump csecwin
if enum == 170:
   jump selenawin
if enum == 210:
    jump triswin
if enum == 40:
    if  farmbrand == True:
        $fgscrews = -666
call enhide


b " The [enemy] gives up and slinks off. Your victory nets you [eex] experience points. \n \n Your health is now [chlth] out of [mxhlth], and your lust is [lust] of a maximum of [maxlust]. "

if fooddropper == True and cashdropper == True:
      $ droll = renpy.random.randint(1, 100)
      if droll > 50:
            b " The [enemy] has dropped [foodgot] days food and £[reward]! You pack them away and get ready to move on. "
      $cash = cash + reward
      $ffood = ffood + foodgot

label lastday:
    nvl clear
    " It's the last day!"
    " You have survived the full forty days of quarentine and get rescued. \n \n Probably by army guys or something, I don't know."
    jump ending

label infectod:
        call infmaxend

label ending:
    #nvl clear
    #" You survived for [day] days, and ammassed £[cash]. \n \n [virtaker]."
    "The End"
    $ renpy.full_restart()


image title = "TITLE.png"
#characters
image farmgirl = "farmgirl.png"
image redhead = "redhead.png"
image chav = "chav.png"
image businesswoman = "businesswoman.png"
image highlandlass = "highlandlass.png"
image jewprincess = "jewprincess.png"
image mononerd = "mononerd.png"
image swollenerd = "swollennerd.png"
image plainjane = "plain.png"
image goth = "goth.png"
image housewife = "housewife.png"
image fatgoth = "fatgoff.png"
image girlnextdoor = "girlnextdoor.png"
image futanextdoor = "futanextdoor.png"
image spookygirl = "spookygirl.png"
image goatgirl = "goatgirl.png"
image japangirl = "jap.png"
image scorpiongirl = "japtail.png"
image spidergoth = "spidergoth.png"

#stupid rasna stuff
image rasnaone = "rasna1.png"
image rasnatwo = "rasna1snakeeyes.png"
image rasnathree = "rasna2.png"
image rasnafour = "rasna3.png"

#blank enemy placeholder image thing-me-do
image blank = "blankem.png"

image blankman = "genman.png"



# Declare characters used by this game.
init:

    $ narrator = Character(None, kind=nvl)
    $ b = Character(None)


    # Define some new transitions here - combat transition flash and shits
    $ slowdissolve = Dissolve(1.0)
    $ flashbulb = Fade(0.0,0.0, 0.7, color='#FFFFFF')

init python:
    menu = nvl_menu


init python:

    # The color of a menu choice when it isn't hovered.
    style.nvl_menu_choice.idle_color = "#f00"

    # The color of a menu choice when it is hovered.
    style.nvl_menu_choice.hover_color = "#ffff00"

    # The color of the background of a menu choice, when it isn't
    # hovered.
    style.nvl_menu_choice_button.idle_background = "#ff000000"

    # The color of the background of a menu choice, when it is
    # hovered.
    #style.nvl_menu_choice_button.hover_background = "#00000000"
    style.nvl_menu_choice_button.hover_background = "#ff000044"


    # How far from the left menu choices should be indented.
    style.nvl_menu_choice_button.left_margin = 20


###############################
# The game starts here.
label start:

############################################
# setting variables begins here....
##############################################

#game settings here, exploration mode etc...

$testchar = False # test char on or offf

$randomattacks = True #random ambush attacks in streets on or offf....

$expmode = True # Exploration mode on or off......

#locations - must be true for them to appear as options to visit......
$supermarket = False
$cornershop = False
$farms = False
$lanca = False
$westsi = False
$riversi = False
$spooko = False
$conffound = False
$libraryfound = False
$collfound = False
$seafi = False
$vgfound = False
$sewerfound = False
$supfound = False
$labfound = False
$mcgonvgfound = False
$mcgonconfound = False
$mcgonrivfound = False
$vgconffound = False


label kamala_E2:
    stop music fadeout 1.0
    "I accept her advances, giving into her lustful desires."
    "A deep blush forms over Kamala's cheeks, complementing the coy smile growing on her face."
    "Once the reality of the situation hits me, my heartbeat intensifies, each beat resonating throughout my body. "
    show Kamala Clothed Lustful
    with charDissolve
    "I try to gather myself and catch my breath, but I find these attempts futile as she forces herself closer to me, enticing me with her erotic gaze. "
    "She's so clearly trying to tempt me as she removes her sundress...flirtatiously eyeing me...her thighs sensually rubbing together below its thin veil."
    "I can just barely contain myself when her voice finally escapes her lips, despite it being no louder than a lustful murmur amidst the surrounding ambience of the night. "
    "I'm not sure how much longer I can wait, I feel all feelings of restraint leaving my body."
    show Kamala Lingerie Lustful
    with charDissolve
    "As her sundress touches the ground, her voluptuous chest catches my eye, provoking a enticing wink while simultaneously gesturing at her most special place."
    show Kamala at spriteZoom
    "Moments later her body pushes against my own, her soft skin and bare chest pressed against my flesh."
    "An erotic breath breaks out from her lips, tickling my neck as we fall to the ground together. "
    "Kamala's body wraps around me, her mouth tracing a path from my collar to my lips as our bodies intertwine. "
    "As our faces meet, our hot breaths and sensual whispers fade into the passion of the moment. "
    "Our lips lock as she shifts her weight onto me, one hand strung around me lovingly while the other removes my clothes."
    show Kamala at flinch
    "Kamala pulls me closer to her, and I begin to sneak a finger into her in exchange, first sliding over her supple skin. "
    "Our mouths part to breathe, a string of saliva still hanging between our glistening lips."
    show Kamala Naked Lustful
    with charDissolve
    "I finally slide my finger inside of her."
    "Her face initially twists in an awkward pain, but relaxes as a wave of ecstasy rushes over her. She whimpers as her body accepts me."
    "I give into her warmth and relax myself. Kamala nuzzles closer in turn, releasing short, hot gasps of air against me between her muted moans of pleasure as she tries her best to restrain herself. "
    show Kamala at flinch
    "She grinds against me as I feel her dripping, her thighs struggling for mercy against my delicate touch."
    "Kamala slides her hand over me and I instinctively jerk from the sensation, thrusting my fingers even deeper into her as the heat and moisture grows around my hand."
    "Letting out a slight moan myself, I sense another wave of pleasure rush over her as her back arches, pushing her breasts tightly against my chest. She grips me even tighter in her soft palms, her primal urges beginning to overcome her staunch dignity."
    "I feel myself reaching my limit as the space between our bodies tightens again. Whatever arms we have free move to embrace each other. "
    "Amidst hot sweat and more passionate whispers, she removes her hand from me and pulls her body up, drawing her arm around my back to rest upon my shoulder."
    "As she straddles me, we stare deeply into each others eyes, and I pull my fingers from her, letting her body rest at last."
    "Kamala releases a desperate moan as I run my hand across her inner thigh, trailing her juices along with it. "
    "For the first time in our moments of intense passion, I her voice more clearly; yet between steamy breaths and continued moans, her accent is faded and her vocals remain slightly muffled."
    ka "Dear wanderer...I see it in your eyes...won't you further this bond?."
    "Her question is in vain. We both know she doesn't need an answer. Without words, she aggressively grinds against the dampness she's left on my body."
    "Between the eager movements of her body she grips me again, this time with a grasp far tighter than before. Kamala breathes lustfully as she guides me into her, pressing down on me as she prepares for the sensation. "
    "She lets out a short, pained moan as I enter her. She struggles at first as her body tightens around me, begging me to please her. As she begins to calm herself, we remain still for what feels like minutes, but couldn't have been more than a few short seconds."
    "Then, she starts to move."
    #"<SHOW CG-KAMALA>"
    hide Kamala
    with charDissolve
 #   window hide
 #   with charDissolve
    $ show_box = 0
    show black at alphaCG
    with charDissolve
    show CG Kamala A
    with charDissolve
    pause
    #window show
    $ show_box = 1
    #with charDissolve
    "She lowers her hands to press against my chest, and I feel her close in as she gently squirms. She arches over me, a blush painted across her face. She pants heavily, sweat dripping, her naked body coming into full view."
    "We make eye contact as she rides me, forcefully thrusting her hips up and down. I start to move my body in unison with hers, ramming myself in and out of her."
    "She bites her lip seductively as she closes her eyes."
    "I feel her instincts overcoming her once again as her body shivers. She grits her teeth and speeds up the movement of her hips."
    "Losing herself in pleasure, she throws herself back and lets out a moan, trying her best to restrain herself as her body gives in to its sinful lust."
    "She begins to lose her balance amid her sensitive moans and whimpers, and so I pull her back over me. We gaze into each other's eyes and drown out the world around us. Without hesitation or distraction, we focus on each others' bodies."
    "I'm completely entranced by Kamala's blushing face, another look of pure ecstasy written across it, an expression of pent-up sexual desire being released. "
    "I want to make her body squirm more...I want to hear her passionate moans again."
    "I speed up my own movements to please her, as the sound of our bodies now overtakes the calm ambience of the night around us."
    "Yet despite my wishes, with a final thrust of her hips, I find myself no longer hold back what's built up inside me. As I reach my absolute limit, the sensation overtakes my entire body."
    pa "K-Kamala, I..."
  #  window hide
    $ show_box = 0
   # with charDissolve
    show CG Kamala B
    with charDissolve
    pause
   # window show
   # with charDissolve
    $ show_box = 1
    "But before I can retrieve the rest of my words, I'm greeted with a flash of white as we both share one final, passionate moan together. She clamps down on me and I feel what's pent me up in me empty deep inside her."
    "A few more moments pass as the embarrassment and afterglow of orgasm ultimately escapes us. We lean into each other once more, gripping each other closely in a vulnerable embrace while we share our final kiss."
    "As our lips part once more, she moves her hands to cover both my shoulders, gazing deep into my eyes."
    hide black
    with charDissolve
    hide CG Kamala B
    with charDissolve
    show Kamala Naked Neutral at sp1_1
    with charDissolve
    ka "My dear [playername]...I thank you."
    show Kamala Naked Sad
    with charDissolve
    show Kamala at spriteZoom
    "Unable to find anymore words, she retreats into the grip of my arms."
    "With memories made and experiences come to pass, the night wages on. We stay in each others grips till dawn, bearing witness one last time to the shared intimacy."
    #"<FADE TO BLACK>"
    scene black
    with charDissolve
    $ show_buttons = 0
    if check_inventory(kamalaHope):
        $ add_inventory(kamalaHope)
    centered "\"Kamala's Hope\" acquired!"
    $ variables.append("kamala_5")
    $ variables.append("kamala_end")
    $ show_buttons = 1
    $ persistent.kamala = True
    $ sex_scenes += 1
    $ show_buttons = 0
    $ jivaI = 50
    $ jivas += jivaI
    centered "Jivas increased by [jivaI] as a result of this interaction!"
    $ show_buttons = 1

    $ achievement.grant("KS_KAMALA_GOOD")
    $ achievement.Sync()

    return
    #"<GIVE CHAKRA: TO BE DETERMINED>"
    #"<END KAMALA ROUTE> "
