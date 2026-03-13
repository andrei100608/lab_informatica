from random import randint
from Player import Player
from HumanPlayer import HumanPlayer
from CpuPlayer import CpuPlayer
from FastPlayer import FastPlayer
import time
import csv

massimo = int(input("Inserisci un numero: "))
numero = randint(0,massimo)

nome = input("inserisci nome giocatore: ")
modalita_gioco = input ("scegli modalità di gioco (human/cpu/fast): ")
if (modalita_gioco == "human"):
    giocatore = HumanPlayer(nome)
elif (modalita_gioco=="cpu"):
    giocatore = CpuPlayer()
else:
    giocatore = FastPlayer()

with open('tentativi.tsv',mode='w',newline='') as file:
    tentativi = []
    old_guess = -1
    numero_tentativi = 0
    max = massimo
    min = 0

    if (giocatore.__class__==HumanPlayer):
        tentativo = giocatore.genera_numero()
    elif (giocatore.__class__==CpuPlayer):
        tentativo = giocatore.genera_numero(old_guess,"d",massimo)
    else:
        tentativo = giocatore.genera_numero(old_guess,"d",max,min)

    while (1):
        numero_tentativi+=1

        if (tentativo > numero):
            stringa ="troppo alto"
            max = tentativo-1
        elif (tentativo < numero):
            stringa = "troppo basso"
            min = tentativo+1
        else:
            tentativi.append([tentativo,time.ctime()])
            file.write(nome + " " + str(numero) + " " + str(numero_tentativi))
            file.write("\n")
            writer = csv.writer(file,delimiter="\t")  # Crea un oggetto writer
            writer.writerows(tentativi)
            stringa = "finito"
            break

        print(stringa)
        old_guess = tentativo
        tentativi.append([tentativo,time.ctime()])

        if (giocatore.__class__==HumanPlayer):
            tentativo = giocatore.genera_numero()
        elif (giocatore.__class__==CpuPlayer):
            tentativo = giocatore.genera_numero(old_guess,stringa)
        else: 
            tentativo=giocatore.genera_numero(old_guess,stringa,max,min)
