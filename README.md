**Leandro Ricardo Guimarães**
**Matheus Herman**

Tema Sistemas especialista peso

## Entradas:

	Relação ao IMC
		i.	 Peso em KG
		ii.	 Altura em m
		iii. Idade
	b.Biotipo
    	i.	 Percentual de Gordura
		ii.	 Quando fecha o pulso com o dedo do meio e o dedao
        iii.  O metabolismo é
        iv.   Em realção os seus ombros são

##	Saída
        a.	Se está abaixo ou acima do peso com base no IMC
        b.	Gordura elevada ou não
        c.	Ectomorfia, mesomorfo ou endomorfo
        d.  Se está pior que a média, na média ou melhor que a média em relação a gordura e IMC  
##	Regras

    Regra 1   
       -Se idade for > que 20 anos,  O programa da exit
	   	- Em realação ao IMC 
		- Regra 2 - Se o IMC for:
		 	-  < 18,5 - abaixo do peso
			-  18,5 a 24,9 - peso saudável
			- 25 a 29,9 - sobrepeso
			- 30 a 39,9 – obeso
			- > de 40 - muito obeso 
    Regra 2
	2)	Em relação a gordura 
            Menos que 20 anos
                - < 8% Exelente
                - entre 8% e 10% bom
                - Entre 10% e 16% normal
                - Entre 16% e 20% elevado
                - Maior de 20% muito elevado
            Entre 20 e 29 anos
                - < 11% Atleta
                - entre 11% e 13% bom
                - Entre 14% e 20% normal
                - Entre 21% e 23% elevado
                - Maior de 23% muito elevado
            Entre 30 e 39 Anos
                - < 12% Atleta
                - entre 12% e 14% bom
                - Entre 15% e 21% normal
                - Entre 22% e 24% elevado
                - Maior de 24% muito elevado 
            Entre 40 e 49 Anos
                - < 14% Atleta
                - entre 14% e 16% bom
                - Entre 17% e 23% normal
                - Entre 23% e 26% elevado
                - Maior de 26% muito elevado 
            50 anos ou mais
                < 15% Atleta
                - entre 16% e 17% bom
                - Entre 18% e 24% normal
                - Entre 25% e 27% elevado
                - Maior de 27% muito elevado 

    Regra 3
        Em relação ao biotipo
      		- Se os ombros são mais estreitos que meus quadris e o metabolismo é muito acelerado ou  metabolismo é acelerado, e quando fecha o pulso com o dedo do meio e o dedão o dedo do meio fica por cima do dedão e vice-versa, então ECTOMORFO

		    - Se os ombros são da mesma lagura que meus quadris e o metabolismo é acelerado, e quando fecha o pulso com o dedo do meio, o dedão o dedo do meio fica por cima do dedão e vice-versa ou se tocam na medida, então é MESOMORFO

		    - Se os ombros são mais estreitos que meus quadris e o metabolismo é acelerado, e quando fecha o pulso com o dedo do meio e o dedão o dedo do meio se tocam na medida, então é MESOMORFO

            - Se os ombros são da mais lagos que meus quadris e o metabolismo é lento, e quando fecha o pulso com o dedo do meio e o dedão,o dedo do meio e dedão se tocam na medida, ou não se tocam, então é ENDOMORFO
             
            -  Se os ombros são mais estreitos que meus quadris e não sei meu metabolismo, pulso com o dedo do meio e o dedão o dedo do meio fica por cima do dedão e vice-versa, então ECTOMORFO

            - Se os ombros são da mesma lagura ou mais estreitos que meus quadris e  não sei meu metabolismo, e quando fecha o pulso com o dedo do meio e o dedão, dedo do meio e dedão se tocam na medida, então MESOMORFO

            - Se os ombros são mais largos que meus quadris e não sei meu metabolismo, e quando fecha o pulso com o dedo do meio e o dedão, dedo do meio e dedão se tocam na medida, ou não se tocam, então ENDOMORFO

            - Se nenhum dos casos anteriores, então biotipo indefinido

    Regra 4
            - Se peso é saudável e gordura nivel atleta, ou boa, então melhor que a média

            - Se peso é saudável e nivel de gordura normal, então NA MÉDIA

            - Se peso é saudável e nivel de gordura elevada ou muito elevado, então PIOR QUE A MÉDIA

            - Se está com sobrepeso ou obeso ou muito obeso, e o nivel de gordura é normal, bom ou atleta, então MELHOR QUE A MÉDIA

            - Se está com sobrepeso ou obeso ou muito obeso, e o nivel de gordura é elevado ou muito elevado, então PIOR QUE A MÉDIA
    
## Exemplo de execução

        Altura em m: 1.7
        Peso em kg: 68
        Idade: 21
        Percentual de Gordura: 8
        Quando fecha o pulso com o dedo do meio e o dedão: 
        1 - Dedo do meio fica por cima do dedão e vice-versa
        2 - Dedo do meio e dedão se tocam na medida
        3 - Os dedos não se encostam
        Resposta: 1
        Seu metabolismo é: 
        1 - Muito acelerado
        2 - Acelerado
        3 - Lento
        4 - Não sei
        Resposta: 1
        Em realção aos seus ombros
        1 - São mais estreitos que meus quadris
        2 - São mais largos que meus quadris
        3 - São do mesmo tamanho que meus quadris
        Resposta: 1
        ==================== Resultado =====================
        IMC Calculado: 23.53, a situação é considerada como: Peso saudável
        Biotipo: Ectomorfo
        Gordura: Atleta