class IMC():
    def __init__(self, altura, peso, idade):
        self.__altura = altura
        self.__peso = peso
        self.__idade = idade

    # Metodos Getters e setters

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura

    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
        self.__peso = peso

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def calc(self):

        imc = round(self.getPeso(self) / (self.getAltura(self) ** 2), 2)

        if (imc < 18.5):
            return "Abaixo do peso"
        elif ((imc >= 18.5) and (imc <= 24.9)):
            return "Peso saudável"
        elif ((imc >= 25) and (imc <= 29.9)):
            return "Sobrepeso"
        elif ((imc >= 30) and (imc <= 39.9)):
            return "Obeso"
        elif (imc >= 40):
            return "muito obeso"


class Gordura():
    def __int__(self, gordura, idade):
        self.__gordura = gordura
        self.__idade = idade

    # Metodos Getters e setters
    def getGordura(self):
        return self.__gordura

    def setGordura(self, gordura):
        self.__gordura = gordura

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def gord_inf(self):
        # gordura
        # menos que 20 anos
        if (self.__idade < 20):
            if (self.__gordura < 8):
                return print("Excelente")
            elif ((self.__gordura >= 8) and (self.__gordura <= 10)):
                return print("Bom")
            elif ((self.__gordura > 10) and (self.__gordura <= 16)):
                return print("Normal")
            elif ((self.__gordura > 16) and (self.__gordura <= 20)):
                return print("Elevado")
            elif (self.__gordura > 20):
                return print("Muito Elevado")
        # entre 20 e 29 anos
        elif ((self.__idade >= 20) and (self.__idade <= 29)):
            if (self.__gordura < 11):
                return print("Atleta")
            elif ((self.__gordura >= 11) and (self.__gordura <= 13)):
                return print("Bom")
            elif ((self.__gordura > 13) and (self.__gordura <= 20)):
                return print("Normal")
            elif ((self.__gordura > 20) and (self.__gordura <= 23)):
                return print("Elevado")
            elif (self.__gordura > 23):
                return print("Muito Elevado")
        # entre 30 e 39 anos
        elif ((self.__idade >= 30) and (self.__idade <= 39)):
            if (self.__gordura < 12):
                return print("Atleta")
            elif ((self.__gordura >= 12) and (self.__gordura <= 14)):
                return print("Bom")
            elif ((self.__gordura > 14) and (self.__gordura <= 21)):
                return print("Normal")
            elif ((self.__gordura > 21) and (self.__gordura <= 24)):
                return print("Elevado")
            elif (self.__gordura > 24):
                return print("Muito Elevado")
        # entre 40 e 49 anos
        elif ((self.__idade >= 40) and (self.__idade <= 49)):
            if (self.__gordura < 14):
                return print("Atleta")
            elif ((self.__gordura >= 14) and (self.__gordura <= 16)):
                return print("Bom")
            elif ((self.__gordura > 16) and (self.__gordura <= 23)):
                return print("Normal")
            elif ((self.__gordura > 23) and (self.__gordura <= 26)):
                return print("Elevado")
            elif (self.__gordura > 26):
                return print("Muito Elevado")
        # 50 anos ou mais
        elif (self.__idade >= 50):
            if (self.__gordura < 15):
                return print("Atleta")
            elif ((self.__gordura >= 15) and (self.__gordura <= 17)):
                return print("Bom")
            elif ((self.__gordura > 17) and (self.__gordura <= 24)):
                return print("Normal")
            elif ((self.__gordura > 24) and (self.__gordura <= 27)):
                return print("Elevado")
            elif (self.__gordura > 27):
                return print("Muito Elevado")


class Biotipo():
    def __init__(self, ombro, pulso, met):
        self.__ombro = ombro
        self.__pulso = pulso
        self.__met = met

    # Metodos Getters e setters
    def getOmbro(self):
        return self.__ombro

    def setOmbro(self, ombro):
        self.__ombro = ombro

    def getPulso(self):
        return self.__pulso

    def setPulso(self, pulso):
        self.__pulso = pulso

    def setMet(self, met):
        self.__met = met

    def getMet(self):
        return self.__met

    def biotipo_inf(self):
        # nao ta setando os valores
        # vo arruma esse carai amanha cedo vsf

        if (self.getMet(self) != 4):
            if (((self.getOmbro(self) == 1) and (self.getMet(self) == 1)) or (
                    (self.getMet(self) == 2) and (self.getPulso(self) == 1))):
                return "Ectomorfo"
            elif (((self.getOmbro(self) == 2) and (self.getMet(self) == 2)) and (
                    (self.getPulso(self) == 1) or (self.getPulso(self) == 2))):
                return "Mesomorfo"
            elif ((self.getOmbro(self) == 1) and (self.getMet(self) == 2) and (self.getPulso(self) == 2)):
                return "Mesomorfo"
            elif (((self.getOmbro(self) == 3) and (self.getMet(self) == 3) and
                   (self.getPulso(self) == 2)) or (self.getPulso(self) == 3)):
                return "Endomorfo"
        else:
            if ((self.getOmbro(self) == 1) and (self.getPulso(self) == 1)):
                return "Ectomorfo"
            elif (((self.getOmbro(self) == 2) or (self.getOmbro(self) == 1)) and (self.getPulso(self) == 2)):
                return "Mesomorfo"
            elif ((self.getOmbro(self) == 3) and ((self.getPulso(self) == 2) or (self.getPulso(self) == 3))):
                return "Endomorfo"
            else:
                return "Biotipo indefinido"


def resultado():
    im = IMC()

    biotipo = Biotipo()

    if (im.IMC_inf() == "Abaixo do peso"):
        result = "Pior que a média"

    elif ((im.IMC_inf() == "Peso saudável") and ((im.gord_inf() == "Atleta") or (im.gord_inf() == "Bom"))):
        result = "Melhor que a média"
    elif ((im.IMC_inf() == "Peso saudável") and (im.gord_inf() == "Normal")):
        result = "Está na média"
    elif ((im.IMC_inf() == "Peso saudável") and ((im.gord_inf() == "Elevado") or (im.gord_inf() == "Muito Elevado"))):
        result = "Pior que a média"

    elif (((im.IMC_inf() == "Muito obeso") or (im.IMC_inf() == "Sobrepeso") or (im.IMC_inf() == "Obeso")) and (
            ((im.gord_inf() == "Normal")) or (im.gord_inf() == "Atleta") or (im.gord_inf() == "Bom"))):
        result = "Melhor que a média"
    elif ((im.IMC_inf() == "Muito obeso") or (im.IMC_inf() == "Sobrepeso") or (im.IMC_inf() == "Obeso") and (
            (im.gord_inf() == "Elevado") or (im.gord_inf() == "Muito Elevado"))):
        result = "Pior que a média"

    print("==================== Resultado =====================")
    print(f"IMC.calc(): {im.calc()} a situação sendo consiferada como {im.IMC_inf()}")
    print("Biotipo", biotipo.biotipo_inf())
    print("Gordura", im.gord_inf())
    print("Resultado: ", result)


def main():
    """
    altura = float(input("Altura em m: "))
    peso = float(input("Peso em kg: "))


    IMC.setAltura(IMC, altura)
    IMC.setPeso(IMC, peso)
    IMC.setIdade(IMC, idade)
    IMC.calc(IMC)
    print(IMC.calc(IMC)) #teste se ta dando o resultado certo

    idade = int(input("Idade: "))
    gordura = float(input("Percentual de Gordura: "))
    Gordura.setIdade(Gordura, idade)
    Gordura.setGordura(Gordura, gordura)

    Gordura.gord_inf(Gordura)
    """

    print("Quando fecha o pulso com o dedo do meio e o dedão: ")
    print("1 - Dedo do meio fica por cima do dedão e vice-versa")
    print("2 - Dedo do meio e dedão se tocam na medida")
    print("3 - Os dedos não se encostam")
    pulso = input("Resposta: ")

    print("Seu metabolismo é: ")
    print("1 - Muito acelerado")
    print("2 - Acelerado")
    print("3 - Lento")
    print("4 - Não sei")
    met = input("Resposta: ")

    print("Em realção aos seus ombros")
    print("1 - São mais estreitos que meus quadris")
    print("2 - São mais largos que meus quadris")
    print("3 - São do mesmo tamanho que meus quadris")
    ombro = input("Resposta: ")

    Biotipo.setPulso(Biotipo, pulso)
    Biotipo.setMet(Biotipo, met)
    Biotipo.setOmbro(Biotipo, ombro)

    print(Biotipo.biotipo_inf(Biotipo))


if __name__ == '__main__':
    main()
