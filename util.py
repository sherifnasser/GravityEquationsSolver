from os import system

def clearScr():
    system("clear")

def clearWithInput(__prompt):
    clearScr()
    return input(__prompt)

def exit():
    system("exit")