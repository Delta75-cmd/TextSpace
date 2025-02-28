endingCount = "23"

print("Welcome to TextSpace! A sci-fi text adventure. Background: You are an engineer on a spaceship where the crew is on a mission to colonize a new planet. You are the only crew member stationed on your half of the ship. Most other crew members are in stasis or on the bridge on the other end of the ship. (Only the first half is finished so far! So when making the first decision only going to the engine room will have complete paths!)")
print("\nYou are in a spaceship and the engine just failed.")
print("Will you go to the engine room or stay where you are? \n ('Q' for move or 'E' for stay)")
answer = input(">").lower()
if "q" in answer:
  #engine room
  print("\nYou are now inside of the engine room and the engine is smoking.")
  print("Will you try to repair the engine or try to start the engine? \n ('Q' for repair or E'for start)")
  answer = input(">").lower()
  if "q" in answer:
    #engine repair
    print("\nYou attempt to repair the engine but are missing some tools and parts.")
    print("Will you go into the storage room to find the tools or will you continue to try and repair the engine by yourself? \n ('Q' for storage or 'E' for continue)")
    answer = input(">").lower()
    if "q" in answer:
      #storage room
      print("\nYou walked into the storage room and found the tools and parts that you needed. You went back to the engine and continued to repair it.")
      print("You were repairing the engine and saw two switches. One was red and one was blue. Will you flip the red one or the blue one? \n ('Q' for red or 'E' for blue)")
      answer = input(">").lower()
      if "q" in answer:
        #red switch
        print("\nYou flipped the red switch and it started the engines fuel pumps. There was a leak and the fuel was pooling closer to a sparking wire.")
        print("Will you flip the red switch again or find a way to stop the sparking wire? \n ('Q' for flip again or 'E' for stop)")
        answer = input(">").lower()
        #flip again
        if "q" in answer:
          print("\nYou flipped the red switch again and stopped the fuel pumps but the fuel was still creeping closer to the sparking wire.")
          print("You can try to drain the fuel or you can run and let the fuel possible explode. \n ('Q' for drain or 'E' for run)")
          answer = input(">").lower()
          if "q" in answer:
            #drain
            print("\nYou opened the drainage valve and drained the fuel. The engine was still repairable but you could also just try to escape.")
            print("Will you try to repair the engine again or will you try to escape? \n ('Q' for repair or 'E' for escape)")
            answer = input(">").lower()
            if "q" in answer:
              #repair
              print("You continued to repair the engine and it was successful.")
              print("You can decide wether or not to keep monitoring the engine or return to your room. \n ('Q' for monitor or 'E' for return)")
              answer = input(">").lower()
              if "q" in answer:
                #monitor
                print("\nYou decided to keep monitoring the engine and it seemed to remain stable.")
                print("You can keep the engine running or shut it down just in case. \n ('Q' for keep running or 'E' for shut down)")
                answer = input(">").lower()
                if "q" in answer:
                  #keep running
                  print("\nYou kept the engine running for a while before a the engine's oxygen supply ran out and the engine started to fail.")
                  print("You could try flipped the blue switch or you could shut off the engine. \n ('Q' for flip or 'E' for shut off)")
                  answer = input(">").lower()
                  if "q" in answer:
                    #blue switch
                    print("\nYou flipped the blue switch and turned on the engine's oxygen pumps. Oxygen started getting pumped back into the engine and it was now fully operational.")
                    print("\nYou survived! ENDING 03 / ",endingCount)
                  elif "e" in answer:
                    #shut off
                    print("\nYou tried to shut off the engine but you had to choose wether to flip the green switch or the yellow switch. \n ('Q' for green or 'E' for yellow)")
                    answer = input(">").lower()
                    if "q" in answer:
                      #green switch
                      print("\nYou flipped the green switch and the engine slowly started to shut down. You now had to choose wether to turn the big valve or the small valve. \n ('Q' for big or 'E' for small)")
                      answer = input(">").lower()
                      if "q" in answer:
                        #big valve
                        print("\nYou turned the big valve which realeased a bunch of hot steam pressure and caused you to fall back into the engine")
                        print("\nYou died!")
                        input("EXIT>")
                      elif "e" in answer:
                        #small valve
                        print("\nYou turned the small valve which allowed for the engine to shut down.")
                        print("\nYou survived! ENDING 04 / ",endingCount)
                        input("EXIT>")
                    elif "e" in answer:
                      #yellow switch
                      print("\nYou flipped the yellow switch and it caused a large arc to get sent down the engine causing it to explode.")
                      print("\n You died!")
                      input("EXIT>")
              elif "e" in answer:
                #return to room
                print("\nYou return to your room and wait for a while. You hear a loud noise and you look outside. You see a large asteroid coming towards you.")
                print("You can try to escape or you can try to shoot it down. \n ('Q' for escape or 'E' for shoot)")
                answer = input(">").lower()
                if "q" in answer:
                  #escape
                  print("\nYou try to run and find the escape pods but the asteroid is too fast and collides with the ship.")
                  print("\n You died!")
                  input("EXIT>")
                elif "e" in answer:
                  #shoot down
                  print("\nYou ran into the gunners cockpit and sat down in the chair.")
                  print("You saw two large buttons on the control panel. One was red and one was blue. \n ('Q' for red or 'E' for blue)")
                  answer = input(">").lower()
                  if "q" in answer:
                    #red button
                    print("\nYou pressed the red button and fired a few small laser beams which did not effect the asteroid and it collided with the ship.")
                    print("\n You died!")
                    input("EXIT>")
                  elif "e" in answer:
                    #blue button
                    print("\nYou pressed the blue button and a large laser beam was charged up and fired at the asteroid and destroyed it.")
                    print("\n You survived! ENDING 01 /",endingCount)
                    input("EXIT>")
            elif "e" in answer:
              #escape
              print("\nYou tried to find your way to the escape pods.")
              print("You found a hallway with a set of two doors. One of the doors was locked while the other was unlocked. \n ('Q' for locked door or 'E' for unlocked door)")
              answer = input(">").lower()
              if "q" in answer:
                #locked door
                print("\nYou decided to go through the locked door but before you could open it you would need to find the code.")
                print("You could search the engine room or the storage room. \n ('Q' for engine room or 'E' for storage room)")
                answer = input(">").lower()
                if "q" in answer:
                  #search engine room
                  print("\nYou searched the engine room and found nothing.")
                  print("You ran out of time before you could search the storage room and the engine exploded.")
                  print("\n You died!")
                  input("EXIT>")
                elif "e" in answer:
                  #search storage room
                  print("\nYou searched through the storage room and found a piece of paper (CODE 1: '1'5'3'7') but you found another piece of paper (CODE 2: '6'4'9'8') you took both pieces of paper.")
                  print("You returned to the locked door and have a chance to enter one code or else the security will activate. What code will you enter? \n (Enter one code)")
                  answer = input("CODE>")
                  if answer == "6498":
                    #correct code
                    print("\nYou entered the correct code and the door opened into the security room. There was a few monitors with live security camera footage. There was also another door.")
                    print("Will you check the cameras or will you go through the door? \n ('Q' for cameras or 'E' for door)")
                    answer = input(">").lower()
                    if "q" in answer:
                      #check cameras
                      print("\nYou check the cameras and saw a path from the other door to the escape pods. You followed the path and found the escape pods.")
                      print("There were 4 escape pods. Which one will you choose? \n (Pick a number 1-4)")
                      answer = input("ESCAPE POD>")
                      if answer == "1":
                        #pod 1
                        print("\nYou chose escape pod 1 but that escape pod's engines were broken and the escape pod exploded.")
                        print("\n You died!")
                        input("EXIT>")
                      elif answer == "2":
                        #pod 2
                        print("\nYou chose escape pod 2 and it was successful. You mananged to escape the ship.")
                        print("\n You survived! ENDING 02 /",endingCount)
                        input("EXIT>")
                      elif answer == "3":
                        #pod 3
                        print("\nYou chose escape pod 3 but that escape pod's engines were broken and the escape pod exploded.")
                        print("\n You died!")
                        input("EXIT>")
                      elif answer == "4":
                        #pod 4
                        print("\nYou chose escape pod 4 but the circuits were fried so you couldn't leave. The escaped pod doors locked and you were now trapped inside of the escape pod.")
                        print("\n You died!")
                        input("EXIT>")
                      elif answer != "1" or "2" or "3" or "4":
                        print("\nYou couldn't decide which escape pod to take and ran out of time. The ship exploded.")
                        print("\n You died!")
                        input("EXIT>")
                    elif "e" in answer:
                      print("\nYou went through the door and got lost. The ship exploded.")
                      print("\n You died!")
                      input("EXIT>")
                  elif answer != "6498":
                    #wrong code
                    print("\nYou entered the wrong code and the security activated. The door behind you locked and the turrets activated.")
                    print("\n You died!")
                    input("EXIT>")
              elif "e" in answer:
                #unlocked door
                print("\nYou decided to go through the unlocked door and you walked into a long hallway.")
                print("There were two direction you could go. One was left and one was right. \n ('Q' for left or 'E' for right")
                answer = input(">").lower()
                if "q" in answer:
                  #left door
                  print("\nYou went left and walked into a large room.")
                  print("You saw a large button on the control panel. \n ('Q' for press or 'E' for don't press")
                  answer = input(">").lower()
                  if "q" in answer:
                    #press
                    print("\nYou pressed the button and closed the blast doors sealing you in the room.")
                    print("You saw a keypad and a small vent. Will you try to enter the code or will you try to escape through the vent? \n ('Q' for code or 'E' for vent)")
                    answer = input(">").lower()
                    if "q" in answer:
                      #code
                      print("\nYou went to the keypad and saw two sticky notes with different codes. (CODE 1: '6'3'2'0') and (CODE 2: '9'5'7'4') you took both pieces of paper.")
                      print("You could enter one code or else the security will activate. What code will you enter? \n (Enter one code)")
                      answer = input("CODE>")
                      if answer == "9574":
                        #correct code
                        print("\nYou entered the correct code and the door opened into a room with a large escape pod.")
                        print("You could either leave the ship or stay onboard. \n ('Q' for leave or 'E' for stay)")
                        answer = input(">").lower()
                        if "q" in answer:
                          #leave
                          print("\nYou got into the escape pod and launched it. You managed to survive and make it to a space station.")
                          print("\n You survived! ENDING 22 /",endingCount)
                          input("EXIT>") 
                        elif "e" in answer:
                          #stay
                          print("\nYou stayed onboard but heard a window crack.")
                          print("You saw two buttons. One would seal the window and the other would open the window. \n ('Q' for left or 'E' for right)")
                          answer = input(">").lower()
                          if "q" in answer:
                            #left button
                            print("\nYou pressed the left button and the window sealed. The ship was now fully stabilized.")
                            print("\n You survived! ENDING 23 /",endingCount)
                            input("EXIT>")
                          elif "e" in answer:
                            #right button
                            print("\nYou pressed the right button and the window opened. You were sucked out into space.")
                            print("\n You died!")
                            input("EXIT>")
                      elif answer != "9574":
                        #wrong code
                        print("\nYou entered the wrong code and the security activated. The blast doors locked and the turrets activated.")
                        print("\n You died!")
                        input("EXIT>")
                  elif "e" in answer:
                    #don't press
                    print("\nYou didn't press the button and went back to your room and survived.")
                    print("\n You survived! ENDING 21 /",endingCount)
                    input("EXIT>")
                elif "e" in answer:
                  #right door
                  print("\nYou went right and walked into the storage room. You saw a large switch.")
                  print("Will you flip the switch? \n ('Q' for flip or 'E' for don't flip")
                  answer = input(">").lower()
                  if "q" in answer:
                    #flip
                    print("\nYou flipped the switch and it caused the ship to shut down all systems, including oxygen.")
                    print("\n You died!")
                    input("EXIT>")
                  elif "e" in answer:
                    #don't flip
                    print("\nYou didn't flip the switch and continued to explore the storage room.")
                    print("You found a piece of paper (CODE 1: '3'7'5'1') but you also found another piece of paper (CODE 2: '8'4'6'2') you took both pieces of paper.")
                    print("You saw two doors. Which one will you walk through? \n ('Q' for left or 'E' for right)")
                    answer = input(">").lower()
                    if "q" in answer:
                      #left door
                      print("\nYou walked through the left door and entered a room with a large computer.")
                      print("You saw two large white buttons with different labels. One was labeled 'OFF' and the other was labeled 'ON' which one will you press? \n ('Q' for off or 'E' for on)")
                      answer = input(">").lower()
                      if "q" in answer:
                        #off
                        print("\nYou pressed the 'OFF' button and it caused the entire ship to shut down all systems, including oxygen.")
                        print("\n You died!")
                        input("EXIT>")
                      elif "e" in answer:
                        #on
                        print("\nYou pressed the 'ON' button and the ship began to self repair.")
                        print("\n You survived! ENDING 19 /",endingCount)
                        input("EXIT>")
                    elif "e" in answer:
                      #right door
                      print("\nYou walked through the right door and into a room with a large red button.")
                      print("Will you press the button? \n ('Q' for press or 'E' for don't press")
                      answer = input(">").lower()
                      if "q" in answer:
                        #press
                        print("\nYou pressed the button and it started the ships self destruct sequence.")
                        print("\n You died!")
                        input("EXIT>")
                      elif "e" in answer:
                        #don't press
                        print("\nYou didn't press the button and decided to return to the engine room.")
                        print("You saw the engine was on fire. Will you put it out or will you run? \n ('Q' for put out or 'E' for run)")
                        answer = input(">").lower()
                        if "q" in answer:
                          #put out
                          print("\nYou put out the fire and the engine started to stabilize.")
                          print("\n You survived! ENDING 20 /",endingCount)
                          input("EXIT>")
                        elif "e" in answer:
                          #run
                          print("\nYou ran away from the engine room and the fuel exploded. You could not get far enough away from the explosion.")
                          print("\n You died!")
                          input("EXIT>")
          elif "e" in answer:
            #run
            print("\nYou ran away from the engine room and the fuel exploded. You could not get far enough away from the explosion.")
            print("\n You died!")
            input("EXIT>")
        elif "e" in answer:
          #try to stop
          print("\nYou went back into the storage room to find something to stop the sparking wire.")
          print("You saw a breaker panel but you also saw a pair of wire cutters. Will you use the breaker or the wire cutters? \n ('Q' for breaker or 'E' for wire cutters)")
          answer = input(">").lower()
          if "q" in answer:
            #breaker
            print("\nYou opened the breaker panel and flipped the breaker to stop the sparking wire and it worked.")
            print("Now you can try to clean up the fuel or start the engine. \n ('Q' for clean up or 'E' for start)")
            answer = input(">").lower()
            if "q" in answer:
              #clean fuel
              print("\nYou tried to clean the fuel but slipped and fell into the engine")
              print("\n You died!")
              input("EXIT>")
            elif "e" in answer:
              #start engine
              print("\nYou succesfully started the engine and everything seemed started to work normally.")
              print("\nYou survived! ENDING 13 /",endingCount)
              input("EXIT>")
          elif "e" in answer:
            #wire cutters
            print("\nYou tried to use the wire cutters to cut the sparking wire, but you accidentally electrocuted yourself because you weren't careful enough.")
            print("\n You died!")
            input("EXIT>")
      elif "e" in answer:
        #blue switch
        print("\nYou flipped the blue switch and it started the engines oxygen pumps. The engine was now running without any immediate problems.")
        print("You can stay here to continue monitoring the engine or you can return to where you were before. \n ('Q' for stay or 'E' for return)")
        answer = input(">").lower()
        if "q" in answer:
          #monitor
          print("\nYou stayed to monitor the engine and noticed that pressure was building up.")
          print("There is a big valve and a small valve. Which one will you choose? \n ('Q' for big or 'E' for small)")
          answer = input(">").lower()
          if "q" in answer:
            #big valve
            print("\nYou turned the big valve and released the pressure. The engine started to stabilize")
            print("\n You survived! ENDING 05 /",endingCount)
            input("EXIT>")
          elif "e" in answer:
            #small valve
            print("\nYou turned the small valve which caused the fuel to leak in the engine and the engine exploded.")
            print("\n You died!")
            input("EXIT>")
        elif "e" in answer:
          #return
          print("\nYou returned to your room when you heard a loud noise. You ran back into the engine room and saw a fire.")
          print("Will you put out the fire or try to escape? \n ('Q' for put out or 'E' for escape)")
          answer = input(">").lower()
          if "q" in answer:
            #put out
            print("\nYou put out the fire and the engine started to stabilize.")
            print("You went back to your room and rested.")
            print("\n You survived! ENDING 11 /",endingCount)
            input("EXIT>")
          elif "e" in answer:
            #escape
            print("\nYou ran down the hall to try and find the escape pods. You came across two doors.")
            print("Will you try to go through the door in front of you or the door to your right? \n ('Q' for front or 'E' for right)")
            answer = input(">").lower()
            if "q" in answer:
              #straight
              print("\nYou tried to go through the door in front of you but it was locked and the fire caught up to you.")
              print("\n You died!")
              input("EXIT>")
            elif "e" in answer:
              #right
              print("\nYou went through the door to your right and entered a large room.")
              print("You saw a large button on the control panel. \n ('Q' for press or 'E' for don't press")
              answer = input(">").lower()
              if "q" in answer:
                #press
                print("\nYou pressed the button and it caused blast doors to close, preventing the fire from reaching you.")
                print("You saw a hallway leading left and right. Which way will you go? \n ('Q' for left or 'E' for right)")
                answer = input(">").lower()
                if "q" in answer:
                  #left
                  print("\nYou went left and entered the room with the escape pods.")
                  print("There were 4 escape pods. Which one will you choose? \n (Pick a number 1-4)")
                  answer = input("ESCAPE POD>")
                  if answer == "3":
                    #pod 1
                    print("\nYou chose escape pod 1 but that escape pod's engines were broken and the escape pod exploded.")
                    print("\n You died!")
                    input("EXIT>")
                  elif answer == "1":
                    #pod 2
                    print("\nYou chose escape pod 2 and it was successful. You mananged to escape the ship.")
                    print("\n You survived! ENDING 12 /",endingCount)
                    input("EXIT>")
                  elif answer == "2":
                    #pod 3
                    print("\nYou chose escape pod 3 but that escape pod's engines were broken and the escape pod exploded.")
                    print("\n You died!")
                    input("EXIT>")
                  elif answer == "4":
                    #pod 4
                    print("\nYou chose escape pod 4 but the circuits were fried so you couldn't leave. The escaped pod doors locked and you were now trapped inside of the escape pod.")
                    print("\n You died!")
                    input("EXIT>")
                  elif answer != "1" or "2" or "3" or "4":
                    print("\nYou couldn't decide which escape pod to take and ran out of time. The ship exploded.")
                    print("\n You died!")
                    input("EXIT>")
                elif "e" in answer:
                  #right
                  print("\nYou went right and entered a dark room.")
                  print("You were walking through the dark room when you fell off of a ledge.")
                  print("\n You died!")
                  input("EXIT>")
              elif "e" in answer:
                #don't press
                print("\nYou didn't press the button and the fire crept fast and eventually reached you.")
                print("\n You died!")
                input("EXIT>")
    elif "e" in answer:
      #continue repair
      print("\nYou continued to repair the engine by yourself and were still missing important tools and parts. The engine caught on fire and exploded.")
      print("\n You died!")
      input("EXIT>")
  elif "e" in answer:
    #engine start
    print("\nYou tried to start the engine and succesfully got the engine to start, but only for a few moments before it caught on fire.")
    print("Will you run outside of the engine room or will you try to put out the fire? \n ('Q' for run or 'E' for put out)")
    answer = input(">").lower()
    if "q" in answer:
      #run
      print("\nYou ran outside of the engine room and found a hallway with a set of two doors.")
      print("Will you enter the door on the left or the door on the right? \n ('Q' for left or 'E' for right")
      answer = input(">").lower()
      if "q" in answer:
        #left door
        print("\nYou entered the door on the left and walking into a room with a large red button and a large green button.")
        print("Will you press the red button or the green button? \n ('Q' for red or 'E' for green)")
        answer = input(">").lower()
        if "q" in answer:
          #red button
          print("\nYou pressed the red button and deactivated the asteroid defense systems which caused an asteroid to collide with the ship.")
          print("\n You died!")
          input("EXIT>")
        elif "e" in answer:
          #green button
          print("\nYou pressed the green button and the ship started to repair itself.")
          print("You could now return to where you were before or you could explore the ship. \n ('Q' for return or 'E' for explore)")
          answer = input(">").lower()
          if "q" in answer:
            #return
            print("\nYou returned to where you were before and found a hallway with a set of two doors.")
            print("Will you enter the door on the left or the door on the right? \n ('Q' for left or 'E' for right")
            answer = input(">").lower()
            if "q" in answer:
              #left door
              print("\nYou walked through the left door and entered a dark room above the engine.")
              print("You can explore this room or return to your room and rest. \n ('Q' for explore or 'E' for rest)")
              answer = input(">").lower()
              if "q" in answer:
                #explore room
                print("You were exploring the dark room when you suddenly fell off of a platform")
                print("\n You died!")
                input("EXIT>")
              elif "e" in answer:
                #rest
                print("\nYou returned to your room and rested there for a while.")
                print("\n You survived! ENDING 08 /",endingCount)
                input("EXIT>")
            elif "e" in answer:
              #right door
              print("\nYou walked through the right door and entered the generator room. The generators were all off.")
              print("There was a white switch and a black switch. Which one will you choose? \n ('Q' for white or 'E' for black)")
              answer = input(">").lower()
              if "q" in answer:
                #white switch
                print("\nThe generators started to run but caused a large arc to hit one of the pipes and it caught fire.")
                print("Will you run or try to put out the fire? \n ('Q' for run or 'E' for put out)")
                answer = input(">").lower()
                if "q" in answer:
                  #run
                  print("\nYou tried to run away from the fire but the fire caused the generators to explode.")
                  print("\n You died!")
                  input("EXIT>")
                elif "e" in answer:
                  #put out
                  print("\nYou grabbed a fire extinguisher and put out the fire.")
                  print("You saved the ship from exploding and the ship was now back on course.")
                  print("\n You survived! ENDING 09 /",endingCount)
                  input("EXIT>")
              elif "e" in answer:
                #black switch
                print("\nThe black switch turned off all sources of power and caused the engine to malfuntion and explode.")
                print("\n You died!")
                input("EXIT>")
          elif "e" in answer:
            #explore
            print("\nYou were exploring the ship when you heard a crack come from the window")
            print("You could run and try to seal the window or you could try to fix the window right now. \n ('Q' for run or 'E' for fix)")
            answer = input(">").lower()
            if "q" in answer:
              #run
              print("\nYou ran outside of the room and came across two buttons. One would seal the window and the other would open the window.")
              print("Will you press the left button or the right button? \n ('Q' for left or 'E' for right)")
              answer = input(">").lower()
              if "q" in answer:
                #left button
                print("\nYou pressed the left button which caused the window to open and it sucked you out into space.")
                print("\n You died!")
                input("EXIT>")
              elif "e" in answer:
                #right button
                print("\nYou pressed the right button which caused the window to seal and the ship was now fully stabilized.")
                print("\n You survived! ENDING 10 /",endingCount)
                input("EXIT>")
            elif "e" in answer:
              #try to fix
              print("\nYou tried to fix the window by yourself but it only cracked more and more before it broke and sucked you out into space.")
              print("\n You died!")
              input("EXIT>")
      elif "e" in answer:
          #right door
          print("\nYou went through the door on the right and entered a large room with a door and ladder.")
          print("Will you go through the door or climb the ladder? \n ('Q' for door or 'E' for ladder)")
          answer = input(">").lower()
          if "q" in answer:
            #door
            print("\nYou went through the door and entered the computer room.")
            print("You saw a large monitor with 3 buttons connected to it. Which button will you press? \n (Pick a number 1-3)")
            answer = input("BUTTON>")
            if answer == "1":
              #button 1
              print("\nYou pressed button 1 and it started the ships self destruct sequence.")
              print("\n You died!")
              input("EXIT>")
            elif answer == "2":
              #button 2
              print("\nYou pressed button 2 and it activated the ships distress signal.")
              print("\n You survived! ENDING 14 /",endingCount)
              input("EXIT>")
            elif answer == "3":
              #button 3
              print("\nYou pressed button 3 and it unlocked a secret door.")
              print("Will you enter the door or stay where you are? \n ('Q' for enter or 'E' for stay)")
              answer = input(">").lower()
              if "q" in answer:
                #enter
                print("\nYou entered the secret door and found a room with a large computer.")
                print("You saw two large white buttons with different labels. One was labeled 'OFF' and the other was labeled 'ON' which one will you press? \n ('Q' for off or 'E' for on)")
                answer = input(">").lower()
                if "q" in answer:
                  #off
                  print("\nYou pressed the 'OFF' button and it caused the entire ship to shut down all systems, including oxygen.")
                  print("\n You died!")
                  input("EXIT>")
                elif "e" in answer:
                  #on
                  print("\nYou pressed the 'ON' button and the ship began to self repair.")
                  print("\n You survived! ENDING 16 /",endingCount) 
                  input("EXIT>")
              elif "e" in answer:
                #stay
                print("\nYou stayed where you were and noticed fire creeping into the room.")
                print("You could run through the left door or the right door. \n ('Q' for left or 'E' for right)")
                answer = input(">").lower()
                if "q" in answer:
                  #left door
                  print("\nYou ran through the left door and ended up in a room with a large cracked window.")
                  print("You could try to seal the window or you could try to escape. \n ('Q' for seal or 'E' for escape)")
                  answer = input(">").lower()
                  if "q" in answer:
                    #seal
                    print("\nYou tried to seal the window but the window broke and sucked you out into space.")
                    print("\n You died!")
                    input("EXIT>")
                  elif "e" in answer:
                    #escape
                    print("\nYou kept running and ran into a locked door.")
                    print("You could try to find the code or you could try to break the door down. \n ('Q' for code or 'E' for break)")
                    answer = input(">").lower()
                    if "q" in answer:
                      #code
                      print("\nYou found a peice of paper (CODE 1: '2'6'8'4') but you also found another peice of paper (CODE 2: '1'9'7'3') you took both peices of paper.")
                      print("You returned to the locked door and have a chance to enter one code or else the security will activate. What code will you enter? \n (Enter one code)")
                      answer = input("CODE>")
                      if answer == "1973":
                        #correct code
                        print("\nYou entered the correct code and the door opened into a room with a large escape pod.")
                        print("You got into the escape pod and launched it. The ship exploded but you survived.")
                        print("\n You survived! ENDING 17 /",endingCount)
                        input("EXIT>")
                      elif answer != "1973":
                        #wrong code
                        print("\nYou entered the wrong code and the security activated. The door behind you locked and the turrets activated.")
                        print("\n You died!")
                        input("EXIT>")
                elif "e" in answer:
                  #right door
                  print("\nYou ran through the right door and ended up inside of a room with a large switch.")
                  print("Will you flip the switch? \n ('Q' for flip or 'E' for don't flip)")
                  answer = input(">").lower()
                  if "q" in answer:  
                    #flip
                    print("\nYou flipped the switch and it closed a blast door, then it opened an airlock and sucked you out into space.")
                    print("\n You died!")
                    input("EXIT>")
                  elif "e" in answer:
                    #don't flip
                    print("\nYou didn't flip the switch and the fire slowly crept into the room.")
                    print("You could try to escape or you could try to put out the fire. \n ('Q' for escape or 'E' for put out)")
                    answer = input(">").lower()
                    if "q" in answer:
                      #escape
                      print("\nYou tried to escape but the fire had blocked all other ways to escape.")
                      print("\n You died!")
                      input("EXIT>")
                    elif "e" in answer:
                      #put out
                      print("\nYou put out the fire and the ship started to stabilize.")
                      print("\n You survived! ENDING 18 /",endingCount)
                      input("EXIT>")
            elif answer != "1" or "2" or "3":
              #no button
              print("\nYou couldn't decide which button to press and ran out of time. The fire crept into the room and made a fuel pipe explode.")
              print("\n You died!")
              input("EXIT>")
          elif "e" in answer:
            print("\nYou climbed the ladder and went into a room below the engine room.")
            print("You saw a valve and a switch. Which one will you choose? \n ('Q' for valve or 'E' for switch)")
            answer = input(">").lower()
            if "q" in answer:
              print("\nYou turned the valve and it caused a large steam pressure to be released and you fell off of the platform.")
              print("\n You died!")
              input("EXIT>")
            elif "e" in answer:
              print("\nYou flipped the switch and turned on the backup generators. The ship was now back on course.")
              print("\n You survived! ENDING 15 /",endingCount)
              input("EXIT>")
    elif "e" in answer:
      #put out
      print("\nYou grabbed a fire extinguisher and put out the fire. You saw a locked door and a hatch leading down")
      print("Will you try to open the door or will you go through the hatch? \n ('Q' for door or 'E' for hatch")
      answer = input(">").lower()
      if "q" in answer:
        #door
        print("\nYou tried to open the door but it was locked. You can search the engine room or the hallway for the code.")
        print("Will you search the engine room or the hallway? \n ('Q' for engine room or 'E' for hallway")
        answer = input(">").lower()
        if "q" in answer:
          #search engine room
          print("You searched the engine room and found nothing. Suddenly, more fire started to spread and it reached the fuel line. The engine exploded.")
          print("\n You died!")
          input("EXIT>")
        elif "e" in answer:
          #search hallway
          print("\nYou searched the hallway and found a piece of paper (CODE 1: '4'3'7'5') but you also found another piece of paper (CODE 2: '7'1'1'3') you took both pieces of paper.")
          print("You returned to the locked door and have a chance to enter one code or else the security will activate. (Enter one code)")
          answer = input("CODE>")
          if answer == "7113":
            #correct code
            print("\nYou entered the correct code and the door opened into the ships lightspeed generator. It appears to be offline.")
            print("Will you turn it on or will you leave it off? \n ('Q' for turn on or 'E' for leave off")
            answer = input(">").lower()
            if "q" in answer:
              #turn on
              print("\nYou turned on the lightspeed generator and the ship was now back on course.")
              print("\n You survived! ENDING 06 /",endingCount)
              input("EXIT>")
            elif "e" in answer:
              #leave off
              print("\nYou left the lightspeed generator off and the ship remained stuck in space. The oxygen supply eventually ran out.")
              print("\n You died!")
              input("EXIT>")
          elif answer != "7113":
            #wrong code
            print("\nYou entered the wrong code and the security activated. The door behind you locked and the turrets activated.")
            print("\n You died!")
            input("EXIT>")
      elif "e" in answer:
        #hatch
        print("\nYou went through the hatch and found a room with a large monitor and door")
        print("Will you check the monitor or will you go through the door? \n ('Q' for monitor or 'E' for door")
        answer = input(">").lower()
        if "q" in answer:
          #check monitor
          print("\nYou checked the monitor and saw that the oxygen pumps were turned off. You had to find a way to turn it back on.")
          print("You saw two dials. One was a red dial and one was a blue dial. Which one will you choose? \n ('Q' for red or 'E' for blue)")
          answer = input(">").lower()
          if "q" in answer:
            #red dial
            print("\nYou turned the red dial which fully sealed the oxygen pumps and caused the engine to explode because of the lack of oxygen.")
            print("\n You died!")
            input("EXIT>")
          elif "e" in answer:
            print("You turned the blue dial which reactivated the oxygen pumps and the ship was now fully stable and back on course")
            print("\n You survived! ENDING 07 /",endingCount)
            input("EXIT>")
        elif "e" in answer:
          #door
          print("\nYou walked through the door and walked into a long hallway. But you started hearing alarms. The oxygen supply was running out and you had no time to fix it.")
          print("\n You died!")
          input("EXIT>")
elif "e" in answer:
  #stay put
  print("\nYou stayed where you were and you hear an explosion.")
  print("Will you escape or try to stop the explosions? \n ('Q' for escape or 'E' for stop)")
  answer = input(">").lower()
  if "q" in answer:
    #try to escape
    print("\nYou ran down the hallway and found a set of two doors.")
    print("You are unfamilar with where the doors lead, but one of them will lead to the escape pods. Will you go left or right? \n ('Q' for left or 'E' for right)")
    answer = input(">").lower()
    if "q" in answer:
      #left door
      print("\nYou went left and found a long hallway with a large locked door that required a code")
      print("You can search the offices for the code or the storage room for the code. \n ('Q' for offices or 'E' for storage)")
      answer = input(">").lower()
      if "q" in answer:
        #search offices
        print("\nYou searched through the offices but found nothing.")
        print("Before you have a chance to search the storage room the engine explodes.")
        print("\n You died!")
        input("EXIT>")
      elif "e" in answer:
        #search storage room
        print("\nYou searched through the storage room and found a piece of paper (CODE 1: '1'5'3'7') but you found another piece of paper (CODE 2: '6'4'9'8') you took both pieces of paper.")
        print("You returned to the locked door and have a chance to enter one code or else the security will activate. What code will you enter? \n (Enter one code)")
        answer = input("CODE>")
        if answer == "1537":
          #correct code
          print("\nYou entered the correct code and the door opened into a large room that connects to two hallways.")
          print("Will you go straight or will you go left? \n ('Q' for striaght or 'E' for left)")
          answer = input(">").lower()
          if "q" in answer:
            #straigth
            print("\nYou went straight and walked into a room with 2 escape pods.")
            print("Will you take the left pod or the right pod? \n ('Q' for left or 'E' for right)")
            answer = input(">").lower()
            if "q" in answer:
              #left pod
              print("\nYou took the left pod and it took you to a space station.")
              print("\n You survived! ENDING 13 /",endingCount)
              input("EXIT>")
            elif "e" in answer:
              #right pod
              print("\n you took the right pod and it malfunctioned leaving you stranded in space.")
              print("\n You died!")
              input("EXIT>")
        elif answer != "1537":
          #wrong code
          print("\nYou entered the wrong code and the security activated. The door behind you locked and the turrets activated.")
          print("\n You died!")
          input("EXIT>")
    elif "e" in answer:
      #right door
      print("\nYou went right and wandered into a dead end. But you saw a small hatch on the ceiling that was open.")
      print("Will you turn back or go through the hatch? \n ('Q' for turn back or 'E' for hatch)")
      answer = input(">").lower()
  elif "e" in answer:
    #stop explosions
    print("\nYou tried to find a way to stop the explosions and found a valve conencted to the main fuel line. You also found a switch controling the engine's main power.")
    print("Will you turn the valve or flip the switch? \n ('Q' for valve or 'E' for switch)")
    answer = input(">").lower()
    if "q" in answer:
      #turn valve
      print("\nYou turned the valve but it created more pressure inside of the engine and the engine exploded.")
      print("\n You died!")
      input("EXIT>")
    elif "e" in answer:
      #flip switch
      print("\nYou flipped the switch and the engine stopped exploding, however it also turned the power out.")
      print("You can find a flashlight or try to find the backup generators. \n ('Q' for flashlight or 'E' for backup generators)")