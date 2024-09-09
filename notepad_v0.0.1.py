import os
def zzz():
     os.system("clear")
def moveBack():
    print("Let's pretend we moved up 1 step")
def greet():
    print("Greetings", userName,"!\n Welcome to", prName)

def getUserName():
    userName = input("How should I call you?\n")
    return userName
def getProgName():
    prName = input("""By default this program is called "CATonomous".\n
You may change its name to a different one.
Write new program name, or write 'no' if you wish to call it "CATonomous"\n>>>>""")
    if prName == "no" or prName == "x":
        prName = "CATonomous"
    return prName

#Initial startup here
userName = getUserName() #asking and setting the User name
zzz()
prName = getProgName() #asking and setting the Program name
zzz()
greet()
#-------------------
"""print(userName,"Say hi again") Hm, so with this setup, each time the userName or prName are mentioned
, the machine will actually grab the result of the related functions from its temporary memory?
Or do the variables just grab the values and don't address the functions anymore?"""
initialCommandList = ["\n(1)Settings", "\n(2)Synchronise", "\n(3)Info"]
settingsCommandList = ["\n(1)Change Name", "\n(2)Enable/Disable Features", "\n(3)Remove some/all Data from device you are about to synchronise to"]
#inAvCo = print("Avaliable commands:\n",initialCommandList) #inAvCo = Initially Available Commands
#lList = list that is visible for the user now
#AvCo = print("Available commands:\n", lList)


#def gQuestion(lList,q): #                            Should be seriously changed for applicability all over the app
#    q = input("Let me know what to do next \n>>> ")
#    if q == "1":
#        print(settingsCommandList)
 #   elif q == "2":
 #       print("Enabling Bluetooth, ready your other device too.\n You may customise the synchronisation in the next window")
#    elif q == "3":
#        print("Document with info about the app will be here")
#    elif q == "back":
#        zzz
#        moveBack
#gQuestion

#allCommandsList = ["New task", "Delete task", "New folder", "Delete folder", "List task folders", "List tasks", "Open Cached texts menu",
#              "Synchronise", "Remove some data", "Cypher some data"]
# Some commands, like List task folders, list tasks, are temporary and will exist in the non-graphic version only. Hm maybe I should do several "versions"
# - graphic and non-graphic one!

#allFeatures = ["ScrapingBot","Budget", "Roadmap", "Actual map", "Energy counter", "Routine tasks reminders"]

