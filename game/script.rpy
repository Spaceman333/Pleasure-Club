#######################
#######################
####### DEFINES #######
#######################
#######################

#Player Character
define p = Character("You", color="#c8c8ff")
#define pn = Character('[playername]', color="#CDA559") #alt player

#Encounter Characters
define unk = Character('???', color="#CDA559") #mysterious unknown character - use in surprise ECs!
define an = Character('Anna', color="#CDA559")
define dr = Character('Dryad', color="#CDA559")
define bo = Character('Bouncer', color="#CDA559")


#######################
#######################
##### INIT PYTHON #####
#######################
#######################

# init python:

    #incase I need it, might delete lol




#######################
#######################
######   START  #######
#######################
#######################

label start:

    #Init flag variables

    # Skips
    # $ global intro_passed = False
    # $ global interview_passed = False
    # $ global ritual_completed = False

    # Player neuromancy
#    $ global player_tutor_unlocked = False
#    $ global player_tutor_studied = False

    # Anna
#    $ global ceo_anna_s1 = False

    # Lounge
#    $ global lounge_dryad_s1 = False

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

    jump skiptutorial


label skiptutorial:

    menu:
        "Have you ever played Renpy visual novels before?"

        "No - Do a quick tutorial":
            jump tutorial
        "Yes - I know the controls, skip this":
            pass

    menu:
        "But, do you know what this game's premise is about?"

        "No - Explain premise":
            pass
        "Yes - Skip it":
            jump aftertutorial

    "In this particular VN, you play as yourself and are taken on a journey to explore the magical Pleasure Club."

    "Set in the modern day world, but with a twist of the world being a safe peaceful place and the magic of neuromancy being real."

    "Neuromancy is the magic of affecting the mind. Be it your own mind and/or the mind of another person, making them see and feel things - as if transported to another world."

    "The feeling is sort of like hyper-realistic Virtual Reality (VR) experience, but done through magical touch."

    "The neuromancer and their companion share a unique world in a pocket dimension together. Both feel, sense and see things around them as if they were really there."

    "That said, while the visions and feeling may be imagined, the experienced sensations and orgasms are real."

    "This magic is safe and only works if both people willingly choose to do it. The worst that can happen is temporary fainting or exhaustion from too much pleasure at once."

    "In the club, you will encounter interesting characters with whom you'll do lovely magical sexy fun things together."

    "There is no ending to this game, its more a thing you return to again and again, when you feel like it."

    "Saving and exiting the game means leaving the club, while restarting the game and loading a save means coming back to the club."

    "The only goal in this game is to try everything you find interesting and later repeat the scenes you loved the most."

    "There are number of unique neuromancers you can visit and do sessions with, each offering multiple scenes that unlock as you complete them."

    "There is even a possibility of becoming a neuromancer yourself too! I'll let you discover that part on your own. ; )"

    jump aftertutorial


label tutorial:

    "To advance through the game, mouse left-click or press the Space or Enter keys. Try this now."

    "In a visual novel game, you read text and look at images. Occasionally there are choices you can make that affect the story."

    "In this particular VN, you play as yourself and are taken on a journey to explore the magical Pleasure Club."

    "Set in the modern day world, but with a twist of the world being a safe peaceful place and the magic of neuromancy being real."

    "Neuromancy is the magic of affecting the mind. Be it your own mind and/or the mind of another person, making them see and feel things - as if transported to another world."

    "The feeling is sort of like hyper-realistic Virtual Reality (VR) experience, but done through magical touch."

    "The neuromancer and their companion share a unique world in a pocket dimension together. Both feel, sense and see things around them as if they were really there."

    "That said, while the visions and feeling may be imagined, the experienced sensations and orgasms are real."

    "This magic is safe and only works if both people willingly choose to do it. The worst that can happen is temporary fainting or exhaustion from too much pleasure at once."

    "In the club, you will encounter interesting characters with whom you'll do lovely magical sexy fun things together."

    "There is no ending to this game, its more a thing you return to again and again, when you feel like it."

    "Saving and exiting the game means leaving the club, while restarting the game and loading a save means coming back to the club."

    "The only goal in this game is to try everything you find interesting and later repeat the scenes you loved the most."

    "There are number of unique neuromancers you can visit and do sessions with, each offering multiple scenes that unlock as you complete them."

    "There is even a possibility of becoming a neuromancer yourself too! I'll let you discover that part on your own. ; )"

    "Now a quick primer on useful controls..."

    "When playing the game, right-click or press the escape key to enter the game menu. Press same keys again to exit the menu."

    "In the escape menu, you can Save, Load or change options or exit the game."

    "Alt+f4 is a fast way to exit the game too. Please do not also shift+delete the game folder after doing so."

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

        "First time player - Recommended - Full experience.":
            jump intro
        "Skip to Sample - Skip intro, but still do the first sexy sample session.":
            jump lobbyentry
        "Skip to Club - Skip entire intro.":
            jump realstart


label intro:
    ###################
    #Story begins here
    ###################

    "You're reading an advertisement:"

    "{i}Come visit the magical Pleasure Club, a mature and safe setting for a variety of pleasant sexy services for adults!{i}"

    "{i}We offer magic enhanced love, sex and pleasure though all kinds of usual and unusual sexual acts and fantasies.{i}"

    "{i}Our speciality is the magic of neuromancy; an exotic technique that will stimulate every nerve in your body.{i}"

    "{i}Come and feel every nerve in your body pulsing with pleasure!{i}"

    "{i}Notice: Our services are available to customers over the age of 18. Please bring an ID to pass the entrance verification.{i}"

    p "Sounds interesting, might as well go try this."

    scene bg city
    with fade

    "Its night time in the city you live, the world is so peaceful and safe."
    "Recently this new Pleasure Club thing opened here and claims to offer sexual services - but using magic!"
    "Neuromancy in particular. Some sort of mind magic where the mage can stimulate a person's neurons directly through touch."
    "Sounds exciting and otherworldly, even a little intimidating due to how intense and otherworldly it can get."
    "People say the experience is like being teleported to another world where anything can take place."
    "All laws of physics can be bent and make things happen that would otherwise be impossible in real life."
    "The best part is that having an orgasm during a neuromancy session is literally having an orgasm in real life."
    "Effectively the wildest and tamest fantasies can be performed wherever you are, without actually having to go there."
    "To an outside observer, it just looks like two people holding hands and standing / sitting still."
    "But to the actual participants, they may be in a forest, on the moon, in a temple or at the edge of the universe."
    "Its like Virtual Reality, but far more advanced and done through magic without any special gear or equipment."
    "Luckily, its also entirely safe to do. As soon as either the neuromancer or the companion wants to stop the session, both return to normal almost immediately."
    "Its like turning the heat off on a stove to stop the water inside of a kettle from boiling any longer. With no more heat, the water just cools down again."
    "The 'worst' that can happen is temporarily fainting due to the brain unable to handle more pleasure."
    "Since fainting also stops the neural stimulation, one will only need to rest a short while and wake up again fully recovered."
    "Of course anything can be overdone, so its not advisable to keep getting knocked out over 10 times in a row every day for several weeks."
    "That might actually mess up the head in the long run and cause problems."
    "Then again, usually 1-3 sessions a day is more than enough to satisfy the need for sex, so normally its unlikely for a person to be able to ruin themselves that way."
    "After all, the person still needs to eat, sleep and rest between all of this to keep up, so naturally it all ends up being balanced without even trying."
    "Also at some point, the brain itself will subconsciously refuse to accept more neuromancy sessions until it has had enough rest as a self-preservation measure."

    "Feeling confidently secure with the information on neuromancy, you call the Pleasure Club and make a reservation."

    scene bg metro

    "Riding the local metro line to your destination, you feel excitement in your stomach. You've never done this before."
    "Reading some of the reviews and descriptions about the place, the session can be quite intense."
    "A magician essentially takes control of both of your and their shared neurons and creates sensations that feel like the real thing."
    "Even the neuromancer themselves feel anything you do to them in return, if you stimulate them too in the act."
    "Its not just you who is there. Its a shared moment where both are present."
    "That said its only the reality that is being shared, not each others feelings."
    "You can only feel what you feel and they can only feel what they feel."
    "A neuromancer does have the ability to read your feelings directly from your mind, so they do have that extra thing to them."
    "And they can also optionally merge both of your feelings to one, so that both or one of you can experience what the other person is sensing."
    "But unless the neuromancer specifically does this thing, they won't know or feel your orgasm as much as you won't feel their orgasm."

    p "Looks like this is my stop."

    "You get off the metro train and walk to the address you marked down."

    scene bg outside

    "This seems to be the place."
    "The entrance doesn’t seem much on the outside. Just a blank wall with no windows facing this way, no neon signs, just a small sign besides the door."
    "= Pleasure Club - Welcome ="
    "Besides opening hours and contact information, theres nothing else printed on it."
    "Probably they’re keeping the appearance of the club subtle not to bother families with kids in the neighbourhood with public display of sexual services."
    "You spot few people go in and out, likely other customers judging by their looks. Seems like theres some life inside the building despite the boring exterior."
    "Theres a bouncer at the door. Looks like she’s making sure no one underage comes inside. Better get my ID ready."

    show bouncer
    with dissolve

    bo "Hello, anything I can do you?"
    p "Eyy whatcha got"
    bo "I dont know you, new here?"
    p "Yup."
    bo "Oh, well I work for the [[Pleasure Club]]. We run this base. May I see your card?"
    menu:
        "You hand the bouncer your ID. It says that you're..."

        "Over 18 years old":
            jump idabove
        "Not over 18 years old":
            jump idbelow

        #Answering 'no' doesn't mean the player is turned away. Instead, they're thanked for their honesty, told that the more important factors of entry is mental- and sexual-maturity, latter of which is commonly reached by boys around the ages of 12-16 or 10-14 by girls. By being honest, they're let in anyway but noted that if they haven't yet reached basic biological sexual maturity, then none of this will make sense to them.


label idabove:

    bo "Everything seems to be in order."
    bo "Well if you must, I can let you inside."
    p "Keep talking, I'm here."
    bo "Ok. So heres whats going on..."

    "The bouncer tells you that before you can use the services of the Pleasure Club, you must first talk to Anna, the head of the club."

    p "Good to know, thanks."
    bo "That's great, be seeing you!"

    "No idea what came over the two of you back there, but nevertheless you boldly step inside the club."
    "The bouncer waving at you with an Siriusly goofy smile as you pass them by. Hmm."

    # I swear *no one* is going to get that silly Freelancer reference.

    jump lobbyentry

label idbelow:

    bo "Looks like your age is less than what its technically supposed to be to enter this place."
    bo "At the same time, you had the courage to come all the way here and try entering anyway. I can respect that."
    bo "Tell you what, I can let you inside anyway, but I need you to be aware of something."
    p "..."
    bo "Honesty is a sign of maturity and maturity is the real reason for letting someone in."
    bo "And I assume you're atleast 12-17 years old right now."
    bo "If you're less than that... you're way too early to be here. You should really wait a few years in that case."
    bo "But anyway."
    bo "Age is merely an arbitrary number that we in society expect people to magically gain mental maturity at."
    bo "It doesn't work that way. We can't expect people to gain something if they never had anyone or anything teach them about it first."
    bo "Maturity of the mind is gained through education and information, not after you have a birthday at a certain age."
    bo "As for sexual maturity - a biological thing that is seperate from mental maturity, is commonly reached by boys around the ages of 12-16 or 10-14 by girls."
    bo "As long as you know what sex is and you are mature and respectful of others and you have awakened sexual desires, then you you'll be fine in here."

    "The bouncer tells you that before you can use the services of the Pleasure Club, you must first talk to Anna, the head of the club."

    bo "I hope you'll have a good time!"

    "You enter the club as promised."

    "Author's Note: Because this is a free offline game, I can't stop anyone underage from playing it. This is impossible to control."
    "Author's Note: Please play this game at a later time if you do not know what sex actually is. You may get into trouble in your community if you're under 16 and try play this game anyway."
    "Author's Note: I recommend an online search terms like \"what is sex\" and \"sexual positivity\" to learn more about sex from trusted sources."
    "Author's Note: Sex can be really fun, but it involves a lot of dangers that can make life difficult if you're not careful."
    "Author's Note: Watch videos, read articles, ask trusted experts on the subject and get the necessary information to know what you're getting into. Stay healthy, stay safe, be smart and prepared."

    jump lobbyentry


label lobbyentry:

    scene bg lobby

    "Stepping into the lobby of the club you encounter some serious looking sofas."
    "Sitting there you assume is Anna, the one the bouncer told you about."

    show anna
    with dissolve

    "Noticing you enter she gets up, walks up to you to greet you with a warm smile, while offering a handshake."
    an "Welcome to the Pleasure Club, my name is Anna and I'm the guide here."
    an "I take it you're here for our wonderful services?"
    p "Yes I am."
    an "Excellent. Is this your first time trying neuromantic sex?"
    p "Yes."
    an "Ok, that means I'll need to give you a basic sample session, so you'll know how it works when you meet the rest of our ladies."
    an "Is this okay with you?"
    p "You mean were gonna have sex now and here?"
    an "Oh yes! We'll keep it tame and simple for your first time, to get you used to the whole process."
    an "I'm thinking of a gentle handjob in a peaceful forest setting. You'll be a guy with a penis and I'll be milking you."

    menu:
        an "So what do you say, are you up for this?"

        "Yes please!":
            jump ritual
        "No, I've changed my mind. (end game instantly)":
            $ renpy.full_restart()


label ritual:

    an "Wonderful! Lets take a seat on these sofas, so were comfy and supported. Come with me."
    "The both of you take a seat close to one another and face each other."
    an "Ok. So the way this works is that I, as a neuromancer, will create and maintain a world that will be in."
    an "The idea is that we either sit, stand or lay close enough to touch each other."
    an "Bonus points for being seated on sofas or in a bed."
    an "If either of us faints, we'll safely land on something soft. Safety first!"
    an "In the pocket world that we'll go to, I will guide the session from beginning to the end."
    an "You'll be more on the recieving end of the experience, unless I compel you to do something too."
    an "If at any point you don't like where this is going, simply think really hard of leaving and the session."
    "Author's Note: This not an actual game mechanic, just lore."
    "Author's Note: Use the ctrl key or otherwise skip parts with left mouse button as usual to escape parts you don't want to do."
    an "This will quickly stop the process I'll lose my spell on you. You'll awaken back to \"reality\" soon after."
    an "But I'm sure you wouldn't want that anyway."
    "Anna smugly smiles with a wink"
    an "The actual session begins with the neuromancer and their companion being calm, relaxed and willing in their minds to what they are about to do."
    an "So lets forget our worries and get comfy."
    an "Then, we grab a hold of one another, touch each other in some way and let the magic flow through us."
    an "As the neuromancer, I invoke my powers and begin taking interfacing with your nervous system and connecting it with mine."
    an "As the companion, you simply let go and embrace my control, allowing me to take you wherever we'll go."
    an "The standard way to touch another for contact is to clasp our hands, so our finger intertwine."
    an "That way we have a solid grip on each other and maintain a connection more reliably."
    an "This is how it more or less will be the other neuromancer's you'll get to try at our club."
    an "Some of them may spice things up and break from the norm to give it their own personal touch, so expect surprises too."
    an "Ok, that covers everything."
    an "Lets begin. Time to clasp our hands."
    show zhands2
    with dissolve
    "Anna extends her hands in front of you, gesturing for you to clasp them."
    "Prompted, you grab her hands and you intertwine your fingers with hers."
    hide zhands2    #their hands open
    with dissolve
    show xhands2    #both hands intertwined
    with dissolve
    "With both of you holding each others hands, Anna looks directly at you in the eyes and smiles."
    an "Now relax and look into my eyes."
    "END OF TEST"
    return
