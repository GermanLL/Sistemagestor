class Usuario:
    __idU =  None
    __nombreU = None
    __passU = None
    def __init__(self, id, nom, passw):
        self.__idU = id
        self.__nombreU = nom
        self.__passU = passw
    def getNombre(self):
        return self.__nombreU