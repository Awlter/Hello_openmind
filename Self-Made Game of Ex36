def talking():
    print "-\"Hey, my little bear, what do you want to eat?\""
    print "-\"Anything is ok.\"Smiling"
    print "Here is a list of somethin' she usuallys like to eat. Well..\"usually\".."
    print "[flower, fruit, meat, meat, meat.]"
    
    list = ['flower', 'fruit', 'meat'] 
    i = 0   
    while True and i < 10:  
        ans = raw_input("- ")
        if ans in list:
            print "\"I don't feel like eating", ans, "today.\""
            i = i + 1
        elif ans == "Selling my kidney for the toothsome":
            print "-\"You should add this to your list darling like this\": \n"
            list.append(ans)
            print list
            dead("Happy end without kidneys.")
        else:
            print "-\"No! I hate %r! Don't you know that?\"" % ans
            i = i + 1   
    
    dead("Waste too much time asking her all of these nonsense..")

def dead(why):
    print why, "bye-bye!"
    exit(0)

def start():
    print "It's 5:00pm. You are still reading a book in a classroom with your girlfriend sitting besides you."
    print "You suddenly notice that sha has been contemplating you in silence."
    print "To talk, or not to talk to her, that is a question."
    
    choice = raw_input("> ")
    
    if choice == 'talk to her':
        talking()
    elif choice == 'kiss her':
        dead("Well..She is just hungry")
    else:
        dead("Well..You stupid always-being-single dog.")
        
start()
