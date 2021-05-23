#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

#A CADA RESPOSTA, ELA SERA ARMAZENADA NA LISTA
perguntas=list()
resp=0 #CONTARA QUANTAS VEZES ELE RESPONDEU SIM


print('Responda "Sim" ou"Não"')
perg=str(input("Telefonou para a vítima?: ")).lower().strip()
perguntas.append(perg)             #A LISTA DE PERGUNTAS ARMAZENARA A RESPOSTA DO USUARIO
if perg=='sim':                       #SE CASO FOR "SIM" ELE CONTARA AS RESPOSTA POSITIVAS
    resp+=1

perg=str(input("Esteve no local do crime?: " )).lower().strip()
perguntas.append(perg)
if perg=='sim':
    resp+=1 

perg=str(input("Mora perto da vítima?: ")).lower().strip()
perguntas.append(perg)
if perg=='sim':
    resp+=1
    

perg=str(input("Devia para a vítima?: ")).lower().strip()
perguntas.append(perg)
if perg=='sim':
    resp+=1

perg=str(input("Já trabalhou com a vítima?: ")).lower().strip()
perguntas.append(perg)
if perg=='sim':
    resp+=1
    

print(f'Suas respostas foram {perguntas}')   #ELE EXIBIRA AS RESPOSTAS
if resp<=1:
    print("Classificado: Inocente.")             
elif resp==2:                                      #A QUANTIDADE DE "SIM" RESPONDIDOS SERA COLOCADO NA CONDIÇÃO DE CLASSIFICAR O USUARIO
    print("Classificado: Suspeito(a).")
elif resp<=4:
    print("Classificado: Cumplice.")
elif resp==5:
    print("Classificado: Assassino.")