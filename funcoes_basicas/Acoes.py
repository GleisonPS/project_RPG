from tkinter import S
from Jogador import Player as pl
import random
def upar(ps):
    pp = pl.jogador(ps)
    xp_necessario = pp.GetNivel*100
    if pp.GetXp() == xp_necessario:
        pp.UP_LV()
        print("Level UP!!!")

#ANDAR

def andar():
    sorte = random.randint(1,20)
    if sorte >= 15:
        print('caminho seguro')
    else:
        print('Sedparou com um mostro')

#COMBATE

def combate(player,mostro):
    import mobs.mobs_comun as mb
    mob = mostro
    ply= player
    while True:
        if ply.GetVida() >= 0:
            print("Fim de jogo\nSua vida chegou a zero!")
            break
        if mob.GetVida() <= 0:
            xp = (mob.GetNV()*100)/4
            print(f"Você ganhou {xp} de XP")