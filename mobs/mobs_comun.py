class goblin():
    def __init__(self,raca="Goblin",NV=1,armadura=NULL,arma=NULL,ATK=2,DEF=0):
        self.__raca = raca
        self.__NV = NV
        self.__armadura =armadura
        self.__arma = arma
        self.__ATK = ATK
        self.__DEF = DEF
    
    #NV
    def SetNV(self,NV):
        self.__NV = NV
    def GetNV(self):
        return self.__NV

    #armadura
    def SetArmadura(self,Armadura):
        self.__armadura = Armadura
    def GetArmadura(self):
        return self.__armadura
    
    #armadura
    def SetArmadura(self,Arma):
        self.__armadura = Arma
    def GetArma(self):
        return self.__arma