

#Mochila
class Mochila:
    def __init__(self,itens = []):
        self.__itens = itens
    def SetMochila(self,item):
        self.__itens = item
    def GetMochila(self):
        return self.__itens
    def add_item(self,item):
        box = self.GetMochila()
        box.append(item)
        return self.SetMochila(box)
    def ver_mochila(self):
        print(f"Mochila:\n{self.GetMochila()}\n")

#Status_Jogador
class Status:
    def __init__(self,vida=100,dano_F = 2,dano_M = 2,agilidade = 15) -> None:
        self.__vida = vida
        self.__dano_F = dano_F
        self.__dano_M = dano_M
        self.__agilidade = agilidade
    #vida
    def SetVida(self,vida):
        self.__vida = vida
    def GetVida(self):
        return self.__vida
    #dano fisico
    def Setdano_F(self,dano_F):
        self.__dano_F = dano_F
    def Getdano_F(self):
        return self.__dano_F
    #dano magico
    def Setdano_M(self,dano_M):
        self.__dano_M = dano_M
    def Getdano_M(self):
        return self.__dano_M
    #agilidade
    def Setagilidade(self,agilidade):
        self.__agilidade = agilidade
    def Getagilidade(self):
        return self.__agilidade
    #Upar Nível
    def UP_LV(self):
        NovaV = self.GetVida() + 6
        NovoDF = self.Getdano_F() + 4
        NovoDM = self.Getdano_M() + 1
        NovaA = self.Getagilidade() + 4
        return self.SetVida(NovaV),self.Setdano_F(NovoDF), self.Setdano_M(NovoDM), self.Setagilidade(NovaA)
    #Conferir Status
    def VerStatus(self):
        print(f"Vida: {self.GetVida()}\nDano Fisico: {self.Getdano_F()}\nDano Magico: {self.Getdano_M()}\nAgilidade: {self.Getagilidade()}")

#Player
class jogador(Status):
    def __init__(self, teg=None, nivel = 1,XP = 0, vida=100, dano_F=2, dano_M=2, agilidade=15):
        super().__init__(vida, dano_F, dano_M, agilidade)
        self.__teg = teg
        self.__nivel = nivel
        self.__xp = XP
    #Nome
    def GetTeg(self):
        return self.__teg
    #Nivel
    def GetNivel(self):
        return self.__nivel
    def SetNivel(self,nivel):
        self.__nivel = nivel
    #XP
    def GetXp(self):
        return self.__xp
    def SetXp(self,xp):
        self.__xp = xp
    def VerStatus(self):
        print(f"Teg: {self.GetTeg()}\nNivel: {self.GetNivel()}\nXP: {self.GetXp()}\nXp necessario para upar: {self.GetNivel()*100}")
        return super().VerStatus()

