#Menu
def menu ():
    print("")
    print("")
    print(75*"-")
    print("  __  __          _____ _   _         __  __ ______ _   _ _    _ ")
    print(" |  \/  |   /\   |_   _| \ | |       |  \/  |  ____| \ | | |  | |")
    print(" | \  / |  /  \    | | |  \| |       | \  / | |__  |  \| | |  | |")
    print(" | |\/| | / /\ \   | | |     |       | |\/| |  __| |     | |  | |")
    print(" | |  | |/ ____ \ _| |_| |\  |       | |  | | |____| |\  | |__| |")
    print(" |_|  |_/_/    \_\_____|_| \_|       |_|  |_|______|_| \_|\____/ ")
    print("")
    print("                   PASSWORD CHECKER AND GENERATER                ")
    print("                                                ")
    print("                                                ")
    print("                     (1)   Check Password       ")
    print("                     (2)   Generate Password    ")
    print("                     (3)   Quit                 ")
    print("                                                ")
    print("                                                ")
    print("               Please enter either: '1', '2',or, '3'")
    print("")
    print(75*"-")
#All of the above is just so the user knows what to input and that the menu looks nice
    print("")
    userinput = input("===>")


    while userinput!="3":
        #checkpassword
        if userinput == ("1"):
            print ("You have chosen 'Check Password'")
            checkpassword ()
            menu()
            userinput=input("===>")


    #generatepassword
        if userinput == ("2"):
            print ("You have chosen 'Generate Password'")
            generatepassword ()
            checkpassword ()
            menu()
            userinput=input("===>")
    #quit
    if userinput == ("3"):
        print ("You have chosen 'Quit'")
        print ("Goodbye")
    menu()


#Password checker
def checkpassword ():
    allowed = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "$", "^", "&", "%", "*", "(", ")", "-", "_", "=", "+")
    sequence = ("qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop", "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "zxc", "xcv", "cvb", "vbn", "bnm")
    score = 0
    #All charaters that are allowed in a password are above, aswell as the 'qwe' sequence checker

    while True:
        print("")
        print(75*"-")
        print("")
        password = input("Please insert your Password ===> ")
        lowerpassword=password.lower()

        if  len(password) >24:
            print ("Your password is TOO LONG and therefore is weak: ERROR")
        #If the users inserted password is greater than 24 then this will be displayed and looped back to the start of this section

        elif    len(password) <8:
            print ("Your password is TOO SHORT and therefore is weak: ERROR")
        #If the password is smaller than 8 characters long then the "Your password is TOO SHORT and therefore is weak" will be displayed then you will be looped back to the start of this section

        if len(password) >7 and len(password) <25:
            for i in password:
                #print(i)
                if i not in allowed:
                    print("A invalid character has been entered")
                    break
        #If a charcater that is not in the allowed characters is entered then you will be told A invalid character has been entered and then looped back to the start of the section
        if len(password) >7 and len(password) <25:
            if i in allowed:
                break
    import string
    marks = password
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in marks])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in marks])
    symbols = any([1 if c in string.punctuation else 0 for c in marks])
    nums = any([1 if c in string.digits else 0 for c in marks])
    pattern =  any([1 if c in sequence else 0 for c in marks])
    ALL = all([1 if c in string.ascii_uppercase and string.ascii_lowercase and string.punctuation and string.digits else 0 for c in marks])
    characters = [upper_case,lower_case,symbols,nums,pattern,ALL]

    length = len(password)

    score = length

    #print(f"Password length is {str(length)}, adding {str(score)} points!")

    if sum(characters) > 1:
       score += 5

    if sum(characters) > 2:
       score += 5

    if sum(characters) > 3:
      score += 5

    if sum(characters) > 4:
      score += 5

    if sum(characters) > 5:
       score += 10

    if sum(characters) < 1:
      score -= 5

    if sum(characters) < 2:
      score -= 5

    if sum(characters) < 3:
      score -= 5

    #print(f"Password has {str(sum(characters))}diff char, adding {str(sum(characters))} points!")

    #print(f"Score is {str(score)}")

    for i in password:
        if i in allowed:
            score=score+1
    print(score)

    for i in sequence:
        if i in lowerpassword:
            score=score-5
    print(score)
    if score>20:
        print("")
        print(75*"-")
        print("")
        print("                           PASSWORD SCORE")
        print("                               >",score,"<")
        print("                       Your Password is STRONG")

    if score<0:
        print("")
        print(75*"-")
        print("")
        print("                           PASSWORD SCORE")
        print("                               >",score,"<")
        print("                        Your Password is WEAK")

    if score >1 and score<19:
        print("")
        print(75*"-")
        print("                           PASSWORD SCORE")
        print("                               >",score,"<")
        print("                      Your Password is MEDIUM")



def generatepassword():

  import random

  print ("Your password is:")
  import time

  time.sleep(1)
  import time
  print ("                                ~ Generating ~")

  time.sleep(0.25)
  print ("                                      .")
  time.sleep(0.25)
  print ("                                     . .")
  time.sleep(0.25)
  print ("                                    . . .")
  time.sleep(0.25)
  print ("                                     . .")
  time.sleep(0.25)
  print ("                                      .")





  passwordlength = 12

  alp = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%^&*()-_=+"

  password = "".join(random.sample(alp,passwordlength ))

  print("")
  print ("                              ",password)
  time.sleep(1)
  print("")
  print ("To check the strength of your password or generate another, restart the code!")
menu()
time.sleep(9999999)
import time
menu()