import random
import sys
import time
import os
import datetime

#Logs the launching of the program
global logs
global LogWrite
global Time
Time = str(datetime.datetime.now())
logs = open("Resorces/logs.txt","a")
LogWrite = "The Program was launched"
logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
logs.close()

#Declares global variables
Active = True
ConsolVer = "ALPHA 0.10.3"
UserInput = ""
ChangeLog = '''----------- Change log: -----------'''
SysName = "SYS: "
UserName = "USER: "
CommandsExecutedInSesion = 0
ComIdChar = "/" #Declares the character(s) to reconize commands
Time = str(datetime.datetime.now())
ComExa = open("Resorces/commands_exacuted.txt", "r")
TotalCommandsExacuted = ComExa.read()
ComExa.close()

Time = str(datetime.datetime.now())
logs = open("Resorces/logs.txt","a")
LogWrite = "Global Variables were declared"
logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
logs.close()

#Declares global error variables
ERR_0 = "ERR-0"
ERR_1 = "ERR-1"
ERR_2 = "ERR-2"
ERR_3 = "ERR-3"

Time = str(datetime.datetime.now())
logs = open("Resorces/logs.txt","a")
LogWrite = "Global Error Variables were declared"
logs.writelines("""'
 ["""+ Time + "]: "+ LogWrite)
logs.close()

#Declares global command variables
Com1 = ComIdChar + "help"
Com1Def = ": Shows a list of commands"
Com2 = ComIdChar + "randint"
Com2Def = ": Generates a random number without a decimal between 2 numbers given by the user"
Com3 = ComIdChar + "exit"
Com3Def = ": Closes the program"
Com4 = ComIdChar + "errors"
Com4Def = ": Shows a list of errors"
Com5 = ComIdChar + "percy"
Com5Def = ": Displays a picture of my cat percy out of ASCII characters"
Com6 = ComIdChar + ""
Com6Def = ""
Com7 = ComIdChar + ""
Com7Def = ""
Com8 = ComIdChar + ""
Com8Def = ""
Com9 = ComIdChar + ""
Com9Def = ""
Com10 = ComIdChar + ""
Com10Def = ""

Time = str(datetime.datetime.now())
logs = open("Resorces/logs.txt","a")
LogWrite = "Global Command Variables were declared"
logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
logs.close()

#Defines a function to get the user's input
def GetUserInput():
    global logs
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'GetUserInput' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()
    global UserInput
    global UserInput2
    global UserInput3
    global UserName
    global Com2
    UserInput = input(UserName)
    if UserInput == Com2:
        UserInput2 = input("Enter first parameter for command: ")
        UserInput3 = input("Enter second parameter for command: ")


#Defines the "help" command
def CommandHelp():
    global logs
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'CommandHelp' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()
    global Com1
    global Com1Def
    global Com2
    global Com2Def
    global Com3
    global Com3Def
    global Com4
    global Com4Def
    global Com5
    global Com5Def
    global Com6
    global Com6Def
    global Com7
    global Com7Def
    global Com8
    global Com8Def
    global Com9
    global Com9Def
    global Com10
    global Com10Def
    print("---------- COMMANDS: ----------")
    print(Com1, Com1Def)
    print(Com2, Com2Def)
    print(Com3, Com3Def)
    print(Com4, Com4Def)

   

#Defines the "randomInt" command
def CommandRandomInt(num1, num2):
    global logs
    print(random.randrange(num1, num2))
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'CommandRandomInt' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()

#Defines the "exit" command
def CommandExit():
    global ERR_2
    global TempTotalCommands
    global TotalCommandsExacuted
    global logs
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'CommandExit' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()

    RandNum = random.randrange(1, 1_000_000_000)
    if RandNum != "13":
        print("Closing program...")
        TotalCommandsExacuted = open("Resorces/commands_exacuted.txt", "r")
        TempTotalCommands = TotalCommandsExacuted.readline()
        TotalCommandsExacuted.close()
        if os.path.exists("Resorces/commands_exacuted.txt"):
            os.remove("Resorces/commands_exacuted.txt")
        else:
            print("An error has occured. Error code: ERR-3")
            Time = str(datetime.datetime.now())
            logs = open("Resorces/logs.txt","a")
            LogWrite = "Error. File 'commands_exacuted.txt' does not exist"
            logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
            logs.close()
        TotalCommandsExacuted = open("Resorces/commands_exacuted.txt", "w")
        TotalCommandsExacuted.write(str(TempTotalCommands) + str(CommandsExecutedInSesion))
        TotalCommandsExacuted.close()
        Time = str(datetime.datetime.now())
        logs = open("Resorces/logs.txt","a")
        LogWrite = "The Program was closed"
        logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
        logs.close()
        time.sleep(5)
        sys.exit(0)

    else:
        print("An error has occured. Error code: "+ ERR_1) #if this happens to you... you're VERY lucky
        Time = str(datetime.datetime.now())
        logs = open("Resorces/logs.txt","a")
        LogWrite = "Error ERR-1 has occured"
        logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
        logs.close()

#Defines the "errors" command
def CommandErrors():
    global logs
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'CommandErrors' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()
    print('''Code:       Meaning:

ERR-0: Entered command is not valid or does not exist
ERR-1: The program has failed to close
ERR-3: The "commands_exacuted.txt" file does not exist or is not in the "Resorces" folder
''')
    
def CommandPercy():
    global logs
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'CommandPercy' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()
    print('''@@@@@@@%%@@@%%%%%%%%%%%#%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%@@@@%%%%%%%%%%########%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#*****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@%%%%%%%%%%%%#########%%%@@@@@@@@@@%@@%%@%%%%%*+++++****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%%%%%%%%%%%%%%%%%#******####%%####***++****#*####%##******#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%%%%%%%%%%%%%%%%%%#********#####***+++++++*###%%%##******#%@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%%%%%%%%%%%%%%%%%%********#####%%#******+*#%%%%%##******%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@%%%%%%%%%%%%%%%%%%%#*+++****########*#**#*#%#%%####****+#%@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%*++**++++****#%%*++==+#%%####*******%@@@@%@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%#*++==+++*****#*+=---==+*********++#%@@@%%%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%@%%%%%%%%%%%%%%%%%%%%*===+++++*+++==-------==++********+#@@@@%%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%%%%%%%%%%%%%%%%%%%%%#+==++++++++====--------===+++******#%@@@@@@@@%@@@@@@@@@@%%%%%%%%%%%%%%%@
@@@@@@@%%%%%%%%%%%%%%%%%%%%*===++++++======----=---====+++*****+#%@@@@@%%%%%%#*+++=================+
@@@@@@%%%%%%%%%%%%%%%%%%%%%*====+++++++++++============++++****++#%%#*======-----==================+
@@@@@@@%%%%%%%%%%%%%%%%%%%%#*+++++++********+++++++***+****#%%#+=----------------===================
@@@@@@@%%%%%%%%%%%%%%%%%%%%%#**++++*#%@@@%##***+++*#%@@%#*****+=-----------------===================
@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%#**++***###%#****++++####**++++==-----------------====================
@@@@@@%%%%%%%%%%%%%%%%%%@@@@@@%#***++++****++++++==+++++++=====--------------=======================
@@@@@@@%%%%%%%%%%%%@@@@@@@@@@@@%###***+++++++=========++++=====-----------==========================
@@@@@@@@%@%%%%@@@@@@@@@@@@@@@@@@@%####*+++++++========+++++++==----------========================+++
@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@#####******+++==+==+++++++====--===---=======================+++++
@@@@@@@%%@%%%%@@@@@@@@@@@@@@@@@@@@%######***###****==++++++===============================++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########%%#**+++++++==================++++===+++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#######%###****+++++=+++++++======+++++++=+++++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########****++++++===+++=+======+++++++++++++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%########*****+++===============+++++++++++++++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#************++++==============+++++****++***+++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*************+++++++===========++++********++++++++++++++++
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*************+++++===++++++===++++********+++++++++++++***
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####********++++++++++++++++++++*********++++++++++++++***
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####***************++++++++++++*******++++++++++++******
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%####****************+****+++++*******++++++++**********
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###******++++++*********++**+*******++++++**********##
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*++++++++++++++++********************++*************###
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*++++++++++++++***********************************#####
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#**************#########***####***************#*#######
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%################%%############*********##############
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@%%%%%@%%%##*******#***######%%%%#%%##
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##############%%%%%%%%%%#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##########%%%%%%%%%%%%
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%@@%%%%%%
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@%''')

#Defines th function that processes the user's input
def ExecuteCommand():
    global UserInput
    global UserInput2
    global UserInput3
    global CommandsExecutedInSesion
    global Com1
    global Com2
    global Com3
    global Com4
    global Com5
    global Com6
    global Com7
    global Com8
    global Com9
    global Com10
    global ERR_0
    global logs
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'ExacuteCommand' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()
    if UserInput[0] != ComIdChar:
        print(UserInput)
        CommandsExecutedInSesion = CommandsExecutedInSesion + 1

    else:

        if UserInput == Com1:
            CommandHelp()
            CommandsExecutedInSesion = CommandsExecutedInSesion + 1

        elif UserInput == Com2:
            CommandRandomInt(int(UserInput2), int(UserInput3))
            CommandsExecutedInSesion = CommandsExecutedInSesion + 1

        elif UserInput == Com3:
            CommandExit()
            CommandsExecutedInSesion = CommandsExecutedInSesion + 1

        elif UserInput == Com4:
            CommandErrors()
            CommandsExecutedInSesion = CommandsExecutedInSesion + 1

        elif UserInput == Com5:
            CommandPercy()
            CommandsExecutedInSesion = CommandsExecutedInSesion + 1

        else:
            print("An error has occurred. Error code: "+ ERR_0)
            Time = str(datetime.datetime.now())
            logs = open("Resorces/logs.txt","a")
            LogWrite = "Error ERR-0 has occured"
            logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
            logs.close()
            CommandsExecutedInSesion = CommandsExecutedInSesion + 1

#Defines the start of the program
def ProgramStart():
    global logs
    global LogWrite
    global Time
    Time = str(datetime.datetime.now())
    logs = open("Resorces/logs.txt","a")
    LogWrite = "Function 'ProgramStart' was called"
    logs.writelines("""
 ["""+ Time + "]: "+ LogWrite)
    logs.close()
    print("Welcome to PyTerminal")
    print(ConsolVer)
    print('Enter "/help" for help with commands')

ProgramStart()
while CommandsExecutedInSesion > -1:
    GetUserInput()
    ExecuteCommand()
else:
    print('''IDK what happened, relaunch the terminal.
If this issue persists, uninstall the program and reinstall it.
If it STILL persists, give feedback, you can do this on the website.''')
