#Projekt 2 - Skapa en Lista 

__Author__ = "Hannes"
__version__ = "1.0.0"
__email__ = "hannes.tinnis@elev.ga.ntig.se"

import os
from colors import bcolors
os.system("cls")
print(bcolors.BOLD+""" 
 ________    ___   ________           ___        ___   ________    __________  ________          
|\   ___ \  |\  \ |\   ___  \        |\  \      |\  \  |\   ____\ |\___   ___\|\   __  \     
\ \  \_|\ \ \ \  \ \  |\ \   \       \ \  \     \ \  \ \ \  \___|_\|___ \  \_|\ \  \|\  \     
 \ \  \ |\ \ \ \  \ \  |\ \   \       \ \  \     \ \  \ \ \_____  \    \ \  \  \ \   __  \   
  \ \  \_|\ \ \ \  \ \  |\ \   \       \ \  \____ \ \  \ \|____|\  \    \ \  \  \ \  \ \  \ 
   \ \_______| \ \__|\ \__|\ \__\       \ \_______|\ \__\  ____\_\  \    \ \__\  \ \__\ \__|  
    \|_______|  \|__| \|__| \|__|        \|_______| \|__|| \_________\    \|__|   \|__|\|__|""")#Titel-använde color för att styla 


my_list=[]



print(my_list)


def add(addition):
    my_list.append(addition)

def remove(remove):
    my_list.pop(remove)

def listedit(edit,Nname):
    my_list[edit]=Nname

while True: 
    input1=(input("\nSkirv in ett namn \nEller skriv in en position för att ändra/ta bort\n:"))
    if input1.isdigit():
        select=int(input1)
        if select > 0 and select<=len(my_list):
            action = input("vill du ta bort eller redigera ")
            position = action.upper()
            if position == "TA BORT":
                remove(select-1)
            elif position == "REDIGERA":
                Nname=input(f"Skriv in det nya namnet för {my_list[select-1]}: ")
                listedit(select-1, Nname)
        os.system("cls")
        y=0
        print("--LISTAN--")
        for i in my_list:
            y+=1
            print(f"{y}) { i}")

        print("du har", bcolors.RED+ str(len(my_list)),bcolors.DEFAULT+ "namn i din lista")
    else:
        (add(input1))
            


        os.system("cls")
        y=0
        print("--DIN LISTA--")
        for i in my_list:
            y+=1
            print(f"{y}) { i}")
        print("du har", bcolors.RED+str(len(my_list)),bcolors.DEFAULT+ "namn i din lista")
   


