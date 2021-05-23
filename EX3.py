#03 - Utilizando estruturas de repetição com teste lógico, 
# faça um programa que peça uma senha para iniciar seu processamento,
#  só deixe o usuário continuar se a senha estiver correta, após entrar
#  dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde 
# o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar
#  adivinhar qual número foi escolhido até acertar, a cada palpite do usuário
#  diga a ele se o número escolhido pelo computador é maior ou menor ao que ele 
# palpitou, no final mostre quantos palpites foram necessários para vencer.

import random

nome=str(input("Digite seu nome: ")).capitalize()#RECEBE O NOME COM A LETRA INICIAL MAIUSCULA
password=str(input("Digite a senha: "))#O USUARIO TENTARA ACERTAR A SENHA PEDIDA

while password!='Blue2021':#A ESTRUTRA VAI REPETIR VARIAS VEZES CASO A SENHA NAO SEJA A CORRETA
    print('')
    print("Senha incorreta!")
    password=str(input("Digite a senha: "))

#CASO A SENHA SEJA A CORRETA
else:
    print('')
    print(f"Ola senhor(a) {nome}, bem vindo!")

    dica=0                                 #CONTAGEM DE QUANTAS VEZES PRECISAVA DAR PALPITES
    numero=random.randint(0,10)  #O NUMERO ALEATORIO QUE O COMPUTADOR VAI ESCOLHER DE 0 A 10
    n=numero                      #SERA COLOCADO EM UM VARIAVEL "N"
    print('')
    number=int(input("Acerte o numero escolhido entre 0 a 10: "))    #O USUARIO DEVE ACERTAR O NUMERO
    while number>10:
        print('')                                                     #CASO O USUARIO COLOCA UM NUMERO ACIMA DE 10
        number=int(input("O numero tem que ser entre 0 a 10: "))

    #ESTRUTURA QUE VAI ACONTECER CASO O NUMERO NAO SEJA IGUAL AO ESCOLHIDO
    while number!=n:

        if n>number:
            #print(n)
            dica+=1
            print('')
            print(f'O numero é maior que {number} ')     #O COMPUTADOR CONTINUARA A DAR PALPITES QUE É MAIOR Q O USUARIO COLOCOU
            number=int(input('Tente novamente: '))   #A CADA PALPITE SERA CONTADO 1 A MAIS NA VARIAVEL DICA

  
            
        if n<number:
            #print(n)
            dica+=1
            print('')                                      #MESMA OPERAÇÃO CASO O NUMERO FOR MENOR DOQ FOI COLOCADO
            print(f'O numero é menor que {number}')
            number=int(print("Tente novamente: "))


                
    else:#CASO ELE TENHA ACERTADO
        print('')
        print(f"Eu tinha escolhido {n}!")#O NUMERO ESCOLHIDO
        print("Acertou!!!!!!!")          
        print(f"Eu precisei te dar {dica} dicas.")   #AS QUANTIDADE DE PALPITES
