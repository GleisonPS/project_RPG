from asyncio import all_tasks
from asyncio.windows_events import NULL
from mimetypes import init


class goblin():
    def __init__(self,raca="Goblin",NV=1,armadura=NULL,arma=NULL,ATK=2,DEF=0):
        self.__raca = raca
        self.__NV = NV
        self.__armadura =armadura
        self.__arma = arma
        self.__ATK = ATK
        self.__DEF = DEF