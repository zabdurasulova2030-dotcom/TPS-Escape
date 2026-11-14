default alibek_like = 0
default height = 0
default money = 0
default jump_counter = 0
default drink = 0
default first_jump = False

image ending1 = Text("Ending1. Good ending. You decided not to jump that time and spend the rest of your academic years without getting in trouble anymore until you graduated. Good job!", size=40, color="#FFFFFF")
image ending2 = Text("Route2. Bad ending. You decide to jump that time and Alibek aka caught you.", size=40, color="#BF0000")

define r = Character("You", color="#696969")
define uk = Character("Unknown Person", color = "#000000")
define el = Character("Elshod", color = "#38702E")
define al1 = Character("Unknown Person", color = "#BD3737")
define al = Character("Alibek aka", color = "#BD3737")

init python:
    slurs = {
        "Shit", "SHIT", "shit", "Fuck", "fuck", "FUCK", "Ass", "ass", "ASS", "Bitch", "bitch", "BITCH", "Motherfucker", "motherfucker", "MOTHERFUCKER", "Slut", "SLUT", "slut", "Bitch", "BITCH", "bitch"
    }

    character = {
        "Alibek aka", "ALIBEK AKA", "alibek aka", "Alibek Aka", "Elshod", "ELSHOD", "elshod"
    }

    renpy.music.register_channel("lofi song", mixer="music", loop=True)

label start:
    scene black 
    
    "This game is made by Rustamova Ruhshona, Abdurasulova Zaynabbegim, Toshmatova Sevinch and Begmatova Muhabbat"
    "Your default name is \"Ruhshona\" and your pronouns are she/her. You can change your name during playtime"
    "Have a good time playing our game!"

    scene bg school_outside:
        zoom 1.5

    show rusha excited1 at truecenter:
        zoom 1.8
    with dissolve
    
    r "\"I am finally here!\""
    r "I am so excited to study in my new school. I heard that it has very good conditions and atmosphere!"

    scene bg school_outside1 with dissolve:
        zoom 1.5

    show rusha excited1 at truecenter:
        zoom 1.8

    r "\"Unfortunately I was sick and I couldn't come in the start of the year, but its okay!\""
    "You look around. You don't see much people. But you don't seem to care. Your new school looks..."
    "Awesome!"

    scene bg school_outside2 with dissolve:
        zoom 1.5

    show rusha excited1 at truecenter:
        zoom 1.8

    play music "walking on stones.mp3" volume 1.7
     
    "You pass through guards. They know who you are and nod to you"

    stop music 

    "Then..."

    play music "walking on kafel.mp3" 

    scene bg elshodneutral with dissolve:
        zoom 1.5

    el "\"Hello, new student!\""

    stop music 

    "This must be Elshod! He is the student council president in TPS and he needs to introduce the school to you"
    el "\"Welcome, to our school!\"" 

    scene bg elshoddown with dissolve:
        zoom 1.5

    el "\"Would you like me to introduce you to our school?\""
    
    menu: 
        "\"Yeah!\"":
            jump continue

    label continue:
        el "\"Great\""
        el "\"What is your name?\""

        jump name

        label name:
        
            python:
                player_name = renpy.input("What is my name?", length=20, default="Ruxshona").strip()

            if player_name in slurs:
                $ alibek_like -= 3 

                scene bg elshodangry:
                    zoom 1.5

                el "\"Hey! You can't say that!\""

                jump name

            if player_name in character:
                "This character already exists in the game. It is recommended to pick a new name for yourself."

                "Would you like to change your name?"

                menu:
                    "No":
                        jump game_start

                    "Yes":
                        jump name

        label game_start:
            scene bg elshodneutral with dissolve:
                zoom 1.5
            el "\"Great!\""
            el "\"Nice to meet you [player_name]. As you already might know my name is Elshod and I am students council president in the TPS\""
            el "\"I will be introducing our school to you\""
            r "\"Thanks!\""
            uk "\"Hey! Elshod! Come here it is urgent!\""
            
            scene bg elshoddown:
                zoom 1.5
            
            el "\"Oh no!\""
            r "\"...\""
            r "\"It's okay you can go!\""

            scene bg elshodneutral:
                zoom 1.5

            el "\"Really?\""
            r "\"Yeah, I can explore the school on my own!\""
            el "\"Thanks. Sorry for inconvinience\""
            el "\"Good luck!\""
            r "\"Yeah, thanks!\""
            "You are turning away to go"
            el "\"Wait!\""
            r "\"What?\""
            el "\"Beware of the Alibek aka! He is the staff in the school and he doesn't like students misbehavnig\""
            r "\"I won't be misbehaving\""
            el "\"Great, then!\""
            el "\"Goodbye!\""

            play music "walking on kafel.mp3"

            scene bg besh tashabbus4:
                zoom 1.5

            "You are now standing in the beginning of the long hallway."
            r "\"Wow!\""
            "Again, your new school is very good compared to your old one. Even some strict staff member cannot ruin this very moment"

            scene bg besh tashabbus3:
                zoom 1.5

            play music "walking on kafel.mp3"

            "You walk closer to the end of the hallway and notice a door leading into a glass classroom. The glass is covered in posters probably made by students"

            scene bg besh tashabbus3:
                xalign 0.5
                zoom 2.0

            play music "walking on kafel.mp3"
            
            "You walk towards the door. The room looks like its empty"

            scene bg door opening1:
                zoom 1.5

            play music "door opening attempt.mp3"

            "You try to open the door"

            scene bg door opening:
                zoom 1.5

            "The door is locked"

            scene bg door opening1:
                zoom 1.5
            
            r "\"Oh...\""
            r "\"Looks like it is locked\""

            scene bg besh tashabbus2:
                zoom 1.5

            r "\"Let's go then\""

            scene bg signs:
                zoom 1.5

            play music "walking on kafel.mp3"

            "You look up and see signs showing you directions"
            "How tall are you?"

            menu:
                "\"Tall\"":
                    $ height += 2 
                    jump scene_signs

                "\"Normal\"":
                    $ height += 1 
                    jump scene_signs

                "\"Short\"":
                    $ height -= 1
                    jump scene_signs

            label scene_signs:
                if height == 2:
                    "You knew you were tall so you knew you could easily reach them"

                elif height == 1:
                    "Despite your height being medium for your age, you knew you could reach the signs if you tried hard enough"

                else:
                    "Despite your height being lower for your age, you wanted to know if you could reach the signs"

                "For each jump, you get money that you can use in the vending machine which sis located in the canteen"
                "However, you remember words of Elshod"
                "You were supposed to beware of Alibek aka, who doesn't like students misbehaving"
                "So..?"
                "Should you jump?"

                menu:
                    "\"Yes. I should jump\"":
                        $ jump_counter +=1
                        $ alibek_like -= 2
                        $ first_jump = True
                        jump money_interval

                    "\"No. I should not jump\"":
                        $ alibek_like += 2
                        jump money_interval2
                
                label money_interval:
                    play music "jump.mp3" volume 1.2

                    "You got 10,000 so'ms! Your total money is now 10,000 so'ms"

                    jump scene_jump

                label money_interval2:
                    "You didn't get any money because you did not attempt to jump"

                    jump scene_nojump

                label scene_jump:
                    "You jump"
                    "And..."
                    if height == 2:
                        "You reach the signs easily. Even without putting much effort in it. For you, the limit is the sky"
                        
                        jump alibek_caught

                    elif height == 1:
                        "You reach the signs! You cannot say that was very easy to you, but it was definetly a doable thing if you put enough effort in it"
                        
                        jump alibek_caught

                    else:
                        "You don't reach the signs. Your hand hits warm, school air. Even if you tried to jump as high as you can, the limit is you, not the effort you put in"
                        "You sigh"

                        jump alibek_caught

                    label alibek_caught:
                        "But then..."
                        al1 "\"What are you doing?\"" with vpunch
                        "You turn around and see..."

                        show alibek aka neutral at truecenter:
                            yalign 0.5
                            zoom 1.7

                        "Is that..?"
                        "Is that Alibek aka?"

                        hide alibek aka neutral

                        show alibek aka speak at truecenter:
                            yalign 0.5
                            zoom 1.7

                        al "\"What are you doing? Are you not listening to me?\""

                        hide alibek aka speak

                        show alibek aka neutral at truecenter:
                            yalign 0.5
                            zoom 1.7

                        r "\"I was...\""
                        r "\"I was just...\""
                        r "\"I am sorry\""

                        hide alibek aka neutral

                        show alibek aka speak at truecenter:
                            yalign 0.5
                            zoom 1.7

                        al "\"I don't want to see you doing this ever again, understood?\""

                        hide alibek aka speak 

                        show alibek aka neutral at truecenter:
                            yalign 0.5
                            zoom 1.7

                        r "\"Yes sir...\""
                        
                        hide alibek aka neutral with fade

                        "Alibek aka went away."
                        "Screw it! First day and you were already caught misbehaving by Alibek aka."
                        "You decided to be more careful next time."
                        
                        jump scene_nojump
                    
                    label scene_nojump:
                        scene bg besh tashabbus2 with dissolve:
                            zoom 1.5

                        "You finally reach the end of the hallway"
                        "There you see a a text \"Besh Muhim Tashabbus\" and a lot of photos around it. Those photos are photos of the students and graduates of the school"
                        "You don't really spend a lot of time looking at the old photos and go\""

                        scene bg room105 with dissolve:
                            zoom 1.5

                        "You see an art exhibition and some other staff rooms. You didn't really care about them and decided to head back"
                         
                        scene black

                        scene bg signs2 with dissolve:
                            zoom 1.5

                        "You see signs"
                        "Again"
                        
                        $ money += 15000

                        "Each time you jump, you get money!"

                        if jump_counter == 0:
                            "This time an urge to jump is much higher and you don't resist it"
                            "But before that you look around and see nobody"

                            play music "jump.mp3" volume 1.2

                            "You jump and..."
                              
                            if height == 2:
                                "You got 15,000 so'ms! Your total money is 15,000 so'ms"
                                "You reach the signs easily. Even without putting much effort in it. For you, the limit is the sky"

                            elif height == 1:
                                "You got 15,000 so'ms! Your total money is 15,000 so'ms"
                                "You reach the signs! You cannot say that was very easy to you, but it was definetly a doable thing if you put enough effort in it"

                            else:
                                "You got 15,000 so'ms! Your total money is 15,000 so'ms"
                                "You don't reach the signs. Your hand hits warm, school air. Even if you tried to jump as high as you can, the limit is you, not the effort you put in"
                                "You sigh"

                        else:
                            "Even if you were caught by Alibek aka, the urge to jump is impossible to ignore and you don't resis it"
                            "But before that you look around, your eyes trying to find Alibek aka, but you see nobody"
                            "You jump and..."
                            if height == 2:
                                "You got 15,000 so'ms! You total money is 25,000 so'ms"
                                "You reach the signs easily this time too. Even without any effort"

                            elif height == 1:
                                "You got 15,000 so'ms! You total money is now 25,000 so'ms"
                                "You reach the signs this time too! Again, it wasn't very easy, but it was a possible thing."

                            else:
                                "You got 15,000 so'ms! Your total money is 25,000 so'ms" 
                                "You..."
                                "Reach the signs! This time, your hands finally brushed against plastic sign, but even this light touch brought you happiness"

                        "Now after jumping without being caught by Alibek aka, you head towards the canteen"

                        scene bg oshxona:
                            zoom 1.5

                        play music "walking on kafel.mp3"

                        r "\"Looks like I am in the canteen\""

                        scene bg vending machine side:
                            zoom 1.5

                        play music "walking on kafel.mp3"

                        r "\"Wow! That's a vending machine.\""

                        scene bg vending machine:
                            zoom 1.5

                        play music "walking on kafel.mp3"

                        r "\"Ughh...\""
                        r "\"I am very hungry right now\""

                        scene bg vending machine buttons:
                            zoom 1.5

                        r "\"I should buy something for myself\""
                        r "\"Hmm... How much money do I have?\""
                        r "\"Oh...\""

                        if first_jump == True:
                            r "\"Oh, I have 25,000 so'ms\""
                        else: 
                            r "\"Oh I have 15,000 so'ms"
                        r "\"That's not bad\""
                        r "\"What should I buy? I have [money] so'ms\""

                        jump vending_machine

                        label vending_machine:
                                menu:
                                    "Chips. Cost:25,000 so'ms":
                                        jump chips_int

                                    "Soda. Cost: 10,000 so'ms":
                                        jump soda_int

                                    "Chocolate. Cost: 15,000 so'ms":
                                        jump chocolate_int

                                    "Candy bag. Cost 5,000 so'ms":
                                        $ drink += 1
                                        jump candy_int

                                label chips_int:
                                    if first_jump == True:
                                        show chips bag at truecenter:
                                            yalign 0.5
                                            zoom 0.6
                                    
                                        r "\"Yay! I finally bought some food!\""
                                        "You eat the chips and go explore the rest of the school"

                                        jump next_jump

                                    else: 
                                        "You don't have enough money to buy that"

                                        jump vending_machine

                                label soda_int:
                                    show soda can at truecenter:
                                        yalign 0.5
                                        zoom 1.5

                                    r "\"Yay! I finally bought a bevarage!\""
                                    "You drink your soda and go explore the rest of the school"

                                    jump next_jump

                                label chocolate_int:
                                    show chocolate bar at truecenter:
                                        yalign 0.5
                                        zoom 1.5

                                    r "\"Yay! I finally bought some food\""
                                    "You eat your chocolate and go explore the rest of the school"

                                    jump next_jump

                                label candy_int:
                                    show candy bag at truecenter:
                                        yalign 0.5
                                        zoom 1.5 

                                    r "\"Yay! I finally bought some food\""
                                    "You eat your candies and go explore the rest of the school"

                                    jump next_jump
                                
                                label next_jump:
                                    scene bg vending machine with dissolve:
                                        zoom 1.5

                                    if drink == 1:
                                        "After you are done drinkning your soda, you head out of the canteen to the hallway"

                                    else:
                                        "After you are done with easting your food, you head out of the canteen to the hallway"

                                    scene bg signs3:
                                        zoom 1.5

                                    "There you see the sign again"

                                    scene bg signs33:
                                        zoom 1.5
                                    
                                    "Should you jump this time too?"
                                    
                                    menu:
                                        "Yes":
                                            jump sign_jump

                                        "No":
                                            jump sign_nojump

                                    label sign_nojump:
                                        scene black

                                        "You decided not to jump. If you weren't caught last time, doesn't mean you should repeat it again and again"
                                        "You were smart enough to understand from the first time"

                                        show ending1 at truecenter 
                                        with fade
                                    
                                    label sign_jump:
                                        scene black

                                        "You decided to jump"

                                        play music "jump.mp3" volume 1.2
                                        "You reach the signs easily. You are already used to it"
                                        al "\"Looks like you didn't learn your lesson...\"" with vpunch
                                        "You slowly turn back and see..."
                                        
                                        play music "scream.mp3"

                                        scene bg signs33:
                                            zoom 1.5

                                        show alibek aka final straw at truecenter:
                                            zoom 2.0

                                        "Alibek aka"

                                        stop music 
                                        al "\"{b}{color="#B00000"}{shader=jitter}I already told you that I didn't want to see you jump anymore\"{/b}{/shader}"
                                        r "\"I-I...\""
                                        r "\"I am sorry\""
                                        al "\"{color=#B00000}Your words won't help you\""
                                        al "\"{color=#B00000}You were a very bad kid\""
                                        al "\"{color=#B00000}Now, I have to lock you in the dormitory\""
                                        r "\"No... P-please no!\"\""
                                        al "\"{color=#B00000}Muhahahahahahha\""
                                        
                                        scene black
                                        "This is the end of the Day1 of the \"TPS Escape!\""
                                        
                                        show ending2 at truecenter
                                        with fade

                                        "You played by the second route"