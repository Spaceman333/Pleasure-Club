#######################
#######################
####### DEFINES #######
#######################
#######################

#Player Character
define p = Character("You", color="#c8c8ff")
#define pn = Character('[playername]', color="#CDA559") #alt player

#Encounter Characters
define unk = Character('???', color="#CDA559")
define an = Character('Anna', color="#CDA559")
define dr  = Character('Dryad', color="#CDA559")


#######################
#######################
##### INIT PYTHON #####
#######################
#######################

init python:

    #incase I need it later, might delete tho lol




#######################
#######################
######   START  #######
#######################
#######################

label start:

    #Init flag variables

    # Skips
    $ global intro_passed = False
    $ global interview_passed = False
    $ global ritual_completed = False

    # Player neuromancy
    $ global player_tutor_unlocked = False
    $ global player_tutor_studied = False

    # Anna
    $ global ceo_anna_s1 = False

    # Lounge
    $ global lounge_dryad_s1 = False

    # Dressing Room

    # Courtyard

    # Booths

    # Recovery Beds


    #templates
#    $ global lounge_ecname_s1 = False
#    $ global dressing_ecname_s1 = False
#    $ global booth_ecname_s1 = False
#    $ global court_ecname_s1 = False
#    $ global beds_ecname_s1 = False

    #jump skipscreen


label skiptutorial:

    menu:
        "Have you ever played Renpy visual novels before?"

        "No - Do quick tutorial":
            jump tutorial
        "Yes - You know the controls":
            pass

    "In this particular VN, you play as yourself and are taken on a journey to explore the mysterious Pleasure Club."

    "In the club, you will encounter interesting characters with whom you'll do lovely sexy fun things together."

    "There is no ending to this game, its more a thing you return to again and again, when you feel like it."

    "Saving and exiting the game means leaving the club, while restarting the game and loading a save means coming back to the club."

    "The only goal in this game is to try everything you find interesting and later repeat the scenes you loved the most."

    jump aftertutorial


label tutorial:

    "To advance through the game, mouse left-click or press the Space or Enter keys. Try this now."

    "In a visual novel game, you read text and look at images. Occasionally there are choices you can make that affect the story."

    "In this particular VN, you play as yourself and are taken on a journey to explore the mysterious Pleasure Club."

    "In the club, you will encounter interesting characters with whom you'll do lovely sexy fun things together."

    "There is no ending to this game, its more a thing you return to again and again, when you feel like it."

    "Saving and exiting the game means leaving the club, while restarting the game and loading a save means coming back to the club."

    "The only goal in this game is to try everything you find interesting and later repeat the scenes you loved the most."

    "Now a quick primer on controls..."

    "When playing the game, right-click or press the escape key to enter the game menu. Press same keys again to exit the menu."

    "In the escape menu, you can Save, Load or change options or exit the game."

    "Alt+f4 is a fast way to exit the game too. Please do not shift+delete the game folder after doing so."

    "Hold the Ctrl key to skip past text (Don't do this here). It will stop skipping if you run into a choice."

    "This is handy if you want to go fast and get to your favorite parts quicker."

    "Or you can skip parts that bore you. I don't recommend skipping in the interview part though, or you'll likely fail it."

    "Skipping anywhere else is fine, as the game is designed around player choice and freedom."

    "Use the mousewheel up to go back in time and even redo your choices. Its like a save-load, but more recent."

    "Please use actual saves in the escape menu to secure your progress though. Mousewheel rollback is lost when game exit happens."

    "Mousewheel down works too, but only if you used mousewheel up before. You can try this here now."

    "Pressing H or middle-click will hide this text window. Use this when you want to admire images fully without anything in the way."

    "F toggles fullscreen mode, S creates a screenshot to the game folder."

    "Thats all, you can always press F1 to bring up this information in a web browser if you forget it."

    "Enjoy the game!"

    jump aftertutorial


label aftertutorial:

    menu:
        "Here you can skip intro scenes if you've played the game before"

        "First time player - Recommended - No skips":
            jump intro
        "Skip to interview - if you failed previously." if intro_passed == True:
            jump interview
        "Skip to ritual - if you refused previously." if interview_passed == True:
            jump ritual
        "Skip to Lounge - if you've done the entire intro previously." if ritual_completed == True:
            jump realstart


label intro:
    ###################
    #Story begins here
    ###################

    "You're reading an advertisement:"

    "{i}Come visit the Pleasure Club, a mature and safe setting for a variety of pleasant sexy services for adults!{i}"

    "{i}We offer love, sex, pleasure though all kinds of usual and unusual sexual acts and fantasies.{i}"

    "{i}Our speciality is a surprise that is out of this world; an exotic technique that will stimulate every nerve in your body.{i}"

    "{i}We hope to see you soon!{i}"

    "{i}Notice: Our services are available to customers over the age of 18. Please bring an ID to pass the entrance verification.{i}"

    p "Sounds interesting, might as well go try this."

    scene bg city
    with fade

    "Its night time in the city you live and recently this new Pleasure Club thing opened here."
    "The reviews for it are curiously mixed, since it seems like the negative ones are only from the ones that were denied entry."
    "Only a few neutral reviews stated that it wasn't for them despite trying and enjoying some of it, but felt it was too much for them to handle."
    "Aside from that its being praised a lot and people are loving it."
    "Oddly enough though, no one goes into the details and is adamant to keep the surprise a secret intentionally, recommending people to see it for themselves."
    "The club has been operating for a few months and despite quietly popping on to the scene without much hype, it has managed to thrive so far."
    "Feeling the gentle breeze of the night on the balcony, you look over the peaceful cityscape as you check the directions for the club and head out."

    scene bg metro

    "Taking the local metro line, you ponder a moment about the state of things."

    "About two years ago, sex work was legalized in the country."
    "Some feared it would bring upon the end of civilization, but to everyones surprise it didn't."
    "Unions were set up and the businesses that opened up have been professional. Its all clean, tested and safe."
    "It has turned out to be quite mundane actually, with sex services these days being not that different from a visit to a spa or a massage."
    "Some have even compared it to a common visit to a hairdresser."
    "After all, human beings have a need for love and a need for sex the same way as we have a need for food; once satisfied, we go do something else until we feel hungry for it again."
    "When something happens as often as a lunch does, it stops being such a big deal. You just do it and don't think of it intently once you had it."
    "Nowadays sex work is just a service and business like any other. Its odd how quickly things can change."

    p "Looks like this is my stop."

    "You get off the metro train and walk to the address you marked down."

    scene bg outside

    "This seems to be the place."
    "The entrance doesn’t seem much on the outside. Just a blank wall with no windows facing this way, no neon signs, just a small sign besides the door."
    "\'- Pleasure Club - Welcome -\'"
    "Besides opening hours and contact information, theres nothing else printed on it."
    "Probably they’re keeping the appearance of the club subtle not to bother families with kids in the neighbourhood with public display of sex."
    "You spot few people go in and out, likely customers judging by their looks. Seems like theres some life inside the building despite the boring exterior."
    "Theres a bouncer at the door. Looks like she’s making sure no one underage comes inside. Better get my ID ready."

    show temp one #bouncer
    with dissolve

    #post the bouncer scene here

Also answering 'no' doesn't mean the player is turned away. Instead, they're thanked for their honesty, told that the more important factors of entry is mental- and sexual-maturity, latter of which is commonly reached by boys around the ages of 12-16 or 10-14 by girls. By being honest, they're let in anyway but noted that if they haven't yet reached basic biological sexual maturity, then none of this will make sense to them.


    ""
b- hello, anything I can do you?
p- eyy whatcha got
b- I dont know you, new here?
p- yup
b- oh, well i work for the pleasure club. we run this place. may I see your card
p- *player hands their ID* get choices: a) yes you're over 18 on the ID b) no, you're not over 18 on the ID
b- (assuming no)
b- (assuming yes) everything seems to be in order. well if you must, I can let you inside
p- well yes, I'm interested
b- ok heres whats going on

POPUP
-a description of the pleasure club appears and what you need to do access its services-

good to know, thanks
thats great, you won't regret it

no idea what came over the two of you back there, but nevertheless you boldly step inside the club, the bouncer welcoming you with an goofy smile as you pass them by.

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

    $ intro_passed = True
    jump interview


label interview:

a- welcome to the pleasure club, I take it you're interested in our services?
p- thats why I'm here, yeah.
p- that said, I don't know the specifics of what your services actually are.
a- excellent and no worries, I'm here to give information about anything you want to know.
a- first though, we have a policy to vet out customers to see if we can actually provide our service to them. Our techniques are not compatible with everyone, so for some its just impossible for us to give them our services.
p- vet out? you mean like a test I must pass first?
a- in a sense, yes
a- its more of an interview where we ask about your views on things.
a- youll be coming into rather intimate contact with our people, so we want to ensure their safety and wellbeing by only letting people we can trust and are compatible with their technique.
a- in general its good for any business to check out beforehand if its services are suitable to a customer - blindly accepting everyone in and then resolving conflicts later is never worth it in the long run.
a- you will only need to do this once. Once you pass, you'll gain our trusted member status. you'll be able to come and go as you please.
p- ok, but you keep mentioning a "technique", what is that?
a- its a surprise, but it could be best described as a surprisingly realistic VR experience with very advanced haptic feedback.
a- as advertised, its an experience that is out of this world.
a- along with that, we also offer a variety of regular service of love, like handjobs, hugs, kisses, stroking, caressing and other nice things. If you came to be spoiled with love, sex and care, then this is the right place.
p- CHOICE (sound like my kind of thing/nah, this isn't what I wanted(leave))
no: a- no worries, come back anytime you change your mind, we'll be here.
excusing yourself, you head back out as the next customer in the line goes in. not in the mood today, maybe sometime else. (RETURN MAIN MENU - Unlock speedrun achievement)
yes: a- alright then, lets do the interview. It wont take too long.

Questions (ACTUAL):

how would you treat sex workers in general?
with respect and dignity
however I want

do you see sex workers as valuable people doing a valuable service and essential to society?
yes
no

would you ever hit or yell at someone if they disagree with you?
absolutely not
if they deserve it, yes

how would you react if someone shows unwillingness to something you want?
ask them whats keeping them from giving it and listen fully
keep pushing until I get what I want

when you want something from someone, do you prefer to request it or demand it?
request it
demand it

how do you most feel when you do not get what you want?
-sad and dissapointed
-bitter and angry

are roles of domination and submission important to you?
-not really, anyone can do either depending on the situation
-yes people must have clear roles and stick to them

how do you feel about the idea of a woman taking the leading role?
-neutral or excited
-confused or repulsed

what is your view on communication and consent?
-important
-nonsense

what comes to mind when you hear the word tradition?
-arbitrary rules that may have no sense today the same way they did back then
-an important value that I must uphold no matter what and never question it

Would you be able to fully relax and let go of all control in the embrace of a woman?
-yes
-no

how do you feel about a male turning into a female or a female turning into a male?
- strange / curious / accepting
- repulsed / not cool / forbidden


bad answers:
a- mmyeah... we'd be a terrible fit for you. I can guarantee our ladies would not enjoy working with you. If you were one of them and got these answers, I don't think you'd be too happy about it either. They're human beings with emotions and dignity, not unfeeling robots after all.
a- If you read up on sexual positivity and nonviolent communication, it might change your views and you'd be welcome to try this again at a later date.
a- other than that, we can't really be of service to you. You wouldn't like it anyway.
[Wrong address ending - try again another time]
>TRY AGAIN OPTION
>SET FLAG TO ALLOW SKIPPING TO INTERVIEW

all good answers:
a- very good, seems like we're a good fit for you.
a- i have few more questions, thought these won't prevent your access to our services - they're mainly to catch some misunderstandings before they happen.

Bonus round

how do you define love?
-a basic human need for affection and care that comes when none is available and temporarily goes away as its satisfied
- an intense feeling of deep personal affection or attachement towards someone else. Or a warm fuzzy feeling where I'm gonna get something good from the the other person.

correct
a- very good, that is accurate. Most people think its the other one - often to their dissapointment. Its great to see people that know better.
wrong
a- common belief, its what most of us are taught by others after all. sadly its not correct and often leads to confusion and frustration when early hopeful phase of a relationship subsides. If you're interested in learning to avoid this pitfall, check out Nonviolent Communication by marshall rosenberg on the topic of love.

how do you define sex?
-any form of erotic stimulation of any senses that arouses me, not limited to penetrative acts.
-male on female, dick goes in vagina, anus or mouth. Its not that complicated.

correct
a- good to hear, its wonderful to meet other open-minded individuals that are educated.
wrong
a- Not quite, it is way richer than that.
a- Touching, fondling, stroking, talking can all arouse and even make a person climax all on their own. Not to mention handjobs, sextoys, various tools, equipment, materials, clothing, accessories and many other exciting methods that also can achieve that. The world of sex is a lot more than just putting a peg in a hole and you'll get to discover all this fun in our club, you lucky one.




    $ interview_passed = True
    jump ritual

label ritual:

a- that concludes the interview, you've passed.
a- the only thing left to do is the ritual
p- what ritual?
a- we clasp our hands, look each other in the eyes and relax
p- uhh why?
a- it creates a bond between you and the club, solidifying our mutual trust

CHOICE - do it, doubt
no:
p- this is too wierd, I don't agree to this
a- its the last step to becoming a member to our club, it cannot be skipped
a- as I said earlier, you'd come into very intimate contact with our ladies so this step is crucial to get you ready to be with them.
a- without it, they won't be able to serve you properly.
p- is this about the "technique" you mentioned?
a- yes, it affect that too.
a- don't worry, you'll enjoy the ritual once it starts.

CHOICE accept / refuse

no: I can't do this, sorry.
no worries, maybe some other time then.
[Last second hesitation ending]

^yes/yes: calm / hesitant flag -> ritual start slightly altered
a-excellent, lets begin.

The Ritual:
*do hand clasp
*look in the eyes
*relax
*relax more
*very relaxed
*feeling good
*feeling quite nice
*entranced
*have a session - establish bond and spell of family
*enjoy the moment (maybe even climax and cum or almost cum)
*cool off
*back to reality
*Q&A (what was that, what happens now)
*welcome to the family
*come back for questions and more fun with anna later (or finish/do more sex with her)
*enter pleasure club proper

At the reception, talk to Anna the Greeter
She gives info, suggests to do the interview if you're interested in the services of the pleasure club, then suggests to do a ritual which will make a bond with you and the greater family as well as payment for the entry.


    $ ritual_completed = True

    jump annasendoff

label annasendoff:

As soon you walk in, you’re greeted
with a spacious lounge area. This place
looks bigger than it seems on the
outside.
You are approached by a lady.
“Hello there, is this you first time here?”
YES or NO
Yes -> Continue
No -> Skip to actual start
u “Yes, its my first time here. What is
this place?”
g “Ah, then welcome to the Pleasure
Club. My name is Anna and I’m the
greeter. You may ask me for guidance
and information.”
g “We have a few areas in the club you
may go to. Each of them may have a
selection of ladies that you may engage
with for some fun times”
g “Once you find someone you’re
interested, you may ask them for
pleasure. Some may even ask you.”
g “After that you can either go for
another round or try another encounter.
You are free to choose and mix.”
g “Remember to be respectful and
honor your partners. We want to keep
this a safe space for everyone.”
g “We only ask for a reasonable
entrance fee per visit. We hope to have
you visit us multiple times as a regular
customer.”
u* “Seems fair, the price is affordable
and essentially includes unlimited fun
as long as I have stamina.” - you think
to yourself (internal monologue)
The online ratings you browsed
previously give you confidence to trust
this business even thought you’ve
never used their services before.
u “Sounds great, heres my payment”.
g “Thank you, much appreciated. If you
have any questions, please ask away.
I’m here to help”.
g “If you want a hint where to start, just
try any of the corners of this lounge.
There are a number of ladies available
for some fun.”
g “Oh and occasionally we may also
get new ladies to join our group, so be
sure to come again in the future.”
That last line, she says with a glint in
her eye and a wide smile, looking you
deep in the eyes.
You are taken a back by this gesture,
but compose yourself once again. Its
probably just another part of the
experience.
You thank her for the information and
step forward into the lounge.
    jump game_advisory

label game_advisory:

    scene None
    "Congratulations, you are granted access to the Pleasure Club and its ladies."
    "Remember - in this game, your choices and consent matter."
    "You will go to the different locations of the Pleasure Club and interact with the ladies that offer sessions to you."
    "With each session you complete with them, you'll unlock a new session to try with them in the future."
    "Previously completed session will be available to do again at any time."
    "Each lady is unique and may have a different amount of sessions available to them."
    "Before any session, you will be informed of what to expect, either by a direct hint or a vague clue."
    "If the offer does not sound like something you'd want, do not hesitate to back away and refuse. You can always come back and try it later."
    "You can reload a save or rollback up with mousewheel if you don't want to continue a session."
    "While you're encouraged to try every lady and complete every session possible, it is not mandatory."
    "If you like one fantasy, but dislike another, you don't have to force it down upon yourself. Just enjoy the favorites and ignore the rest if thats how you want it."
    "There is no ending to this game. Keep coming back when you fancy some sexy lewd times, save your progress and load it back up when you return."

    jump realstart

label realstart:
    ########################
    #Game proper begins here
    ########################




label firstloop:

You are considering what to do next.
Standing in the lounge, you can see
different spots where various ladies are
lounging.
Some of them glance your way,
expectingly. Occasionally they wink and
beckon at you.
Others softly flutter their eyes towards
you, while some stare with mild
predatory intimidation.
Seems like theres a lot of variety to be
had for sure.
None of them are too similar to another.
They all seem to have a personality of
their own.
Strangely, you do not see any other
customers around, despite being sure
you saw some go in and come out of
here.
Looking up you see some signs that
indicate places where you can go.
Apparently you can freely go anywhere.
Anna is still here and is ready for any
questions you may have.
What would you like to explore?
Explore Lounges
Explore Dressing Rooms
Explore Bedrooms
Explore Courtyard
Ask Anna a question



label mainloop:


You’re back in the lounge of the Pleasure
Club.
The ladies of the club have noted your
presence and make seductive gestures
your way.
What would you like to explore?
Explore Lounges
Explore Dressing Rooms
Explore Bedrooms
Explore Courtyard
Ask Anna a question

    jump gameloop



label anna_questions:
Q Can you tell me about the areas?
A Sure. The Lounges here is the starting
point and has a general palette of common
kinks.
In the Dressing Rooms, you may find more
of things involved with femdom, role
reversal, crossdressing and other fun things.
The Bedrooms is where usually more
passionate and fierce things happen.
The Courtyard features more alternative and
special experiences. If its exotic you’re
looking for, you might find something excited
there.
Then again, each of these places are not
strictly locked to a theme. Its all mixed and
shuffled.
You’ll never know what you’ll be getting
yourself into until you interact with each lady
a bit deeper.
Some ladies may offer the opposite of what
the place usually offers, so ultimately each
lady is a surprise of their own.
Also some ladies may have you change
locations during a fun session, so even then
you never know where you’ll eventually end
up.
Usually you’ll be able to get a gist of what it’ll
be based on your initial introduction with
them, but they may not reveal everything
right away.
Finding out is part of the fun, but we promise
you’ll have a good time nonetheless with
any of them, she reassures you with a
genuine smile.
If at any point you feel like something is not
your thing, don’t hesitate to back off. No one
will be upset or get mad if you do. Everyone
has their subjective tastes and we respect
your freedom to choose.
Thought some ladies might challenge you and not give you up so easily, but thats also part of the fun, she grins at you with a suggestive look.


#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
# Construction Pieces:
#####################################
#####################################
#####################################


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


# " A [enemy] approaches!"
nvl clear
b " [edescriptl] [fgheight]\n \n The [enemy]'s health is [ehlth] of [ehlthmax], and their skill rating is [eskill]. \n \n Your health is  [chlth] of [mxhlth], and your skill is [pskill]. Your lust is [lust] out of [maxlust]."

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
