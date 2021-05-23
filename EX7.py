#07 - Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
lista=list()                        
pares=list()                     #AS LISTAS NA QUAL A 1° ARMAZENARA TODAS, A 2° ARMAZENARA AS PARES E A ULTIMA OS IMPARES 
impares=list()

for i in range(1,8):#O PEDIDO DE PEDIR NUMERO SERA FEITO 7 VEZES
    temp=int(input(f"Digite  o {i}° numero: "))
    lista.append(temp)           #LISTA VAI RECEBER OS NUMEROS DIGITADOS
print(lista)            #LISTA COM OS NUMEROS

for i in lista:     #A CADA NUEMERO COLOCADO 
    if i%2==0:
        pares.append(i)         #SE OS RESTO DA DIVISAO FOR 0 ELE VAI NA LISTA "PARES"
        
    else:
        impares.append(i)            #CASO NAO VAI NA LISTA "IMPARES"

pares.sort()        
impares.sort()                  #LISTA "PARES" E "IMPARES " SERÃO ORGANIZADAS EM ORDEM CRESCENTE
lista.clear()                   #A "LISTA" TERA OS NUMEROS ARMAZENADOS DELETADOS 
lista.append(pares)                 #A LISTA AGORA RECEBERA A LISTA PARES E IMPARES
lista.append(impares)



print(lista)
