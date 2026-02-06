import time
print(r'''
         _
        (:)_
      ,'    `.
     :        :
     |        |              ___
     |       /|    ______   // _\
     ; -  _,' :  ,'      `. \\  -\
    /          \/          \ \\  :
   (            :  ------.  `-'  |
____\___    ____|______   \______|_______
        |::|           '--`           SSt
        |::|
        |::|
        |::|
        |::;
        `:/
      ''')
print("Welcome to Treasure Island!")
print("Author: Rick19F\n\tDone in 5 attempts")
print("Your mission is to find the treasure")
time.sleep(3)

print(r'''
  ........::::::::::::..           .......|...............::::::::........
     .:::::;;;;;;;;;;;:::::.... .     \   | ../....::::;;;;:::::.......
         .       ...........   / \\_   \  |  /     ......  .     ........./\
...:::../\\_  ......     ..._/'   \\\_  \###/   /\_    .../ \_.......   _//
.::::./   \\\ _   .../\    /'      \\\\#######//   \/\   //   \_   ....////
    _/      \\\\   _/ \\\ /  x       \\\\###////      \////     \__  _/////
  ./   x       \\\/     \/ x X           \//////                   \/////
 /     XxX     \\/         XxX X                                    ////   x
-----XxX-------------|-------XxX-----------*--------|---*-----|------------X--
       X        _X      *    X      **         **             x   **    *  X
      _X                    _X           
''')
decision1 = str(input(
    "You are already in the air with Snoopy and directed straight to a mountain. Wanna go left or right (L or R)?: "))
while decision1 is None or decision1.strip() == '' or (not decision1.upper() in ['L', 'R']) or (not decision1[0].upper() in ['L', 'R']):
    decision1 = str(input("Try again. Wanna go left or right (L or R)?: "))
if decision1.upper() == 'L':
    print(r'''
           _
         -=\`\
     |\ ____\_\__
   -=\c`""""""" "`)
jgs   `~~~~~/ /~~`
        -==/ /
          '-'

          _  _
         ( `   )_
        (    )    `)
      (_   (_ .  _) _)
                                     _
                                    (  )
     _ .                         ( `  ) . )
   (  _ )_                      (_, _(  ,_)_)
 (_  _(_ ,)
''')
    print("GAME OVER, you crashed into another airplane!")
    quit()


print("GREAT! You just dodged some airplanes on the other side\n\n")

time.sleep(3)
decision2 = str(input(
    "Wait... What is that on the clouds? Wanna investigate? (Y or N): "))
while decision2 is None or decision2.strip() == '' or (not decision2.upper() in ['Y', 'N']) or (not decision2[0].upper() in ['Y', 'N']):
    decision2 = str(input("Try again. Wanna investigate (Y or N)?: "))

if decision2.upper() == 'N':
    print("OK, let's continue on our quest...")
    time.sleep(3)
    print(r'''
            ____
  |        | ___\          /~~~|
 _:_______|/'(..)`\_______/  | |
<_|``````  \__~~__/  USAF ___|_|
  :\_____(=========,(*),--\__|_/
  |       \       /---'
           | (*) /
           |____/
''')
    print("BOOM!!! The Red Baron just shot you from above. You are grounded")
    time.sleep(1)
    print("GAME OVER")
    quit()

time.sleep(2)
print("OHHHH that's the Red Baron, it's just good luck he hasn't seen you\n\n")
time.sleep(4)
print(r'''
     .-.                                    ,-.
  .-(   )-.                              ,-(   )-.
 (     __) )-.                        ,-(_      __)
  `-(       __)                      (_    )  __)-'
    `(____)-',                        `-(____)-'
  - -  :   :  - -
      / `-' \
    ,    |   .
         .                         _
                                  >')
               _   /              (\\         (W)
              =') //               = \     -. `|'
               ))////)             = ,-      \(| ,-
              ( (///))           ( |/  _______\|/____
~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::
            _                 ,----':::::::::::::::::
         {><_'c   _      _.--':MJP:::::::::::::::::::
__,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::
:.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:
.:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.
.........................................
''')
print("From up here, you can see everything. There are two pieces of land down there, the treasure must be there!")
decision3 = str(input(
    "Which one do you want to visit? You only have fuel for one and travel back with the treasure (A or B): "))
while decision3 is None or decision3.strip() == '' or (not decision3.upper() in ['A', 'B']) or (not decision3[0].upper() in ['A', 'B']):
    decision3 = str(input("Try again. Wanna visit A or B?: "))

if decision3.upper() == 'B':
    print("Sorry, there is nothing here. Go back for fuel and try the other spot")
    print("GAME OVER")
else:
    print("The treasure doesn't seem to be here...\n\n\n")
    time.sleep(2)
    print("WAIT!!! There it is! You found it!!!!!")
    print("YOU HAVE WON!")
    time.sleep(5)
    print(r'''
             _.---,-..
           ,'    )(__)\__
          /  ,-.',<..-'  `._
         :  |  |' /       (_)
         |  `-'  (        /
          `.._    >-----''
           _..).-(
     ,-._,'_.;.--':   _
__.-' ,._,' /  _.,'.(( ,-.
 -'),'     :.   / /,\_. <
  `'       |:  '\    ::`'
           :   --'   ||
   ___,-':.-`________;;________
  /                            \
 /  __________________________  \
/  SSt                           \
''')
