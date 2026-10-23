class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi
        

class Kutubxona(Kitob):
    def __init__(self):  
        self.kitoblar = []
                            
    def qosh(self, kitob):
        self.kitoblar.append(kitob)

    def soni(self):
        return len(self.kitoblar) 


k = Kutubxona()
k.qosh(Kitob("Ufq"))
k.qosh(Kitob("Shum bola"))
print("Kitoblar soni:", k.soni())