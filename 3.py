class Shaxs:
    def __init__(self):
        self.__ism = "Nomalum"

    def ismni_ber(self, ism):
        if ism != "":
            self.__ism = ism
        else:
            print("Ism bo'sh bo'lishi mumkin emas")

    def ismni_ol(self):
        return self.__ism
    
s = Shaxs()
print(s.ismni_ol())
s.ismni_ber("Ali")
s.ismni_ber("")
print(s.ismni_ol())            


        