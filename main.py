from ast import Break
from pydoc import plain
import Jogador.Player as pl

p1 = pl.jogador("Mario")
p1.SetNivel(2)
p1.SetXp(152)
while True:
    if p1.GetVida() <= 0:
        print("GAMER OVER!!!")
        Break
    if p1.GetXp() >= p1.GetNivel()*100:
        p1.UP_LV()
        p1.SetXp(0)
    p1.VerStatus()
    