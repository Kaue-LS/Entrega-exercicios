#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e 
   # mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40. 




#RECEBE OS DOIS NUMEROS
n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))

print(f"A soma de {n1} + {n2} é = {n1+n2}")#FAZ A SOMA ENTRE ELES
print(f"A multiplicação de {n1} * {n2} é = {n1*n2}")# A MULTIPLICAÇÃO
if n1>n2:
   print(f"A divisao inteira de {n1} / {n2} é = {n1//n2}")# DIVISAO INTEIRA SE O NUMERO 1 FOR MAIOR QUE NUMERO 2
else:
   print(f"A divisao inteira de {n2} / {n1} é = {n2//n1}")# DIVISAO INTEIRA SE O NUMERO 2 FOR MAIOR QUE NUMERO 1

if n1>n2:#FAZ A CONDIÇÃO SE O NUMERO 1 É MAIOR QUE A 2
   print(f" {n1} é maior que {n2}")
else:# FAZ A CONDIÇÃO COM O CONTRARIO DOQ FOI PEDIDO
   print(f" {n2} é maior que {n1}")
if (n1+n2)%2==0:#SE A SOMA ENTRE ELES DIVIDIDO POR 2 TEM O RESTO DA DIVISAO IGUAL A ZERO
   print(f"O resultado de {n1} + {n2} é Par")
else:
   print(f"O resultado de {n1} + {n2} é Impar")


if n1>n2:
   if n1*n2>40:
#SE O NUMERO 1 É MAIOR QUE A 2, ADICIONANDO A CONDIÇÃO DE SER A MULTIPLICAÇÃO ENTRE ELES É MAIOR QUE 40
#SERA DIVIDIDO O RESULTADO DA MULTIPLICAÇÃO COM O RESULTADO DA DIVISAO INTERIRA
      print(f"A divisao da {n1*n2} com a {n1//n2} é igual a: {int((n1*n2)/(n1//n2))}")
elif n2>n1:
   if n2*n1>40:
# SERIA O CONTRARIO DA ANTERIOR COM OS NUMERO INVERTIDOS, MAS A OPERAÇÃO SERIA A MESMA:
      print(f"A divisao da {n1*n2} com a {n2//n1} é igual a: {int((n1*n2)/(n2//n1))}")
elif n1*n2<40:
#CASO O A MULTIPLICAÇÃO NAO FOR MAIOR QUE 40
   print("A multiplicação nao foi maior que 40")
   
   


