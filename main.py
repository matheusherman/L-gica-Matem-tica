def main():
    altura = float(input("Altura em m: "))
    peso = float(input("Peso em kg: "))

    # calculo imc
    imc = round(peso / (altura ** 2), 2)

    if (imc < 18.5):
        result_imc = "Abaixo do peso"
    elif ((imc >= 18.5) and (imc <= 24.9)):
        result_imc = "Peso saudável"
    elif ((imc >= 25) and (imc <= 29.9)):
        result_imc = "Sobrepeso"
    elif ((imc >= 30) and (imc <= 39.9)):
        result_imc = "Obeso"
    elif (imc >= 40):
        result_imc = "muito obeso"

    idade = int(input("Idade: "))
    gordura = float(input("Percentual de Gordura: "))

    # calculo gordura
    if (idade < 20):
        if (gordura < 8):
            result_gordura = "Excelente"
        elif ((gordura >= 8) and (gordura <= 10)):
            result_gordura = "Bom"
        elif ((gordura > 10) and (gordura <= 16)):
            result_gordura = "Normal"
        elif ((gordura > 16) and (gordura <= 20)):
            result_gordura = "Elevado"
        elif (gordura > 20):
            result_gordura = "Muito Elevado"
    # entre 20 e 29 anos
    elif ((idade >= 20) and (idade <= 29)):
        if (gordura < 11):
            result_gordura = "Atleta"
        elif ((gordura >= 11) and (gordura <= 13)):
            result_gordura = "Bom"
        elif ((gordura > 13) and (gordura <= 20)):
            result_gordura = "Normal"
        elif ((gordura > 20) and (gordura <= 23)):
            result_gordura = "Elevado"
        elif (gordura > 23):
            result_gordura = "Muito Elevado"
    # entre 30 e 39 anos
    elif ((idade >= 30) and (idade <= 39)):
        if (gordura < 12):
            result_gordura = "Atleta"
        elif ((gordura >= 12) and (gordura <= 14)):
            result_gordura = "Bom"
        elif ((gordura > 14) and (gordura <= 21)):
            result_gordura = "Normal"
        elif ((gordura > 21) and (gordura <= 24)):
            result_gordura = "Elevado"
        elif (gordura > 24):
            result_gordura = "Muito Elevado"
    # entre 40 e 49 anos
    elif ((idade >= 40) and (idade <= 49)):
        if (gordura < 14):
            result_gordura = "Atleta"
        elif ((gordura >= 14) and (gordura <= 16)):
            result_gordura = "Bom"
        elif ((gordura > 16) and (gordura <= 23)):
            result_gordura = "Normal"
        elif ((gordura > 23) and (gordura <= 26)):
            result_gordura = "Elevado"
        elif (gordura > 26):
            result_gordura = "Muito Elevado"
    # 50 anos ou mais
    elif (idade >= 50):
        if (gordura < 15):
            result_gordura = "Atleta"
        elif ((gordura >= 15) and (gordura <= 17)):
            result_gordura = "Bom"
        elif ((gordura > 17) and (gordura <= 24)):
            result_gordura = "Normal"
        elif ((gordura > 24) and (gordura <= 27)):
            result_gordura = "Elevado"
        elif (gordura > 27):
            result_gordura = "Muito Elevado"

    print("Quando fecha o pulso com o dedo do meio e o dedão: ")
    print("1 - Dedo do meio fica por cima do dedão e vice-versa")
    print("2 - Dedo do meio e dedão se tocam na medida")
    print("3 - Os dedos não se encostam")
    pulso = int(input("Resposta: "))
    if (pulso < 1 or pulso > 3):
        print("Entrada invalida")

    print("Seu metabolismo é: ")
    print("1 - Muito acelerado")
    print("2 - Acelerado")
    print("3 - Lento")
    print("4 - Não sei")
    met = int(input("Resposta: "))
    if (met < 1 or met > 4):
        print("Entrada invalida")

    print("Em realção aos seus ombros")
    print("1 - São mais estreitos que meus quadris")
    print("2 - São mais largos que meus quadris")
    print("3 - São do mesmo tamanho que meus quadris")
    ombro = int(input("Resposta: "))
    if (ombro < 1 or ombro > 3):
        print("Entrada invalida")

    # calculo biotipo
    if ((met >= 1) and (met < 4)):
        if (((ombro == 1) and (met == 1)) or ((met == 2) and (pulso == 1))):
            result_biotipo = "Ectomorfo"
        elif (((ombro == 2) and (met == 2)) and ((pulso == 1) or (pulso == 2))):
            result_biotipo = "Mesomorfo"
        elif ((ombro == 1) and (met == 2) and (pulso == 2)):
            result_biotipo = "Mesomorfo"
        elif (((ombro == 3) and (met == 3) and (pulso == 2)) or (pulso == 3)):
            result_biotipo = "Endomorfo"
        else:
            result_biotipo = "Biotipo indefinido"
    elif (met == 4):
        if ((ombro == 1) and (pulso == 1)):
            result_biotipo = "Ectomorfo"
        elif (((ombro == 2) or (ombro == 1)) and (pulso == 2)):
            result_biotipo = "Mesomorfo"
        elif ((ombro == 3) and ((pulso == 2) or (pulso == 3))):
            result_biotipo = "Endomorfo"
        else:
            result_biotipo = "Biotipo indefinido"

    # resultado comparado com a media populacional
    if (result_imc == "Abaixo do peso"):
        result = "Pior que a média"
    elif ((result_imc == "Peso saudável") and ((result_gordura == "Atleta") or (result_gordura == "Bom"))):
        result = "Melhor que a média"
    elif ((result_imc == "Peso saudável") and (result_gordura == "Normal")):
        result = "Está na média"
    elif ((result_imc == "Peso saudável") and (
            (result_gordura == "Elevado") or (result_gordura == "Muito Elevado"))):
        result = "Pior que a média"
    elif (((result_imc == "Muito obeso") or (result_imc == "Sobrepeso") or (result_imc == "Obeso")) and (
            ((result_gordura == "Normal")) or (result_gordura == "Atleta") or (result_gordura == "Bom"))):
        result = "Melhor que a média"
    elif ((result_imc == "Muito obeso") or (result_imc == "Sobrepeso") or (result_imc == "Obeso") and (
            (result_gordura == "Elevado") or (result_gordura == "Muito Elevado"))):
        result = "Pior que a média"

    print("==================== Resultado =====================")
    print(f"IMC Calculado: {imc}, a situação é considerada como: {result_imc}")
    print("Biotipo:", result_biotipo)
    print("Gordura:", result_gordura)
    print("Resultado:", result)


if __name__ == '__main__':
    main()
