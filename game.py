#constants
C_BEGIN = "1"
C_EXPLANATION = "2"
C_EXIT = "3"
C_EXPLORE_BATMAN = "1"
C_STR_SCRSM_JESSICA = "2"
C_HOUSEWIFE_STORY = "3"
C_WINNIE_POOH = "4"
C_SANTA = "5"


#this functions prints the menu and asks for input  
def get_menu_option():
	print("\n-----The python challenge game------")
	print("MENU")
	print("(1) Begin")
	print("(2) Explanation")
	print("(3) EXIT")
	menu_option = input("CHOOSE:")
	return menu_option
#end get_menu_option()

def batman_story():
	print('Woohoo !! You are Batman\n')
	print('Congratulations! You are Batman, the legendary Dark Knight of Gotham City.')
	print('As Batman, you lead a fascinating life filled with thrilling adventures and heroic deeds.')
	print('By day, you are the enigmatic billionaire Bruce Wayne, but when the sun sets, you wear')
	print('the iconic black cape and cowl to protect the innocent and fight against injustice. Your arsenal')
	print('includes cutting-edge gadgets, unmatched combat skills, and an unwavering dedication to justice.')
	print('With your keen intellect and indomitable spirit, you patrol the shadows, ensuring the safety')
	print('of Gotham\'s citizens. As Batman, you inspire hope and strike fear into the hearts of criminals.\n')
	print('Embrace your destiny, for you are the hero that Gotham needs!')

	#second level decision
	print('Now comes an important decision: who would you like to defend Gotham from:')
	print('1: The Joker')
	print('2: The Riddler')

	sel_option = input ('CHOOSE:')

	if sel_option == "1":
		print("Dear Batman,")
		print()
		print("Your relentless pursuit of justice has led you to one of your greatest adversaries,")
		print("the Joker. This deranged and unpredictable criminal mastermind has wreaked havoc")
		print("upon Gotham City with his twisted schemes and diabolical laughter.")
		print()
		print("But fear not, for you are the Dark Knight, the one who stands between chaos")
		print("and order.")
		print()
		print("Your strategic mind and exceptional detective skills will be put to the test")
		print("as you engage in a battle of wits with the Joker. His elaborate traps and mind")
		print("games may challenge you, but your unwavering determination and commitment to")
		print("protect the innocent will guide you.")
		print()
		print("You know that defeating the Joker requires more than just physical strength.")
		print("It demands understanding the chaotic nature of his mind and finding ways to")
		print("outsmart him at every turn.")
		print()
		print("As he attempts to unravel the very fabric of Gotham's sanity, you will rise")
		print("above, bringing justice to his twisted reign.")
		print()
		print("Remember, Batman, you are the symbol of hope, the guardian of Gotham. With")
		print("every step you take, every punch you throw, and every brilliant deduction you")
		print("make, you will inch closer to dismantling the Joker's web of madness.")
		print("Gotham is counting on you, for only you possess the strength and determination")
		print("to overcome this notorious nemesis.")
		print()
		print("Stay vigilant, Batman, and may the night guide you to victory.")
		print()
		print("Sincerely,")
		print("Your faithful ally")
	elif sel_option == "2":
		print("Dear Batman,")
		print()
		print("Your relentless pursuit of justice has led you to one of your greatest adversaries,")
		print("the Riddler. This enigmatic and cunning criminal mastermind has plagued Gotham City")
		print("with his mind-bending puzzles and riddles.")
		print()
		print("But fear not, for you are the Dark Knight, the one who stands between chaos")
		print("and order.")
		print()
		print("Your strategic mind and exceptional detective skills will be put to the test")
		print("as you engage in a battle of wits with the Riddler. His intricate enigmas and")
		print("twisted games may challenge you, but your unwavering determination and commitment")
		print("to protect the innocent will guide you.")
		print()
		print("You know that defeating the Riddler requires more than just physical strength.")
		print("It demands deciphering his cryptic messages and unraveling his intricate schemes.")
		print()
		print("As he weaves his web of riddles, you will rise above, bringing justice to his")
		print("puzzling reign.")
		print()
		print("Remember, Batman, you are the symbol of hope, the guardian of Gotham. With")
		print("every step you take, every clue you solve, and every strategic move you make,")
		print("you will inch closer to dismantling the Riddler's web of perplexity.")
		print("Gotham is counting on you, for only you possess the intellect and determination")
		print("to overcome this cunning nemesis.")
		print()
		print("Stay vigilant, Batman, and may your sharp mind guide you to victory.")
		print()
		print("Sincerely,")
		print("Your faithful ally")

#Jessica Jones story
def jessica_jones_story():
	print("""Good Choice! You are Jessica Jones, sitting down in a bar and enjoying your favorite drink.
		  When a big a big fellow walks in, sits down next to you and starts talking.""")
	#Options for how to react

	print("""The guy starts talking to you. What do you do now?""")
	choice = input("""
	(1) NOTHING
	(2) SARCASM
	(3) LEAVE
	=== """)
	if choice == '1':
		print ("""You ignore the guy and have another sip of your drink, why bother?
			   He does not like being ignore and insists on starting a bar fight. You leave your favorite bar in bad shape""")
		print ('Your favorite bar is ruined for days - time to find a new spot.')
		print ('Regret your super hero choice - try again.')

	elif choice == '2': # Give a snarky comment
		print ('You make a snarky comment and the guy leaves. Finally you can enjoy your drink in peace.')
		print ('ANOTHER EVENTLESS EVENING IN YOUR FAVORITE BAR.')
		print ('Regret your super hero choice - try again.')
	elif choice =='3': # Just go home
		print ("""You are not up for dealing with people and decide to drink in the comfort of your own home.""")
		print ("ANOTHER EVENTLESS EVENING IN THE COMFORT OF YOUR OWN HOME.")
		print ('Regret your super hero choice - try again.')
	else:
		print('what else do you want to do - pick again')

#housewife story	
def housewife_story():    
    print("Great choice. You are Mrs. Cleanington, and you are on your epic journey to conquer the chaos in your home. Armed with your trusty vacuum cleaner and other magic devices start on your heroic journey")
    #### Housewife
    ###Chose location actions of Mrs. Cleanington

    location=input ("""Choose the Battlefield:
    1. Livingroom
    2. Kitchen
    3. Bathroom
    4. I am advanced in epic cleaning, I choose Super Level
    """)
    ### Living room actions
    if location == '1':

        print ("Welcome to the 'Livingroom Cleaning: Lounge Chaos' level! You have to do justice and return each item to its right place in the living room!")

        livingroom_challange = input("""Where do we start?
        1. Challenge the mysterious cables
        2. Your AI robot is trying to take your Playstation under his control. You need to hurry and cancel the Robots Uprise
        3. Save from collapse the biggest books-pisa-tower
        """)

        if livingroom_challange== '1':
            print ("Congratulations you have found a new super power, now you will definitely find the way out of the cable jungles")
        elif livingroom_challange =='2':
            print("Congratulates. You have gained a new super power, now it's in your power to turn off the technical equipment from the network and delay Robots disobedience")
        elif livingroom_challange== '3':
            print ("Congratulations you have gained a new super power, now you can build stable towers from books and other objects")
        else:
            print("Please make your choice")

    ### Kitchen actions
    elif location == '2':
        print("Welcome to the 'Kitchen Cleaning: Ultimate Chaos' level! Here you will dive into an exciting adventure to free your kitchen from madness and turn it into a true culinary paradise!")
        kitchen_challange=input("""Where do we start?
        1. Defeat the mountain of dirty  dishes
        2. Clean dirt and arrange chaos on the table
        3. Master the sorting garbage and getting rid of it
        """)
        if kitchen_challange== '1':
            print ("Congratulations. You have now learned how to load dishes into the dishwasher and to turn it on. Now its is your new superpower")
        elif kitchen_challange =='2':
            print("Congratulates on your new superpower, you have learned to use a magic rag")
        elif kitchen_challange== '3':
            print ("It was not easy, but you've managed it. Bring your knowledge to the world")
        else:
            print("Make your choice")

    ### Bathroom actions
    elif location == '3':
        print ("Welcome to the level 'Bathroom Cleaning: Bathing Mess'! Here you will find a journey into the world of unstoppable fun of tile washing and scraping")

        bathroom_challange=input("""Where do we start?
        1. Collect rubber ducks
        2. Mysterious spots on the mirror are trying to send you a secret message from a parallel world. Clean it
        """)

        if bathroom_challange== '1':
            print ("Congratulations, you have got a new super power, now you are proficient in collecting and arranging yellow objects")
        elif bathroom_challange =='2':
            print("That's right, it's better not to open pandora's box, thanks for closing a portal to another world")
        else:
            print("Make your choice")

    ### super level choice
    elif location == '4':
        print ("Welcome to the Super Level 'Resident Evil: Uninvited guests'! Here you will find a real battle not only for cleanliness and order in the house, but also for the title of Master of the house. In the bedroom, you have found a real cockroach party!")

        action_choice=input("""You ran out of insect deactivation tools (DeBugging). What will you do?
        1. Look with wide open eyes into the face of Danger, Scream and Run away, hoping they will be paralyzed by my Ultrasound
        2. Take a call and fight in an unequal battle and possibly die a hero's death
        3. Upgrade your skills before the final fight for life and death
        """)
        ### ultrasound
        if action_choice == '1':
            print("Sorry to hear that, but you have just lost your beautiful house. Enemies are celebrating victory. But you do have a very beautiful voice. Try to develop your Ultrasound super power and next time for sure you will win")
        ### fight
        elif action_choice == '2':
            print("Great choice. Let's get ready to Rumble")

            deep_action=input("""Chose your way:
            1. I will use a mean of mass knockout
            2. I will ask them politely to leave my house
            """)

            ### knockout (vacuum cleaner and flip flop)
            if deep_action == '1':
                print("Chose your method.")
                mass_knockout=input("""What will it be?
                1. Vacuum cleaner
                2. Flip flop
                """)
                ### vaccum cleaner
                if mass_knockout == '1':
                    print("It's a Victory. You did it. The house is yours, you have protected it")
                ### flip flop
                elif mass_knockout == '2':
                    print("It's a Victory. You did it. The house is yours, you have protected it")
                else:
                    print("Don't panic. You are on the right way. Soon this nightmare will end. Just make a choice")

            elif deep_action== '2':
                print("You have excellent interpersonal communication and negotiation skills, soft skills lessons did actually healped you, congratulations they are gone.")
            ### upgrade skills
            elif action_choice == '3':
                print("Great choice. Choose a course on means of mass knockout")
                course_action=input("""What do you prefer?
                1. 'The secret code of the vacuum cleaner' - at the end of the course you will receive a certificate of a professional vacuum cleaner, and you will learn the secret functions and life hacks.
                2. 'Deadly flip flops' - at the end of the course you will receive a certificate of a professional flip flopper, and you will learn secret functions and life hacks
                """)
                ### vacuum cleaning course
                if course_action == '1':
                    print("Congratulations. you passed the express course. the certificate will be emailed")
                    action_after_course=input("""Now you're ready for the real fight:
                    1. Nothing going to stop me. Its my house. Where is my vacum cleaner?
                    2. I'll better pray
                    """)
                    ### actos after vaccum cleaner course
                    if action_after_course == '1':
                        print("Congratulations. You have won this battle")
                    elif action_after_course == '2':
                        print("Sorry to admit, but these super powers are not for you. Game over")
                    else:
                        print("Just take the last step. You are so close to victory")

                ### flip flop course
                elif course_action == '2':
                    print("Congratulations. you passed the express course. the certificate will be emailed")
                    action_after_course=input("""Now you're ready for the real fight:
                    1. Nothing going to stop me. Its my house. Going to look for my flip flops
                    2. I'll better pray
                    """)
                    ### after flip flop course
                    if action_after_course == '1':
                        print("Congratulations. You have won this battle")
                    elif action_after_course == '2':
                        print("Sorry to admit, but these super powers are not for you. Game over")
                    else:
                        print("Just take the last step. You are so close to victory")
        else:
            print("I know you have a panic attack and scared to death but you have to make this choice. So what will it be?")

    ### no point of desnitation
    else :
        print("You still dont have point of destination. Please choose a number")

def winnie_pooh_story():
	print("""Great choice!
	You are Winnie Pooh and you are doing what you like most,
	laying in your comfy bed and  eating a big jar of honey.
	Suddenly you hear a noise. A bee is in your house, looking for the honey you just stole from her.
	What do you do? """)
	winnie_choice=input("""
	1)HIDE
	2)GO AND TALK TO HER
	3)FIGHT
	=== """)
	if winnie_choice=="1":
		print("As soon as you noticed the bee, ")
		print("you immediately hide under your bed and wait until she leaves")
	elif winnie_choice=="2":
		print("As a polite guy you are,you know that the communication is the key.")
		print("You decide to talk to her and explain why you stole her honey. ")
	elif winnie_choice=="3":
		print("You get angry why she entered your property without knocking first.")
		print("Comme on, somebody gotta show her who is the boss of the house.")
	else:
		print("Please choose a correct number!")

#santa story
def santa_story():
    print("Congratulations - you're Santa Claus and know if Children have been naughty or nice. On Christmas  you put on your red suit and spill the beans about how kids, and adults, behave on Santa's lap.")
    santa_input = input("""What do you want to do?
        1) Make children happy!
        2) Make children unhappy!
          """)
    if santa_input == "1":
        print("THE KIDS ARE LOVING YOU!")
    elif santa_input == "2":
        print("THE KIDS HATE YOU! THANK YOU FOR NOTHING SANTA")
#end santa story

#this function prints a text depending to choice selected by user
def print_selection (curr_option):
	if curr_option == C_BEGIN:
		#code for Begin
		#print("The game is to biuld this game. And seems to be working!") 

		super_power = input("""Please pick your super power :
		1) To explore
		2) Super strength and sarcasm
		3) Make order out of chaos
		4) Eat honey all day
		5) Make children happy or unhappy
		=== """)

		#play selected story
		if super_power == C_EXPLORE_BATMAN:
			batman_story()
		elif super_power == C_STR_SCRSM_JESSICA:
			jessica_jones_story()
		elif super_power == C_HOUSEWIFE_STORY:
			housewife_story()
		elif super_power == C_WINNIE_POOH:
			winnie_pooh_story()
		elif super_power == C_SANTA:
			santa_story()


	elif curr_option == C_EXPLANATION:
		#code for explanation
		print("This is the explanation of how the game works ;)")
		print("If you select option 1 from main menu, the guided strory begins")
		print("There are different stories and each has different options, you will")
		print("be guided through the process all along.")
		print("\nHAVE FUN!!! :)")
	else:
		#ask for a valid option
		print("Please choose a valid option from the menu")
#end print_selection()

#start of the main program----------------------------------
current_option = get_menu_option()

while current_option !=C_EXIT:

	#print selected option 
	print_selection(current_option)
	
	#ask for next option    
	current_option = get_menu_option()

#exit loop    

#print exit titles and finish program
print("Exiting game, have fun!")

#end of the main program-----------------------------------
