class KlasaA:
    def metoda(self):
        print("KlasaA")


class KlasaB(KlasaA):
    def metoda(self):
        super().metoda()
        print("KlasaB")


class KlasaC(KlasaB):
    def metoda(self):
        super().metoda()
        print("KlasaC")



class Using(KlasaA, KlasaB, KlasaC):
    ...
    # def metoda(self):
    #     super().metoda()

# class Using(KlasaC, KlasaB, KlasaA):
#     ...
#     def metoda(self):
#         super().metoda()
#         print("Woła using")

if __name__ == '__main__':
    inst = Using()
    inst.metoda()